# World History Hack — Platinum Course Build Playbook

A step-by-step workflow **and copy-paste prompts** to build a new licensable **World History Hack** course edition to the exact platinum standard we built *Foundations of Constitutional Government* (Government Hack) — feature-for-feature, guardrail-for-guardrail, with UDL 3.0 + MTSS embedded and evidenced.

Run the phases in order. Each phase has a **prompt you paste to Claude Code** (in a repo session). Every phase ends with a **verification gate** and **commit + push**. Fill the `{{PLACEHOLDERS}}` once in Phase 0 and reuse.

---

## Phase 0 — Parameters (set once)

| Placeholder | Government value (example) | World History value |
|---|---|---|
| `{{COURSE_NAME}}` | Foundations of Constitutional Government | **World History & Geography** (use the exact TN course title) |
| `{{BRAND}}` | Government Hack | **World History Hack** |
| `{{COURSE_CODE}}` | GC | *(from the TN standards doc)* |
| `{{STD_PREFIX}}` | GC.01–GC.35 | *(from the TN standards doc, e.g. `W.01–W.xx`)* |
| `{{COURSE_DIR}}` | courses/foundations-constitutional-government | courses/world-history-hack |
| `{{STANDARDS_SOURCE}}` | government_standards_source.json | the official TN World History & Geography standards (you provide) |

**You must supply, before Phase 1:** (a) the **official state standards** file/text (verbatim standards + unit map + content tags), and (b) later, the **sourced primary-source images** with citations (Phase 2). Claude never invents standards, citations, sources, or images.

---

## The GUARDRAILS block — paste into EVERY phase prompt

```
GUARDRAILS (non-negotiable):
- Source of truth only: never invent or paraphrase a standard, citation, primary source, date, name, statute, treaty, or image. If it isn't in the provided standards/source files, it doesn't go in.
- No cross-edition / source-district leakage. This edition is "World History Hack". Its deliverables must NEVER contain any other edition's brand or codes or the source district — forbidden strings: "History Hack" (except the exact brand "World History Hack"), "Government Hack", "U.S. History", "WCS", "Williamson", "US.0x"/US.xx codes, "GC.xx" codes, "flight log". Scan every built artifact (docx word/*.xml, deck HTML with base64 stripped) and fail on any hit.
- Answer keys and reteach live TEACHER-SIDE only; student sections never reveal keys.
- No claims of state / waiver / Textbook Commission approval; label items "classroom-formative · pre-field-test".
- Primary sources must be genuinely public-domain with accurate citations (repository + page URL + rights).
- Historical accuracy: every date, number, name, battle, dynasty, treaty, and population is verifiable; when unsure, keep it conceptual — do not fabricate. (Run the historian-factcheck-agent skill on content and items.)
- Evergreen: never assert a "current" fact that will go stale; teach the process of finding it.
- UDL 3.0 (CAST) + MTSS are embedded as DISTRICT-DEFENSIBLE FRAMEWORKS and must be EVIDENCED in the design (real affordances), not just labeled. A strip/callout counts only where the artifact delivers the option.
- Every phase: verify, then commit + push to the working branch.
```

## The UDL / MTSS wording block — reuse verbatim across decks, workbooks, assessments

```
UDL 3.0 (CAST): read-aloud on request · key terms glossed (EN/ES) · respond in writing, speech, or a labeled diagram · large-print & screen-reader friendly. Same learning target for everyone; supports vary the means, not the ceiling.
MTSS: Tier 1 — core lesson for all · Tier 2 — small-group reteach of this standard (Cornell cues + graphic organizer), then re-check · Tier 3 — intensive 1:1 with concrete→representational→abstract scaffolding, progress-monitored to the same standard.
```

## Reusable assets to COPY from the Government build (don't rebuild these)

