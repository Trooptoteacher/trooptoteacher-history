# U.S. History Hack™ — Course Standard (Platinum) build system

Reproducible source + guardrails + Unit 1 deliverables for the platinum curriculum system,
authored to the canonical Unit 5 template. © 2026 TroopToTeacher Technologies LLC.

## Folders
- **build/** — the generators (docx-js `.js` + Python render/data). Run from a dir with `analysis/`,
  `assets/primary_sources/`, and the unit JSON:
  - `build_workbook.js` — Student Workbook (7 activities/standard; Cornell paired to the deck; HIPPO;
    CER; exit tickets; doodle zones; print-safe images).
  - `build_teacher_guide.js` — Teacher How-to-Use & MTSS Guide (SSP + dimension crosswalks, 6-pt CER
    rubric, answer keys, exit-ticket keys + "What's Next" reteach).
  - `build_assessment_book.js` — Formative checkpoints · Summative Form A/B · Teacher Key/Analysis/Reteach.
  - `build_organizer_toolkit.js` — reproducible Graphic Organizer Toolkit.
  - `build_cover.js` — sale-ready **Cover Wrap** (front · spine · back + print/listing spec).
  - `preflight.py` — 11 release checks (standards verbatim, no answer leak, de-bias, citations+alt,
    crosswalks, disclosures, no "WCS").
  - `uno_fields.py <in.docx> <baked.docx> <out.pdf>` — bakes TOC page numbers + renders PDF (3 args).

## Guardrails (source of truth)
- **Standards + "I can" targets** — verbatim from the state standards column and the instructional
  guide's right-hand column. **Never print "WCS."**
- **Primary sources / images** — pulled only from the canonical bank in `history-hack-web-app`
  (`public/data/us-history/primary-sources/…`, `questions/…`); every image cited (Chicago) + alt text.
- **Print-safe images** — the interior prints black-and-white. Photos, engravings, and line cartoons
  are safe. When color *encodes* meaning (shaded/choropleth maps), mark the record `colorKey:true`:
  the build prints a "view the full-color version on the projection slide" note and the color original
  lives in the deck. Flagged in Unit 1: the 1890 railroad map (US.01) and the 1890 foreign-born map (US.06).
- **Answer keys are teacher-side only; de-bias answer positions; verify by rendering; pre-field-test
  disclosure on all assessment items.**

See `guardrails/SKILL.md` for the full rule set; the Claude skill
`history-hack-course-standard-builder` carries the same memory.

## Unit 1 deliverables (`deliverables_unit1/`)
Student Workbook (90 pp) · Teacher Guide · Assessment Book · Graphic Organizer Toolkit · Cover Wrap.
Decks are generated separately (PPTX) and omitted here for size.
