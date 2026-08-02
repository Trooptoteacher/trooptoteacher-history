# Guided Cornell notes + NOTES SUPPORTS ladder (LOCKED — Unit 6 · US.45 reference)

The Course Standard workbook, the Student deck, and the Teacher deck all follow **one sequence**
so a student can follow the lecture and take notes in a clear, sequential pattern. Activity 3
(Direct Teaching Cornell Notes) is the spine of that alignment. This is the approved design; build
it with `scripts/build_guided_notes.py`, which guarantees identical formatting across all standards.

## The design (front + back, one worksheet)

**FRONT — Activity 3 guided Cornell notes.** The cue column is *pre-seeded* (not blank) with the
standard's **direct-instruction (DI) segments in lecture order**, one cue block per DI slide:

- **Navy bold topic** — e.g. `①  Key Characteristics of Fascism`
- **Gold marker** — `▶ Deck · DI N of M` — maps 1:1 to the teacher deck's own on-slide
  "N of M" DI labels. This is the guided-notes bridge: cue `DI 2 of 4` ⇄ deck slide labeled
  "2 of 4". Use the *relative* "N of M", **not** an absolute slide number — it survives deck
  renumbering.
- **Italic guiding question** — what to listen for (`What drives history — and who owns property?`).

The "My notes" column keeps its ruled lines and RESPONSE CHOICE line ("sentences · bullets ·
symbols & quick sketches · a concept map"); the final `Key terms →` row is untouched.

**BACK — "NOTES SUPPORTS — build your notes, your way".** A four-rung support ladder so a
high-need student can produce full notes **from the back alone** — the ceiling never drops
(CAST UDL 3.0 guideline 5.3, graduated support; MTSS Tier 2/3 on the verso, Tier 1 on the front):

1. **① Sentence frames — finish the thought** (4 frames)
2. **② Fill-in notes — write just the missing word(s)** (4 cloze bullets + a **word bank**) —
   the student writes only 1–2 words per line
3. **③ How to build your answer** — `Name it → Define it in your own words → Give one example`
   + a **worked model** on a tinted card
4. **④ Try it — write one full note in your own words** — **lined notebook paper** (5 ruled
   lines) + a **Quick self-check** rubric row:
   `☐ I named the idea  ☐ I defined it in my own words  ☐ I gave an example  ☐ A reader could follow it`

Intro line, verbatim: *"Use one, some, or all — as much support as you need. Works alongside,
never in place of, your IEP or 504 plan."* (the non-replacement guardrail).

## Front / back print rule (LOCKED)

Core activity on the **front** (1 page); **all** supports on its **back** (1 page). A teacher
prints **one side** to drop supports or **two sides (duplex)** to include them. The front's goal
and rigor are identical whether or not the back is printed. See `STUDENT_WORKBOOK_PLATINUM_STANDARD.md`
§7.1.

## Spacing (LOCKED — fixes the "too compact / cognitive overload" feedback)

Generous gaps before each rung heading; loose line spacing inside rungs; the word bank on its own
tinted line; the model on its own tinted card. Do not re-tighten the ladder to reclaim space — the
white space here is intentional (it is labeled workspace, exempt under §5.1).

## Two formatting lessons (do NOT regress — see `build_guided_notes.py`)

1. **Notebook paper is a TABLE, not stacked bordered paragraphs.** Empty paragraphs that each
   carry only a `w:bottom` border **collapse** in Word/LibreOffice — adjacent identical paragraph
   borders merge and only *one* line renders (looks like a single rule above the self-check).
   Build ruled notebook paper as a **borderless table whose rows each carry a bottom border**
   (row/cell borders never collapse). `notebook_table()`: 5 rows, `trHeight` 460 twips exact,
   cell `w:bottom single sz 8 color 9AA0AB`.
2. **One `w:spacing` per paragraph.** Setting `space_before/after` via python-docx *and* appending
   your own `w:spacing` yields two sibling `w:spacing` elements; Word reads the first and silently
   drops your exact line height (so the border collapse in lesson 1 gets worse). Always build a
   single merged `w:spacing` with all of before/after/line/lineRule.

## Propagation (all standards) — clone, don't rebuild

Formatting parity is the requirement. For every standard other than the US.45 reference:
- **FRONT:** `seed_guided_cornell(cornell_tbl, cues)` — the cue column is empty (or carries stale
  auto-generated close-read questions) in every standard; seeding overwrites it uniformly.
- **BACK:** `clone_notes_supports(reference_block, cfg, anchor)` — **deep-copy US.45's NOTES
  SUPPORTS block** (preserves every fill/border/font/spacing) and swap only the standard-specific
  text (title code, 4 frames, 4 cloze, word bank, model). The notebook table and self-check line
  are copied verbatim — identical for every standard by design.

Author each standard's `cues` from that standard's teacher-deck DI slides ("N of M") and its four
rungs from the standard's content, add the entry to `STANDARDS` in `build_guided_notes.py`, run it,
then **render and QC** (zero blank pages; notebook lines visible as separate rules; word bank/model
show only the new standard's text — never appended to US.45's).
