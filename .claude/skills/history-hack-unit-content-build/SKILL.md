---
name: history-hack-unit-content-build
description: "End-to-end pipeline for building a complete History Hack U.S. History **unit (Course Standard) content set** to the Platinum bar — the exact process proven on Unit 6 (WWII, US.45–US.58). This builds the **unit student workbook** (the lesson-by-lesson book: 7-activity cycle, guided Cornell notes, back-page UDL/MTSS supports, deck-aligned spine) and its companions — NOT a standalone DBQ packet (that is a separate product; use `history-hack-dbq-workbook` for the DBQ SKU). Use when asked to build, finish, remediate, or QA a unit's four-piece set: Student Workbook, Teacher How-to-Use & MTSS Guide, Student (Lean) slide deck, and Teacher (Full) slide deck; to add guided Cornell notes + the NOTES SUPPORTS ladder, add back-page UDL/MTSS supports, rewrite hooks, rebuild practice quizzes from the authoritative question bank, build the teacher answer-key guide, finalize decks to the canonical palette, or key the workbook to the deck slides. Enforces render-and-QC gates (zero blank pages), historically accurate models, bank-sourced quiz items verified by content, canonical branding, and bidirectional deck↔workbook slide-keying. Every unit also ships a Standards Alignment / Adoption Crosswalk with Social Studies Practices (SSP.01–06) + cross-curricular ELA, a UDL 3.0 (CAST, 2024) supports back page, generous notebook-lined writing space, and a tagged-PDF/UA accessibility (Schedule F 'Rubric F') gate."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.1"
  reference_implementation: "Unit 6 — World War II (US.45–US.58), Course Standard Edition"
  changelog_1_1: "Added LOCKED gates: adoption crosswalk + SSP.01–06, UDL 3.0 (CAST 2024) back page, generous notebook-lined writing space, and tagged-PDF/UA accessibility (Rubric F). New reference references/adoption-crosswalk-and-ssp.md."
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

## Canonical brand tokens (LOCKED — America 250; every piece aligns to these)

Use the **America 250 palette** — full spec in `00_START_HERE/BRAND_PALETTE.md`:
Heritage Blue `#1F3A5F` (structure) · Patriot Red `#B22234` (emphasis) · Founders Cream `#F8F5EF`
(dominant field) · Muted Gold `#C9A227` (sparingly) · writing-line `#9AA0AB`. Cream-dominant,
blue-structure, red-emphasis, gold-sparingly. The legacy tokens `#1B2A4A`/`#0A1F3C`/`#143159` (navy),
`#C89B3C`/`#C9A84C` (gold/amber), `#F7F5EF` (cream), `#C62828` (red) are **retired** — migrate any
lingering use to the canonical set (see `references/decks.md`). (Liberty Navy `#1A2332` and Phoenix
Gold `#F9A825` are *broader*-palette America 250 tokens for special surfaces, not retired.)

## Non-negotiable gates

- **DOCX-native → PDF (LOCKED — print-first):** author documents as native `.docx`
  (`build_guided_notes.py` / `build_teacher_guide.py`), then convert with LibreOffice
  (`soffice --headless --convert-to pdf`). **Never HTML→PDF** (it mangles page breaks/headers/footers/
  page numbers). The editable `.docx` is the **author's archive / master** (source of truth for future
  edits); the **PDF is what teachers receive and print** — a faithful convert, not teacher-edited.
  See `00_START_HERE/BUILD_STANDARD.md` §4.
- **Render-and-QC gate:** no workbook/guide/deck change ships until it is rendered to PDF and
  inspected page-by-page. **Zero blank or near-empty pages**; page breaks, header/footer, and the live
  page-number field survive the convert. See `references/rendering-and-qc.md`.
- **Historical accuracy:** every model answer (HIPPO analysis, CER model), quiz item, and
  answer key is verified against the record. Run `historian-factcheck-agent` on new prose.
- **Bank-sourced assessments:** practice-quiz items come from the authoritative bank, verified
  on-topic by content — never auto-trusted by code, never silently authored to fill gaps
  without saying so.
- **One product:** canonical palette everywhere; the workbook and Student deck key to each other
  on every standard.
