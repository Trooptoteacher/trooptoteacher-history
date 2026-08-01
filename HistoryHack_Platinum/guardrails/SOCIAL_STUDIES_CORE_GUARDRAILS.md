# Social Studies Hack — CORE Build Guardrails (all courses)

**This is the foundation.** These guardrails are **course-agnostic** and apply to
**every** History Hack / Social Studies Hack course — U.S. History Hack today, and
**Government Hack, World History Hack**, Economics, Geography, and any future
course as they are built. When you start a new course, you inherit this file; you
do not re-derive these rules. Course-specific format/templates (e.g. the U.S.
History "Course Standard / Platinum" layout in `SKILL.md`) sit *on top of* this
core — they may add rules, never weaken the ones below.

Each course differs only in three parameters:
- **Standards set & code prefix** — e.g. US History `US.xx`, World History &
  Geography `W.xx`, U.S. Government & Civics `GC.xx`. Use the official state
  standards, verbatim.
- **Content data** — the course's own `*_content.json` files (same shape).
- **Provenance ledger** — the course's own `geo_provenance.json` (same schema).

The mechanisms and tools below are shared; only the data changes.

---

## 1. Sourcing & citation policy (adoption-grade)

- **Authoritative sources only.** Every factual claim, place, date, and figure
  must be traceable to an **authoritative government, archival, or scholarly
  source** — e.g. the Office of the Historian (U.S. State Dept.), National
  Archives, Library of Congress, National Park Service, U.S. Army/Navy history
  commands, the relevant state historical encyclopedia (e.g. Tennessee
  Encyclopedia), presidential libraries, peer-reviewed scholarship.
- **Approved-source allowlist (enforced).** `guardrails/approved_sources.py` is the
  single policy: `classify(url_or_repo)` returns **approved** (authoritative
  government/archival/scholarly — LoC, NARA, Office of the Historian, NPS, Army/Navy
  history, Smithsonian, Tennessee Encyclopedia, `*.gov`/`*.edu`, …), **prefer_original**
  (Wikimedia Commons / DPLA — acceptable *host* for a genuinely public-domain work,
  but a reviewer prefers the original repository, so swap to LoC/NARA where the same
  item exists), or **blocked** (tertiary encyclopedias — Britannica, Wikipedia — never
  a cited source). Both `geo_review_audit.py` (citations) and
  `asset_standards_crosswalk.py` (image assets) enforce it: **blocked/unrecognized
  sources fail the build; prefer_original is a warning to upgrade.** Applies to every
  course.
- **Primary sources** in student materials must be public-domain (or licensed)
  with **full citations**; secondary claims trace to identified scholarly sources
  via a per-unit bibliography (Chicago/Turabian).
- This satisfies the **state adoption rubric's accuracy/currency criterion**
  (TDOE High School Social Studies rubric, C5 "Historical Accuracy & Currency").

## 2. Geography is a priority skill (high-miss)

- Geography is one of the **most-missed skills on the state EOC**, across courses.
- **Any standard that carries geography data (`geo` set) MUST render a
  Geographer's Lens page — never silently skip it.** (This was a real bug once;
  the guard is now permanent.)
- The page opens with the prominent **`geoPriorityBar()`** banner ("PRIORITY
  SKILL · Geography — do not skip it"), the same prominence vocabulary priority
  terms get. `geo` with an empty `geo_places` still renders the page.

## 3. Content review & SME sign-off (tracked in data)

- Authored content that isn't machine-derived (geography places, narrative,
  interpretive framing) carries a **review-status object** and **citations**:
  `geo_sources: [...]` and
  `geo_review: {status: "drafted|sme_approved|needs_fix|n/a", by, date, note}`.
- **A subject-matter expert signs off by setting `status: "sme_approved"`** (with
  `by`/`date`) — that is where sign-off is recorded, per course.
- **Historical/content accuracy** also requires **external expert review**;
  attach the reviewer's report to the course's adoption package.

## 4. Standards alignment

- Use the **official state standards, verbatim** (text and code). Never paraphrase
  a standard into the `tn`/standard-text field.
- Every deliverable maps to its standard; the standards *range* is a course
  parameter, not a hard-coded US.xx list.

## 5. Accessibility, bias, and print-safety (carried from the format layer)

- **UDL/MTSS** supports built in; **bilingual** (EN/ES) where the course serves
  ELLs; **read-aloud**-friendly.
- **De-bias** assessment answer positions (no key clustering) with one shared
  helper across every surface.
- **Print-safe**: letter size, margins, header/footer, copyright, no bleed; images
  print-legible and licensed.

## 6. Legal / compliance / currency

- **IP & privacy**: third-party images/sources cleared or public-domain with
  attribution; FERPA/COPPA posture accurate; correct AI-use disclosures.
- **Adoption**: maintain the state adoption self-assessment (Schedule F) per
  course.
- **Currency**: the quarterly **Administrative Review**
  (`06_COMPLIANCE_INTERNAL/ADMINISTRATIVE_REVIEW.md`) tracks changes to standards,
  TDOE alignment, use of AI, and new laws — for the **whole suite**, not one
  course.

---

## Shared tooling (course-agnostic)

Both scripts operate on `build_*/*_content.json` under a course's Platinum tree, so
they work for any course that follows the layout:

- **`guardrails/apply_geo_provenance.py`** — stamps the course's `geo_provenance.json`
  (citations + review status) into its content JSONs. Idempotent; never overwrites
  an `sme_approved` standard. **Run after any re-derive.** Each course supplies its
  own `SOURCES`/ledger; the stamping mechanism is shared.
- **`guardrails/geo_review_audit.py`** — the sign-off + sourcing ledger. Reports
  places/sources/review status across all units and **fails on tertiary sources**
  or (with `--require-approved`) on any standard not yet SME-approved. Wire it into
  each course's build and the quarterly Administrative Review.
- **`guardrails/asset_standards_crosswalk.py`** — the **source & asset crosswalk**:
  rolls every primary source, image, map, and chart up against the standard it
  serves (with citation, license, and geographic positions), and with `--strict`
  fails on any standard missing a primary source, any asset missing a
  citation/license, or any geography standard missing positions. This is the
  sourcing backbone of Phase 2.

## Building a whole course

See **[`COURSE_PRODUCTION_WORKFLOW.md`](./COURSE_PRODUCTION_WORKFLOW.md)** — the
cradle-to-grave pipeline (Phase 0 standards ingest → 9 adoption package), the full
per-course deliverable inventory (workbooks, teacher guides, decks, organizer
toolkit, assessment book, covers, lesson plans, narrative textbook with the flight
crew + Flight Logs, and the DBQ book last), the web-app + testing-DB parity
requirement, the quality gates, and the skill that owns each phase.

## Starting a new Social Studies Hack course (Government, World History, …)

1. Create the course's Platinum tree with the same `build_unit*/` layout and
   `*_content.json` shape.
2. Set the **standards set + code prefix** to the official state standards for that
   course (verbatim text and codes).
3. Author each standard's `geo` + `geo_places` where the standard carries
   geography; the builder's geo guard + `geoPriorityBar()` apply automatically.
4. Create the course's **`geo_provenance.json`** with authoritative citations
   (§1 policy — no tertiary sources) and `geo_review: drafted`.
5. Run `apply_geo_provenance.py` then `geo_review_audit.py` — must pass the
   tertiary-source check; drive standards to `sme_approved` before adoption.
6. Everything else in the format layer (`SKILL.md`) — templates, de-bias,
   print-safety, decks — applies as written.

---
© 2026 TroopToTeacher Technologies, LLC · Social Studies Hack suite · Internal build foundation.
