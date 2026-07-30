# World History Hack — Platinum Course Build Playbook (complete)

A step-by-step workflow **and copy-paste prompts** to build a new licensable **World History Hack** course edition to the exact platinum standard we built *Foundations of Constitutional Government* (Government Hack) — feature-for-feature, guardrail-for-guardrail, with **UDL 3.0 embedded and evidenced**.

> **Framework citation (use verbatim in every UDL artifact):**
> **CAST (2024). *Universal Design for Learning Guidelines version 3.0.* Lynnfield, MA: Author.** — https://udlguidelines.cast.org/
> Three principles (Engagement / Representation / Action & Expression), 9 guidelines, 30 considerations. Tagline: *Until learning has no limits.* Use the 3.0 names — Welcoming Interests & Identities, Sustaining Effort & Persistence, Emotional Capacity, Strategy Development — never the 2.x terms ("checkpoints," "self-regulation," "Access/Build/Internalize").

Run phases in order. Each phase has a **prompt to paste**, a **verification gate**, and **commit + push**. Set `{{PLACEHOLDERS}}` once in Phase 0.

---

## COMPLETE DELIVERABLES INVENTORY — this is "absolutely everything" (Definition of Done)

**Per standard (all standards):** verbatim-standard content record · EN/ES vocab (term, pronunciation, Spanish, definition) · "I can" targets · a cited public-domain **primary source** · CFU · hook · learning targets/criteria/cues · per-standard TN tie where genuinely part of the standard · **20 question-bank items** · per-standard UDL/MTSS strip, Choice & Voice, Reflect & Connect.

**Per unit:**
1. **Content JSON** (source of truth for every generator)
2. **Teacher Slide Deck** (PDF, tagged) — primary sources embedded, Make It Stick, per-standard UDL/MTSS strip
3. **Student Slide Deck** (PDF, tagged) — teacher notes + answer keys removed, UDL access slide added
4. **Student Workbook** (docx) — Cornell, Frayer, Close-Read, Primary-Source/Data, CER, Guided + Light Support, UDL/MTSS callout, multi-modal CER response, Choice & Voice, Reflect & Connect, embedded cited sources
5. **Student Workbook — Large-Print edition** (docx, 16.5 pt)
6. **Teacher Guide** (How-To + MTSS) (docx)
7. **Teacher Graphic Organizer Toolkit** (PDF) — Quick Guide + SSP crosswalk + 15 blank reproducibles + best-fit labeled organizers
8. **Assessment Book (Teacher)** (docx) — formative + parallel Form A/B; Part 4 Key, Part 5 Psychometric Blueprint, Part 6 UDL Supports & Remediation
9. **DBQ / Primary-Source Investigation Book** (docx) — 2–3 sourced documents, HIPPO/OPTIC + SOAPS analysis, scaffolded CER, language-access (EN/ES) companion, teacher guide + rubric + Schedule-F self-score
10. **4 Covers** (docx) — Student Workbook, Teacher Edition, Assessment Book, Organizer Toolkit

