# History Hack — Unit 6 Visual Asset Package (WWII, TN US.45–US.58)

This package contains the complete staged maps/data-graphics asset set for
History Hack Unit 6 (World War II), built from the verified sourcing
manifest at `SOURCING_MANIFEST.md` (copied unmodified from
`/home/user/workspace/history_hack_unit6_maps_data_sourcing_manifest.md`).

All work was performed locally under `/home/user/workspace/UNIT6_VISUAL_ASSETS`.
**Nothing in this package was uploaded externally.**

## Structure

```
UNIT6_VISUAL_ASSETS/
├── README.md                    (this file)
├── SOURCING_MANIFEST.md         (verified sourcing manifest, copied/cleaned)
├── ASSET_INDEX.csv              (one row per asset: standard, type, status, license, source, attribution, caveat)
├── QA_REPORT.md                 (READY / READY WITH CAVEAT / HOLD for every asset, plus QA methodology)
├── build_assets.py              (reusable Python/matplotlib build script for all charts + fresh maps)
├── build_asset_index.py         (generates ASSET_INDEX.csv)
├── US.45/  US.46/  US.47/  US.48/  US.50/  US.52/  US.53/  US.54/
├── US.55/  US.56/  US.57/  US.58/         (one folder per standard with assets/holds)
└── _basemap_data/                (public U.S. state-boundary GeoJSON used for fresh schematic maps)
```

Only standards with actual assets or holds have folders (US.45–US.58, skipping
any standard not covered by the manifest). US.49 has only a HOLD file (no
data-graphic was in scope for that standard).

## What's in each standard folder

- **Downloaded, verified, unmodified map images** (US.47, US.48, US.50 ×2,
  US.57, US.58) — each preserves exact original pixels from its verified
  public-domain or CC BY 3.0 source. No cropping, re-encoding, or license
  stripping was performed.
- **Fresh-built schematic maps** (US.53, US.54, US.56) — built with
  matplotlib on a public U.S. state-boundary basemap, because no defensible
  ready-made map could be sourced without a share-alike or reprint-permission
  blocker.
- **HOLD files** (US.45, US.46, US.49) — `HOLD_LICENSE_OR_BUILD_FRESH.md`
  documents the exact licensing blocker, the candidate URL, a safer path, and
  the required action. No rejected/unlicensed image binaries were downloaded.
- **Fresh-built data-graphic PNGs** — every chart required by the task,
  built from the corrected/verified figures in the sourcing manifest.
- **`.citation.md` sidecars** — one per image (downloaded or built), with
  title, creator/institution, date, source page URL, direct download/data
  URL, license/rights, commercial-use status, share-alike status, exact
  attribution, verification date (2026-08-01), factual caveats, and alt text.
- **`.data.csv` sidecars** — one per built chart, containing the exact
  underlying data values used to render it.
- **`.svg` pointer files** — one per built chart, noting how to regenerate
  an editable vector version from the paired `.data.csv` via `build_assets.py`.

## How the assets were sourced/built

