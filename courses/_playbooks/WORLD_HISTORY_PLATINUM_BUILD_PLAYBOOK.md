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
16. **Compliance pack** — standards matrix, scope & sequence, UDL/MTSS framework crosswalk, Schedule F alignment
17. **Web edition** manifests (primary-sources + questions) · **Master Deliverables Index** · **district package ZIP**

---

## SKILLS ROSTER — which skill runs which phase
| Skill | Use for |
|---|---|
| `history-hack-course-standard-builder` | Orchestrate the whole cradle-to-grave course build (Phase 1) |
| `history-hack-curriculum-architect` / `instructional-design-specialist` | Unit structure, instructional flow, content design (Phase 3) |
| `history-hack-graphic-organizer-workbook` | The Graphic Organizer Toolkits (Phase 5) |
| `history-hack-platinum-unit-builder` | Consolidate a unit's workbook/guide/deck to platinum (Phase 6) |
| **`tn-assessment-specialist`** (the question/assessment skill) | Write + assemble + QC assessment items and books (Phases 7–8) |
| **`tcap-item-writer-v2`** (the psychometrics/item-writer skill) | Full psychometrics — IRT 3PL, Hess CRM, distractor codes (Phase 8) |
| `history-hack-platinum-workbook` | Standalone **DBQ / primary-source investigation books** (Phase 9) |
| `udl-cast-expert` | CAST UDL 3.0 audit + evidence-mapped gap closure (Phase 11) |
| `historian-factcheck-agent` | Claim-by-claim factual verification of content + items |
| `tn-textbook-adoption-agent` | Schedule F / adoption alignment (Phase 12) |
| `history-hack-print-qc-auditor` | Print-readiness QC of PDFs/docx |
| `docx` / `pdf` / `pptx` | Format work (tagged PDF, large-print, packaging) |

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
- **Question-bank toolkit** (subject-agnostic): `courses/foundations-constitutional-government/08_QUESTION_BANK/{consolidate_bank.py, bank_qc.py, add_udl_remediation.py, generate_parallel_tests.py, build_inventory.py}`.
- **Golden docx builders** (parameterized): `BUILD/unit1/build_{workbook,teacher_guide,cover,assessment_book}.js` (carry UDL/MTSS callout, multi-modal CER, Choice & Voice, Reflect & Connect, LARGEPRINT flag) + `BUILD/engine/`.
- **Deck builder** `BUILD/decks/Unit1_Teacher_Deck/build_deck.py` (per-standard UDL/MTSS strip, AUDIENCE=student, base64-stripped leak guard, tagged-PDF).
- **Image pipeline** `BUILD/sync_images.py`.
- **Compliance templates** `06_COMPLIANCE_INTERNAL/{udl-mtss-framework.html, UDL_AUDIT_REPORT.md, MTSS_SUPPORT_MAP.md, ACCESSIBILITY_STATEMENT.md}` + `05_STANDARDS_ALIGNMENT/{standards-matrix.html, scope-sequence.html, udl_mtss_alignment.json}`.

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

## Lessons carried from the Government build
- **Leak scans must strip base64** before scanning decks (3-letter guards false-trip on random image bytes).
- **Drive connector: hard 10 MB per-file cap** — re-export bigger; **tiny inline files can truncate** — pull ≥~1200 px so they route through the on-disk tool-result path; decode with `jq -r '.content' | base64 -d`.
- **A "strip" is a signpost, not embedding** — the CAST audit credits only guidelines with a real artifact affordance; close gaps with design, not labels.
- **LibreOffice may be non-functional in the sandbox** — deck PDFs tag via Chromium `--export-tagged-pdf`; workbook tagged-PDF is a one-command Word/LibreOffice export on the district side (document honestly).
- **Reference-unit builders may be gitignored** — the rendered deliverables are what's tracked.

## One-shot kickoff prompt
```
Build a new licensable "World History Hack" course edition ({{COURSE_NAME}}) to the platinum standard of courses/foundations-constitutional-government, following courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md phase by phase — producing EVERYTHING in its Deliverables Inventory (content, teacher + student slide decks, student workbooks + large-print, teacher guides, organizer toolkits, assessment books, DBQ books, covers, the 20-item/standard question bank with psychometrics + UDL + remediation, parallel-test generator, inventory + standards crosswalk, primary-source bank, 9/9 CAST UDL 3.0 audit, MTSS map, accessibility statement, compliance pack, master index, web edition, district package). Invoke history-hack-course-standard-builder to orchestrate; tn-assessment-specialist + tcap-item-writer-v2 for questions/psychometrics; history-hack-platinum-workbook for DBQ books; history-hack-graphic-organizer-workbook for organizers; udl-cast-expert (CAST 2024 UDL 3.0) for the audit; historian-factcheck-agent for accuracy. Apply the GUARDRAILS block everywhere; verify + commit + push after each phase. I'll paste the official TN World History & Geography standards now, and drop the sourced primary-source images (with downloadable links + citations) in a Drive folder at Phase 2. STOP and show me the standards→unit map before authoring.
```