**Course-wide:**
11. **Question Bank** — `world_history_question_bank.json`: **20 items/standard**, superset schema (flagship fields + full psychometrics: Bloom's, Hess CRM cell, IRT 3PL a/b/c, C3, SSP, coded distractors + rationales) + CAST 3.0 `udl_supports` + distractor-based MTSS `remediation`; debiased keys; mixed types (MC + SA/CR/ER/DBQ)
12. **Parallel-Test Generator** — equated forms (matched DOK + IRT difficulty), student form + teacher answer-key-with-remediation, equating report
13. **Bank QC / rigor report**, **Full Inventory + Standards Crosswalk** (`QUESTION_BANK_INVENTORY.md`, `standards_crosswalk.csv`, `item_inventory.csv`)
14. **Primary-source image bank** (`ASSETS/primary_sources/`) with citations (`primary_source_sourcing.json`)
15. **UDL 3.0 CAST audit** (9/9 evidenced) · **MTSS Support Map** · **Accessibility Statement**
16. **Compliance pack** — standards matrix, scope & sequence, UDL/MTSS framework crosswalk, Schedule F alignment, **Rights-Clearance Log + NOTICES** (copyright/IP/OSS)
17. **Web edition** manifests (primary-sources + questions) registered in the **Social Studies Suite** · **Master Deliverables Index** (with QC-gate attestation) · **district package ZIP**

---

## SKILLS ROSTER — EVERY skill, and which phase it runs
**Orchestration & content**
| Skill | Use for | Phase |
|---|---|---|
| `history-hack-course-standard-builder` | Orchestrate the whole cradle-to-grave course build | 1 (all) |
| `history-hack-curriculum-architect` | Unit structure, instructional flow, rigor, scope & sequence | 1, 3 |
| `instructional-design-specialist` | Lesson/unit/assessment design, TN-standards alignment | 3 |
| `learning-experience-designer` | Interactive/inclusive UX, UDL, engagement systems (student decks, web edition) | 4, suite |
| `history-hack-platinum-unit-builder` | Consolidate a unit's workbook/guide/deck to platinum | 6 |
| `history-hack-platinum-workbook` | Standalone **DBQ / primary-source investigation books** | 9 |
| `history-hack-graphic-organizer-workbook` | The Graphic Organizer Toolkits | 5 |
| `history-hack-comic-mission-builder` / `history-hack-comic-script-creator` | Optional comic-based lesson packets/scripts (suite content extension) | opt |

**Assessment**
| Skill | Use for | Phase |
|---|---|---|
| **`tn-assessment-specialist`** | Write + assemble + **QC** items and Assessment Books (built-in psychometric + bias review) | 7, 8 |
| **`tcap-item-writer-v2`** | Full psychometrics — IRT 3PL, Hess CRM, DOK/Bloom's, coded distractors, TDOE stem conventions | 8 |
| `history-hack-question-forge` | Fast standards-aligned item/quiz generation with built-in QC (supplementary pools) | 8 |

**QC / compliance / accuracy (the gate)**
| Skill | Use for | Phase |
|---|---|---|
| `historian-factcheck-agent` | Claim-by-claim primary-source factual verification of content + items | QC |
| `udl-cast-expert` | CAST UDL 3.0 audit (9/9 evidenced) + evidence-mapped gap closure | 11 / QC |
| `tn-textbook-adoption-agent` | Schedule F / TN adoption alignment (standards, balance, rubric self-score) | 12 / QC |
| `copyright-integrity-accreditation` | **Copyright / IP / rights clearance**, FERPA/COPPA data privacy, OSS licensing, ToS | 2 / QC / suite |
| `history-hack-print-qc-auditor` | Print-readiness QC of PDFs/docx (defects, layout, fix priorities) | QC |
| `history-hack-teacher-ux-reviewer` | Teacher-facing UX review (guides, dashboards, web flows) | suite |
| `tt-education-research-team` | ESSA evidence tiers, research-foundations doc, pilot-study design for district RFPs | opt / suite |

**Format & platform**
| Skill | Use for |
|---|---|
| `docx` / `pdf` / `pptx` / `xlsx` | Word/PDF/deck/spreadsheet format work (tagged PDF, large-print, packaging, sourcing sheets) |
| `dataviz` | Any chart/analytics visual (bank inventory, psychometric spread, mastery dashboards) |
| `history-hack-website-builder` | Web edition + **Social Studies Suite** integration (design tokens, brand, components) |
| `troop-prompt-refiner` | Sharpen any sub-prompt before handing it to another tool/agent |

---

## The GUARDRAILS block — paste into EVERY phase prompt
```
GUARDRAILS (non-negotiable):
- Source of truth only: never invent or paraphrase a standard, citation, primary source, date, name, dynasty, battle, treaty, population, or image. If it isn't in the provided standards/source files, it doesn't go in.
- No cross-edition / source-district leakage. This edition is "World History Hack". Forbidden strings in any deliverable: "History Hack" (except the exact brand "World History Hack"), "Government Hack", "U.S. History", "WCS", "Williamson", "US.0x"/US.xx codes, "GC.xx" codes, "flight log". Scan every artifact (docx word/*.xml; deck HTML with base64 stripped first) and fail on any hit.
- Answer keys and reteach live TEACHER-SIDE only; student sections never reveal keys.
- No claims of state / waiver / Textbook Commission approval; label items "classroom-formative · pre-field-test".
- Primary sources genuinely public-domain (PD-old / PD-US / CC0) with accurate citations (repository + page URL + rights).
- Historical accuracy: every date/number/name/battle/dynasty/treaty is verifiable; when unsure, stay conceptual. Run historian-factcheck-agent.
- Evergreen: never assert a "current" fact that will go stale.
- UDL 3.0 (CAST, 2024) + MTSS are DISTRICT-DEFENSIBLE FRAMEWORKS, EVIDENCED in the design (real affordances), not just labeled. A strip/callout counts only where the artifact delivers the option.
- Every phase: verify, then commit + push to the working branch.
```

## The UDL / MTSS wording block — reuse verbatim across decks, workbooks, assessments, DBQ books
```
UDL 3.0 (CAST, 2024): read-aloud on request · key terms glossed (EN/ES) · respond in writing, speech, or a labeled diagram · large-print & screen-reader friendly. Same learning target for everyone; supports vary the means, not the ceiling.
MTSS: Tier 1 — core lesson for all · Tier 2 — small-group reteach of this standard (Cornell cues + graphic organizer), then re-check · Tier 3 — intensive 1:1 with concrete→representational→abstract scaffolding, progress-monitored to the same standard.
Citation on every UDL artifact: CAST (2024). Universal Design for Learning Guidelines version 3.0.
```

## Reusable assets to COPY from the Government build (don't rebuild)
All paths are under `courses/foundations-constitutional-government/`.
- **Question-bank toolkit** (subject-agnostic): `08_QUESTION_BANK/{consolidate_bank.py, bank_qc.py, add_udl_remediation.py, generate_parallel_tests.py, build_inventory.py}`.
- **Golden docx builders** — copy the **brand-locked** `BUILD/engine/build_{workbook,teacher_guide,cover,assessment_book,organizer_toolkit}.js` (or any `BUILD/unitN/` copy) into each new `BUILD/unitN` and repoint analysis paths. They carry UDL/MTSS callout, multi-modal CER, Choice & Voice, Reflect & Connect, LARGEPRINT flag. Run with `NODE_PATH="../unit1/node_modules" node build_X.js` (docx-js lives in unit1's node_modules).
- **Deck builder** `BUILD/decks/Unit1_Teacher_Deck/build_deck.py` (per-standard UDL/MTSS strip, AUDIENCE=student, base64-stripped leak guard, tagged-PDF) + `BUILD/engine/render_pdf.py`.
- **Image pipeline** `BUILD/sync_images.py`.
- **Compliance templates** `06_COMPLIANCE_INTERNAL/{udl-mtss-framework.html, UDL_AUDIT_REPORT.md, MTSS_SUPPORT_MAP.md, ACCESSIBILITY_STATEMENT.md, schedule-f-alignment.html, build_udl_framework.py}` + `05_STANDARDS_ALIGNMENT/{standards-matrix.html, scope-sequence.html, udl_mtss_alignment.json, build_alignment.py}`.

## ⭐ WORKBOOK BRAND-LOCK — the layout every course must match (non-negotiable)
The student workbook is the brand. It is locked to the owner's actual **U.S. History Hack Unit 8 Student Workbook**; the reference doc + full spec live at `courses/foundations-constitutional-government/REFERENCE/{USHistory_Unit8_Student_Workbook.docx, README.md}`. The brand-locked builders already bake these in — **do not change them**, and **verify them after copying**:

| Setting | Locked value |
|---|---|
| Page | 12240 × 15840 twips (8.5"×11") |
| Margins | top/bottom **1152**, left/right **1224**, header/footer **720** |
| Printable / table width `CW` | **9792** (every table fills it edge-to-edge; column arrays sum to 9792) |
| Column splits | even divisions of 9792 → 4896 (2-col), 3264 (3-col), 2448 (4-col) |
| Cornell notes | grid 4896\|4896; cells **2448 (cue)** \| **7344 (notes)**; navy header `1B2A4A`; zebra `F7F5EF`/`FFFFFF`; cantSplit; row height atLeast 520; ruled lines fill the notes column |
| Ruled writing line | empty paragraph, `spacing before 80 / after 140`, bottom border `single sz6 space1 color C9C2B4` (large-print scales height) |

**Verify-after-copy (all three must be true in each `build_workbook.js`):** `grep -o "CW=[0-9]*"` → `CW=9792`; `grep -c "function cornell("` → `1`; `grep -o "left:1224,right:1224"` → present. Then build and confirm: `<w:pgMar ... w:left="1224" ...>`, every `<w:tblGrid>` sums to **9792**, Cornell tables show `2448`/`7344` cells, and `C9C2B4` writing-line borders are present. The **seven activities per standard** (Word Bank · Vocabulary Studio/Frayer · Cornell Notes · Close Read · Primary Source/Data · Practice Quiz · CER) must each appear once per standard.

---

## Phase 0 — Parameters
`{{COURSE_NAME}}`=World History & Geography (exact TN title) · `{{BRAND}}`=World History Hack · `{{COURSE_CODE}}`/`{{STD_PREFIX}}`= from the standards doc · `{{COURSE_DIR}}`=courses/world-history-hack · `{{STANDARDS_SOURCE}}`= the official TN World History & Geography standards you provide.

---

# THE WORKFLOW

## Phase 1 — Standards intake, unit map & verbatim targets
```
Invoke history-hack-course-standard-builder. Stand up "World History Hack" ({{COURSE_NAME}}) under courses/world-history-hack, mirroring courses/foundations-constitutional-government. Create the branch and scaffold (00_START_HERE, 05_STANDARDS_ALIGNMENT, 06_COMPLIANCE_INTERNAL, 08_QUESTION_BANK, BUILD, WEB_EDITION, ASSETS). From the official TN World History & Geography standards I'm providing [PASTE], build world_history_standards_source.json (per standard: code, title, standard=verbatim, ican, dimensions, tca/legally_required, unit, unit_title, quarter), unit-map.md, and 00_START_HERE/{WORLD_HISTORY_HACK_BRAND_KIT.md, PLATINUM_MEMORY.md}. [GUARDRAILS]. Verify every provided standard appears once; codes contiguous. STOP and show me the standards→unit map before authoring. Commit + push.
```

## Phase 2 — Primary-source sourcing WITH downloadable links + how to save them
**Prompt:**
```
Build 05_STANDARDS_ALIGNMENT/primary_source_sourcing.json — one genuine public-domain primary source per standard: {unit, standard, standard_title, type, work_title, creator, year, repository, page_url, direct_file_url, rights, verified, filename ("{{STD}}_slug.ext"), search_hint}. For EACH source give me the exact DOWNLOADABLE LINK (the direct image/PDF URL, not just the catalog page) using the repository patterns below, plus the page_url and the rights statement. Only pre-1929 / government / CC0 works. Do NOT fabricate URLs — if egress is blocked, output the sourcing list for me to pull.
Create ASSETS/primary_sources/{README.md, EXPECTED_FILENAMES.txt} listing the exact filenames.
[GUARDRAILS]. Commit + push.
```
**Where to get downloadable primary sources (give the DIRECT file link, and the rights):**
| Repository | How to get the direct downloadable file | Rights |
|---|---|---|
| **Library of Congress** loc.gov | Item page → "Download" dropdown → largest JPEG/TIFF (files on `tile.loc.gov` / `cdn.loc.gov`) | PD (US gov / pre-1929) |
| **Wikimedia Commons** commons.wikimedia.org | File page → **"Original file"** (`upload.wikimedia.org/...`) → full-res; copy the license from the box | PD-old / PD-US / CC0 |
| **National Archives Catalog** catalog.archives.gov | Item → **Download** the primary object (JPG/PDF) | PD (US gov) |
| **Smithsonian Open Access** si.edu/openaccess | Object marked CC0 → **Download** | CC0 |
| **Met Museum Open Access** metmuseum.org | Object marked "Open Access" → **Download** | CC0 |
| **NYPL Digital Collections** digitalcollections.nypl.org | Public-domain item → **Download** | PD |
| **Gallica / BnF** gallica.bnf.fr | Item → download icon → image/PDF | PD (verify) |
| **Rijksmuseum** rijksmuseum.nl | Object → **Download** | PD / CC0 |
| **Internet Archive** archive.org | Item → download JP2/JPG/PDF | PD |
| **Europeana / British Library / Yale (LUNA)** | Item → download; keep only PD/CC0 with the rights line recorded | varies |

**How to save & get them into the build (the exact method we used):**
1. Name each file **exactly** `{{STD}}_slug.ext` (from `EXPECTED_FILENAMES.txt`), e.g. `W.14_magna-carta.jpg`.
2. Put them all in **one Google Drive folder**; give Claude the folder link.
3. Claude pulls via the **Google Drive connector**: list the folder, download each. Files whose response exceeds the inline limit **auto-save to an on-disk tool-result `.txt`** → decode without bloating context: `jq -r '.content' <toolresult>.txt | base64 -d > ASSETS/primary_sources/<TITLE>`. Match each by its `.title`.
4. The connector has a **hard 10 MB per-file cap** → re-export anything >10 MB to **≤10 MB (~2000 px)**. Very small files pasted inline can truncate → prefer **≥~1200 px** so they route through the on-disk path.
5. Run `python3 BUILD/sync_images.py` to fan the canonical bank into every deck/unit/web asset folder (rasterizes SVG→PNG for docx), then rebuild decks/workbooks. Verify each is a valid image and the citation is accurate.

## Phase 3 — Content authoring (per unit) — fan out one agent per unit
```
Invoke instructional-design-specialist / history-hack-curriculum-architect. Author BUILD/unitN/analysis/unitN_content.json for {{COURSE_NAME}} Unit N in full schema parity with courses/foundations-constitutional-government/BUILD/unit6/analysis/unit6_content.json. Unit-level {code,title,course_name,standards_range,quarter,suggested_days,essential_question,publisher,footer,perspectives(+intro),tn_connection(+label+task) where real,cover_era,cover_title_lines,cover_image,frameworks{udl_designed_in,mtss},belief_check,play,spiral,discussion_norms}. Per standard {title, standard(verbatim), ican, vocab[{term,say,es,def}], sources, cfu(4 opts, debiased key), learning_targets, criteria, cues, lenses, hook, civic_label, ssp_focus, ref, per-standard tn_connection where real}. Ground ONLY in the verbatim standards + sourced records; historically accurate. [GUARDRAILS]. Verify JSON parses, fields present, CFU keys debiased, leak-clean. Commit + push.
```
> After all units: run `historian-factcheck-agent` on the content; fix flagged claims.

## Phase 4 — Teacher + Student Slide Decks (UDL/MTSS strips, tagged PDF/UA)
```
Copy Government's BUILD/decks/Unit1_Teacher_Deck/build_deck.py as template. Per unit build BUILD/decks/UnitN_Teacher_Deck (build_deck.py + unitN_images.json): per-standard slides, source_frame() embedding the cited primary source (base64) or a cited placeholder, "Make It Stick" slide, per-standard UDL 3.0 + MTSS strip [UDL/MTSS block], ★ connection chip where present, base64-stripped leak guard. Add AUDIENCE=student → a Student Deck per unit (drop teacher-note strips + all keys, retitle, add an opening "supports available to everyone" UDL slide) at BUILD/decks/UnitN_Student_Deck. Render every deck to PDF: Chromium --headless --no-sandbox --disable-gpu --no-pdf-header-footer --export-tagged-pdf --generate-pdf-document-outline, then pikepdf-stamp PDF/UA metadata (/Lang=en-US, Title, MarkInfo/Marked, DisplayDocTitle). [GUARDRAILS]. Verify images embed in BOTH decks, student decks have 0 teacher notes / 0 keys, strips present, tagged (StructTreeRoot), leak-clean. Commit + push.
```

## Phase 5 — Graphic Organizer Toolkits
```
Invoke history-hack-graphic-organizer-workbook. Per unit build the Toolkit at platinum: Quick Guide ("Which Organizer, When") + SSP crosswalk + the 15 blank reproducibles (Venn2/3, T-chart, matrix, cause-effect chain/split, timeline, concept web, main idea, KWL, 5 Ws, problem-solution, Frayer, CER, HIPPO, + a Connection organizer) + N best-fit labeled organizers mapped to each standard's high-impact skill. Each organizer offers multi-modal response ("write, say (record), draw, or build") + scaffold/extend. Render PNG @2x + combined tagged PDF. [GUARDRAILS]. Verify pages render, leak-clean. Commit + push.
```

## Phase 6 — Student Workbooks (+ Large-Print) + Teacher Guides + Covers
```
Copy the leak-fixed Government builders (BUILD/unit1/build_{workbook,teacher_guide,cover}.js) into each BUILD/unitN, repoint analysis paths to unitN. They already carry: per-standard "UDL ACCESS & MTSS SUPPORT" callout, the CER "SHOW WHAT YOU KNOW — YOUR WAY" multi-modal response element, "CHOICE & VOICE" (7.1/7.2), "REFLECT & CONNECT" (9.2/9.3/9.4), EN/ES vocab, Cornell/Frayer/CER/HIPPO, Guided + Light Support, LARGEPRINT scale. Generate BUILD/unitN/analysis/unitN_images.json (SVG→PNG for docx). Build per unit: Student Workbook (embeds cited sources), a Large-Print edition (LARGEPRINT=1.5 → *_LargePrint.docx), Teacher Guide (How-To + MTSS), 4 covers. [GUARDRAILS]. Verify workbook embeds images; UDL/MTSS + Choice&Voice + Reflect&Connect callouts = #standards each; keys teacher-side; leak-clean. Commit + push.
```

## Phase 7 — Assessment Books (per unit)
```
Invoke tn-assessment-specialist + tcap-item-writer-v2 (apply craft + psychometrics; World-History scope — no US.xx codes/US EOC categories; use "RC-WH{N}: {unit title}"). Per unit author BUILD/unitN/analysis/unitN_assessment.json {disclosure, formative{by-standard}, formA[], formB[]} — one item per standard per form {stem,std,dok,choices[4],key,rc,reteach} + full psychometrics + per-item udl_supports + distractor-based remediation. Debias keys A/B/C/D. Copy build_assessment_book.js; render each Assessment Book with Part 4 Teacher Key, Part 5 Psychometric Blueprint, Part 6 UDL Supports & Remediation — all teacher-side. [GUARDRAILS]. Verify keys teacher-side, JSON valid, leak-clean. Commit + push.
```

## Phase 8 — Deep Question Bank (20 items/standard) + parallel tests + inventory/crosswalk
```
Invoke tn-assessment-specialist + tcap-item-writer-v2. Build a deep pool mirroring the U.S. History flagship all_questions.json then DOUBLE it → 20/standard.
Round 1 (Q01–Q10): 7 MC + 3 open, DOK 2/4/4, superset schema (id, standard, unit, question_number, type, dok, level, question, options, correct_answer, tennessee_specific, topics + full psychometrics) → BUILD/unitN/analysis/unitN_item_bank.json.
Round 2 (Q11–Q20): DOK-3-weighted (2/3/5), 8 MC (≥3 DOK3) + 2 open (DOK3), distinct constructs → unitN_item_bank_ext.json. document_based items cite genuine PD sources.
Then copy the 08_QUESTION_BANK toolkit and run: consolidate_bank.py → add_udl_remediation.py → bank_qc.py (must PASS) → build_inventory.py (QUESTION_BANK_INVENTORY.md + standards_crosswalk.csv + item_inventory.csv) → generate_parallel_tests.py --forms 4 --scope all. Confirm equating spread ≤ ~0.35, UDL banner on student forms, teacher keys carry answer key + remediation. [GUARDRAILS]. Commit + push per unit and for the consolidated bank.
```

## Phase 9 — DBQ / Primary-Source Investigation Books
```
Invoke history-hack-platinum-workbook. For each unit (or each high-yield standard) build a standalone DBQ Book (docx): a compelling historical question, 2–3 genuine PUBLIC-DOMAIN documents (cited, from Phase 2 sources), guided source analysis with HIPPO + OPTIC + SOAPS, a scaffolded CER/argument workspace with the multi-modal response option and sentence/argument frames, an EN/ES language-access companion, a teacher guide with a point rubric and reteach, and a Schedule-F self-score. Keys/rubrics teacher-side. [GUARDRAILS + UDL/MTSS block]. Verify documents are PD + cited, keys teacher-side, leak-clean, tagged/large-print where applicable. Commit + push.
```

## Phase 10 — (rolled into 8) Bank QC, inventory & crosswalk — confirm PASS + deliver the crosswalk

## Phase 11 — UDL 3.0 CAST audit + gap closure (target 9/9 evidenced)
```
Invoke udl-cast-expert. Produce 06_COMPLIANCE_INTERNAL/UDL_AUDIT_REPORT.md scoring all 9 CAST 3.0 guidelines ✅/⚠️/❌ against ARTIFACT EVIDENCE (a strip counts only where the design delivers the affordance), citing CAST (2024) UDL 3.0. Close every ⚠️/❌ with real design fixes: multi-modal response on constructed tasks, MTSS_SUPPORT_MAP.md (named Tier 1/2/3 per standard), ACCESSIBILITY_STATEMENT.md, large-print editions, PDF/UA-tagged deck PDFs, Choice & Voice (7.1), Reflect & Connect (9.2/9.3/9.4). Re-score to 9/9; state any external step honestly (workbook tagged-PDF via Word/LibreOffice). Commit + push.
```

## Phase 12 — Compliance pack + package + master index + web edition
```
Build 05_STANDARDS_ALIGNMENT/{standards-matrix.html, scope-sequence.html, udl_mtss_alignment.json} + 06_COMPLIANCE_INTERNAL/{udl-mtss-framework.html, schedule-f-alignment.html}; invoke tn-textbook-adoption-agent (Schedule F) + history-hack-print-qc-auditor (print readiness). Build WEB_EDITION/public/data/world-history/{primary-sources,questions} manifests. Generate 00_START_HERE/MASTER_DELIVERABLES_INDEX.md (per-unit deliverables + sizes + assessment psychometrics + image-bank status + integrity attestation). Compile the district package: per-unit folders (workbook + large-print, teacher guide, teacher deck + student deck, organizer toolkit, assessment book, DBQ book, covers) + Course_Level artifacts + the master index; zip and deliver (split ≤30 MB parts if large). [GUARDRAILS]. Commit + push.
```

---

---

## COPYRIGHT & RIGHTS CLEARANCE — do this at Phase 2 and re-verify at the QC gate
Run `copyright-integrity-accreditation` over the course. Nothing ships without a clean rights trail.
```
Invoke copyright-integrity-accreditation. Audit {{COURSE_DIR}} for copyright/IP + data-privacy compliance:
1. Every primary source is genuinely public-domain (PD-old ≥ pre-1929 / PD-US-gov / CC0) — verify the rights line at its repository; record repository + page_url + direct_file_url + rights + verified=true in primary_source_sourcing.json. NO fabricated URLs; NO "fair use" assumptions for images.
2. Authored close-reads are labeled "World History Hack-authored instructional synthesis" (NOT presented as primary sources).
3. Third-party marks, logos, textbook text, and paywalled/CC-BY-ND/NC assets are ABSENT.
4. Open-source: docx-js / Chromium / pikepdf / fonts used are license-compatible for redistribution; record in a NOTICES file.
5. Student-data privacy for the web edition: FERPA/COPPA posture (no PII in content; auth/entitlement handled by the platform).
6. Produce 06_COMPLIANCE_INTERNAL/RIGHTS_CLEARANCE_LOG.md — a per-source clearance table (source, repo, rights, URL, verified) + an integrity attestation ("all sources public-domain & cited; no third-party IP; authored text labeled").
[GUARDRAILS]. Commit + push.
```
**Citation standard (every source, everywhere it appears):** `{Title}. {Creator}, {Year}. {Repository}. Public domain ({PD basis}). {page_url}`.

---

## MASTER QC GATE — run before packaging (Phase 12). Nothing ships red.
Every check names its skill/tool and its pass bar. Fail → fix → re-run.
| # | Check | Skill / tool | Pass bar |
|---|---|---|---|
| 1 | **Leak scan** (cross-edition / source-district) | grep over `word/*.xml` + deck HTML **with base64 stripped first** | 0 hits on forbidden strings (see GUARDRAILS) |
| 2 | **Historical accuracy** | `historian-factcheck-agent` | every date/name/dynasty/battle/treaty/number VERIFIED or made conceptual; 0 unresolved |
| 3 | **Copyright & rights** | `copyright-integrity-accreditation` | RIGHTS_CLEARANCE_LOG clean; all sources PD + cited; NOTICES present |
| 4 | **Item rigor / bank QC** | `bank_qc.py` + `tn-assessment-specialist` | PASS: coverage 20/std, DOK ≈20/35/45, keys debiased, no dup stems, required fields, leak-clean |
| 5 | **Parallel-test equating** | `generate_parallel_tests.py` | mean-IRT spread ≤ ~0.35; UDL banner on student forms; keys+remediation teacher-side |
| 6 | **UDL 3.0 CAST audit** | `udl-cast-expert` | **9/9 guidelines ✅ evidenced** (affordance in the artifact, not a label); external steps stated honestly |
| 7 | **Accessibility** | `docx`/`pdf` + audit | large-print edition per workbook; deck PDFs PDF/UA-tagged (StructTreeRoot, Lang, Title); alt-text = image count |
| 8 | **Print readiness** | `history-hack-print-qc-auditor` | no orphaned headers, no blank/half pages, tables within margins, images ≥150dpi |
| 9 | **Workbook brand-lock** | grep + build check (see ⭐ section) | CW=9792 · margins 1224 · `function cornell(` · tables sum 9792 · 7 activities/std |
| 10 | **Standards & adoption** | `tn-textbook-adoption-agent` | every standard covered once; Schedule F self-score attached; balance defensible |
| 11 | **Teacher-side keys** | grep student artifacts | 0 answer keys / reteach in any student deck, workbook, or student test form |
| 12 | **Teacher UX** (if web/guide surfaces built) | `history-hack-teacher-ux-reviewer` | guide + web flows clear across tech-skill levels |

Record the gate result in `00_START_HERE/MASTER_DELIVERABLES_INDEX.md` (integrity attestation).

---

## SOCIAL STUDIES SUITE — this course is an EDITION inside the platform, not a new app
World History Hack ships **in addition to** the main History Hack web app, which becomes a **multi-course Social Studies Suite**: one platform, multiple entitlement-gated course editions — **U.S. History (flagship) · Government & Civics (Government Hack) · World History (World History Hack)** · future (Economics, Geography, World Geography). Mirror the flagship's platform patterns; do **not** fork the app.
```
Invoke history-hack-website-builder (+ learning-experience-designer for UX, history-hack-teacher-ux-reviewer for review).
Register World History Hack as a course edition in the Social Studies Suite:
- Use the platform's existing design tokens, typography, dark History Hack brand — no new visual system.
- Publish WEB_EDITION/public/data/world-history/{primary-sources.json, questions.json} manifests in the SAME shape as the U.S. History + Government manifests.
- Entitlement/gating: the edition is unlocked by license like the others; content is data-driven off the manifests (no per-course code fork).
- Suite navigation: add World History alongside U.S. History and Government in the course switcher; keep per-course standards codes namespaced ({{STD_PREFIX}}, RC-WH{N}).
- Keep teacher keys / answer data server-side / entitlement-gated, never in the student bundle.
[GUARDRAILS]. Verify manifests match the shared schema, suite switcher lists all editions, no cross-edition leakage. Commit + push.
```
> When the suite adds a course, the ONLY new inputs are: its standards doc, its sourced PD images, and its content JSON. Everything else (builders, toolkit, QC gate, UDL/MTSS blocks, brand-lock) is reused verbatim. That is the point of this playbook.

---

## Lessons carried from the Government build
- **Leak scans must strip base64** before scanning decks (3-letter guards false-trip on random image bytes).
- **Drive connector: hard 10 MB per-file cap** — re-export bigger; **tiny inline files can truncate** — pull ≥~1200 px so they route through the on-disk tool-result path; decode with `jq -r '.content' | base64 -d`.
- **A "strip" is a signpost, not embedding** — the CAST audit credits only guidelines with a real artifact affordance; close gaps with design, not labels.
- **LibreOffice may be non-functional in the sandbox** — deck PDFs tag via Chromium `--export-tagged-pdf`; workbook tagged-PDF is a one-command Word/LibreOffice export on the district side (document honestly).
- **Reference-unit builders may be gitignored** — the rendered deliverables are what's tracked.

## One-shot kickoff prompt
```
Build a new licensable "World History Hack" course edition ({{COURSE_NAME}}) to the platinum standard of courses/foundations-constitutional-government, following courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md phase by phase — producing EVERYTHING in its Deliverables Inventory (content, teacher + student slide decks, student workbooks + large-print, teacher guides, organizer toolkits, assessment books, DBQ books, covers, the 20-item/standard question bank with psychometrics + UDL + remediation, parallel-test generator, inventory + standards crosswalk, primary-source bank, 9/9 CAST UDL 3.0 audit, MTSS map, accessibility statement, rights-clearance log + NOTICES, compliance pack, master index, web edition, district package).

Copy the reusable Government assets rather than rebuilding: the 08_QUESTION_BANK toolkit, the BRAND-LOCKED docx builders in BUILD/engine/ (student workbook MUST match the ⭐ WORKBOOK BRAND-LOCK exactly — margins 1224, width 9792, the Cornell table, C9C2B4 ruled lines, seven activities/standard; reference at courses/foundations-constitutional-government/REFERENCE/), the deck builder, sync_images.py, and the compliance templates.

Invoke: history-hack-course-standard-builder to orchestrate; instructional-design-specialist / history-hack-curriculum-architect for content; tn-assessment-specialist + tcap-item-writer-v2 for questions/psychometrics; history-hack-platinum-workbook for DBQ books; history-hack-graphic-organizer-workbook for organizers; udl-cast-expert (CAST 2024 UDL 3.0) for the audit; historian-factcheck-agent for accuracy; copyright-integrity-accreditation for rights clearance; tn-textbook-adoption-agent for Schedule F; history-hack-print-qc-auditor for print QC; history-hack-website-builder for registering this edition in the Social Studies Suite (it ships IN ADDITION to the main History Hack web app, which is becoming a multi-course suite — one platform, entitlement-gated editions, no fork).

Apply the GUARDRAILS block everywhere; run the MASTER QC GATE before packaging; verify + commit + push after each phase. I'll paste the official TN World History & Geography standards now, and drop the sourced primary-source images (with downloadable links + citations) in a Drive folder at Phase 2. STOP and show me the standards→unit map before authoring.
```
