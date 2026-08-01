---
name: history-hack-unit-content-build
description: "End-to-end pipeline for building a complete History Hack U.S. History unit content set to the Course Standard (Platinum) bar — the exact process proven on Unit 6 (WWII, US.45–US.58). Use when asked to build, finish, remediate, or QA a unit's four-piece set: Student Workbook, Teacher How-to-Use & MTSS Guide, Student (Lean) slide deck, and Teacher (Full) slide deck; to add back-page UDL/MTSS supports, rewrite hooks, rebuild practice quizzes from the authoritative question bank, build the teacher answer-key guide, finalize decks to the canonical palette, or key the workbook to the deck slides. Enforces render-and-QC gates (zero blank pages), historically accurate models, bank-sourced quiz items verified by content, canonical branding, and bidirectional deck↔workbook slide-keying."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.0"
  reference_implementation: "Unit 6 — World War II (US.45–US.58), Course Standard Edition"
---

# History Hack — Unit Content Build

## Purpose

Repeat, for any unit, the exact end-to-end pipeline proven on Unit 6 to produce a
self-consistent **four-piece Course Standard set**:

1. **Student Workbook** — editable `.docx` + print `.pdf`
2. **Teacher How-to-Use & MTSS Guide** — `.docx` + `.pdf`
3. **Student (Lean) Slide Deck** — `.pptx`
4. **Teacher (Full) Slide Deck** — `.pptx`

The set must read as **one product**: shared canonical palette, shared standard-code spine,
and **bidirectional deck↔workbook slide-keying** (workbook prints `▶ Deck slide N`; deck shows
`✍ In your workbook · <activity>`).

This skill is the *orchestration* layer. It composes the locked standards and the specialist
skills below; it does not restate their internal logic.

## Authoritative inputs (source of truth, in order)

1. `00_START_HERE/STUDENT_WORKBOOK_PLATINUM_STANDARD.md` — workbook geometry, palette, section
   order, white-space rules, response-space rules, per-standard anatomy, QC gate.
2. `00_START_HERE/SLIDE_DECK_PLATINUM_STANDARD.md` — deck geometry, palette, chip system,
   per-standard slide arc, and the deck↔workbook keying contract (§1).
3. `00_START_HERE/PLATINUM_REFERENCE_BUILD/` — the locked reference exemplar (Unit 6 US.45).
   Clone its structure; never diverge from it silently.
4. The **authoritative question bank** in the `history-hack-web-app` repo:
   `public/data/us-history/questions/unit-N/dok-{1,2,3}.json` (~4,760 items, IRT-parameterized,
   with `correctAnswer`, bilingual choices, `standardCodes`, `explanation`). See
   `references/quiz-sourcing.md` — **its `standardCodes` use an older numbering; match by content.**

## Canonical brand tokens (LOCKED — every piece aligns to these)

Navy `#1B2A4A` · Red `#B22234` · Gold `#C89B3C` · Card `#F7F5EF` · writing-line `#9AA0AB`.
Deck tokens `#1A2332` (navy), `#C9A84C`/`#F9A825` (gold/amber), `#C62828` (red) are **deprecated**
and migrate to the canonical set (see `references/decks.md`).

## Non-negotiable gates

- **Render-and-QC gate:** no workbook/guide/deck change ships until it is rendered to PDF and
  inspected page-by-page. **Zero blank or near-empty pages.** See `references/rendering-and-qc.md`.
- **Historical accuracy:** every model answer (HIPPO analysis, CER model), quiz item, and
  answer key is verified against the record. Run `historian-factcheck-agent` on new prose.
- **Bank-sourced assessments:** practice-quiz items come from the authoritative bank, verified
  on-topic by content — never auto-trusted by code, never silently authored to fill gaps
  without saying so.
- **One product:** canonical palette everywhere; the workbook and Student deck key to each other
  on every standard.
- Keep work on the designated branch; gated approval before release.

## Required skill composition

