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
- [ ] **Phase 2** — primary-source sourcing (`primary_source_sourcing.json`, one PD source/standard) + pull images from Drive → `ASSETS/primary_sources/`; rights clearance (`copyright-integrity-accreditation`).
- [ ] **Phase 3** — per-unit content JSON (`BUILD/unitN/analysis/unitN_content.json`) → historian fact-check.
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
