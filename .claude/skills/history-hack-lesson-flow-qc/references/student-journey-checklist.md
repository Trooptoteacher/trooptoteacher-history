# Student-journey checklist (the audit, step by step)

Run this per standard, in teacher-deck presentation order. The goal is a journey a student can
follow without ever being confused, stuck, or sent backward.

## Before you start
- [ ] Confirm the three files: teacher (lecture) deck, student (review) deck, student workbook.
- [ ] Run `scripts/build_alignment_maps.py TEACHER STUDENT WORKBOOK` → get the maps + mechanical flags.
- [ ] Note the student deck's total slide count (for resolving ▶ Deck refs).

## Step 0 — build the Workbook → Exact-Slide mapping table FIRST (the primary artifact)
Anchor on the **student workbook**. Before the narrative walk, produce the per-standard mapping table —
one row per workbook activity, each resolved to an **exact slide number**:

`activity · workbook page · exact student-deck slide # · exact teacher-deck slide # · content-match? · reached-in-order? · OK/finding`

The test is "can a student follow along with zero guesswork?" **Any of these is a finding:**
- an activity that resolves to no slide, or to a *range* where one specific slide is meant, or where it's unclear "which one";
- a `▶ Deck slide N` that points to the wrong slide or a nonexistent one;
- a slide's `✍ In your workbook · X` with no matching activity X;
- the mapped slide's content differing from the activity (different vocab/source/item);
- an activity whose slide sits earlier than the previous activity's (backward jump).

A clean standard = every activity row resolves to an exact slide, content matches, in order.

## The walk (each teacher-deck slide is one step)
For every slide, in order:
- [ ] **Role clear?** Title names its role (HOOK, DIRECT INSTRUCTION, PRIMARY SOURCE, PROGRESS CHECK…).
- [ ] **Student action?** Is the student watching, discussing, or writing? If writing —
  - [ ] the slide shows a `✍ In your workbook · <activity>` cue (student deck) or notes cue (teacher deck);
  - [ ] that activity exists in the workbook, and its `▶ Deck` reference points back to *this* slide;
  - [ ] the workbook has somewhere to write it (lines, table, or an explicit notebook redirect).
- [ ] **Taught before asked?** Nothing on this slide asks for content a *later* slide teaches.
- [ ] **Content parity?** Terms / source / item shown here match the workbook's version verbatim
      (same vocabulary, same primary source, same quiz/Progress-Check item + answer).

## Guided Cornell ↔ DIRECT INSTRUCTION (the spine)
- [ ] Count teacher-deck DI slides for the standard = M.
- [ ] The workbook's Activity 3 cue column has exactly M segments, `DI 1 of M … DI M of M`, and their
      topics match the DI slide titles **in the same order**.
- [ ] The **student** deck has M DI slides too (so "DI k of M" always has a home when the student reviews).
- [ ] Each DI segment's guiding question is answerable from that DI slide's content.

## Sequence (no backward jumps)
- [ ] Student-deck role order tracks workbook activity order: Vocabulary → (Vocab Studio) → Cornell/
      Close Read → Primary Source → Practice Quiz/Progress Check → CER. Vocabulary must not trail content.
- [ ] Teacher-deck teacher-only slides (QUICK REVIEW, CONFIDENCE CHECK, PEOPLE WHO SHAPED, facilitation)
      may exist without a workbook home — but must not sit *between* a task cue and its workbook activity
      in a way that makes the student flip past unrelated screens mid-task.

## Student deck coverage (100% of what was taught)
- [ ] Every piece of *content* the teacher taught appears in the student deck (teacher-only facilitation
      and answer-reveal slides removed is correct; taught content missing is a finding).
- [ ] The "How This Deck Works / UDL-MTSS legend" is not a student-facing lecture slide in the middle
      of a standard (move to an appendix or remove — per Sean).

## Pacing
- [ ] Writing moments are cued and spaced, not stacked on rapid content slides.
- [ ] Exit ticket / Progress Check falls at the end of the standard, after its teaching.

## Record each finding as
`severity · US.xx · deck slide N / workbook p.P · what the student experiences · fix owner`

## Reference run — Unit 6 committed pre-propagation build (2026-08)
Systemic, every standard:
- **MAJOR — DI under-coverage:** teacher deck 4–5 DI slides vs. student deck 2–3. Student review deck
  does not cover 100% of what was taught; once the guided Cornell keys `DI 1..4`, "DI 4 of 4" has no
  home in the student deck.
- **MAJOR — vocab sequence flipped:** student deck presents KEY VOCABULARY after DIRECT INSTRUCTION,
  but the workbook does Vocabulary as Activity 1–2 (first). Student is sent backward.
- **Note:** the committed workbook keys Cornell to `▶ Deck slides 3–5` (student-deck numbers), so a
  student following the *teacher's* lecture (different counts/numbers) can't use those references.
- Fix owner: `history-hack-unit-content-build` propagation + deck re-key (rebuild the student deck as
  the teacher deck minus teacher-only slides; make DI counts match; move vocab before content; re-key
  workbook to the shared sequence). Re-run this agent until it returns 0 blocker / 0 major.