- **Question-bank toolkit** (subject-agnostic): `courses/foundations-constitutional-government/08_QUESTION_BANK/{consolidate_bank.py, bank_qc.py, add_udl_remediation.py, generate_parallel_tests.py, build_inventory.py}` → copy into `{{COURSE_DIR}}/08_QUESTION_BANK/`.
- **Engine docx builders** (parameterized by content JSON): `BUILD/engine/` + the leak-fixed `BUILD/unit1/build_{workbook,teacher_guide,cover,assessment_book}.js` as the golden templates (they carry the UDL/MTSS callout, response-mode CER choice, Choice & Voice, Reflect & Connect, LARGEPRINT flag).
- **Deck builder** `BUILD/decks/Unit1_Teacher_Deck/build_deck.py` (per-standard UDL/MTSS strip, AUDIENCE=student variant, base64-stripped leak guard, `--export-tagged-pdf`).
- **Organizer skill** `history-hack-graphic-organizer-workbook`.
- **Compliance templates**: `06_COMPLIANCE_INTERNAL/{udl-mtss-framework.html, UDL_AUDIT_REPORT.md, MTSS_SUPPORT_MAP.md, ACCESSIBILITY_STATEMENT.md}`, `05_STANDARDS_ALIGNMENT/{standards-matrix.html, scope-sequence.html, udl_mtss_alignment.json}`.

---

# THE WORKFLOW (12 phases)

## Phase 1 — Standards intake, unit map & verbatim targets
**Prompt:**
```
Invoke the history-hack-course-standard-builder skill. Stand up a new course edition "World History Hack" ({{COURSE_NAME}}) inside the platform under courses/world-history-hack, mirroring the structure of courses/foundations-constitutional-government. Create the branch, scaffold the directory tree (00_START_HERE, 05_STANDARDS_ALIGNMENT, 06_COMPLIANCE_INTERNAL, 08_QUESTION_BANK, BUILD, WEB_EDITION, ASSETS).
From the official TN World History & Geography standards I am providing [PASTE/ATTACH], build:
1) world_history_standards_source.json — every standard: {code, title, standard (verbatim), ican, dimensions, tca (legally_required), unit, unit_title, quarter}. Verbatim text unaltered.
2) unit-map.md — units with titles, quarters, and the standard list per unit.
3) 00_START_HERE/WORLD_HISTORY_HACK_BRAND_KIT.md and PLATINUM_MEMORY.md (definition of done).
Do not invent standards or content. [GUARDRAILS block]
Verify: every provided standard appears once, codes contiguous, unit map matches. Commit + push.
```

## Phase 2 — Primary-source sourcing & rights
**Prompt:**
```
Build 05_STANDARDS_ALIGNMENT/primary_source_sourcing.json: one genuine public-domain primary source per standard {unit, standard, standard_title, type, work_title, creator, year, repository, page_url, direct_file_url, rights, verified, filename (STD_slug.ext), search_hint}. Prefer Library of Congress, National Archives, Smithsonian, Wikimedia Commons, British Library, Gallica, Rijksmuseum, Met Open Access — pre-1929 or gov/PD works only. Do NOT fabricate URLs; give me the list to source if egress is blocked.
Create ASSETS/primary_sources/ with README + EXPECTED_FILENAMES.txt (the exact filenames).
When I drop the sourced images in a Drive folder, pull them via the Google Drive connector: for files that exceed the connector's 10 MB cap, ask me to re-export ≤10 MB; decode via the on-disk tool-result path (jq .content | base64 -d) so bytes never bloat context; match each by .title to its filename. Then build BUILD/sync_images.py (fan the canonical bank into every deck/unit/web asset folder; rasterize SVG→PNG for docx) and rebuild.
[GUARDRAILS block]. Verify each image is a valid file, citations accurate. Commit + push.
```

## Phase 3 — Content authoring (per unit) — delegate one agent per unit
**Prompt (repeat/fan-out per unit N):**
```
Author BUILD/unitN/analysis/unitN_content.json for {{COURSE_NAME}} Unit N, in full schema parity with the Government course's unit content (read courses/foundations-constitutional-government/BUILD/unit6/analysis/unit6_content.json as the template). For the unit: {code, title, course_name, standards_range, quarter, suggested_days, essential_question, publisher, footer, perspectives(+intro), tn_connection(+label+task) where genuinely part of a standard, cover_era, cover_title_lines, cover_image, frameworks{udl_designed_in, mtss}, belief_check, play, spiral, discussion_norms}. Per standard: {title, standard(verbatim)=the state text, ican, vocab[{term, say(pronunciation), es(Spanish), def}], sources, cfu (4 options, debiased key A/B/C/D across the unit), learning_targets, criteria, cues, lenses, hook, civic_label, ssp_focus, ref, and per-standard tn_connection where the standard genuinely has a TN tie}.
Ground ONLY in the verbatim standards + sourced records; historically accurate; no fabrication. UDL/MTSS embedded as frameworks. [GUARDRAILS block].
Verify JSON parses, per-standard fields present, CFU keys debiased, leak-clean. Commit + push.
```
> After all units: run `historian-factcheck-agent` on the content for date/name/number verification; fix flagged items.

