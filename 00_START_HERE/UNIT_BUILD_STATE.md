# UNIT BUILD — STATE & ASSET REGISTRY (read FIRST in any new chat)

**Purpose:** stop re-discovering where things live. This is the single place that records the
qualified skills, the corpus/answer-key locations (repo + Google Drive IDs), skill versions, the
LOCKED rules, and what is done vs. pending. Pair with `BUILD_PREFLIGHT.md` (never build from memory).

## Asset location registry (so nothing gets lost again)

**Skills (canonical, on `main` — pull with `git show origin/main:.claude/skills/<skill>/SKILL.md`):**
| Job | Skill | Version note |
|---|---|---|
| Unit student workbook (7-activity) | `history-hack-unit-content-build` | **main = v1.2** (course-parameterized; adoption-crosswalk+SSP, UDL 3.0 back page, notebook-lined space, Rubric-F). This work branch was stale v1.0. |
| Teacher/lecture deck | `history-hack-tcap-deck-builder` | **main = v3.4** (course-parameterized, palette 1A2332). This branch carries the America-250 migration (1F3A5F) + deck fixes 1–2. Reconcile at PR. |
| Primary Source Packet / DBQ SKU | `history-hack-dbq-workbook` | On main. Uses HIPPO; loads `assets/unit-N-sources.json` which is **MISSING** from git. |
| Graphic organizers (real shapes) | `history-hack-graphic-organizer-workbook` | Correct builder (Venn3/T-chart via `toolkit_lib.py` + pack modules). The print-pipeline toolkit was built by an OUTDATED path — rebuild via this skill. |
| New course orchestrator | `history-hack-new-course-builder` | Add a Primary Source Packet step + preflight guardrail here. |

**Primary-source corpus — IN A REPO (not Drive). CORRECTED 2026-08-05.**
The canonical primary-source + image bank lives in repo **`Trooptoteacher/history-hack-web-app`**
(`add_repo`; workspace `/workspace/history-hack-web-app`), fully version-controlled:
- **Text primary sources (the excerpts):** `public/data/us-history/primary-sources/unit-<N>.json` — **309 records** across units 1–10 (Unit 6 = 28). Fields: `id · standardId · documentTitle · author · date · excerpt · bracketedTerms · question · socialStudiesPractice · options`.
- **Image primary sources:** `public/data/us-history/primary-sources/images/unit-<N>.json` — **112 records** (full Chicago citation, rights, alt/altEs).
- **Image files:** `public/images/textbook/unit-<N>/…` (record `src` points here). Schema: `lib/primary-sources/schema.ts`.
- **Question bank** (assessment source): same repo, `public/data/us-history/questions/unit-<N>/dok-{1,2,3}.json`.
> This IS the corpus. The Packet generator's `unit{N}_all_sources.json` was a build-time EXTRACT of the above — build straight from `history-hack-web-app` instead; do not depend on the ephemeral extract.

**Packet generator:** `build/build_unit_standard.py` in repo `Trooptoteacher/History-Hack-US-History-Workbooks` (HIPPO mode; TeacherKey / Student Worksheets / Clean Reader). Consolidate it into the `history-hack-dbq-workbook` skill so it's pullable with the skill.

**Google Drive = built distribution PDFs ONLY (no source assets there).** Per Sean: **no asset lives only on Drive — everything sourced from a repo.** The masters (DBQ Student Workbook `1A6PvVaNyJM7FpCrY-aQ3XRTRbagLO3A3`, Teacher Answer Key `1iuE6Q6oQhsHLjPc7dp5DVuptEhlI5if_`) are print PDFs whose *content* is the web-app corpus above; the Drive "Source of Truth" doc `1_4FDBH7PHN087n17UmjMg77qi1HlXeNMM9mBRtLH-lg` is only a registry pointing at the repo. If a built PDF is ever needed in git, commit it to a repo — never rely on Drive.

