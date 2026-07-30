# World History Hack — Platinum Build Memory (phase tracker)

Working branch: `claude/world-history-platinum-build-mv5z17`
Playbook: `courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md` · Handoff: `courses/_playbooks/HANDOFF_WORLD_HISTORY.md`
Reusable build kit (canonical source to copy from): `courses/_build_kit/{engine, question_bank_toolkit, compliance_templates, reference}`

## Course facts
- 4 quarters · 13 units · **92 standards** (W.01–W.89; a/b splits W.08, W.56, W.63) · SSP.01–SSP.06.
- Standards source of truth: `05_STANDARDS_ALIGNMENT/world_history_standards_source.json` · human map: `unit-map.md`.
- Q1 legal mandates: Constitution Day (36 U.S.C. §106) + Freedom Week (TCA §49-6-1014).
- TN (T) standards: W.39, W.40, W.51, W.52, W.53, W.66, W.81, W.89. Genuine TN ties: Cordell Hull (W.51), Oak Ridge/Manhattan Project (W.52), drug/human trafficking in TN (W.81).

## Assets confirmed on hand
- **Brand-lock engine** verified (CW=9792, one `cornell()`, margins 1224) in both `_build_kit/engine/` and `world-history-hack/BUILD/engine/`.
- **Reference workbook** `REFERENCE/USHistory_Unit8_Student_Workbook.docx` (brand geometry target).
- **TCAP seeds** (Drive): `WH.07`–`WH.37`, 5 MC items each, full psychometrics; map 1:1 to W.NN; re-tag units to instructional-guide unit map on ingest.
- **Primary-source images:** to be dropped in the Drive **"World History Hack"** folder at Phase 2, named `{{STD}}_slug.ext`.

## Phase status
- [x] **Phase 0** — parameters set; build kit installed (skills at `.claude/skills/`, playbooks, `_build_kit`); brand-lock verified.
- [x] **Phase 1** — standards intake: `world_history_standards_source.json` (92 verbatim standards + I-can + dimensions + unit/quarter), `unit-map.md`, brand kit, this memory. Validated: every standard present once, codes contiguous 1–89, bidirectional unit-map match. **Standards→unit map shown to owner.**
- [x] **Phase 2** — primary-source sourcing complete: `primary_source_sourcing.json` (92/92 standards, one PD source each; 89 with search-verified repository pages, 3 flagged — W.44, W.82, W.84), `ASSETS/primary_sources/{README.md, EXPECTED_FILENAMES.txt}`, preliminary `RIGHTS_CLEARANCE_LOG.md` + `NOTICES.md`. **Pending owner action:** pull the 92 files (repository "Original file"/Download → save as the exact `EXPECTED_FILENAMES.txt` names) into the Drive "World History Hack" folder; then `sync_images.py`. Full `copyright-integrity-accreditation` audit re-runs at QC once images are on disk.
- [~] **Phase 3** — per-unit content JSON (`BUILD/unitN/analysis/unitN_content.json`) → historian fact-check. Schema contract extracted → `BUILD/CONTENT_SCHEMA.md`.
  - **REUSE-FIRST (owner directive):** before authoring, pull existing U.S. History resources where standards overlap. Crosswalk built → `05_STANDARDS_ALIGNMENT/{us_world_history_crosswalk.json, us-world-crosswalk.html, REUSE_PLAN.md}` (**INTERNAL — references US.xx by design; exclude from any student/teacher deliverable and the district ZIP**). Overlap: **28 strong · 22 partial · 7 thematic · 35 author-fresh**; ~422 existing US items harvestable. US corpus in repo root: `all_questions.json` (742) + `Questions_US84-95_Generated.json` (120), `03_TEXTBOOK_UNITS/`, `01_STUDENT_PACKETS/`. On reuse: reframe to the global WH I-can + de-leak (strip US.xx / "U.S. History" / US-EOC; retag W.xx / RC-WH{N}).
  - NEXT: prove one reference unit end-to-end, then fan out remaining units (reuse-first per crosswalk); run historian-factcheck after.
  - **UNIT 1 (Age of Revolutions — reference build, author-fresh) IN PROGRESS:**
    - [x] `BUILD/unit1/analysis/unit1_content.json` — 5 standards, full 7-activity schema, EN/ES vocab, cited sources, keys debiased (7A/6B/6C/6D), leak-clean, verbatim standards preserved.
    - [x] Engine de-leak: `build_workbook.js` parameterized (course banner/standards banner/TN investigation from `U.*`); brand-lock geometry untouched.
    - [x] **Student Workbook + Large-Print built & verified** — pgMar 1224/1152/720, every tblGrid=9792, Cornell 2448|7344, 1284 C9C2B4 ruled lines, 5 standard pages, 7-activity cycle, LP ×1.5, LEAK-CLEAN.
    - [ ] Teacher Guide · 4 Covers · Organizer Toolkit · Assessment Book (+unit1_assessment.json) — need engine de-leak (cover/organizer/assessment/teacher_guide) then build.
    - [ ] Teacher + Student decks (build from render_unit_html template → Chromium tagged PDF; deck builder not in kit).
    - [ ] DBQ book (history-hack-platinum-workbook).
    - [ ] Unit 1 question bank (20/std ×5 = 100 items) via tcap-item-writer-v2 (author-fresh; no WH TCAP seed below W.07).
- [ ] **Engine de-leak (Phase 5–7 prerequisite)** — parameterize hardcoded Government text in build_cover/organizer_toolkit/workbook/assessment/teacher_guide from `U.*` (geometry untouched). Details in `BUILD/CONTENT_SCHEMA.md`. Verify 0 forbidden strings in rendered `word/*.xml`.
- [ ] **Phase 4** — teacher + student slide decks (tagged PDF/UA).
- [ ] **Phase 5** — graphic organizer toolkits.
- [ ] **Phase 6** — student workbooks (+ large-print) + teacher guides + covers.
- [ ] **Phase 7** — assessment books (per unit).
- [ ] **Phase 8** — deep question bank (20/standard) + parallel tests + inventory/crosswalk (ingest TCAP seeds).
- [ ] **Phase 9** — DBQ / primary-source investigation books.
- [ ] **Phase 11** — UDL 3.0 CAST audit (9/9 evidenced) + MTSS map + accessibility statement.
- [ ] **Phase 12** — compliance pack + master index + web edition (Suite registration) + district ZIP + MASTER QC GATE (12 checks).

## Open decisions for the owner
1. Confirm the 13-unit / 92-standard spine is locked (map shown).
2. Phase 2 image drop: confirm the target Drive folder + naming; some units need many sources (Unit 13 = 13 standards).
3. Green-light to proceed into Phase 2/3 authoring.