## Phase 4 — Teacher + Student Decks (UDL/MTSS strips, tagged PDFs)
**Prompt:**
```
Copy courses/foundations-constitutional-government/BUILD/decks/Unit1_Teacher_Deck/build_deck.py as the template. For each unit build BUILD/decks/UnitN_Teacher_Deck (build_deck.py + unitN_images.json) with: per-standard slides, source_frame() embedding the cited primary source (base64) or a cited placeholder, "Make It Stick" slide, a per-standard UDL 3.0 + MTSS strip [UDL/MTSS wording block], per-standard ★ connection chip where present, and a base64-stripped leak guard.
Add AUDIENCE=student mode → a Student Deck per unit (drop teacher-note strips + all answer keys, retitle, add an opening "supports available to everyone" UDL slide) at BUILD/decks/UnitN_Student_Deck.
Render every deck to PDF with Chromium --headless --no-sandbox --disable-gpu --no-pdf-header-footer --export-tagged-pdf --generate-pdf-document-outline, then stamp PDF/UA metadata via pikepdf (/Lang=en-US, Title, MarkInfo/Marked, DisplayDocTitle).
[GUARDRAILS block]. Verify: images embed in both decks, student decks have 0 teacher notes / 0 keys, strips present, tagged (StructTreeRoot), leak-clean. Commit + push.
```

## Phase 5 — Graphic Organizer Toolkits
**Prompt:**
```
Invoke history-hack-graphic-organizer-workbook. For each unit build BUILD/organizers/UnitN_..._Graphic_Organizer_Toolkit at platinum: Quick Guide ("Which Organizer, When") + SSP crosswalk + the 15 blank reproducibles (Venn2/3, T-chart, matrix, cause-effect chain/split, timeline, concept web, main idea, KWL, 5 Ws, problem-solution, Frayer, CER, HIPPO, plus a Connection organizer) + N best-fit labeled organizers mapped to each standard's high-impact skill. Every organizer offers multi-modal response ("students may write, say (record), draw, or build") and scaffold/extend. Render PNG @2x + combined tagged PDF.
[GUARDRAILS block]. Verify pages render, leak-clean. Commit + push.
```

## Phase 6 — Workbook + Teacher Guide + Covers (+ large-print)
**Prompt:**
```
Copy the leak-fixed Government builders (BUILD/unit1/build_{workbook,teacher_guide,cover}.js) into each BUILD/unitN, repoint the analysis paths to unitN. These already carry: per-standard "UDL ACCESS & MTSS SUPPORT" callout, the CER "SHOW WHAT YOU KNOW — YOUR WAY" multi-modal response element, "CHOICE & VOICE" (7.1/7.2) and "REFLECT & CONNECT" (9.2/9.3/9.4) blocks, EN/ES vocab, Cornell/Frayer/CER/HIPPO, Guided + Light Support, and the LARGEPRINT scale flag.
Generate BUILD/unitN/analysis/unitN_images.json from the deck manifest + sourcing (SVG→PNG for docx). Build per unit: Student Workbook (embeds cited sources), Teacher Guide (How-To + MTSS), 4 covers; then a large-print edition (LARGEPRINT=1.5 → *_LargePrint.docx).
[GUARDRAILS block]. Verify: workbook embeds images, UDL/MTSS + Choice&Voice + Reflect&Connect callouts = #standards each, keys teacher-side, leak-clean across all word/*.xml. Commit + push.
```

