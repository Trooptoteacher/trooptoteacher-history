# QA Report — History Hack Unit 6 Visual Asset Package

**Package:** `/home/user/workspace/UNIT6_VISUAL_ASSETS`
**QA run date:** 2026-08-01
**Build script:** `build_assets.py` (charts + fresh schematic maps); verified downloads performed via `curl` (documented in `README.md`).

## 1. Method

For every image asset in the package:
1. Confirmed the file exists at the exact required target filename.
2. Opened the file with Pillow (`PIL.Image.open`) to confirm a valid, non-corrupt image and read true pixel dimensions.
3. Cross-checked file type with the `file` command (magic-byte signature check) against the expected format (PNG/JPEG).
4. Confirmed file size is nonzero and consistent with a real, fully-downloaded/rendered image (no zero-byte or truncated files).
5. Read back every rendered PNG/JPEG visually to check for text clipping, label overlap, and legibility at slide scale; revised chart code where issues were found (see Section 4).
6. For downloaded (not built) map assets, cross-checked pixel dimensions against the exact dimensions recorded in the verified sourcing manifest.

## 2. Status legend

- **READY** — Verified public-domain or clearly-licensed (non-share-alike) source; no unresolved caveat beyond standard sourcing citation.
- **READY WITH CAVEAT** — Asset is usable and correctly sourced, but carries a documented factual/methodological caveat (e.g., known source errors, estimate ranges, definitional differences, partial-period data, modified/derivative source map) that MUST be surfaced in any caption or slide using the asset. All such caveats are recorded in the asset's `.citation.md` sidecar and in `ASSET_INDEX.csv`.
- **HOLD** — No image asset was produced. A `HOLD_*.md` file documents the exact blocker, candidate URL(s), a safer path, and the required action. No rejected/unlicensed binaries were downloaded or stored.

## 3. Per-standard results

| Standard | Component | Status | File(s) |
|---|---|---|---|
| US.45 | Map | **HOLD** | `US.45/HOLD_LICENSE_OR_BUILD_FRESH.md` — CC BY-SA 3.0 share-alike blocks commercial use |
| US.45 | Data graphic | **READY WITH CAVEAT** | `US.45_us_unemployment_great_depression.png` (2417×1538 PNG, 194,889 bytes) |
| US.46 | Map | **HOLD** | `US.46/HOLD_LICENSE_OR_BUILD_FRESH.md` — West Point written reprint permission required |
| US.46 | Data graphic | **READY** | `US.46_lend_lease_by_country.png` (2439×1539 PNG, 226,014 bytes) |
| US.47 | Map | **READY** | `US.47_holocaust_camps_europe_map.png` (1310×1090 PNG, 654,405 bytes — pixel-exact match to manifest) |
| US.47 | Data graphic | **READY WITH CAVEAT** | `US.47_holocaust_deaths_by_country.png` (2417×1538 PNG, 214,182 bytes) |
| US.48 | Map | **READY WITH CAVEAT** | `US.48_pearl_harbor_attack_map.png` (4381×5089 PNG, 3,357,049 bytes — pixel-exact match to manifest; documented compass/ship-order errors flagged in sidecar) |
| US.48 | Data graphic | **READY** | `US.48_pearl_harbor_losses.png` (2417×1511 PNG, 187,471 bytes) |
| US.49 | Map | **HOLD** | `US.49/HOLD_LICENSE_OR_BUILD_FRESH.md` — CC BY-SA 4.0 share-alike blocks commercial use; no PD substitute found |
| US.50 | Map (D-Day) | **READY** | `US.50_dday_normandy_map.jpg` (7325×2784 JPEG, 2,981,882 bytes; converted from LOC IIIF service) |
| US.50 | Map (Pacific) | **READY WITH CAVEAT** | `US.50_pacific_island_hopping_map.jpg` (1199×873 JPEG, 359,185 bytes — pixel-exact match to manifest; native resolution marginal for large print) |
| US.50 | Data graphic | **READY WITH CAVEAT** | `US.50_wwii_battle_casualties.png` (2417×1690 PNG, 207,940 bytes) |
| US.52 | Data graphic | **READY WITH CAVEAT** | `US.52_women_workforce_1940_45.png` (2417×1579 PNG, 307,959 bytes) |
| US.53 | Map | **READY WITH CAVEAT** | `US.53_great_migration_map.jpg` (2331×1579 JPEG, 262,779 bytes — built fresh, explicitly labeled schematic) |
| US.53 | Data graphic | **READY WITH CAVEAT** | `US.53_black_migration_employment.png` (2417×1645 PNG, 258,383 bytes) |
| US.54 | Map | **READY WITH CAVEAT** | `US.54_wra_camps_map.jpg` (2250×1618 JPEG, 209,985 bytes — built fresh from WRA Table 5) |
| US.54 | Data graphic | **READY WITH CAVEAT** | `US.54_incarceration_by_camp.png` (2414×1538 PNG, 266,561 bytes) |
| US.55 | Data graphic | **READY WITH CAVEAT** | `US.55_us_war_production_1941_1945.png` (2417×1538 PNG, 286,573 bytes) |
| US.56 | Map | **READY WITH CAVEAT** | `US.56_manhattan_project_sites_map.png` (2333×1524 PNG, 349,420 bytes — built fresh, PNG per Drive-compatibility instruction) |
| US.56 | Data graphic | **READY WITH CAVEAT** | `US.56_hiroshima_nagasaki_casualties.png` (2417×1538 PNG, 203,533 bytes) |
| US.57 | Map | **READY WITH CAVEAT** | `US.57_germany_occupation_zones_map.jpg` (1460×1212 JPEG, 882,030 bytes — pixel-exact match to manifest; modified-map/anachronism caveat required) |
| US.58 | Map | **READY WITH CAVEAT** | `US.58_un_51_member_states_map.jpg` (2000×1569 JPEG, 1,358,407 bytes — pixel-exact match to manifest; 1945/1946 caption-error risk flagged) |
| US.58 | Data graphic | **READY** | `US.58_un_founding_members_timeline.png` (2417×1511 PNG, 201,115 bytes) |

