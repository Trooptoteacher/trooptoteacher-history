# Social Studies Hack — Cradle-to-Grave Course Production Workflow

**Purpose.** A single, repeatable pipeline to build ANY Social Studies Hack course
to U.S. History Hack quality — identical format, frameworks, web-app features,
testing, and QC. Inherits [`SOCIAL_STUDIES_CORE_GUARDRAILS.md`](./SOCIAL_STUDIES_CORE_GUARDRAILS.md)
(non-negotiable rules) and the format layer in [`SKILL.md`](./SKILL.md).

**The suite (5 foundation courses):**
1. **U.S. History Hack** — `US.xx` — *the reference build (done).*
2. **Government Hack** — U.S. Government & Civics `GC.xx`
3. **World History Hack** — World History & Geography `W.xx`
4. **Eighth Grade History Hack** — Grade 8 U.S. History `8.xx`
5. **Tennessee History Hack** — TN-focused standards

Every course is built the same way and ships the same inventory below.

---

## THE FULL PER-COURSE INVENTORY (what "done" means)

Per **unit** (× all units in the course), authored to the exact frameworks used
for U.S. History Hack — **UDL 3.0 / CAST 2024**, MTSS, 6-point CER, 5-element
HIPPO, de-biased keys, print-safe:

| # | Deliverable | Format | Builder / Skill |
|---|---|---|---|
| 1 | **Student Workbook** (Course Standard) | DOCX + PDF | `build_workbook.js` · course-standard-builder |
| 2 | **Teacher Workbook** (How-to-Use & MTSS guide) | DOCX + PDF | `build_teacher_guide.js` |
| 3 | **Student (Lean) Slide Deck** | PPTX + PDF | `build_student_deck.py` |
| 4 | **Teacher (Full) Slide Deck** | PPTX + PDF | `build_teacher_deck.py` + teacher-deck-workbook-aligner |
| 5 | **Teacher Graphic Organizer Toolkit** | DOCX / Canva | `build_organizer_toolkit.js` |
| 6 | **Unit Assessment Book** (Formative · Summative A/B · Key + Item Analysis + Reteach) | DOCX + PDF | `build_assessment_book.js` · question-forge |
| 7 | **Cover Wraps** (front · spine · back, per book) | DOCX + PDF | `build_cover.js` |
| 8 | **TEAM Lesson Plans** (per standard) | DOCX + PDF | `lesson_plans/build_lessonplans.js` |
| 9 | **History Hack Narrative Textbook** — same flight crew + **Flight Logs**, UDL 3.0 / CAST 2024 | Web + PDF | narrative builder · comic-script-creator |
| 10 | **DBQ Book** — *built LAST* | DOCX + PDF | question-forge · adoption-agent |

Per **course** (once):

| # | Deliverable | Builder / Skill |
|---|---|---|
| 11 | **Standards alignment + crosswalks** (SSP, dimension, TCAP/EOC) | derive + course-standard-builder |
| 12 | **Source & Asset Catalog + Crosswalk** (primary sources, images, maps, charts → standards; geo positions; citations + licenses) | `asset_standards_crosswalk.py` + `geo_provenance.json` |
| 13 | **Schedule F self-assessment + adoption package** (manifests, SHA-256) | tn-textbook-adoption-agent |
| 14 | **Web app integration** — narrative reader, library, assignments, gradebook, PLC, tools — **feature parity with U.S. History Hack** | history-hack-website-builder · learning-experience-designer |
| 15 | **Testing** — test suite (vitest/axe) + **seeded testing database** — parity | website-builder |

---

## THE PIPELINE (phases, gates, owners)

Each phase has a **hard gate** that must pass before the next begins.

**Phase 0 · Course setup & standards ingest**
- Create the course tree (`build_unit*/` layout). Extract the **official state
  standards verbatim** (text + codes); set the code prefix. Build the unit map.
- *Gate:* every standard captured verbatim; standards range confirmed.

**Phase 1 · Content derivation**
- Per unit: derive the grounded `*_content.json` (I-CAN, criteria, vocab, text
  primary sources, CFU keys **de-biased**, TN connection, `geo` + `geo_places`
  where the standard calls for geography).
- *Gate:* de-bias parity test passes; every geography standard has `geo_places`.

**Phase 2 · Sourcing & asset crosswalk**  ← *the sourcing backbone*
- **Ingest the course's completed sourcing spreadsheet first** (these already exist
  in Drive per course — e.g. `Government_Hack_Primary_Source_Sourcing_List_Completed.xlsx`
  with a verified Download Manifest: title, creator, date, repository, citation,
  rights, MIME, dimensions, SHA-256). Run `ingest_sourcing_list.py <xlsx> <course>_images.json`
  to load them into the asset catalog — **do not re-source what is already cited.**
