# Unit 6 (WWII) — Visual Sourcing Manifest

**Scope:** MAPS and DATA GRAPHICS only. Your Google Drive already holds ~3 **cited photos** per standard
(US.45–US.58) — those are done and are **not** re-listed here. The gap across the whole system (Drive
*and* decks) is maps and data charts; this manifest fills exactly that.

## How to read this
- Each row: asset · description · source institution · candidate link · license · attribution · target filename.
- **Verification status:** links were surfaced by web search and the license reasoning is sound, but
  **WebFetch is blocked in the build environment**, so no page was opened to read its license box here.
  **Confirm each license at download** (open the file page; for Wikimedia use the API call below) — your
  standard sourcing step. This keeps the product defensible.
- **Data graphics are BUILD-FRESH** from public-domain datasets (Census/BLS/OMB/official histories), so the
  chart itself is unambiguously ours — the row gives the PD data source, not a copyrighted chart.
- Drop each file into `00_START_HERE/UNIT6_VISUAL_ASSETS/US.<nn>/` using the target filename.

**Wikimedia license check (do this per Commons file at download):**
`https://commons.wikimedia.org/w/api.php?action=query&titles=File:<NAME>&prop=imageinfo&iiprop=url|extmetadata&format=json`
→ read `LicenseShortName`, `UsageTerms`, `Artist`, and `url` (the full-res `upload.wikimedia.org` link).

## License cautions (read before downloading)
- ✅ Prefer **U.S. federal / PD** (NARA, LOC, West Point/USMA, Army CMH, Census, BLS, OMB, DOE, NPS, presidential libraries).
- ⚠️ **CC BY-SA (share-alike)** items are flagged below — allowed with attribution, but for a paid product
  prefer the PD substitute noted, or **build the map fresh** on a PD basemap.
- ⛔ **Do NOT use UN Photo (media.un.org)** for US.58 — UN retains rights. Use the Truman Library/NARA image.
- ⛔ Excluded already: Getty, Alamy, Shutterstock, Statista, Britannica, Densho graphics (CC BY-NC-SA), Pittsburgh Courier scans.

---

## MAPS

| Std | Description | Source | Candidate link | License | Attribution | Filename |
|---|---|---|---|---|---|---|
| US.45 | Political map of Europe, interwar 1929–1938 (fascist Italy/Germany + USSR) | Wikimedia (user) | https://commons.wikimedia.org/wiki/File:EUROPE_1929-1938_POLITICAL_MAP.svg | ⚠️ CC BY-SA 2.5 — or build fresh on a PD "Europe 1938" basemap | "Europe 1929–1938 Political Map, Wikimedia Commons, CC BY-SA 2.5" | US.45_europe_political_map_1938.svg |
| US.46 | Axis aggression/expansion in Europe & Asia, 1935–1941 | USMA West Point, Dept. of History (WWII Atlas) | https://dhc.westpoint.edu/atlases/ | ✅ PD (U.S. federal, USMA) | "West Point Atlas, USMA Dept. of History. Public domain (U.S. gov)." | US.46_axis_expansion_map.jpg |
| US.47 | Nazi concentration & extermination camps across Europe | Wikimedia (Dennis Nilsson) | https://commons.wikimedia.org/wiki/File:WW2-Holocaust-Europe.png | ⚠️ CC BY 3.0 — attribution; USHMM's own maps are ©, do NOT lift | "WW2-Holocaust-Europe by Dennis Nilsson, Wikimedia Commons, CC BY 3.0" | US.47_holocaust_camps_europe_map.png |
| US.48 | Ships at Pearl Harbor, 7 Dec 1941 (Battleship Row) | U.S. Navy / NARA | https://commons.wikimedia.org/wiki/File:Map_showing_ships_present_at_Pearl_Harbor_on_7_December_1941.png | ✅ PD (U.S. Navy) | "U.S. Navy via National Archives. Public domain." | US.48_pearl_harbor_attack_map.png |
| US.49 | World map: Allies vs. Axis vs. neutral (optional — photos already cover this) | Wikimedia (user) | https://commons.wikimedia.org/wiki/File:Map_of_participants_in_World_War_II.svg | ⚠️ CC BY-SA 4.0 — or build fresh | "Map of participants in World War II, Wikimedia Commons, CC BY-SA 4.0" | US.49_allies_vs_axis_world_map.svg |
| US.50 | D-Day / Normandy invasion, 6 June 1944 | U.S. Army CMH via Library of Congress | https://www.loc.gov/item/94681943 | ✅ PD (U.S. Army CMH) | "Map, D-Day Normandy 1944, U.S. Army Center of Military History, via LOC. Public domain." | US.50_dday_normandy_map.jpg |
| US.50 | Pacific Theater / island-hopping | U.S. Army CMH via Wikimedia | https://commons.wikimedia.org/wiki/File:Pacific_Theater_Areas;map1.JPG | ✅ PD (U.S. Army CMH) | "Pacific Theater Areas, U.S. Army Center of Military History. Public domain." | US.50_pacific_island_hopping_map.jpg |
| US.53 | The Great Migration, 1910–1970 (flows/destinations) | U.S. Census Bureau | https://www.census.gov/dataviz/visualizations/020 | ✅ PD (U.S. Census) | "The Great Migration, 1910–1970. U.S. Census Bureau. Public domain." | US.53_great_migration_map.jpg |
| US.54 | WRA incarceration camp locations (10 camps, western U.S.) | National Park Service ("Confinement and Ethnicity") | https://www.npshistory.com/series/anthropology/wacc/74/chap1.htm | ✅ PD (U.S. gov, NPS) | "WRA relocation center locations, NPS, 'Confinement and Ethnicity.' Public domain." | US.54_wra_camps_map.jpg |
| US.56 | Manhattan Project sites (Oak Ridge TN, Los Alamos, Hanford) — **TN** | Wikimedia (user) / OSTI | https://commons.wikimedia.org/wiki/File:Manhattan_Project_US_Canada_Map.svg  ·  PD alt: https://www.osti.gov/opennet/manhattan-project-history/Resources/site_map.htm | ⚠️ CC BY-SA 3.0 — prefer OSTI PD map or build fresh | "Manhattan Project US/Canada Map, Wikimedia, CC BY-SA 3.0 (or OSTI, PD)" | US.56_manhattan_project_sites_map.svg |
| US.57 | Allied occupation zones of Germany + Berlin, 1945 | U.S. Army via Wikimedia | https://commons.wikimedia.org/wiki/File:Germany_occupation_zones_with_border.jpg | ✅ PD (U.S. Army) | "Allied occupation zones of Germany, 1945, U.S. Army. Public domain." | US.57_germany_occupation_zones_map.jpg |
| US.58 | UN founding — "51 Nations Unite for Peace" Newsmap (world + members) | U.S. War Dept. Newsmap via UNT Digital Library | https://digital.library.unt.edu/ark:/67531/metadc834/ | ✅ PD (U.S. War Dept.) | "Newsmap, U.S. War Department, 1946, via UNT Digital Library. Public domain." | US.58_un_51_member_states_map.jpg |