## Phase 7 — Assessment Books (per unit)
**Prompt:**
```
Invoke tn-assessment-specialist + tcap-item-writer-v2 (apply the craft + psychometrics; adapt from US-History scope to World History standards — no US.xx codes, no US EOC reporting categories; use "RC-WH{N}: {unit title}"). For each unit author BUILD/unitN/analysis/unitN_assessment.json {disclosure, formative{by-standard}, formA[], formB[]}, one item per standard per form, {stem, std, dok, choices[4], key, rc, reteach} + full psychometrics {blooms, hess_crm_cell, irt_a/b/c, c3_dimension, ssp, distractor_tags, key/dok/blooms_rationale, bias_flag, tcap_format, field_test_ready} + per-item udl_supports + distractor-based remediation. Debias keys across A/B/C/D. Copy build_assessment_book.js; render each Assessment Book with Part 4 Teacher Key, Part 5 Psychometric Blueprint, Part 6 UDL Supports & Remediation — all teacher-side.
[GUARDRAILS block]. Verify keys teacher-side, JSON valid, leak-clean. Commit + push.
```

## Phase 8 — Deep Question Bank (20 items/standard)
**Prompt (base 10, then DOK-3-weighted +10):**
```
Invoke tn-assessment-specialist + tcap-item-writer-v2. Build a deep pool mirroring the U.S. History flagship all_questions.json (~10/standard) then DOUBLE it: 20 items/standard.
Round 1 (Q01–Q10/standard): 7 MC + 3 open (SA/CR/DBQ or ER), DOK 2/4/4, mixed types, TN-flag, topics, full psychometrics, debiased keys. Superset schema = flagship fields (id, standard, unit, question_number, type, dok, level, question, options, correct_answer, tennessee_specific, topics) + psychometrics. Write BUILD/unitN/analysis/unitN_item_bank.json.
Round 2 (Q11–Q20/standard): DOK-3-weighted (2/3/5), 8 MC (≥3 DOK3) + 2 open (DOK3), distinct constructs, → unitN_item_bank_ext.json.
Ground in the unit content; historically accurate; document_based items cite genuine public-domain sources. [GUARDRAILS block].
Verify per unit: 20/standard, DOK spread, DOK3-MC present, keys valid, leak-clean. Commit + push each unit.
```

## Phase 9 — Consolidate → UDL/remediation → QC → parallel tests → inventory & crosswalk
**Prompt:**
```
Copy the 08_QUESTION_BANK toolkit from the Government course. Then run, in order:
python3 08_QUESTION_BANK/consolidate_bank.py         # merge per-unit pools → world_history_question_bank.json
python3 08_QUESTION_BANK/add_udl_remediation.py      # CAST 3.0 udl_supports + distractor-based MTSS remediation on every item
python3 08_QUESTION_BANK/bank_qc.py                  # coverage, DOK/type/Bloom's, key balance, IRT spread, dup detection, leak scan (must PASS)
python3 08_QUESTION_BANK/build_inventory.py          # QUESTION_BANK_INVENTORY.md + standards_crosswalk.csv + item_inventory.csv
python3 08_QUESTION_BANK/generate_parallel_tests.py --forms 4 --scope all --title WH_EOC_Practice
Confirm the equating report (difficulty spread ≤ ~0.35), UDL banner on student forms, teacher keys carry answer key + remediation. Commit + push (inventory + crosswalk are a named deliverable).
```

## Phase 10 — UDL 3.0 CAST audit + gap closure
**Prompt:**
```
Invoke udl-cast-expert. Produce 06_COMPLIANCE_INTERNAL/UDL_AUDIT_REPORT.md: score all 9 CAST 3.0 guidelines ✅/⚠️/❌ against ARTIFACT EVIDENCE (a strip counts only where the design delivers the affordance) with pointers. Then close every ⚠️/❌ with real design fixes (not labels): multi-modal response on constructed tasks, MTSS_SUPPORT_MAP.md naming Tier 1/2/3 resources per standard, ACCESSIBILITY_STATEMENT.md, large-print editions, PDF/UA-tagged deck PDFs, Choice & Voice (7.1) and Reflect & Connect (9.2/9.3/9.4). Re-score to 9/9; state any external step honestly (e.g., workbook tagged-PDF via Word/LibreOffice) rather than over-claim. Commit + push.
```