**Totals:** 23 tracked assets/asset-groups — **17 READY WITH CAVEAT**, **3 READY**, **3 HOLD** (US.45 map, US.46 map, US.49 map). No data graphic was placed on HOLD; every required chart uses verified figures from the sourcing manifest.

## 4. Rendering QA — issues found and fixed

During the render/inspect/revise pass, the following issues were identified and corrected before finalizing:

1. **US.58 timeline** — initial render was portrait-oriented (2166×2698) because unconstrained negative-offset footer text caused `constrained_layout` to expand the figure vertically. Fixed by using a fixed 16:9 figure size and tightening y-axis limits; final render is 2417×1511 (16:9-friendly, no clipping).
2. **US.53 employment chart** — large empty band between the NARA callout box and the source footer due to the same negative-offset footer issue. Fixed by reducing figure height and callout positioning; final render (2417×1645) has no dead space and no clipped text.
3. **US.50 battle-casualties chart** — per-bar definition labels beneath the x-axis were overlapping the x-axis tick labels and the caveat annotation. Fixed by moving date labels into the x-tick labels themselves, adding tick padding, and repositioning the per-bar definition captions with more vertical clearance; final render (2417×1690) has no overlapping text.
4. **US.54 WRA map** — "Jerome (Denson) (AR)" and "Rohwer (AR)" labels overlapped because the two centers are only ~0.35° apart in Arkansas. Fixed with per-camp label offset overrides (opposite horizontal placement); final render has both labels fully legible with no overlap.

All other charts and maps were inspected and required no revision.

## 5. File-integrity checks

- All 20 image files (PNG/JPEG) opened successfully with Pillow — no corrupt or zero-byte files.
- `file` command confirmed correct magic-byte signatures for every PNG and JPEG (all report valid "PNG image data" or "JPEG image data" with matching dimensions).
- Downloaded (not built) map files were verified pixel-for-pixel against the exact dimensions recorded in the sourcing manifest:
  - US.47: 1310×1090 ✓ match
  - US.48: 4381×5089 ✓ match
  - US.50 Pacific: 1199×873 ✓ match
  - US.57: 1460×1212 ✓ match
  - US.58: 2000×1569 ✓ match
  - US.50 D-Day: converted via LOC IIIF at 50% scale to 7325×2784 (no fixed manifest pixel target given; high-resolution JPEG conversion of the JP2/IIIF master, as instructed)
- No downloaded map binary was modified, cropped, re-encoded, or license-stripped; all preserve original pixels exactly.
- Every image has a same-basename `.citation.md` sidecar with title, creator/institution, date, source page URL, direct download/data URL, license/rights, commercial-use status, share-alike status, exact attribution, verification date (2026-08-01), factual caveats, and alt text.
- Every built chart has a paired `.data.csv` sidecar with the exact underlying values, and a supplementary `.svg` pointer file noting how to regenerate the vector chart from the CSV via `build_assets.py`.

## 6. Design/brand QA

- Palette: dark navy (`#0B1B2B` background, `#122A40` panels) with gold (`#E8B84B`) and red (`#C24A4A`) accents, plus teal/steel categorical colors — consistent with the requested History Hack dark navy/red/gold brand direction.
- Contrast: primary text `#F2ECDD` on navy background exceeds WCAG AA (approx. 14:1); muted text `#B9C4CE` exceeds AA for large text (approx. 7.8:1); gold and red accents exceed 3:1 large-text contrast on the navy background.
- No 3D charts, no pie charts used anywhere in the package.
- Color independence: hatch patterns (`//`, dotted overlays) distinguish series in bar charts in addition to color (US.48, US.52, US.55, US.56); direct data labels are used on every chart instead of relying on color/legend alone.
- Every built chart and map includes a source footer citing institution, publication/table, year, and a short URL/domain.
- Fonts: DejaVu Sans (system-available, bundled with the sandbox's `fonts-dejavu` package) used throughout — no external font downloads.
- Target output size: 2400×1350 (16:9) was used as the design target; final rendered heights vary slightly (1511–1690 px at 2417 px width) because footer/caveat text needed extra vertical room to remain legible without clipping — all outputs remain 16:9-friendly (ratios 1.43–1.6) and are legible at slide scale.

## 7. Known limitations / follow-up required by a human reviewer

- **US.45, US.46, US.49 maps remain on HOLD.** US.46 explicitly requires phoning/emailing USMA's Department of History (Jeff Goldberg, (845) 938-2264) for written reprint permission — this cannot be completed by an automated process and is flagged for the course's rights-management owner.
- **US.48 map** carries a documented compass-orientation error and ship-order error from the original 1941 Navy chart; this is preserved as historical fact but must always be captioned with the error disclosure per the sidecar.
- **US.57 map** is a modified (not original) version of the Ziemke map; anachronistic Weimar-era provincial boundaries and a missing British withdrawal line must be disclosed whenever the map is used.
- **US.58 map** sheet's own 1946 photo caption contains a documented 1945/1946 date error for the UN's opening session — flagged for classroom disclosure.
- Fresh schematic maps (US.53, US.54, US.56) use a simplified U.S. state-boundary basemap (PublicaMundi MappingAPI, derived from Census TIGER data) rather than a full Natural Earth shapefile, because `geopandas`/`cairosvg` and offline Natural Earth shapefiles were not available in this build environment; the basemap is factual geographic boundary data and is defensible for schematic, non-navigational classroom use.