- Then fill any remaining gaps: populate `*_images.json` asset records (file,
  medium, title, creator, year, **citation**, **rights/license**, alt). Author **maps** for every geography standard and
  **charts/graphs** where data is used. Capture **geographic positions** in
  `geo_places`. Fill `geo_provenance.json` with **authoritative citations only —
  no tertiary encyclopedias**.
- *Gate:* `asset_standards_crosswalk.py --strict` passes (every standard has a
  primary source; every asset cited + licensed; every geo standard has positions
  and a map). `geo_review_audit.py` shows no tertiary sources.

**Phase 3 · Build print deliverables** (#1–8)
- Run the course-standard builders; render; white-space audit; fix; re-bake TOC.
- *Gate:* `history-hack-print-qc-auditor` clean; format identical to reference.

**Phase 4 · Narrative textbook** (#9)
- Same **flight crew + Flight Logs**, UDL 3.0 / CAST 2024. Reader + PDF.
- *Gate:* accuracy + SME review; reading level + UDL supports verified.

**Phase 5 · Assessment authoring** (#6 items, banks)
- Use the **assessment-writer skills** (question-forge) → item banks, forms,
  keys, item analysis, reteach routing. **Fact-check every item.**
- *Gate:* DOK balance, key de-bias, standards coverage, answer-accuracy check.

**Phase 6 · Web app + testing parity** (#14–15)
- Wire the course into the app with the **same features**; seed the **testing
  database**; port the **test suite** (vitest + axe).
- *Gate:* all tests green; accessibility (axe) clean; feature parity checklist.

**Phase 7 · QC / fact-check / SME sign-off**
- Copyright/IP + license audit (copyright-integrity-accreditation); historical
  accuracy + **external SME sign-off** (`geo_review`/content review → approved);
  print QC; accessibility.
- *Gate:* Schedule F self-assessment complete; all reviews `sme_approved`.

**Phase 8 · DBQ Book** (#10) — *last*
- Author DBQs from the vetted source catalog (Phase 2) + assessment frameworks.
- *Gate:* every DBQ document cited/licensed; rubric-aligned; fact-checked.

**Phase 9 · Adoption package**
- Assemble all artifacts + reports + `SHA256_MANIFEST.txt`; zip; deliver.

---

## QUALITY GATES (must ALL pass to ship a course)

- `asset_standards_crosswalk.py --strict` — sourcing/asset coverage
- `geo_review_audit.py --require-approved` — geography sourced + SME-approved, no tertiary
- De-bias parity test — assessment keys
- `history-hack-print-qc-auditor` — print-safety/layout
- axe + vitest — web app accessibility + tests
- Schedule F self-assessment — adoption criteria
- External SME sign-off + fact-check — accuracy
- Copyright/IP + license audit — every source/asset cleared

---

## 5-DAY EXECUTION PLAN (4 new courses to reference quality)

DBQs are **last across all courses**. Web-app + testing parity runs in parallel
with print builds once content is derived. Realistic sequencing:

- **Day 1 — Government Hack:** Phase 0–2 (standards ingest, content derive,
  sourcing/asset crosswalk + provenance). Start World History Phase 0 in parallel.
- **Day 2 — Government Hack:** Phase 3–5 (print set, narrative, assessments).
  **World History Hack:** Phase 1–2.
- **Day 3 — World History Hack:** Phase 3–5. **Eighth Grade** + **Tennessee
  History:** Phase 0–2.
- **Day 4 — Eighth Grade + Tennessee History:** Phase 3–5. **All courses:**
  Phase 6 (web app + testing DB parity).
- **Day 5 — All courses:** Phase 7 (QC/fact-check/SME sign-off), **Phase 8 DBQ
  Books**, Phase 9 adoption packages.

Each phase can be **fanned out with multi-agent orchestration** (one agent per
unit/standard) to hit the timeline; the gates above keep quality constant.

### What is required from the owner to start (inputs the build cannot invent)
1. **Official state standards** documents for GC / W / Grade-8 / TN (verbatim source).
2. **Source material / decks** or a go-ahead to source primary documents + images
   from authoritative public-domain repositories (LoC, NARA, TN Encyclopedia, …).
3. **Web-app repo access** + the reference course's feature/test manifest to port.
4. **SME reviewer(s)** for the accuracy sign-off gate.

---
© 2026 TroopToTeacher Technologies, LLC · Social Studies Hack suite · Course production workflow.