## Phase 11 — Compliance pack
**Prompt:**
```
Build 05_STANDARDS_ALIGNMENT/{standards-matrix.html, scope-sequence.html, udl_mtss_alignment.json (36 CAST considerations + MTSS tiers + design contract + defensibility)} and 06_COMPLIANCE_INTERNAL/{udl-mtss-framework.html, schedule-f-alignment.html}. Invoke tn-textbook-adoption-agent for the Schedule F / adoption alignment and history-hack-print-qc-auditor for a print-readiness pass. [GUARDRAILS block]. Commit + push.
```

## Phase 12 — Package + master index + web edition
**Prompt:**
```
Build WEB_EDITION/public/data/world-history/{primary-sources, questions} manifests. Generate 00_START_HERE/MASTER_DELIVERABLES_INDEX.md (per-unit deliverables with sizes + assessment psychometrics + image-bank status + integrity attestation). Compile a district-ready package: per-unit folders (workbook incl. large-print, teacher guide, deck teacher+student, organizer toolkit, assessment book, covers) + Course_Level artifacts + the master index; zip it and deliver (split into ≤30 MB parts if large). Commit + push the index.
```

---

## Definition of Done — Platinum checklist (per course)
- [ ] Every standard: content JSON (verbatim standard, EN/ES vocab, ican, sources, CFU, hook, learning targets, per-standard TN tie where real).
- [ ] Per unit: Student Workbook (+ large-print), Teacher Guide, Teacher Deck + Student Deck (tagged PDF), Organizer Toolkit, Assessment Book, 4 covers.
- [ ] Primary sources: genuine public-domain, embedded in decks + workbooks + web, accurate citations.
- [ ] Question bank: 20 items/standard, full psychometrics (Bloom's, Hess, IRT 3PL, C3, SSP, coded distractors), UDL supports + MTSS remediation, debiased keys; consolidated + QC PASS + inventory + standards crosswalk; parallel-test generator producing equated forms.
- [ ] UDL 3.0 CAST audit = 9/9 evidenced (real affordances per section: UDL/MTSS strips, response-mode choice, Choice & Voice, Reflect & Connect); MTSS Support Map; Accessibility Statement; large-print; tagged PDFs.
- [ ] Guardrails: zero cross-edition/source-district leakage (scanned), keys teacher-side, no approval claims, historically fact-checked, evergreen.
- [ ] Compliance pack + master index + district package.

## Notes carried from the Government build (lessons)
- **Leak scans must strip base64** before scanning decks (random byte sequences false-trip 3-letter guards).
- **Large Drive files (>10 MB)** exceed the connector cap — re-export smaller; and **tiny files pasted as base64 can truncate** — pull ≥~1200 px so they route through the on-disk tool-result path.
- **Builders may be gitignored in the reference unit** (unit1) — the rendered deliverables are what's tracked; that's fine.
- **A "strip" is a signpost, not embedding** — the CAST audit only credits guidelines with a real artifact affordance; close gaps with design, not labels.
- **LibreOffice may be non-functional in the sandbox** — deck PDFs tag via Chromium; workbook tagged-PDF is a one-command Word/LibreOffice export on the district side (document it honestly).

---

## One-shot kickoff prompt (if you want Claude to drive the whole thing)
```
Build a new licensable "World History Hack" course edition ({{COURSE_NAME}}) to the platinum standard of courses/foundations-constitutional-government, following courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md phase by phase. Invoke history-hack-course-standard-builder to orchestrate; use tn-assessment-specialist + tcap-item-writer-v2 for the 20-item/standard bank with psychometrics, udl-cast-expert for the 9/9 evidenced UDL audit, history-hack-graphic-organizer-workbook for organizers, and historian-factcheck-agent for accuracy. Apply the GUARDRAILS block everywhere. I will provide the official TN World History & Geography standards now, and the sourced primary-source images when you reach Phase 2. Fan out one agent per unit for content, decks, workbooks, assessments, and the item bank; verify (leak scan, keys teacher-side, images embedded, JSON valid) and commit + push after each phase. Stop and show me the standards→unit map (Phase 1) before authoring.
```