- **Data visualization (build wherever content warrants):** where a standard carries quantitative or
  spatial data, generate an **original, accurate, sourced chart/graph** (bar/line/pie/histogram or a
  point-location map schematic on a PD basemap) programmatically from a **verified dataset** — used as
  a read-the-data stimulus AND a student create/represent move. Do not ration them. Every chart carries
  a citation sidecar (source/date/units/N), **alt text + a plain data-table fallback** (WCAG 2.2 AA),
  honest axes (zero-baseline bars, labeled units), and is grayscale-legible. No invented numbers. See
  `00_START_HERE/STUDENT_WORKBOOK_PLATINUM_STANDARD.md` §7.11.
- **Schedule F grounds everything (LOCKED — Sean):** the TDOE Social Studies Schedule F rubric is
  the running standard for all work, not a final gate. **Every completed section ships its own
  `SCHEDULE_F_SELF_SCORE.md`** (honesty doctrine: score as-built, hold indicators low on principle,
  accuracy is foundational per Policy 2.600 — a known factual error blocks "fully met"). Sub-sections
  score only the indicators they touch; unit deliverables get full Tables 2–4 (/36). Resolve
  critical/major deficiencies before a section is "done." See `references/schedule-f-self-score.md`;
  the `tn-textbook-adoption-agent` skill runs the formal panel review.
- **Adoption crosswalk + Social Studies Practices (LOCKED):** every unit ships a **Standards
  Alignment / Adoption Crosswalk** listing, per standard: the **verbatim TDOE standard**, the
  **Social Studies Practices (SSP.01–SSP.06)** it exercises, cross-curricular **TDOE ELA** links,
  DOK coverage, and a reviewer-assurances block (accuracy/Policy 2.600, bias, copyright/PD sources,
  accessibility, conventions). SSP appears in the workbook's alignment front-matter **and** the
  crosswalk. See `references/adoption-crosswalk-and-ssp.md`.
- **UDL 3.0 (CAST, 2024) back page (LOCKED):** every student workbook carries a dedicated **UDL 3.0
  supports page on the verso/back** — the three-principle crosswalk (Engagement / Representation /
  Action & Expression) naming the real affordances the book delivers, with the citation *CAST (2024).
  Universal Design for Learning Guidelines version 3.0.* This is **in addition to** the per-standard
  NOTES SUPPORTS ladder. Use the 3.0 names, never 2.x. (Design owner: `udl-cast-expert`.)
- **Generous notebook-lined writing space (LOCKED):** every write-in activity gives students real
  room — ruled **notebook lines** built as a borderless table with per-row bottom borders
  (`notebook_table()`), sized to the task, never a single cramped line (regression guard on the
  "too compact" feedback). See `references/guided-notes-and-supports.md`.
- **Accessibility / Rubric F gate (LOCKED):** the delivered PDF is a **tagged PDF/UA** export
  (`/Lang`, Title, `MarkInfo/Marked`, `DisplayDocTitle`) with complete **alt text**, logical reading
  order, **WCAG 2.2 AA** contrast, and large-print/screen-reader friendliness; bilingual parity where
  the edition requires it. Run **`accessibility-qc-agent`** as the terminal gate before release
  (Section 508 / ADA Title II / Schedule F "Rubric F" accessibility).
- Keep work on the designated branch; gated approval before release.

## Editions (absorbed from `course-standard-student-workbook` — one engine, five editions)

The workbook engine emits a **universal Cornell + 7-activity spine** that renders as five editions from the same source content — never five hand-built books:

- **Base** — the standard student edition.
- **Support (MTSS Tier 2/3)** — verso NOTES SUPPORTS default-on, denser scaffolds, fading held earlier.
- **EL (WIDA)** — English/Spanish parity, cognates, sentence frames, simplified glosses (route ELL-specific review through `ell-bilingual-review-specialist`).
- **Modified (IEP/504)** — reduced item counts, extended response space; supports add paths, never lower the ceiling; never a substitute for the IEP/504 itself.
- **Honors/Extension** — extension prompts, independent-fade Cornell, deeper CER.

Editions are a **print/render flag on the same source**, consistent with the "lighter book = print flag" rule (verso supports are never relocated out of the student book; §7.9a). Do not fork content per edition — parameterize.

## Required skill composition

Load as applicable: `instructional-design-specialist`, `udl-cast-expert`,
`ell-bilingual-review-specialist`, `accessibility-qc-agent`, `historian-factcheck-agent`,
`tn-textbook-adoption-agent`, `tn-assessment-specialist` (all assessment items — supersedes the
retired `tcap-item-writer-v2`), `spaced-repetition-engine` (spaced retrieval scheduling),
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
