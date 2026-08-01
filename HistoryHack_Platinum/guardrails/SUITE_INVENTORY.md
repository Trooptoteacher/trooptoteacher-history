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

## World History numbering — RESOLVED (no reconciliation needed)

- **`W.xx` is canonical and the item docs already use it.** Verified by reading `WH.05`:
  it opens *"Standard: W.05 — Identify the major causes of the French Revolution…"* (verbatim
  match to the official TDOE standard) with item IDs `WH-MC-W05-001`. **"WH" is just the
  World-History item-bank label; the standard key is `W.xx`.** So `WH.05 = W.05` — there is no
  competing numbering scheme, and no renumbering is required.
- **Item bank quality (reusable as-is):** each doc carries ~5 MC items per standard with IRT
  parameters (a/b/c), DOK + Bloom's + Hess CRM distribution, tagged distractors with
  misconception codes, a QA checklist, TCAP-format flags, and a **JSON export block** — so items
  can be programmatically ingested into the World History question bank.
- **Coverage:** item docs seen span at least W.01–W.35; confirm the full range (through W.89)
  when building. The web-app Unit 1 content and these items share the same `W.xx` keys, so they
  line up directly.

---

## Reuse principle (see `overlap_crosswalk.md`)

Standards overlap heavily across courses (WWI, WWII, Cold War, imperialism, the Constitution,
suffrage, civil rights). **Source and question once, reuse across courses.** The overlap
crosswalk maps each Government/World/TN standard to its U.S. History analog and the specific
already-sourced primary source to reuse — turning the suite into a genuine *combination*
curriculum rather than five siloed products.

---
© 2026 TroopToTeacher Technologies, LLC · Social Studies Hack suite · Internal inventory.
