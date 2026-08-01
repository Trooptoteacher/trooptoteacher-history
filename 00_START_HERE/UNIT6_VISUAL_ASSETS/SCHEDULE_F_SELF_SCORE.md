# Schedule F Self-Score — Unit 6 Visual Assets (section)

**Instrument:** TDOE High School Social Studies Instructional Materials Scoring Rubric (Schedule F).
**Scale:** 0 = not present · 1 = present, intent not fully met · 2 = present and fully met.
**Scope:** the Unit 6 visual-asset layer (maps + data graphics). Full-unit Schedule F (Tables 2–4,
/36) is scored at the unit deliverable level; this section-score covers only the indicators the
visual layer touches. **Honesty doctrine applies: scored as-built, gaps stated plainly.**
**Status:** TroopToTeacher Technologies LLC self-assessment (supplemental material, T.C.A. §49-6-2202).

## Indicators the visual layer touches

| Indicator | Score | As-built evidence / gap |
|---|---|---|
| **Content accuracy** (foundational — TDOE Policy 2.600) | **1 → 2 after remediation** | Data graphics all verified (see `FACTCHECK_REPORT.md`). **BUT three sourced maps carry documented factual defects** (see deficiencies). A map with known errors cannot be marked fully met until fixed. |
| **SSP.06 Geographic awareness** (Table 3) | **2** | Maps for US.47 (camps), US.50 (D-Day + Pacific), US.53 (migration), US.54 (WRA camps), US.56 (Manhattan sites), US.57 (occupation zones), US.58 (UN) give students real geographic reasoning material across the unit. |
| **Disciplinary literacy** (Table 2) | **2** | Data graphics (unemployment, Lend-Lease, war production, casualties, incarceration) require reading charts/quantitative evidence; maps require spatial reasoning. |
| **Multiple perspectives** (Table 2) | **2** | Visual set spans home front, women, Black war workers + Great Migration, Japanese American incarceration, the Holocaust — not a single-narrative set. |
| **Accessibility** (Table 4) | **2** | Every asset has **alt text** in its `.citation.md`; charts are value-labeled + grayscale-legible; print-res + digital. Aligns with UDL/WCAG intent. |
| **Sourcing integrity** (accuracy/credibility) | **2** | Every asset has a `.citation.md` (creator, date, source URL, license, commercial-use, share-alike, attribution, caveats). Built maps disclose basemap + data provenance. `QA_REPORT.md` + `ASSET_INDEX.csv` bind it. |

## Deficiencies (severity-rated)

| # | Sev | Asset | Issue | Remediation |
|---|---|---|---|---|
| 1 | **MAJOR** | `US.48_pearl_harbor_attack_map.png` | Sourced map has **documented compass / ship-order errors** (per its `.citation.md`). Known factual errors fail Policy 2.600 accuracy. | **Do not ship as-is.** Replace with an accurate PD Pearl Harbor map (NHHC/NARA) that passes QA, **or drop the map** (US.48 is carried by the losses chart + Pearl Harbor photos). |
| 2 | **MINOR** | `US.57_germany_occupation_zones_map.jpg` | Modified-map / anachronism caveat — could misdate/misattribute if used raw. | Mandatory caption caveat stating date + that it is a modified/derivative map; or replace with a clean PD occupation-zones map. |
| 3 | **MINOR** | `US.58_un_51_member_states_map.jpg` | 1945/1946 caption-error risk (Newsmap dating). | Caption must state the correct date; verify against the source before print. |

## Maps recommendation (Schedule-F-grounded)

- **Approve for use:** US.47 Holocaust camps, US.50 D-Day, US.50 Pacific — clean, sourced, accurate.
- **Approve (built schematics):** US.53 Great Migration, US.54 WRA camps, US.56 Manhattan sites —
  academically defensible **because** they are clearly labeled "schematic," plot documented
  locations on a PD U.S. Census basemap, and cite authoritative data (NPS/WRA/Census). They support
  SSP.06 and carry no license risk. A TDOE reviewer accepts a labeled schematic with sourced data.
- **Fix or drop before approval:** US.48 (MAJOR — known errors), US.57 & US.58 (MINOR — caption).
- **No map (resolved):** US.46 removed; US.45 & US.49 optional, never built.

## Section verdict
**Not yet fully approvable** — one MAJOR accuracy deficiency (US.48 map) must be resolved. Everything
else meets the bar. On remediation of deficiency #1 (and captions for #2/#3), the visual layer is
Schedule-F-clean: accurate, sourced, SSP.06-supporting, accessible, commercial-safe.
