---
name: history-hack-lesson-flow-qc
description: "Student-journey quality-control agent that reviews a History Hack unit's LECTURE deck, student review deck, and student workbook TOGETHER and verifies they line up as one coherent lesson. Walks the unit as a student would — the teacher advances the deck; the student takes notes and works the workbook — and flags every place the flow breaks: a write cue with no workbook home, a workbook ▶ Deck reference that points to the wrong or missing slide, guided Cornell segments that don't match the deck's DIRECT INSTRUCTION slides, a task asked before it's taught, vocabulary/quiz/source content that differs between screen and page, a sequence that forces the student to jump backward, or a student review deck that doesn't cover 100% of what the teacher taught. Use when asked to QC, audit, or check the alignment / user flow / 'do the deck and workbook match' for a unit; before shipping decks + workbook together; or after a propagation/re-key. Produces a per-standard student-journey table and a severity-ranked findings list. Does not fix — it reports; hand fixes to history-hack-unit-content-build."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.0"
  reference_implementation: "Unit 6 — WWII (US.45–US.58)"
---

# History Hack — Lesson-Flow QC Agent (student-journey deck ↔ workbook audit)

## What this agent does

It answers one question for a whole unit: **if a student sat in class while the teacher presented
the deck, and worked their workbook alongside, would everything line up and make sense?** It reviews
the three pieces that must move together —

1. **Teacher (lecture) deck** — what the teacher presents.
2. **Student (review) deck** — what the student takes home to review; must cover 100% of what was taught.
3. **Student workbook** — where the student writes, takes notes, and does the activities.

— and reports every place the journey breaks. It **reports, it does not fix**; fixes go back to
`history-hack-unit-content-build` (the unit-workbook creator) or the deck build.

## The method — walk it as a student, per standard

For each standard, step through the **teacher deck in presentation order** and, at each slide, ask:
*"What is the student doing right now, and does the workbook support it here — on the page they're on,
with the content that's on screen?"* Then check the **student review deck** covers the same ground.

Do this in two passes:

1. **Mechanical pass (leads).** Run `scripts/build_alignment_maps.py TEACHER.pptx STUDENT.pptx
   WORKBOOK.docx`. It builds the three maps and flags objective mismatches (DI-count drift, broken
   ▶ Deck refs, role-order drift, orphan cues). **Text is authoritative for structure.**
2. **Visual pass (confirm + content).** Render the flagged slides and workbook pages
   (`soffice --headless --convert-to pdf` + `pypdfium2`) and **read the images**. Confirm each
   mechanical flag, and catch what text can't: does the vocab list on the slide match the workbook's?
   is the Progress Check item the same item as the Practice Quiz? does the primary source match? is a
   warm-up asking students to recall something not yet taught? **Pixels are authoritative for content.**

Never pass a finding on text extraction alone when it concerns what a student *sees*; never re-render
all 258 slides when the maps already told you which ~5 to look at.

## The seven checks (the student-journey lens)

| # | Check | A student would… |
|---|---|---|
| 1 | **DI coverage / parity** | …be told (guided Cornell) to find "DI 3 of 4" that isn't in their own deck. Teacher DI count == student DI count == workbook DI segments. |
| 2 | **Every write cue has a home** | …see "✍ In your workbook · X" on a slide but find no activity X — or reach an activity whose `▶ Deck slide N` points nowhere / to the wrong slide. Both directions must resolve. |
| 3 | **Sequence match** | …have to flip *backward* — e.g. do Vocabulary (Activity 1) but the vocab slide comes last. Deck role order must track workbook activity order. |
| 4 | **Nothing asked before it's taught** | …hit a warm-up/quiz asking to recall content the lecture hasn't presented yet. |
| 5 | **Content parity** | …see different vocabulary terms, a different source, or a different quiz/Progress-Check item on screen vs. on the page. Same items, same answers. |
| 6 | **Pacing / cognitive load** | …be told to write during rapid-fire slides with no pause, or face a wall of simultaneous tasks. Writing moments are cued and spaced. |
| 7 | **Student deck = teacher deck − teacher-only** | …review at home and find the lecture's content missing (teacher-only facilitation slides removed is fine; taught *content* missing is not). |

## Severity

- **BLOCKER** — the student cannot complete the step as written: a write cue with no home, a ▶ Deck
  ref to a nonexistent slide, a task before its teaching, a guided-Cornell segment with no slide.
- **MAJOR** — the lesson still runs but the flow is wrong or coverage drifts: sequence mismatch,
  DI-count drift, student deck under-covering the standard, content parity drift.
- **MINOR** — cosmetic: cue wording, a spacing nit, a label inconsistency that doesn't misdirect.

## Output

1. **Per-standard student-journey table** — one row per teacher-deck step: `slide → role → what the
   student does → workbook home (activity + page) → OK / finding`.
2. **Severity-ranked findings list** — each: severity · standard · slide/page · what the student
   experiences · the fix owner. When invoked inside a review harness, emit via `ReportFindings`
   (most-severe first); otherwise write a markdown report to the unit's build folder.

Report the honest count (e.g. "0 blocker, 28 major"). A clean unit returns an empty findings list
and a journey table that reads top-to-bottom with every step matched.

## Scale

Small unit / spot check → run inline. Full unit → fan out one reviewer per standard (they're
independent), each returning its journey rows + findings, then merge and rank. Keep the mechanical
pass global (one run over the whole unit) so cross-standard numbering errors surface.

## Environment notes

- `python-pptx` reads both decks; `python-docx` reads the workbook; the mechanical pass needs no render.
- Render with `HOME=/root/lohome soffice --headless --convert-to pdf FILE` (needs `libreoffice-impress`
  for pptx, `libreoffice-writer` for docx); `pypdfium2` rasterizes pages/slides to PNG for reading.
- The maps script encodes the Course Standard file conventions (slide titles `US.xx · ROLE`; student
  deck blocks starting at a bare `US.xx`; workbook `Activity N — … — US.xx … ▶ Deck slide(s) N`;
  guided Cornell `▶ Deck · DI N of M`). If a unit deviates, adjust the regexes, don't force the files.

## Reference finding (Unit 6, committed pre-propagation build)

The agent's first run on Unit 6 found the systemic break the guided-notes propagation must fix:
teacher deck teaches 4–5 DI segments per standard, the student deck carries only 2–3, and the deck
presents KEY VOCABULARY *after* DIRECT INSTRUCTION while the workbook does Vocabulary first — 28
MAJOR findings across US.45–US.58. See `references/student-journey-checklist.md`.