### Verified downloads (exact pixels preserved)
| Standard | File | Source |
|---|---|---|
| US.47 | `US.47_holocaust_camps_europe_map.png` | [Wikimedia Commons, WW2-Holocaust-Europe (CC BY 3.0)](https://commons.wikimedia.org/wiki/File:WW2-Holocaust-Europe.png) |
| US.48 | `US.48_pearl_harbor_attack_map.png` | [Wikimedia Commons, U.S. Navy NH 83109 (public domain)](https://commons.wikimedia.org/wiki/File:Map_showing_ships_present_at_Pearl_Harbor_on_7_December_1941.png) |
| US.50 | `US.50_dday_normandy_map.jpg` | [Library of Congress, D-Day the 6th of June: Normandy 1944](https://www.loc.gov/item/94681943/) (converted from IIIF service) |
| US.50 | `US.50_pacific_island_hopping_map.jpg` | [Wikimedia Commons, Pacific Theater Areas;map1 (public domain, U.S. Army)](https://commons.wikimedia.org/wiki/File:Pacific_Theater_Areas;map1.JPG) |
| US.57 | `US.57_germany_occupation_zones_map.jpg` | [Wikimedia Commons, Germany occupation zones with border (public domain, modified Ziemke map)](https://commons.wikimedia.org/wiki/File:Germany_occupation_zones_with_border.jpg) |
| US.58 | `US.58_un_51_member_states_map.jpg` | [UNT Digital Library, Newsmap v.4 no.40 (public domain)](https://digital.library.unt.edu/ark:/67531/metadc834/) (front image via IIIF) |

### Fresh-built schematic maps
| Standard | File | Basis |
|---|---|---|
| US.53 | `US.53_great_migration_map.jpg` | [National Archives, The Great Migration (1910-1970)](https://www.archives.gov/research/african-americans/migrations/great-migration) figures on a public U.S. states basemap; explicitly labeled schematic |
| US.54 | `US.54_wra_camps_map.jpg` | [WRA, The Evacuated People (1946), Table 5](https://fraser.stlouisfed.org/files/docs/publications/wra/1946_wra_evacuatedpeople.pdf) locations on a public U.S. states basemap |
| US.56 | `US.56_manhattan_project_sites_map.png` | [NPS, Manhattan Project National Historical Park](https://www.nps.gov/mapr/learn/manhattan-project.htm) 3 confirmed sites on a public U.S. states basemap |

### HOLD (no image produced)
| Standard | Reason |
|---|---|
| US.45 | Only Commons candidate is CC BY-SA 3.0 (share-alike) — commercially unusable as-is |
| US.46 | West Point Digital History Center requires written reprint permission (contact: Jeff Goldberg, (845) 938-2264) |
| US.49 | Only Commons candidate is CC BY-SA 4.0 (share-alike); no PD substitute found |

### Data graphics (all built fresh as PNG)
All 11 required data graphics (US.45, US.46, US.47, US.48, US.50, US.52,
US.53, US.54, US.55, US.56, US.58) were built with `build_assets.py` using
only the corrected/verified figures in `SOURCING_MANIFEST.md`. See
`QA_REPORT.md` for the specific caveats attached to each.

## Design system

- **Palette:** dark navy background/panels, gold and red accents, teal/steel
  categorical colors — History Hack brand direction.
- **Contrast:** primary text ~14:1 on navy background; muted text ~7.8:1 —
  both exceed WCAG AA.
- **No 3D charts. No pie charts.** Color-independent patterns (hatching,
  open/filled markers, dotted overlays) supplement color coding throughout.
- **Direct labels** on every data point instead of relying solely on legends.
- **Source footers** on every chart/map citing institution, publication/
  table, year, and a short URL/domain.
- **16:9-friendly PNGs**, sized around 2400×1350 where the content allows;
  a few charts render slightly taller (up to ~1690 px at 2417 px width) to
  keep footer/caveat text legible without clipping — still slide-scale
  legible and widescreen-friendly.
- **System fonts only** — DejaVu Sans (bundled in the build environment).

## Reproducing the build

```bash
cd /home/user/workspace/UNIT6_VISUAL_ASSETS
python3 build_assets.py        # builds all 11 data graphics + 3 fresh schematic maps
python3 build_asset_index.py   # regenerates ASSET_INDEX.csv
```

Verified map downloads (US.47, US.48, US.50 ×2, US.57, US.58) were performed
via direct `curl` requests to the exact URLs recorded in each `.citation.md`
sidecar and in `SOURCING_MANIFEST.md` — they are not re-fetched by
`build_assets.py`, since the task requires preserving exact original pixels
rather than re-downloading on every run.

## QA status summary

See `QA_REPORT.md` for full detail. Summary: **17 assets READY WITH CAVEAT**,
**3 assets READY**, **3 map HOLDs** (US.45, US.46, US.49). All 20 image files
were verified for valid dimensions, nonzero size, and correct file-format
signatures; all renders were visually inspected for clipping/overlap and
revised where issues were found.
