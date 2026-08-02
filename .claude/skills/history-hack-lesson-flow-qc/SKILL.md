---
name: history-hack-lesson-flow-qc
description: "Student-journey quality-control agent (the 'student QC expert') that follows the decks ALONGSIDE the student workbook and verifies the student can follow the lesson with everything DIRECTLY MAPPED from the workbook to the EXACT slides. Anchored on the student workbook, it walks the unit as a student would — the teacher advances the deck; the student takes notes and works the workbook — and confirms every workbook activity resolves to a specific slide number, in order, unambiguous, easy to follow. Flags every break: a workbook activity with no exact slide (or a ▶ Deck reference to the wrong/missing slide), a write cue with no workbook home, guided Cornell segments that don't match the deck's DIRECT INSTRUCTION slides, a task asked before it's taught, vocabulary/quiz/source content that differs between screen and page, a sequence that forces the student to jump backward, or a student review deck that doesn't cover 100% of what the teacher taught. Use when asked to QC, audit, or check the alignment / user flow / 'do the deck and workbook match' / 'can a student follow along' for a unit; before shipping decks + workbook together; or after a propagation/re-key. Produces a per-standard WORKBOOK→EXACT-SLIDE mapping table + a student-journey table + a severity-ranked findings list. Does not fix — it reports; hand fixes to history-hack-unit-content-build."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.1"
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

## The core job (LOCKED — Sean): the student follows the workbook, directly mapped to exact slides

**Anchor on the STUDENT WORKBOOK.** The student QC expert follows the deck **alongside the student
workbook**, activity by activity, and confirms the student can follow along with **zero guesswork**:
**every workbook activity maps to an EXACT slide (a specific number), in order, unambiguous, easy to
follow.** "Easy to follow" is a pass/fail bar, not a nicety — if a student has to hunt for the slide,
guess which slide an activity means, jump backward, or land on a slide whose content doesn't match the
activity, that is a finding.

The deliverable that proves it is the **Workbook → Exact-Slide mapping table** (see Output): one row
per workbook activity, per standard, resolving to the precise slide number(s) — in the student deck
(for at-home review) and consistent with the teacher deck's lecture order (for in-class).

## The method — walk it as a student, per standard

Anchored on the workbook, step through it **in workbook order** (Activity 1 → 7 + opener + exit
ticket) and, for each activity, resolve the **exact slide** it maps to and confirm the student lands
there cleanly. Cross-walk against the **teacher deck in presentation order** to confirm the same
sequence holds in class, and confirm the **student review deck** carries every mapped slide (100% of
what was taught). At each step ask: *"On the page the student is on, does the named slide exist, is it
the right one, is its content the same, and did the student reach it without flipping backward?"*

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
| 2 | **Direct workbook→exact-slide mapping** | …reach a workbook activity and not know which slide it means, or its `▶ Deck slide N` points nowhere / to the wrong slide, or a slide's "✍ In your workbook · X" finds no activity X. **Every activity must resolve to a specific slide number, both directions, no ambiguity.** |
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

1. **Workbook → Exact-Slide mapping table (primary deliverable)** — per standard, one row per
   workbook activity (opener · Vocab 1–2 · Cornell/Close Read 3–4 · Source 5 · Quiz 6 · CER 7 ·
   exit ticket): `activity · workbook page · exact student-deck slide # · exact teacher-deck slide # ·
   content-match? · reached-in-order? · OK / finding`. Every cell must resolve to a specific slide —
   a blank, a range where a single slide is meant, or a "which one?" is itself a finding.
2. **Per-standard student-journey table** — one row per deck step: `slide → role → what the student
   does → workbook home (activity + page) → OK / finding`.
3. **Severity-ranked findings list** — each: severity · standard · slide/page · what the student
   experiences · the fix owner. When invoked inside a review harness, emit via `ReportFindings`
   (most-severe first); otherwise write a markdown report to the unit's build folder.

Report the honest count (e.g. "0 blocker, 28 major"). **A clean unit = the mapping table is 100%
resolved (every activity → an exact slide, content matches, in order) with an empty findings list.**

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