## DATA GRAPHICS — build fresh from these public-domain datasets

| Std | Chart to build | PD data source | Link | Key figures (from search — verify) | Filename |
|---|---|---|---|---|---|
| US.45 | U.S. unemployment, 1929–1940 (Great Depression severity) | U.S. Dept. of Labor history / BLS (FRASER) | https://www.dol.gov/general/aboutdol/history/chapter5 | peak ~24.9% (1933) | US.45_us_unemployment_great_depression.png |
| US.46 | Lend-Lease aid by recipient country | U.S. War Dept. (1952) via AHA | https://www.historians.org/resource/how-much-of-what-goods-have-we-sent-to-which-allies/ | Br. Commonwealth $31.6B · USSR $11B · France $3.2B · China $1.6B (~$49.1B) | US.46_lend_lease_by_country.png |
| US.47 | Jewish losses in the Holocaust by country | USHMM (facts; build fresh — do not copy USHMM graphic) | https://encyclopedia.ushmm.org/content/en/article/jewish-losses-during-the-holocaust-by-country | Poland ~3M; USSR ≥1M; etc. | US.47_holocaust_deaths_by_country.png |
| US.48 | Pearl Harbor losses (ships, aircraft, casualties) | Naval History & Heritage Command | https://www.history.navy.mil/ (Pearl Harbor raid) | 2,403 killed; 1,178 wounded; 4 BB sunk +4 damaged; ~188 aircraft | US.48_pearl_harbor_losses.png |
| US.50 | Casualties across major battles (Midway, D-Day, Iwo Jima, Okinawa) | NHHC + Army CMH | https://www.history.navy.mil/ | Midway ~317; D-Day ~2,501; Iwo Jima ~6,800 KIA; Okinawa 12,520 KIA/MIA | US.50_wwii_battle_casualties.png |
| US.52 | Women in the U.S. labor force, 1940–1945 | BLS / U.S. Census | https://www.census.gov/topics/employment.html | 11.97M → 18.61M (28% → ~36%) | US.52_women_workforce_1940_45.png |
| US.53 | Black migration numbers + wartime defense employment | U.S. Census / NARA (FEPC) | https://www.archives.gov/research/african-americans/migrations/great-migration | ~5M (1940–70); defense jobs 3% → ~8% | US.53_black_migration_employment.png |
| US.54 | Number incarcerated by WRA camp / total | WRA, *The Evacuated People* (1946), PD | (NARA RG 210 / WRA report) | 120,313 total; 10 camps | US.54_incarceration_by_camp.png |
| US.55 | U.S. war production 1941–45 (aircraft/tanks/ships) + military % of GDP | AAF Statistical Digest; War Production Board; OMB Historical Tables 3.1/6.1 | https://www.whitehouse.gov/omb/budget/historical-tables/ | build fresh | US.55_us_war_production_1941_1945.png |
| US.56 | Hiroshima & Nagasaki casualties/effects | Manhattan Engineer District report (1946), PD | https://www.atomicarchive.com/resources/documents/med/med_chp10.html | build fresh (MED ch.10) | US.56_hiroshima_nagasaki_casualties.png |
| US.58 | UN founding members (51) / timeline | UN founding facts (PD Newsmap doubles as source) | https://digital.library.unt.edu/ark:/67531/metadc834/ | 50 signed 6/26/1945; Poland 10/15/1945 = 51 | US.58_un_founding_members_timeline.png |

---

## Priority order (biggest instructional payoff first)
1. **US.50** D-Day + Pacific maps — WWII's signature geography; nothing teaches island-hopping without them.
2. **US.56** Manhattan Project sites map (**Oak Ridge, TN** — your differentiator) + Trinity/Westcott photos you already have.
3. **US.47** Holocaust camps map; **US.54** WRA camps map — geography is core to both standards' content.
4. **US.45 / US.46 / US.57** Europe political / Axis expansion / occupation-zones maps — the war's arc.
5. **US.58** UN members map (**Cordell Hull, TN**); **US.48** Pearl Harbor map.
6. Data graphics (build-fresh) — add as the deck build reaches each standard.

## Notes
- No maps/data are duplicated from your Drive photo library (checked — Drive has photos only for these standards).
- Two maps are CC BY-SA (US.45, US.49, US.56 Wikimedia option) — prefer the PD substitute or build fresh to keep everything PD.
- These visuals go into the **decks (especially the student deck)**, not the workbook — per the lean-consumable decision.
