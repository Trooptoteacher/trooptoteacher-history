---
name: history-hack-workbook-print-bundle
description: "THE print-bundle LAYOUT standard for a History Hack U.S. History unit STUDENT WORKBOOK — the page architecture, duplex activity/supports rhythm, bidirectional deck↔workbook slide-keying, writing-space, no-bleed, and per-activity print rules that make the printed book classroom-clear and self-guiding. Use whenever building, reformatting, or QC-ing the PRINT LAYOUT of a unit workbook: 'the activity doesn't point to the deck / the deck doesn't point back to the activity', 'make it clear which slides a page maps to', 'too cramped / add breathing room', 'close the white-space gap', 'key terms should be first', 'give more writing space', 'all writing must be on ruled lines', 'activity bleeds to the next page', 'make the practice quiz self-grading', 'put the supports on the back of each activity', or 'match the Unit 6 print layout'. This owns LAYOUT/PRINT rules only; the 7-activity CONTENT engine is `history-hack-unit-content-build` and UDL support content is `udl-cast-expert` — this skill is INVOKED by `history-hack-unit-content-build` / `history-hack-platinum-unit-builder`, and it does not author content or re-implement those engines. Reference implementation: Unit 6 (WWII, US.45–US.58)."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.0"
  owner_of: "Unit student-workbook print-bundle LAYOUT standard (duplex rhythm, deck-keying precision, writing-space, no-bleed, per-activity print rules)"
  reference_implementation: "Unit 6 — World War II (US.45–US.58), Course Standard Edition"
  applies_to: "TroopToTeacher Technologies — U.S. History Hack Web App unit workbooks (US.01–US.95) and every future course"
---

# History Hack Unit Workbook — Print-Bundle Layout Standard

> **The printed book must be self-guiding.** A student holding the paper always knows (1) exactly which
> slide(s) each activity comes from, (2) where to write (always on ruled lines), and (3) where the help
> is (on the back of the same page). No hunting, no guessing, no dead white space.

This skill owns the **print LAYOUT** of the unit student workbook. It does **not** author content
(that is `history-hack-unit-content-build`) or design UDL supports (that is `udl-cast-expert`); it is
**invoked** by `history-hack-unit-content-build` and `history-hack-platinum-unit-builder` to enforce
how the 7-activity cycle is laid out on paper. Print-first doctrine (DOCX-native → PDF) and the
America 250 brand come from `00_START_HERE/BUILD_STANDARD.md` and `BRAND_PALETTE.md`; the fuller
workbook spec is `00_START_HERE/STUDENT_WORKBOOK_PLATINUM_STANDARD.md`.

## 1. The Duplex Law — activity on the front, its supports on the back

Every activity prints on the **front** of its leaf; the **CAST UDL 3.0 (2024) supports for that same
activity** print on the **back (verso) of that leaf**. The rhythm is per-activity, in order:

| Front (recto) | Back (verso) |
|---|---|
| Activity 1 — Vocabulary Word Bank | Activity 1 supports |
| Activity 2 — Vocabulary Studio (Frayer) | Activity 2 supports |
| Activity 3 — Cornell Notes (Direct Instruction) | Activity 3 supports |
| Activity 4 — Close Read | Activity 4 supports |
| Activity 5 — Primary Source / Data Analysis | Activity 5 supports |
| Activity 6 — Core Application: Practice Quiz | Activity 6 supports |
| Activity 7 — Constructed Response (CER) | Activity 7 supports |

- The supports are the four-rung ladder (frames → cloze + word bank → how-to + worked model → try-it +
  self-check), **scoped to the activity on the front** and drawn from `udl-cast-expert`. They stay
  **in the student book, default-included** — never gated into a teacher pack.
- **Print flag, not a content change:** _duplex_ = activity + its supports; _single-sided_ = activity
  only (supports suppressed at print time). A "lighter book" is this flag — supports are never deleted
  from the master.
- An activity that legitimately runs to a second leaf keeps the pattern: activity fronts, supports
  backs — never activity-front / activity-back.

## 2. Bidirectional deck ↔ workbook keying — exact, and clear both ways

**The deck model (LOCKED decision).** Each deck has one job, so the reference is unambiguous:

- **Teacher deck = the full teach.** Projected during the lesson; this is where students *follow along
  and take their notes*. **The workbook's exact slide numbers point to the TEACHER deck** — so a
  student taking notes live is never lost.
- **Student deck = minimal review / catch-up.** Lean, student-navigable; a student who missed something
  in class flips through it afterward to catch up. It is **not** a copy of the teacher deck and does
  **not** carry workbook slide numbers. Its only alignment obligation is **coverage**: every concept
  the teacher taught (every DI segment) must have a review slide, so no taught idea is un-reviewable.
  Coverage is owned by `history-hack-lean-deck-builder`; "same slide count as the teacher deck" is
  **not** the rule (that would make it redundant).
- **Workbook = the throughline** between them: notes are taken off the teacher deck, and those same
  notes are what let a student close gaps with the student deck later.

A role label alone is **not enough**. The student must be pointed to the **exact teacher-deck
slide(s)**, and the teacher deck must point **back to the activity number**.

**Workbook → deck (on every activity header):** name the exact slide number(s) *and* the role, e.g.

> `Activity 2 — Vocabulary Studio (Frayer) — US.45   ⏱ ~7 min   ▶ Deck · Key Vocabulary · slides 8, 16`

