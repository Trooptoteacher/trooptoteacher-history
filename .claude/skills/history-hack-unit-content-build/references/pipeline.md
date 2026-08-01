# The unit content-build pipeline (ordered playbook)

This is the exact sequence proven on Unit 6. **Phase order matters** — later phases shift
pagination, so do structural work before cosmetic work, and re-run the QC gate after every phase.

## Phase 0 — Intake & audit
- Confirm the unit number, its standard codes (e.g., US.45–US.58), and the unit title.
- Locate existing assets before building anything:
  - Student workbook `.docx` (may be in uploads or a prior build folder).
  - Existing decks `.pptx` (student + teacher).
  - The question bank in `history-hack-web-app` (`add_repo` + shallow clone if not present).
- **Assess, don't recreate.** The Unit 6 decks were already complete and on-brand; the correct
  move was to keep and retune them, not rebuild 371 slides. Recreate only what is missing or broken.

## Phase 1 — Workbook structure & blank-page fix
Goal: a clean N-standard book, full 7-activity cycle, **zero blank/near-empty pages**.
- Detect blanks with `pypdfium2` ink-fraction per page (`references/rendering-and-qc.md`).
- Root causes seen on Unit 6 and their fixes:
  - **Front-matter stray page** — an empty paragraph carrying a `w:br` page break after a full
    page. Convert to `pageBreakBefore` on the next heading and delete the empty carrier.
  - **Notebook-redirect boxes with on-page lines** — HOOK ("think before you dig in"), ACTIVATE
    ("jot in your notebook"), MAKE IT YOURS ("do this in your notebook/whiteboard") should NOT
    carry on-page writing lines; the lines spill to orphan pages. Remove them.
  - **Content overflow by a hair** — a section tips one box onto a near-empty page. Tighten
    writing-line heights (e.g., `w:line` 255→200 exact on rating grids) or table cell spacing to
    pull it back; only shrink, never grow (shrinking can't create new spills within a
    `pageBreakBefore`-delimited section).
- See `references/workbook-methods.md` for the docx idioms.

## Phase 2 — Guided notes + back-page UDL/MTSS supports

### 2a — Guided Cornell notes (Activity 3 front) + NOTES SUPPORTS ladder (its verso)
The workbook, Student deck, and Teacher deck follow **one sequence**; Activity 3 is the spine.
- **FRONT:** seed Activity 3's cue column with the standard's **direct-instruction segments in
  lecture order** — navy topic · gold `▶ Deck · DI N of M` (maps 1:1 to the teacher deck's on-slide
  "N of M" labels) · italic guiding question.
- **VERSO (NOTES SUPPORTS — "build your notes, your way"):** a four-rung ladder so a high-need
  student can produce full notes from the back alone — ① sentence frames → ② fill-in cloze + word
  bank → ③ how to build your answer + worked model → ④ **try it on lined notebook paper + a Quick
  self-check rubric**.
- Method: `scripts/build_guided_notes.py` — seeds cues from scratch and **clones the US.45 NOTES
  SUPPORTS block** for every other standard (formatting parity), swapping only standard-specific
  text. Two locked lessons live in the script: notebook paper is a **table** (stacked bordered
  paragraphs collapse to one line) and each paragraph gets **one** `w:spacing`. See
  `references/guided-notes-and-supports.md`.

### 2b — The other three verso supports
Per standard, add three more verso pages matching the reference exemplar:
- **VOCABULARY SUPPORTS** — word-attack + a real Spanish cognate for that standard + quick practice.
- **HIPPO SUPPORTS** — guiding questions + sentence frame + a **model source analysis specific to
  that standard's Activity 5 source** + sourcing warm-up.
- **WRITING SUPPORTS** — sentence stems + a **model CER answer specific to that standard's Activity
  7 prompt** + CER rubric + argument word bank. The **exit ticket rides on this page** (remove the
  redundant back-page "Plan it first" lines; the front CER page already has planning space).
- Method: deep-copy the reference block XML (preserves shading/borders/fonts), then rebuild the
  model paragraphs with **bold labels + regular body** runs (don't collapse runs — that makes the
  whole line bold). Script: `scripts/build_backpage_supports.py`.

## Phase 3 — Per-standard content
- **Hooks:** replace any hook that restates the standard verbatim with a vivid, 2–3-sentence,
  question-driven opener ending in a reading cue (see US.45's voice).
- **Practice quizzes (Activity 6):** the auto-assembled quizzes are unreliable (off-topic /
  mis-standardized items, wrong counts). Rebuild each standard's quiz with **4 verified,
  standard-aligned MC items** from the bank + an on-page self-check answer key. See
  `references/quiz-sourcing.md`.
- Fact-check all new prose and keys (`historian-factcheck-agent`).

## Phase 4 — Teacher Guide
Generate the How-to-Use & MTSS Guide (`scripts/build_teacher_guide.py`): cover, how-to-use +
pacing across the three schedule variants (protect the exit ticket), UDL/MTSS implementation,
CER scoring rubric, and per-standard answer keys (quiz keys with rationale + exit-ticket keys)
with a reteach move. Pull quiz explanations from the bank; derive exit-ticket keys as the
substantive, non-hedged option and verify historically.

## Phase 5 — Decks finalize
Assess → keep → retune. Migrate palette to canonical; unify stray accents; fix known layout
defects (long DIRECT INSTRUCTION titles clipping the divider). Validate with the pptx skill's
`validate.py --original`. See `references/decks.md`.

## Phase 6 — Slide-keying (bidirectional)
Build the deck slide map (title-labeled blocks), then:
- Workbook → deck: append `▶ Deck slide N` (gold) to each activity header, numbers from the
  deck's real positions.
- Deck → workbook: add `✍ In your workbook · <activity>` to matching slides (on-slide gold for
  Student deck; speaker notes for Teacher deck).
See `references/slide-keying.md`.

## Phase 7 — Final QA & commit
- Full contact-sheet review of every piece; zero blank pages; decks validate.
- Commit each piece to its `00_START_HERE/UNITn_*_BUILD/` folder with a STATUS.md; push to the
  designated branch. Do not open a PR unless asked.
