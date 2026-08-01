#!/usr/bin/env python3
"""Generates ASSET_INDEX.csv for the UNIT6_VISUAL_ASSETS package."""
import csv
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

rows = [
    # standard, asset_type, filename, status, license, source_institution, source_page, attribution, caveat
    ("US.45", "map", "HOLD_LICENSE_OR_BUILD_FRESH.md", "HOLD", "CC BY-SA 3.0 (rejected)", "Wikimedia Commons / USMA West Point",
     "https://commons.wikimedia.org/wiki/File:EUROPE_1929-1938_POLITICAL_MAP.svg",
     "n/a - not used", "Share-alike license blocks commercial use; West Point alternative requires reprint permission"),
    ("US.45", "data_graphic", "US.45_us_unemployment_great_depression.png", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "U.S. Bureau of the Census", "https://www2.census.gov/library/publications/1949/compendia/hist_stats_1789-1945/hist_stats_1789-1945.pdf",
     "U.S. Bureau of the Census, Historical Statistics of the United States, 1789-1945 (1949), Series D62-76 (NICB), col. D65",
     "NICB series, not modern BLS estimates; 1940 not comparable to 1929-39; midyear from 1930 on"),

    ("US.46", "map", "HOLD_LICENSE_OR_BUILD_FRESH.md", "HOLD", "Rights unclear / reprint permission required", "USMA West Point Digital History Center",
     "https://dhc.westpoint.edu/atlases/", "n/a - not used", "Explicit reprint-permission requirement from West Point (Jeff Goldberg); written permission required"),
    ("US.46", "data_graphic", "US.46_lend_lease_by_country.png", "READY", "No Copyright - United States (NoC-US)",
     "Office for Emergency Management / FEA / Dept. of State (Twenty-First Report to Congress)",
     "https://fraser.stlouisfed.org/files/docs/publications/llo/llo_report_19460131.pdf",
     "Twenty-First Report to Congress on Lend-Lease Operations, Table 2 (31 Jan 1946)",
     "Do not mix with unverified later cumulative totals ($31.4B/$11.3B/etc.)"),

    ("US.47", "map", "US.47_holocaust_camps_europe_map.png", "READY", "CC BY 3.0", "Dennis Nilsson (Wikimedia Commons)",
     "https://commons.wikimedia.org/wiki/File:WW2-Holocaust-Europe.png",
     "Dennis Nilsson, CC BY 3.0, via Wikimedia Commons", "Content sourced from USHMM & Wikipedia, not a primary cartographic source; low native resolution"),
    ("US.47", "data_graphic", "US.47_holocaust_deaths_by_country.png", "READY WITH CAVEAT", "Public domain factual data (chart built fresh)",
     "United States Holocaust Memorial Museum", "https://encyclopedia.ushmm.org/content/en/article/jewish-losses-during-the-holocaust-by-country",
     "United States Holocaust Memorial Museum, Jewish Losses during the Holocaust: By Country (2018)",
     "All figures are estimates subject to change; sub-entries excluded to avoid double-counting"),

    ("US.48", "map", "US.48_pearl_harbor_attack_map.png", "READY WITH CAVEAT", "Public domain (PD-USGov-Military-Navy)",
     "U.S. Navy / Naval History and Heritage Command", "https://commons.wikimedia.org/wiki/File:Map_showing_ships_present_at_Pearl_Harbor_on_7_December_1941.png",
     "U.S. Navy photo NH 83109, Naval History and Heritage Command (public domain)",
     "Documented compass error (~45 deg) and mis-ordered ship nests per Commons description"),
    ("US.48", "data_graphic", "US.48_pearl_harbor_losses.png", "READY", "Public domain (U.S. Government)",
     "Naval History and Heritage Command", "https://www.history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/1941/pearl-harbor.html",
     "Naval History and Heritage Command, Pearl Harbor Attack",
     "Totals are sums of NHHC service-level figures, not separately published totals"),

    ("US.49", "map", "HOLD_LICENSE_OR_BUILD_FRESH.md", "HOLD", "CC BY-SA 4.0 (rejected)", "Wikimedia Commons (Svenskbygderna)",
     "https://commons.wikimedia.org/wiki/File:Map_of_participants_in_World_War_II.svg",
     "n/a - not used", "Share-alike license blocks commercial use; no PD substitute found"),

    ("US.50", "map", "US.50_dday_normandy_map.jpg", "READY", "Free to use/reuse (LOC, no rights advisory)",
     "U.S. Army Center of Military History / Library of Congress", "https://www.loc.gov/item/94681943/",
     "Center of Military History, D-Day the 6th of June: Normandy 1944. Library of Congress, Geography and Map Division",
     "Full sheet includes verso text/local maps; converted from IIIF at 50% scale"),
    ("US.50", "map", "US.50_pacific_island_hopping_map.jpg", "READY WITH CAVEAT", "Public domain (PD-USGov-Military-Army)",
     "U.S. Army Center of Military History", "https://commons.wikimedia.org/wiki/File:Pacific_Theater_Areas;map1.JPG",
     "U.S. Army Center of Military History (public domain)", "Native resolution marginal for large print (1199x873)"),
    ("US.50", "data_graphic", "US.50_wwii_battle_casualties.png", "READY WITH CAVEAT", "Public domain (U.S. Government, multiple)",
     "NHHC / govinfo / NPS / U.S. Army CMH", "https://www.history.navy.mil ; https://www.nps.gov ; https://history.army.mil",
     "See per-bar sources in citation sidecar", "Figures use different official definitions; not directly comparable across battles"),

    ("US.52", "data_graphic", "US.52_women_workforce_1940_45.png", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "U.S. Bureau of the Census", "https://www2.census.gov/library/publications/1949/compendia/hist_stats_1789-1945/hist_stats_1789-1945.pdf",
     "U.S. Bureau of the Census, Historical Statistics of the United States, 1789-1945 (1949), Series D11-31",
     "Distinguishes labor force from employed; ~25%->35% share, not the popular unverified 28%->36%"),

    ("US.53", "map", "US.53_great_migration_map.jpg", "READY WITH CAVEAT", "Public domain data + open basemap (PublicaMundi)",
     "National Archives and Records Administration", "https://www.archives.gov/research/african-americans/migrations/great-migration",
     "National Archives, The Great Migration (1910-1970)",
     "Explicitly schematic, not person-by-person routes; original Census visualization returns 404, built fresh"),
    ("US.53", "data_graphic", "US.53_black_migration_employment.png", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "Committee on Fair Employment Practice / National Archives", "https://www.govinfo.gov/content/pkg/GOVPUB-PR32_400-7f2cb8a4569c8faad7121fff6a1a6109/pdf/GOVPUB-PR32_400-7f2cb8a4569c8faad7121fff6a1a6109.pdf",
     "Committee on Fair Employment Practice, First Report (1 May 1945)",
     "Early 1942 shown as open marker (<3%, not exact); NARA migration figure is separate, not an annual series"),

    ("US.54", "map", "US.54_wra_camps_map.jpg", "READY WITH CAVEAT", "Public domain data + open basemap (PublicaMundi)",
     "U.S. Department of the Interior, War Relocation Authority", "https://fraser.stlouisfed.org/files/docs/publications/wra/1946_wra_evacuatedpeople.pdf",
     "U.S. Dept. of the Interior, War Relocation Authority, The Evacuated People (1946), Table 5",
     "Markers approximate post-office/county locations, not camp boundaries; official NPS map unavailable, built fresh"),
    ("US.54", "data_graphic", "US.54_incarceration_by_camp.png", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "U.S. Department of the Interior, War Relocation Authority", "https://fraser.stlouisfed.org/files/docs/publications/wra/1946_wra_evacuatedpeople.pdf",
     "U.S. Dept. of the Interior, War Relocation Authority, The Evacuated People (1946), Table 5",
     "120,313 cumulative custody total explicitly not the sum of the 10 peak-population bars (which sum to 112,581)"),

    ("US.55", "data_graphic", "US.55_us_war_production_1941_1945.png", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "War Production Board / Office of Technology Assessment", "https://www.princeton.edu/~ota/disk3/1979/7917/791711.PDF",
     "War Production Board, Program and Statistics Bureau, Table B-6, reprinted in OTA Appendix B",
     "1940/1945 bars are partial periods (flagged with dotted overlay); excludes GDP%, tank counts, unverified Table 74"),

    ("US.56", "map", "US.56_manhattan_project_sites_map.png", "READY WITH CAVEAT", "Public domain data + open basemap (PublicaMundi)",
     "National Park Service", "https://www.nps.gov/mapr/learn/manhattan-project.htm",
     "National Park Service, Manhattan Project National Historical Park",
     "Only 3 NPS-confirmed sites shown (Oak Ridge, Los Alamos, Hanford); other wartime facilities intentionally excluded"),
    ("US.56", "data_graphic", "US.56_hiroshima_nagasaki_casualties.png", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "Manhattan Engineer District, United States Army", "https://www.gutenberg.org/ebooks/685",
     "The Atomic Bombings of Hiroshima and Nagasaki, Manhattan Engineer District (29 Jun 1946), Table A",
     "1946 MED estimates, not exact counts; later estimates diverge widely and are not shown"),

    ("US.57", "map", "US.57_germany_occupation_zones_map.jpg", "READY WITH CAVEAT", "Public domain (U.S. Army)",
     "U.S. Army / Earl F. Ziemke, Library of Congress catalog", "https://commons.wikimedia.org/wiki/File:Germany_occupation_zones_with_border.jpg",
     "U.S. Army; from Earl F. Ziemke, The U.S. Army in the Occupation of Germany (1975); modified version via Wikimedia Commons",
     "MODIFIED version of the original 1975 map; anachronistic pre-Nazi provincial boundaries; British withdrawal line not drawn"),

    ("US.58", "map", "US.58_un_51_member_states_map.jpg", "READY WITH CAVEAT", "Public domain (U.S. Government)",
     "United States Army Information Branch / UNT Digital Library", "https://digital.library.unt.edu/ark:/67531/metadc834/",
     "Newsmap for the Armed Forces: UNO, 51 Nations Unite For Peace, v.4 no.40 (21 Jan 1946), U.S. Army Information Branch",
     "Sheet's own photo caption records opening session date as 1945; actual opening was 10 Jan 1946 - documented error risk"),
    ("US.58", "data_graphic", "US.58_un_founding_members_timeline.png", "READY", "Factual data, chart built fresh",
     "United Nations", "https://www.un.org/en/about-us/history-of-the-un/san-francisco-conference",
     "United Nations, The San Francisco Conference",
     "Uses 'delegates of fifty nations' phrasing, not an unverified exact '50 signatories'"),
]

path = os.path.join(ROOT, "ASSET_INDEX.csv")
with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["standard", "asset_type", "filename", "status", "license", "source_institution", "source_page", "attribution", "caveat"])
    for r in rows:
        w.writerow(r)

print(f"Wrote {path} with {len(rows)} rows")
