#!/usr/bin/env python3
"""
Apply geography provenance (citations + review status) to every unit content JSON.

Single source of truth: guardrails/geo_provenance.json (written by this script the
first time, then hand-editable). For each geo-tagged standard it stamps:
  - geo_sources: authoritative citations backing the authored places
  - geo_review : {status, by, date, note}

Sourcing policy (aligned to TDOE High School Social Studies rubric, C5 Historical
Accuracy & Currency): citations are authoritative government / archival / scholarly
references — Office of the Historian, National Archives, Library of Congress, NPS,
U.S. Army/Navy history, DOE, FHWA, JFK Library, 9/11 Memorial, Tennessee
Encyclopedia. Tertiary general encyclopedias (Britannica, Wikipedia) are used only
as fact-check aids, never as cited sources.

Idempotent and sign-off-safe: a standard already marked "sme_approved" is NOT
overwritten. Run this after any re-derive so curated provenance is never lost.

Usage:
  python3 apply_geo_provenance.py [/path/to/HistoryHack_Platinum]
"""
import json, os, sys, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_provenance.json")

NOTE = ("Places drafted from the standard's official TN text and criteria; anchor "
        "facts verified against the cited authoritative sources. Pending SME sign-off.")

# Authoritative citations per geo standard. Anchor facts verified via web research;
# sources are government / archival / scholarly references only (no tertiary
# encyclopedias). Edit here (or geo_provenance.json) to maintain provenance.
SOURCES = {
  "US.01": [
    "Homestead Act (1862) — U.S. National Archives: https://www.archives.gov/milestone-documents/homestead-act",
    "Golden Spike / Transcontinental Railroad completed May 10, 1869 — National Park Service: https://www.nps.gov/gosp/",
    "The Golden Spike (Chronicling America) — Library of Congress: https://guides.loc.gov/chronicling-america-golden-spike",
  ],
  "US.11": [
    "Labor in the Gilded Age (Homestead 1892, Pullman 1894) — Library of Congress: https://guides.loc.gov/gilded-age-business/people/labor",
    "Homestead Strike (Chronicling America) — Library of Congress: https://guides.loc.gov/chronicling-america-homestead-strike",
    "Convict Lease Wars / Coal Creek War (1891–92) — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/convict-lease-wars/",
  ],
  "US.18": [
    "19th Amendment (1920); Tennessee the 36th ratifying state, Aug 18, 1920 — U.S. National Archives: https://www.archives.gov/milestone-documents/19th-amendment",
    "Woman Suffrage and the 19th Amendment — U.S. National Archives (education): https://www.archives.gov/education/lessons/woman-suffrage",
  ],
  "US.19": [
    "U.S. diplomacy & yellow journalism, 1895–1898 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1866-1898/yellow-journalism",
    "Secretary Hay and the Open Door in China (1899) — Office of the Historian: https://history.state.gov/milestones/1899-1913/hay-and-china",
    "The Spanish-American War — Library of Congress: https://www.loc.gov/classroom-materials/spanish-american-war-the-united-states-becomes-a-world-power/",
  ],
  "US.21": [
    "The Spanish-American War, 1898 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1866-1898/spanish-american-war",
    "Treaty of Paris of 1898 (Cuba, Puerto Rico, Guam, Philippines) — Library of Congress: https://guides.loc.gov/world-of-1898/treaty-of-paris",
  ],
  "US.22": [
    "Building the Panama Canal, 1903–1914 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1899-1913/panama-canal",
    "Roosevelt Corollary to the Monroe Doctrine, 1904 (Dominican customs; lineage of Dollar Diplomacy) — Office of the Historian: https://history.state.gov/milestones/1899-1913/roosevelt-and-monroe-doctrine",
  ],
  "US.23": [
    "The World in 1914 (alliances) — U.S. Dept. of State, Office of the Historian: https://history.state.gov/departmenthistory/short-history/worldin1914",
    "U.S. Participation in WWI (Western Front, neutrality) — Library of Congress: https://www.loc.gov/classroom-materials/united-states-history-primary-source-timeline/progressive-era-to-new-era-1900-1929/united-states-participation-in-world-war-i/",
  ],
  "US.25": [
    "The Meuse-Argonne, 26 Sept–11 Nov 1918 (York, Pershing) — U.S. Army Center of Military History: https://history.army.mil/portals/143/Images/Publications/catalog/77-8.pdf",
    "Harlem Hell Fighters (369th Infantry) — Library of Congress: https://blogs.loc.gov/headlinesandheroes/2019/02/harlem-hell-fighters-african-american-troops/",
    "Commission for Relief in Belgium (Hoover) — U.S. National Archives: https://www.archives.gov/publications/prologue/1989/spring/hoover-belgium.html",
  ],
  "US.28": [
    "The Great Migration (1910–1970) — U.S. National Archives: https://www.archives.gov/research/african-americans/migrations/great-migration",
    "The Great Migration — Library of Congress: https://www.loc.gov/classroom-materials/great-migration/",
  ],
  "US.30": [
    "Grand Ole Opry / WSM (radio, 1925; named 1927) — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/grand-ole-opry/",
    "William Christopher “W.C.” Handy (Memphis, Beale Street) — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/william-christopher-handy/",
    "Bristol Sessions (1927) — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/bristol-sessions/",
  ],
  "US.40": [
    "Dust Bowl Migration — Library of Congress: https://www.loc.gov/classroom-materials/dust-bowl-migration/",
    "Voices from the Dust Bowl / the migrant experience (Route 66, California) — Library of Congress: https://www.loc.gov/collections/todd-and-sonkin-migrant-workers-from-1940-to-1941/articles-and-essays/the-migrant-experience/",
    "Weedpatch Camp (Dust Bowl migrants in California) — National Park Service: https://www.nps.gov/places/weedpatch-camp.htm",
  ],
  "US.50": [
    "Battle of Midway, 4–7 June 1942 — U.S. Navy History & Heritage Command: https://www.history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/1942/midway.html",
    "Operation Overlord / D-Day, June 1944 — U.S. Navy History & Heritage Command: https://www.history.navy.mil/content/history/museums/nmusn/explore/photography/wwii/wwii-europe/operation-overlord.html",
    "Records Relating to D-Day / Normandy — U.S. National Archives: https://www.archives.gov/research/military/ww2/d-day",
  ],
  "US.56": [
    "Manhattan Project — Manhattan Project National Historical Park (NPS): https://www.nps.gov/mapr/learn/manhattan-project.htm",
    "Manhattan Project Science at Oak Ridge — National Park Service: https://home.nps.gov/articles/000/manhattan-project-science-at-oak-ridge.htm",
    "Manhattan Project background (Oak Ridge, Hanford, Los Alamos; 1945 bombings) — U.S. Department of Energy: https://www.energy.gov/lm/manhattan-project-background-information-and-preservation-work",
  ],
  "US.62": [
    "The Korean War, 1950–1953 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1945-1952/korean-war",
    "The Landing at Inch'on (Sept 1950) — U.S. Army Center of Military History: https://www.history.army.mil/books/korea/20-2-1/sn25.htm",
    "Crossing the 38th Parallel — U.S. Army Center of Military History: https://history.army.mil/books/PD-C-10.HTM",
  ],
  "US.65": [
    "The Cuban Missile Crisis, October 1962 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1961-1968/cuban-missile-crisis",
    "Cuban Missile Crisis (Bay of Pigs, Jupiter missiles in Turkey) — John F. Kennedy Presidential Library: https://www.jfklibrary.org/learn/about-jfk/jfk-in-history/cuban-missile-crisis",
  ],
  "US.66": [
    "U.S. Involvement in Vietnam: the Gulf of Tonkin (1964) — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1961-1968/gulf-of-tonkin",
    "Dien Bien Phu & the Fall of French Indochina, 1954 (Geneva Accords; 17th parallel) — Office of the Historian: https://history.state.gov/milestones/1953-1960/dien-bien-phu",
    "Remembering Vietnam (North/South division, the war) — U.S. National Archives: https://www.archives.gov/exhibits/remembering-vietnam-online-exhibit-episodes-1-4",
  ],
  "US.74": [
    "National Interstate and Defense Highways Act (1956) — U.S. National Archives: https://www.archives.gov/milestone-documents/national-interstate-and-defense-highways-act",
    "History of the Eisenhower Interstate System — Federal Highway Administration: https://www.fhwa.dot.gov/interstate-70th/history_eisenhower_interstate_system.cfm",
  ],
  "US.80": [
    "Montgomery Bus Boycott (1955–56) — National Park Service: https://www.nps.gov/articles/montgomery-bus-boycott.htm",
    "The Civil Rights Movement (Little Rock, Nashville, Birmingham, Selma, Memphis) — Library of Congress: https://www.loc.gov/classroom-materials/civil-rights-movement/",
  ],
  "US.90": [
    "The Berlin Wall Falls and USSR Dissolves — U.S. Dept. of State, Office of the Historian: https://history.state.gov/departmenthistory/short-history/berlinwall",
    "The First Gulf War (1990–91) — Office of the Historian: https://history.state.gov/departmenthistory/short-history/firstgulf",
    "The Collapse of the Soviet Union (1989–1992) — Office of the Historian: https://history.state.gov/milestones/1989-1992/collapse-soviet-union",
  ],
  "US.92": [
    "Remembering 9/11 — U.S. National Archives: https://www.archives.gov/news/topics/9-11-anniversary",
    "Events of the Day (WTC, Pentagon, Shanksville) — National September 11 Memorial & Museum: https://www.911memorial.org/learn/resources/911-primer/module-1-events-day",
  ],
}


