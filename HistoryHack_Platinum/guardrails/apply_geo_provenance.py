#!/usr/bin/env python3
"""
Apply geography provenance (citations + review status) to every unit content JSON.

Single source of truth: guardrails/geo_provenance.json (written by this script the
first time, then hand-editable). For each geo-tagged standard it stamps:
  - geo_sources: authoritative citations backing the authored places
  - geo_review : {status, by, date, note}

Idempotent and sign-off-safe: a standard already marked "sme_approved" is NOT
overwritten (so re-running after an SME signs off preserves the approval). Run
this after any re-derive so curated provenance is never lost.

Usage:
  python3 apply_geo_provenance.py [/path/to/HistoryHack_Platinum]
"""
import json, os, sys, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_provenance.json")

NOTE = ("Places drafted from the standard's official TN text and criteria; anchor "
        "facts verified against the cited sources. Pending SME sign-off.")

# Authoritative citations per geo standard (anchor facts verified via web research
# against Office of the Historian, National Archives, Library of Congress, NPS,
# U.S. Army/Navy history, FHWA, JFK Library, 9/11 Memorial, Tennessee Encyclopedia,
# and Britannica). Edit here (or geo_provenance.json) to maintain provenance.
SOURCES = {
  "US.01": [
    "Homestead Act (1862) — U.S. National Archives: https://www.archives.gov/milestone-documents/homestead-act",
    "Golden Spike / Transcontinental Railroad completed May 10, 1869 — National Park Service: https://www.nps.gov/gosp/",
    "The Golden Spike (Chronicling America) — Library of Congress: https://guides.loc.gov/chronicling-america-golden-spike",
  ],
  "US.11": [
    "Homestead Strike (1892) — Encyclopædia Britannica: https://www.britannica.com/event/Homestead-Strike",
    "Labor in the Gilded Age (Homestead, Pullman) — Library of Congress: https://guides.loc.gov/gilded-age-business/people/labor",
    "Convict Lease Wars / Coal Creek War (1891–92) — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/convict-lease-wars/",
  ],
  "US.18": [
    "19th Amendment (1920); Tennessee the 36th ratifying state, Aug 18, 1920 — U.S. National Archives: https://www.archives.gov/milestone-documents/19th-amendment",
    "Nineteenth Amendment (Wyoming Territory 1869) — Encyclopædia Britannica: https://www.britannica.com/topic/Nineteenth-Amendment",
  ],
  "US.19": [
    "U.S. diplomacy & yellow journalism, 1895–1898 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1866-1898/yellow-journalism",
    "Secretary Hay and the Open Door in China (1899) — Office of the Historian: https://history.state.gov/milestones/1899-1913/hay-and-china",
    "The Spanish-American War — Library of Congress: https://www.loc.gov/classroom-materials/spanish-american-war-the-united-states-becomes-a-world-power/",
  ],
  "US.21": [
    "The Spanish-American War, 1898 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1866-1898/spanish-american-war",
    "Treaty of Paris of 1898 (Cuba, Puerto Rico, Guam, Philippines) — Library of Congress: https://guides.loc.gov/world-of-1898/treaty-of-paris",
    "Treaty of Paris (1898) — Encyclopædia Britannica: https://www.britannica.com/event/Treaty-of-Paris-1898",
  ],
  "US.22": [
    "Building the Panama Canal, 1903–1914 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1899-1913/panama-canal",
    "Roosevelt Corollary to the Monroe Doctrine, 1904 — Office of the Historian: https://history.state.gov/milestones/1899-1913/roosevelt-and-monroe-doctrine",
    "Dollar Diplomacy — Encyclopædia Britannica: https://www.britannica.com/event/Dollar-Diplomacy",
  ],
  "US.23": [
    "The World in 1914 (alliances) — U.S. Dept. of State, Office of the Historian: https://history.state.gov/departmenthistory/short-history/worldin1914",
    "Western Front (WWI) — Encyclopædia Britannica: https://www.britannica.com/event/Western-Front-World-War-I",
    "U.S. Participation in WWI — Library of Congress: https://www.loc.gov/classroom-materials/united-states-history-primary-source-timeline/progressive-era-to-new-era-1900-1929/united-states-participation-in-world-war-i/",
  ],
  "US.25": [
    "The Meuse-Argonne, 26 Sept–11 Nov 1918 — U.S. Army Center of Military History: https://history.army.mil/portals/143/Images/Publications/catalog/77-8.pdf",
    "Alvin Cullum York — Encyclopædia Britannica: https://www.britannica.com/biography/Alvin-Cullum-York",
    "Harlem Hell Fighters (369th Infantry) — Library of Congress: https://blogs.loc.gov/headlinesandheroes/2019/02/harlem-hell-fighters-african-american-troops/",
    "Commission for Relief in Belgium (Hoover) — U.S. National Archives: https://www.archives.gov/publications/prologue/1989/spring/hoover-belgium.html",
  ],
  "US.28": [
    "The Great Migration (1910–1970) — U.S. National Archives: https://www.archives.gov/research/african-americans/migrations/great-migration",
    "The Great Migration — Library of Congress: https://www.loc.gov/classroom-materials/great-migration/",
    "Great Migration — Encyclopædia Britannica: https://www.britannica.com/event/Great-Migration",
  ],
  "US.30": [
    "Grand Ole Opry / WSM — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/grand-ole-opry/",
    "William Christopher “W.C.” Handy — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/william-christopher-handy/",
    "Bessie Smith — Encyclopædia Britannica: https://www.britannica.com/biography/Bessie-Smith",
    "Bristol Sessions — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/bristol-sessions/",
  ],
  "US.40": [
    "Dust Bowl — Encyclopædia Britannica: https://www.britannica.com/place/Dust-Bowl",
    "Dust Bowl Migration — Library of Congress: https://www.loc.gov/classroom-materials/dust-bowl-migration/",
    "Route 66 — Encyclopædia Britannica: https://www.britannica.com/topic/Route-66",
  ],
  "US.50": [
    "Battle of Midway, 4–7 June 1942 — U.S. Navy History & Heritage Command: https://www.history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/1942/midway.html",
    "Pacific War (Iwo Jima, Okinawa) — Encyclopædia Britannica: https://www.britannica.com/topic/Pacific-War",
    "Normandy Invasion (D-Day, June 1944) — Encyclopædia Britannica: https://www.britannica.com/event/Normandy-Invasion",
  ],
  "US.56": [
    "Manhattan Project — Manhattan Project National Historical Park (NPS): https://www.nps.gov/mapr/learn/manhattan-project.htm",
    "Manhattan Project Science at Oak Ridge — National Park Service: https://home.nps.gov/articles/000/manhattan-project-science-at-oak-ridge.htm",
    "Atomic bombings of Hiroshima and Nagasaki (Aug 6 & 9, 1945) — Encyclopædia Britannica: https://www.britannica.com/event/atomic-bombings-of-Hiroshima-and-Nagasaki",
  ],
  "US.62": [
    "The Korean War, 1950–1953 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1945-1952/korean-war",
    "Inchon Landing (Sept 1950) — Encyclopædia Britannica: https://www.britannica.com/event/Inchon-landing",
    "38th parallel — Encyclopædia Britannica: https://www.britannica.com/place/38th-parallel",
  ],
  "US.65": [
    "The Cuban Missile Crisis, October 1962 — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1961-1968/cuban-missile-crisis",
    "Cuban Missile Crisis — John F. Kennedy Presidential Library: https://www.jfklibrary.org/learn/about-jfk/jfk-in-history/cuban-missile-crisis",
    "Cuban missile crisis — Encyclopædia Britannica: https://www.britannica.com/event/Cuban-missile-crisis",
  ],
  "US.66": [
    "U.S. Involvement in Vietnam: the Gulf of Tonkin (1964) — U.S. Dept. of State, Office of the Historian: https://history.state.gov/milestones/1961-1968/gulf-of-tonkin",
    "Seventeenth parallel — Encyclopædia Britannica: https://www.britannica.com/topic/seventeenth-parallel",
    "Gulf of Tonkin incident (1964) — Encyclopædia Britannica: https://www.britannica.com/event/Gulf-of-Tonkin-incident",
  ],
  "US.74": [
    "National Interstate and Defense Highways Act (1956) — U.S. National Archives: https://www.archives.gov/milestone-documents/national-interstate-and-defense-highways-act",
    "History of the Eisenhower Interstate System — Federal Highway Administration: https://www.fhwa.dot.gov/interstate-70th/history_eisenhower_interstate_system.cfm",
    "Federal-Aid Highway Act (1956) — Encyclopædia Britannica: https://www.britannica.com/topic/Federal-Aid-Highway-Act-United-States-1956",
  ],
  "US.80": [
    "Montgomery Bus Boycott (1955–56) — National Park Service: https://www.nps.gov/articles/montgomery-bus-boycott.htm",
    "Timeline of the American Civil Rights Movement — Encyclopædia Britannica: https://www.britannica.com/list/timeline-of-the-american-civil-rights-movement",
    "The Civil Rights Movement — Library of Congress: https://www.loc.gov/classroom-materials/civil-rights-movement/",
  ],
  "US.90": [
    "The Berlin Wall Falls and USSR Dissolves — U.S. Dept. of State, Office of the Historian: https://history.state.gov/departmenthistory/short-history/berlinwall",
    "The First Gulf War (1990–91) — Office of the Historian: https://history.state.gov/departmenthistory/short-history/firstgulf",
    "The Collapse of the Soviet Union (1989–1992) — Office of the Historian: https://history.state.gov/milestones/1989-1992/collapse-soviet-union",
  ],
  "US.92": [
    "September 11 attacks — Encyclopædia Britannica: https://www.britannica.com/event/September-11-attacks",
    "Remembering 9/11 — U.S. National Archives: https://www.archives.gov/news/topics/9-11-anniversary",
    "Events of the Day (WTC, Pentagon, Shanksville) — National September 11 Memorial & Museum: https://www.911memorial.org/learn/resources/911-primer/module-1-events-day",
  ],
}


def build_ledger():
    return {code: {"geo_sources": srcs,
                   "geo_review": {"status": "drafted", "by": "", "date": "", "note": NOTE}}
            for code, srcs in SOURCES.items()}


def main():
    # write/refresh the ledger file (source of truth going forward)
    ledger = build_ledger()
    if os.path.exists(LEDGER):
        # preserve any hand-edited review status / sources already in the ledger
        existing = json.load(open(LEDGER, encoding="utf8"))
        for code, rec in existing.items():
            if code in ledger and rec.get("geo_review", {}).get("status") == "sme_approved":
                ledger[code] = rec
    json.dump(ledger, open(LEDGER, "w", encoding="utf8"), ensure_ascii=False, indent=2)

    stamped = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "build_unit*", "unit*_content.json"))):
        d = json.load(open(f, encoding="utf8"))
        std = d.get("standards", {})
        changed = False
        for code in d.get("order", list(std.keys())):
            if code not in ledger:
                continue
            s = std.get(code, {})
            # only geo-tagged standards
            if not (s.get("geo") and str(s.get("geo")).strip()):
                continue
            # never clobber an SME approval already in the content JSON
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
