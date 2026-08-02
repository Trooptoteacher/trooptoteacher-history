# 2026-27 Tennessee Social Studies Academic Standards — Source of Truth

Canonical, machine-readable copies of the Tennessee Academic Standards for Social Studies used across History Hack builds. **One place** so every skill, build, and crosswalk references the same standards instead of scattered copies.

**Valid year:** 2026-27 — the last year of the current (2019) standards before the 2024-adopted revisions take effect in 2027-28.

## Contents (397 standards across 7 courses)

| Level | File (`standards/…`) | Prefix | Standards | Geo-flagged | Status |
|---|---|---|---|---|---|
| Grade 6 | `grade-06-world-history-geography` | 6 | 62 | 17 | ⚠️ verify |
| Grade 7 | `grade-07-world-history-geography` | 7 | 65 | 22 | ⚠️ verify |
| Grade 8 | `grade-08-us-history-geography` | 8 | 75 | 29 | ⚠️ verify |
| High School | `hs-government-civics` | GC | 35 | 2 | ✅ verified |
| High School | `hs-us-history` | US | 7 | 0 | ⚠️ verify |
| High School | `hs-world-history` | W | 89 | 83 | ✅ verified |
| High School / Elective | `tennessee-history` | TN | 64 | 33 | ✅ verified |

## Schema
Each `standards/<course>.json`:
```
{
  "course": "grade-08-us-history-geography",
  "level": "Grade 8",
  "standardsPrefix": "8",
  "title": "…official course title…",
  "source": { … original ingest source … },
  "provenance": "how this copy was obtained",
  "verified": true|false,
  "practices": [ { "code": "SSP.01", "text": "…" } … ],
  "standards": [ { "code": "8.1", "text": "verbatim", "strand": [], "geo": true|false, "cluster": "unit/era heading" } … ]
}
```
`geo: true` marks standards that involve geographic features/maps/movement/regions. `cluster` is the course's own unit/era grouping. `index.json` is the machine-readable manifest of all files.

## How to consume
Reference files by path (e.g. a skill loads `standards-2026-27/standards/tennessee-history.json`). Once this is promoted to its own repo, raw URLs become `https://raw.githubusercontent.com/Trooptoteacher/tn-social-studies-standards-2026-27/main/standards/<course>.json`.

## Why this lives inside `trooptoteacher-history` (for now)
It was meant to be a **standalone repo** (`tn-social-studies-standards-2026-27`). The session's GitHub App cannot create repositories (`403 Resource not accessible by integration`). So it's built here as a self-contained folder — version-controlled and reachable from anywhere. **To promote to a standalone repo:** create an empty repo named `tn-social-studies-standards-2026-27`, then copy this folder's contents into it (nothing else depends on its location). See `PROVENANCE.md` for verification status.

## Known gaps / to-do
- **HS US History** — only US.01–US.07 present; full US.01–US.95 needs assembly from the official TDOE PDF (currently egress-blocked) or the product unit sources.
- **Grades 6–8** standards were reconstructed from GitHub mirrors + WebSearch cross-check (tn.gov is egress-blocked) — verify verbatim text against the official TDOE PDF before treating as final.
- **Economics** (and any other SS electives) not yet included.