def build_ledger():
    return {code: {"geo_sources": srcs,
                   "geo_review": {"status": "drafted", "by": "", "date": "", "note": NOTE}}
            for code, srcs in SOURCES.items()}


def main():
    ledger = build_ledger()
    if os.path.exists(LEDGER):
        # preserve any hand-edited SME approvals already recorded in the ledger
        existing = json.load(open(LEDGER, encoding="utf8"))
        for code, rec in existing.items():
            if code in ledger and rec.get("geo_review", {}).get("status") == "sme_approved":
                ledger[code] = rec
    json.dump(ledger, open(LEDGER, "w", encoding="utf8"), ensure_ascii=False, indent=2)

    stamped = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "build_*", "*_content.json"))):
        d = json.load(open(f, encoding="utf8"))
        std = d.get("standards", {})
        changed = False
        for code in d.get("order", list(std.keys())):
            if code not in ledger:
                continue
            s = std.get(code, {})
            if not (s.get("geo") and str(s.get("geo")).strip()):
                continue
            if (s.get("geo_review") or {}).get("status") == "sme_approved":
                continue
            s["geo_sources"] = ledger[code]["geo_sources"]
            s["geo_review"] = dict(ledger[code]["geo_review"])
            changed = True
            stamped += 1
        if changed:
            json.dump(d, open(f, "w", encoding="utf8"), ensure_ascii=False, indent=2)
            print(f"stamped {os.path.basename(os.path.dirname(f))}")
    print(f"DONE: {stamped} geo standards stamped; ledger at {LEDGER}")


if __name__ == "__main__":
    main()