## LOCKED rules captured this session (do not relearn the hard way)
- **Never build from memory.** Pull the most-updated skill from `main` first; run its LOCKED-gate checklist; verify (`verify_workbook_platinum.py` exit 0). See `BUILD_PREFLIGHT.md`.
- **Primary Source Packet** is the product name — NOT "DBQ workbook."
- **HIPPO throughout (text + visual). If a packet references OPTIC, it is the WRONG workflow.**
- **No asset lives only on Google Drive.** Every source asset (primary sources, images, question bank) is version-controlled in `history-hack-web-app`; Drive holds only built PDFs. Build from the repo, never from Drive.
- **Unit 6 is the reference standard.**
- **Deck word wall: NO per-term initials** (no "HA" on Homestead Act).
- **A check answer never shares a slide with its question** (two-slide reveal — spaced).
- **Bidirectional deck↔workbook keying** (`▶ Deck · DI N of M` ↔ `▶ Workbook · Activity N`).
- **Decks include spaced repetition (present) + Future Ready (to add).**
- **Cover required** on every workbook: image · unit · standards · summary · Tennessee Connection (highlighted) · what students/families can expect · copyright.
- **No .docx** — print-first via the WeasyPrint `print-pipeline` (Sean's directive; the skill text still says DOCX — reconcile via skills-only PR).

## Guardrails added this session (in `print-pipeline/` + `00_START_HERE/`)
`BUILD_PREFLIGHT.md` · `verify_workbook_platinum.py` (7-activity + cover + adoption-crosswalk + UDL-back-page gates, wired into the build) · `verify_dbq.py` (blocks image-only or missing-corpus) · `MASTER_SKILLS_MATRIX.xlsx`.

## Done vs pending (Unit 1)
**DONE + verified (print-pipeline, no docx):** Unit 1 **student workbook** — cover, full 7-activity flow, guided Cornell with notebook lines, EN/ES vocab, bank-sourced quiz with corrected keys, visible differentiation, adoption crosswalk + SSP, UDL 3.0 back page, Future Ready + ACT tags; passes the platinum guardrail. Teacher **deck** on America-250 with **fixes 1–2** (no word-wall initials; spaced confidence-check reveal).

**PENDING (the next chat should SHIP these, not build more guardrails):**
1. Deck **fixes 3–4**: bidirectional keying + Future Ready in the deck; then full-deck QC.
2. Open **skills-only PRs to `main`**: workbook v1.2 reconcile + deck v3.4/America-250/fixes; make it canonical.
3. **Recover the DBQ corpus** (`unit-N-sources.json`) from the Drive Source-of-Truth doc; commit into `history-hack-dbq-workbook`; rebuild the Unit 1/6 **Primary Source Packet** (HIPPO) via the qualified generator.
4. **Graphic organizer toolkit** rebuild via the correct skill (real shapes).
5. Consolidate the Primary Source Packet generator + corpus into the skill on `main`; add the step + guardrail to `history-hack-new-course-builder`.

## Repo map (4 repos) + skill consolidation plan — added 2026-08-05

| Repo | Role | Canonical? |
|---|---|---|
| `trooptoteacher-history` | Curriculum + **skills** (`.claude/skills/`, 29) + guardrails + print-pipeline | **YES — single source of truth for skills** |
| `history-hack-web-app` | Primary-source **corpus** (309 text + 112 img), image files, **question bank** (Next.js app) | YES — runtime/data source of truth |
| `History-Hack-US-History-Workbooks` | Production catalog + **Primary Source Packet generator** (`build_unit_standard.py`); built PDFs (Azure/Drive) | build/catalog |
| `history-hack-skill-library` | **Backup bundle** of 9 QC/compliance skills as ZIPs + `qc-reports/` archive; versioned v1.0.0→v1.3.0 | **NO — backup only; partially stale** |

**Skill-library status:** subset backup, NOT canonical. Still ships the RETIRED `tcap-item-writer-v2`
(canonical retired it → `tn-assessment-specialist`). Its Aug-4 v1.2.0/v1.3.0 commits added two things
unique to the backup that must be PORTED into canonical `.claude/skills/`:
1. **`future-ready-framework`** standalone skill (canonical has it only as FRAMEWORKS_CANON §5 — never promoted). → promote as a real skill dir + register in SKILLS.md.
2. **SSP.01–06 required per assessment item** (added under the retired `tcap-item-writer-v2`). → verify/fold into `tn-assessment-specialist`.

**Consolidation (do in the next chat):** (a) port the two items above into canonical via a skills-only PR;
(b) repurpose `history-hack-skill-library` as an auto-generated backup (zip canonical skills on release) —
stop hand-editing skills there; (c) then the four repos have clear, non-overlapping roles.

**Commit built PDFs to a repo (Sean directive):** stop leaving built distribution PDFs Drive-only. Commit
them into `History-Hack-US-History-Workbooks` under a tracked `books/` path (or Git LFS) — remove the
`*.pdf` gitignore for the shipped deliverables so every artifact (source AND output) lives in a repo.
