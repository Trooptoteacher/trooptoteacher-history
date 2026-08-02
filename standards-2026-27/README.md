> **AUTHORITATIVE SOURCE:** https://github.com/Trooptoteacher/2026-27-Tn.-Social-Studies-Standards
> This folder is a synced mirror kept for in-repo builds. Edit the standalone repo; re-sync here.

# 2026-27 Tennessee Social Studies Academic Standards — Source of Truth

Canonical, machine-readable copies of the Tennessee Academic Standards for Social Studies, parsed **verbatim from the official TDOE PDFs**. One place so every skill, build, and crosswalk references the same standards.

**Valid year:** 2026-27 — the last year of the current standards before the 2024-adopted revisions take effect in 2027-28.

## Contents — 485 standards across 7 courses

| Level | File (`standards/…`) | Prefix | Codes | Standards | Geo | Status |
|---|---|---|---|---|---|---|
| Grade 6 | `grade-06-world-history-geography.json` | 6 | 6.01–6.62 | 62 | 42 | ✅ verified (official PDF) |
| Grade 7 | `grade-07-world-history-geography.json` | 7 | 7.01–7.65 | 65 | 56 | ✅ verified (official PDF) |
| Grade 8 | `grade-08-us-history-geography.json` | 8 | 8.01–8.75 | 75 | 48 | ✅ verified (official PDF) |
| High School | `hs-government-civics.json` | GC | GC.01–GC.35 | 35 | 2 | ✅ verified (official PDF) |
| High School | `hs-us-history.json` | US | US.01–US.95 | 95 | 48 | ✅ verified (official PDF) |
| High School | `hs-world-history.json` | W | W.01–W.89 | 89 | 83 | ✅ verified (official PDF) |
| High School / Elective | `tennessee-history.json` | TN | TN.01–TN.64 | 64 | 33 | ✅ verified (official PDF) |

## Schema
Each `standards/<course>.json`:
```
{
  "course": "...", "level": "...", "standardsPrefix": "...", "title": "official course title",
  "source": { "drive_file_id": "...", "title": "official TDOE PDF" },
  "provenance": "Official TDOE PDF — verbatim", "verified": true,
  "practices": [ { "code": "SSP.01", "text": "verbatim" } … SSP.06 ],
  "standards": [ { "code": "6.01", "text": "verbatim incl. bulleted sub-items", "strand": ["C","G","H"], "geo": true, "cluster": "era/unit heading w/ dates" } … ]
}
```
`geo` is true when the standard's content strand includes **G** (geography). `cluster` is the course's own era/unit heading. `strand` letters: C-Culture, E-Economics, G-Geography, H-History, P-Politics/Government, T-Tennessee, TCA-legally required. `index.json` is the manifest.

## How to consume
Raw URL pattern: `https://raw.githubusercontent.com/Trooptoteacher/2026-27-Tn.-Social-Studies-Standards/main/standards/<course>.json`

## Provenance
All seven courses are parsed verbatim from the official TDOE Social Studies standards PDFs (stored in the owner's Drive "TN Standards 2026-27" folder). See `PROVENANCE.md`. Grades 6-8 and HS US History were re-parsed directly from those PDFs (replacing earlier GitHub-mirror drafts); HS World History, Government, and Tennessee History were ingested from the same official PDFs.
