# Social Studies Hack Suite — Asset Inventory & Reconciliation

**Verify before you build. Nothing in this list gets recreated — it gets reused or extended.**
Snapshot as of this session; refresh when assets change.

Build priority (per owner): **US History (template, done) → Government → World History →
Tennessee**, then **8th → 7th → 6th Grade**.

---

## Per-course status

### 1. U.S. History Hack — `US.xx` — REFERENCE / TEMPLATE (done)
- **Content repo** (`HistoryHack_Platinum/build_unit1…10`): full content JSONs (US.01–US.95),
  images, assessments, exit tickets, print builders. Geo provenance complete (20 standards,
  authoritative citations, drafted). Asset crosswalk generated.
- **Web app** (`public/data/us-history/`): fully authored (254 files, 87 MB).
- This is the platinum standard every other course matches.

### 2. Government Hack — `GC.xx` (GC.01–GC.35)
- **Sourcing: COMPLETE.** `Government_Hack_Primary_Source_Sourcing_List_Completed.xlsx`
  (Drive) — every standard has a verified primary source with citation, rights/license,
  MIME, dimensions, SHA-256, and a `GC.NN_short-name` filename. Ingest with
  `ingest_sourcing_list.py`.
- **Standards:** in the TN Standards folder + `Standards & I Can` (Legislative Branch,
  Citizen Participation, Foundations of Constitutional Government strand PDFs).
- **Web app** (`public/data/government/`): stub (6 files).
- **Content/print repo:** none yet.
- *Sourcing note:* the completed list leans on Wikimedia Commons for ~20/35 — acceptable for
  PD works but **prefer the original repository (LoC/NARA)**; 3 rows flagged VERIFY
  (GC.13, GC.29, GC.30). The allowlist audit enforces this.

### 3. World History Hack — `W.xx` (W.01–W.89) — Unit 1 STARTED, then paused
- **Web app** (`public/data/world-history/`): **Unit 1 fully authored** — "Age of
  Revolution" (W.01–W.09): textbook 460 KB, vocabulary 64 KB, **Cornell notes** 27 KB.
  **Units 2–13 are scaffolded stubs.** Canonical numbering here is **W.xx** (matches the
  official TDOE PDF).
- **Drive:** `WH.01–WH.35+ TCAP World History Assessment Items.docx` (legacy **WH.xx**
  numbering) + `2025-2026, HS, World History and Geography` standards docx.
- **Content/print repo:** none yet.

### 4. Tennessee History Hack — (TN standards) — not started
- **Standards:** `Tennessee.pdf` in the TN Standards folder.
- Drive folder + sourcing-list template created (empty, awaiting standards population).

### 5–7. Eighth / Seventh / Sixth Grade History Hack — not started
- **Standards:** `8th Grade.pdf`, `7th Grade.pdf` in the TN Standards folder (6th grade TBD).
- 8th-grade Drive folder + sourcing-list template created.

---

## World History numbering reconciliation — `W.xx` (canonical) vs `WH.xx` (legacy)

- **Canonical = `W.xx`** — matches the official TDOE World History & Geography standards
  (W.01–W.89) and the web-app Unit 1 content.
- **Legacy = `WH.xx`** — the Drive assessment-item docs (`WH.01 … WH.35+`). These predate the
  web-app content and stop around 35 (vs 89 standards).
- **Working hypothesis:** `WH.NN` maps to `W.NN` (same number, older prefix) for the standards
  that existed when the items were written. **This must be spot-verified** — open 2–3 item docs
  (e.g. WH.05, WH.17) and confirm the item text matches the `W.05` / `W.17` standard before any
  item is reused. Do not assume a clean 1:1 across all numbers.
- **Action:** once verified, rename/alias the item bank to `W.xx`; treat `W.xx` as the single
  source of truth everywhere (content, items, sourcing, web app).

---

## Reuse principle (see `overlap_crosswalk.md`)

Standards overlap heavily across courses (WWI, WWII, Cold War, imperialism, the Constitution,
suffrage, civil rights). **Source and question once, reuse across courses.** The overlap
crosswalk maps each Government/World/TN standard to its U.S. History analog and the specific
already-sourced primary source to reuse — turning the suite into a genuine *combination*
curriculum rather than five siloed products.

---
© 2026 TroopToTeacher Technologies, LLC · Social Studies Hack suite · Internal inventory.
