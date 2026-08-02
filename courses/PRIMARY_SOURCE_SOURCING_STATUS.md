# Primary-Source Crosswalk — Sourcing Status

_Last updated: 2026-08-02 (overnight autonomous run)_

## Goal
Per-course Excel crosswalk: every standard → 2–4 **academically-accepted, commercial-use-cleared, fully-cited** primary sources, each with a **verified catalog link + download link**, saved to the course's Google Drive folder. Plus charts where possible, Tennessee connections highlighted, and geographic features covered.

## ⛔ Hard blocker hit this run: egress policy
This build environment's network policy **blocks the archive hosts** required to source and verify primary sources. Confirmed via the agent proxy:

| Host | Result |
|---|---|
| `loc.gov` (Library of Congress) | 403 policy denial |
| `catalog.archives.gov` (NARA) | 403 policy denial |
| `si.edu` (Smithsonian) | 403 policy denial |
| `tn.gov` (TDOE standards) | 403 policy denial |
| `archive.org` | 403 policy denial |
| GitHub + package registries | ✅ reachable (only these) |

The proxy README is explicit: **do not route around organization policy denials — report them.** So verified catalog/download links and license checks **cannot be produced in this environment**, and I did **not** guess or fabricate any links (a wrong link or wrong license in a commercial product is worse than a blank cell).

## ✅ What was completed (real, non-fabricated)
Standards secured and per-course **crosswalk scaffolds** built + uploaded to Drive (native `.xlsx`, one row per standard, geographic-feature + TN-connection flags, full source-column schema ready to fill, approved-repository rules embedded on a README tab):

| Course | Standards | Standards provenance |
|---|---|---|
| World History (HS) | 89 | repo-verified |
| Tennessee History | 64 | repo-verified |
| US History — Grade 8 | 75 | GitHub mirror + WebSearch cross-check — **verify vs official TDOE PDF** |
| World History & Geography — Grade 7 | 65 | GitHub mirror + cross-check; exemplar "(e.g., …)" lists omitted — **verify vs official PDF** |
| World History & Geography — Grade 6 | 0 | **blocked** — tn.gov unreachable, no GitHub mirror found; honest stub committed |

## To finish (needs a human/admin step)
1. **Allowlist the archive hosts** in the environment's network policy: `loc.gov`, `catalog.archives.gov`, `si.edu`, `nps.gov`, `history.state.gov`, `dp.la`, `tnencyclopedia.net` / `teva.contentdm.oclc.org`, `tn.gov`, `commons.wikimedia.org` — or run the sourcing pass in an environment that can reach them.
2. Then the verified-source workflow runs per course: 2–4 sources/standard, each fetched + license-confirmed, filling the scaffold's source columns.
3. **Grade 6 standards** + the **Grade 7/8 verbatim text** should be re-pulled from the official TDOE PDF once `tn.gov` is reachable (or drop the official PDF into Drive and I'll ingest it directly, the way the World History / TN History standards were ingested).
4. Charts/graphs for the student workbook: pending source data.

## Where things live
- Standards JSON: `courses/<course>/standards/<course>-standards.json`
- Scaffold generator: run this repo's overnight script against those JSONs
- Drive scaffolds: each course's `_… Hack` folder (Grade 7 got a new `_Grade 7 World History Hack` folder)