- **List every slide** the activity maps to. When one workbook page draws on **several** deck slides,
  say so plainly — e.g. `▶ Deck · Direct Instruction · slides 4–6 (all three on this page)`. Never
  leave the student to infer which slides.
- Keep **both** the role (durable) **and** the slide numbers (student-clear). Numbers are generated,
  never hand-typed.

**Deck → workbook (on every slide a workbook activity uses):** a back-reference cue naming the activity
**number**:

> `✍ In your workbook · Activity 2`

**Sync rule (why this needs the reproducible deck build):** the slide numbers in the workbook and the
activity numbers on the deck come from **one shared activity↔slide map**, emitted by the same build
run. Hand-typed absolute slide numbers go stale on a re-key and are forbidden — generate both sides
together so they can never disagree.

## 3. Global guardrails (LOCKED — hard-won)

1. **All student writing space is ruled.** Every place a student writes has **workbook-lined (ruled)
   writing area** — never a blank white box or open white gap. This scaffolds handwriting **and**
   closes white-space gaps: if a page has empty room, fill it with task-tied ruled lines, not blank
   space.
2. **No-bleed.** Each activity fits its allotted page(s). Nothing bleeds uncontrolled onto the next
   page. Cap image heights and table-row counts so an activity never spills a stray line/paragraph
   over the page break.
3. **Breathing room between activities.** Leave clear space after an activity ends before the next
   heading — not cramped. A visible section break, not a jammed title.
4. **Ruled space is sized to the task.** More-demanding prompts get more ruled lines; short prompts get
   fewer — so the page is full of *useful* writing space, never padded and never cramped.

## 4. Per-activity print rules

- **Activity 1 — Vocabulary Word Bank.** Front; supports on verso; header carries exact deck
  slide(s) + `Key Vocabulary`.
- **Activity 2 — Vocabulary Studio (Frayer).** Front; supports on verso. Header points to the exact
  KEY VOCABULARY slide(s); those deck slides back-ref `✍ In your workbook · Activity 2`. Frayer
  boxes are ruled writing areas.
- **Activity 3 — Cornell Notes (Direct Instruction).** Front; supports on verso. Header lists **all**
  Direct-Instruction slide numbers (often several); each of those deck slides back-refs `Activity 3`.
  The Cornell cue column keeps `▶ Deck · DI k of M`.
- **Activity 4 — Close Read.** Four required fixes:
  1. **Key Terms FIRST.** The "Key terms first: …" line goes at the **top**, *before* the reading
     (pre-teach), never underneath the CORE PATH reading box.
  2. **Breathing room after.** Add space after the Close Read before the next title — not cramped.
  3. **More writing space for the text-dependent questions.** The Close-Read Evidence Lab rows are
     **large ruled** answer areas (Evidence + Your answer), sized generously.
  4. **Fill the page with ruled space, not white.** The old white-space gap under the Evidence Lab is
     closed by enlarging the ruled answer area — never left blank.
- **Activity 5 — Primary Source / Data Analysis.** **Must not bleed to another page.** Cap the source
  image by height and keep the HIPP/analysis with it so the whole activity fits its page(s).
- **Activity 6 — Core Application: Practice Quiz — SELF-GRADING.** Print the **answer key at the bottom
  of the activity** (small, boxed/inverted "Answers" strip) so students self-check immediately, and
  **add one more question** than the prior build. Items come from the authoritative bank via
  `history-hack-unit-content-build`; this skill only requires the self-check block + the extra item.
- **Activity 7 — Constructed Response (CER).** Front; supports on verso; claim/evidence/reasoning
  answer space is ruled and generous.

## 5. Print-bundle QC gate (must pass before a workbook ships)

Run after every workbook build; fix any ✗ before release:

- [ ] **Duplex rhythm:** each activity is on a front and its supports are on that leaf's back (or the flag is single-sided).
- [ ] **Workbook→deck:** every activity header shows exact slide number(s) **and** role; multi-slide pages say which slides.
- [ ] **Deck→workbook:** every referenced deck slide carries `✍ In your workbook · Activity N`; numbers match the shared map.
- [ ] **All writing ruled:** no blank white writing box or open white gap anywhere.
- [ ] **No-bleed:** no activity spills onto an unplanned page; **Activity 5 fits**.
- [ ] **Activity 4:** key terms at top; generous ruled Evidence-Lab space; breathing room after.
- [ ] **Activity 6:** answer key printed at the bottom; one extra question vs. prior build.
- [ ] **Spacing:** clear break between each activity and the next heading (not cramped).

## 6. How this composes

- **Invoked by:** `history-hack-unit-content-build` (the content engine that emits the workbook and the
  activity↔slide map) and `history-hack-platinum-unit-builder` (the unit orchestrator).
- **Consumes:** UDL support content from `udl-cast-expert`; brand tokens from `BRAND_PALETTE.md`;
  the shared activity↔slide map that the reproducible deck build (`history-hack-tcap-deck-builder` /
  `history-hack-lean-deck-builder`) and the workbook build both read.
- **Verified by:** `history-hack-lesson-flow-qc` (deck↔workbook alignment) and
  `history-hack-print-qc-auditor` (print-defect / white-space audit). This skill defines the LAYOUT
  those gates check; it does not replace them.