Load as applicable: `instructional-design-specialist`, `udl-cast-expert`,
`ell-bilingual-review-specialist`, `accessibility-qc-agent`, `historian-factcheck-agent`,
`tn-textbook-adoption-agent`, `tn-assessment-specialist` / `tcap-item-writer-v2`,
`office/docx`, `office/pptx`, `office/pdf`.

## The pipeline (phase order matters)

Read `references/pipeline.md` for the detailed, ordered playbook. Summary:

0. **Intake & audit.** Confirm unit number, standard codes, and locate existing assets
   (workbook docx, decks pptx, bank). Never recreate a strong existing asset — assess first.
1. **Workbook — structure & blank-page fix.** Get to a clean N-standard book with the full
   7-activity cycle and **zero blank pages**. See `references/workbook-methods.md`.
2. **Workbook — guided notes + back-page supports.** (a) Make Activity 3 a **guided Cornell**:
   seed the cue column with the standard's direct-instruction segments in lecture order
   (`▶ Deck · DI N of M`, keyed to the teacher deck), and build its verso **NOTES SUPPORTS
   ladder** (frames → cloze + word bank → how-to + model → try-it on lined notebook paper +
   self-check rubric). Script: `scripts/build_guided_notes.py`; design + the two locked
   formatting lessons in `references/guided-notes-and-supports.md`. (b) Add the other three verso
   supports (Vocabulary, HIPPO, Writing) by cloning the reference blocks and swapping in
   **standard-specific, accurate** models; consolidate the exit ticket onto the Writing Supports
   page. Script: `scripts/build_backpage_supports.py`.
3. **Workbook — per-standard content.** Rewrite verbatim hooks into engaging openers; rebuild
   Activity 6 practice quizzes from the bank (4 verified items + on-page self-check key per
   standard). See `references/quiz-sourcing.md`.
4. **Teacher Guide.** Generate the How-to-Use & MTSS Guide (pacing across the 46/43/41-min
   variants, UDL/MTSS, CER rubric, per-standard quiz + exit-ticket keys with rationale, reteach).
   Script: `scripts/build_teacher_guide.py`.
5. **Decks — finalize.** Assess existing decks (usually keep, don't recreate); migrate palette to
   canonical; unify stray accents; fix known layout defects (e.g., long DIRECT INSTRUCTION titles).
   See `references/decks.md`.
6. **Slide-keying (bidirectional).** Add `▶ Deck slide N` to every workbook activity (computed
   from the deck's real slide positions) and `✍ In your workbook · <activity>` to matching deck
   slides (on-slide for the Student deck; speaker notes for the Teacher deck). See
   `references/slide-keying.md`.
7. **Final QA & commit.** Full contact-sheet review of each piece; validate decks; commit each
   piece to its `00_START_HERE/UNITn_*_BUILD/` folder with a STATUS.md; push.

## Output folder convention

```
00_START_HERE/
  UNITn_STUDENT_WORKBOOK_BUILD/   Unit_n_Student_Workbook_CourseStandard.{docx,pdf} + STATUS.md
  UNITn_TEACHER_GUIDE_BUILD/      Unit_n_Teacher_Guide_CourseStandard.{docx,pdf} + build script + STATUS.md
  UNITn_DECKS_BUILD/              Unit_n_{Student,Teacher}_Deck_CourseStandard.pptx + STATUS.md
```
Each STATUS.md records what's in the folder, how it was made, sources, and remaining work.

## Environment notes (learned the hard way)

- LibreOffice needs the right module: `libreoffice-writer` for docx, `libreoffice-impress` for
  pptx. Convert with `HOME=/root/lohome soffice --headless --convert-to pdf FILE` (sandbox off).
- `pypdfium2` renders PDF pages for blank-page detection and contact sheets; `python-docx` and
  `python-pptx` for structural edits; `defusedxml` for the pptx skill scripts.
- python-pptx reads a deck that LibreOffice refuses only because the Impress module is missing —
  install it before concluding a file is corrupt.

## Completion report

Report per piece: page/slide counts, blank-page status (must be zero), standards covered, sources
used (bank paths + fact-check status), and remaining blockers. Never mark a file complete on a
manifest entry alone — it must render and pass the page-by-page gate.
