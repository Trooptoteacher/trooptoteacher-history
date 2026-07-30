# World History Hack — Brand Kit

**Edition:** World History Hack — TN *World History & Geography*
**Suite:** A course edition inside the multi-course **Social Studies Suite** (U.S. History flagship · Government & Civics · **World History**). Not a new app, not a fork — reuse the platform brand, tokens, and manifest schema; keys entitlement-gated, teacher-side only.

## Naming & codes
| Item | Value |
|---|---|
| Exact brand string | **World History Hack** (the only permitted "… Hack" string in deliverables) |
| Course name | World History & Geography |
| Standard prefix | `W` (W.01–W.89; a/b splits on W.08, W.56, W.63) |
| Assessment reporting categories | `RC-WH{N}: {unit title}` |
| Course dir | `courses/world-history-hack` |
| Web manifest path | `WEB_EDITION/public/data/world-history/{primary-sources.json, questions.json}` |

## Numbering reconciliation (important)
- The owner's Drive **TCAP item files are named `WH.NN`**; they map **1:1 to standard `W.NN`** (verified: `WH.34` = W.34 "Define total war…", item IDs coded `W34`). Ingest by **standard code**.
- TCAP item files use a **condensed internal unit numbering** (e.g., WWI tagged "Unit 3"). The **authoritative unit assignment is the 13-unit instructional-guide map** in `05_STANDARDS_ALIGNMENT/unit-map.md` (WWI = Unit 7). Re-tag on ingest.
- TCAP items currently exist for **~W.07–W.37 only, 5 items each** → seeds for Phase 8 (expand to 20/standard); author the rest fresh (W.01–06, W.38–89).

## GUARDRAILS (apply every phase — from the playbook)
- **Source of truth only.** Never invent a standard, citation, source, date, name, dynasty, battle, treaty, or number. If it isn't in the standards/source files, it doesn't ship.
- **No cross-edition / source-district leakage.** Forbidden strings in any deliverable: `History Hack` (except the exact `World History Hack`), `Government Hack`, `U.S. History`, `WCS`, `Williamson`, `US.0x`/`US.xx` codes, `GC.xx` codes, `flight log`. Scan `word/*.xml` and deck HTML (base64 stripped first); fail on any hit.
- **Keys teacher-side only.** No answer keys/reteach in any student deck, workbook, or student form.
- **No approval claims.** Label assessments "classroom-formative · pre-field-test".
- **Primary sources genuinely public-domain** (PD-old pre-1929 / PD-US-gov / CC0) with accurate citations (repository + page URL + rights).
- **Historically accurate** — run `historian-factcheck-agent`; when unsure, stay conceptual. Evergreen (no soon-stale "current" facts).
- **UDL 3.0 (CAST, 2024) + MTSS evidenced, not labeled** — a strip counts only where the artifact delivers the affordance.
- **Every phase: verify → commit → push.**

## ⭐ Workbook brand-lock (non-negotiable geometry — verify after any copy)
Page 12240×15840 · margins top/bot **1152**, left/right **1224**, header/footer **720** · printable width **`CW=9792`** (every table sums to 9792) · column splits 4896/3264/2448 · Cornell grid 4896|4896, cells **2448 (cue) | 7344 (notes)**, navy header `1B2A4A`, zebra `F7F5EF`/`FFFFFF` · ruled writing line bottom border `single sz6 space1 color C9C2B4`. Seven activities/standard: Word Bank · Vocabulary Studio/Frayer · Cornell · Close Read · Primary Source/Data · Practice Quiz · CER. Reference: `REFERENCE/USHistory_Unit8_Student_Workbook.docx`.

## UDL / MTSS wording block (verbatim across decks, workbooks, assessments, DBQ books)
> **UDL 3.0 (CAST, 2024):** read-aloud on request · key terms glossed (EN/ES) · respond in writing, speech, or a labeled diagram · large-print & screen-reader friendly. Same learning target for everyone; supports vary the means, not the ceiling.
> **MTSS:** Tier 1 — core lesson for all · Tier 2 — small-group reteach of this standard (Cornell cues + graphic organizer), then re-check · Tier 3 — intensive 1:1 with concrete→representational→abstract scaffolding, progress-monitored to the same standard.
> Citation on every UDL artifact: **CAST (2024). *Universal Design for Learning Guidelines version 3.0.***

© 2026 TroopToTeacher Technologies LLC. Proprietary.
