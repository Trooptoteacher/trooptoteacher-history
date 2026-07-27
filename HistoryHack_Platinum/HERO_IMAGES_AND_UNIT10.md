# Unit 10 build + cover/workbook hero images

## Unit 10 — "Modern America, 1965–2016" (US.83–US.95, 13 standards)

Full Course Standard (Platinum) print set, built from the app's canonical data
(`ican`, `vocabulary`, `primary-sources`, `questions`) exactly like Units 1–9:

- **Student Workbook** — 133 pp. Hero cover (Reagan at the Brandenburg Gate,
  1987), Geographer's Lens for US.90 (end of Cold War / Gulf War) and US.92
  (9/11 sites), grounded synthesis "The Making of Modern America — Four Threads,"
  and a Baker/Gore/Gig-City Tennessee Connection. Zero pages over the 85%
  whitespace/bleed threshold.
- **Teacher How-to-Use & MTSS Guide** — 16 pp.
- **Assessment Book (Teacher)** — 27 pp (26 formative, Form A/B of 39 each,
  de-biased, keyed).
- **Graphic Organizer Toolkit** — 47 pp.
- **4 Cover wraps** (Student / Teacher / Assessment / Toolkit).

Source in `build_unit10/`. Standard order is numerically sorted so US.84
(last in the ican file) sits between US.83 and US.85.

## Hero images on every cover and workbook cover page

Each unit now carries its curated, **public-domain** hero photograph on the
cover wrap (front panel, gold-ruled, credited) and on the workbook's own cover
page (captioned + credited). Art comes from the app's own unit hero set
(`public/images/units/unit-N.jpg`) — verified by eye, not by the textbook
image bank (whose filenames/titles are unreliable).

`build/patch_heroes.py` applies this uniformly to the cloned `_uN` scripts
(cover: swaps the `HERO=''` stub + aspect-fit `heroImg`; workbook: injects a
`coverHero()` helper and inserts it on the cover page, trimming spacing so the
page never overflows).

| Unit | Hero | Rights |
|------|------|--------|
| 1 | Golden Spike, Promontory Summit 1869 (Russell) | Public domain |
| 2 | Pennsylvania Ave. crowd, DC, early 1900s | Public domain (LoC) |
| 3 | Roosevelt & Rough Riders, San Juan Heights 1898 (Dinwiddie) | Public domain (LoC) |
| 4 | Ford assembly line, early 1900s | Public domain |
| 5 | *(source template — no build scripts in this system)* | — |
| 6 | **SKIPPED** — app hero is Rosenthal's Iwo Jima flag-raising | **© Associated Press — NOT public domain** |
| 7 | Berlin Wall construction 1961 | Public domain (NARA) |
| 8 | Buzz Aldrin on the Moon, Apollo 11 1969 (Armstrong/NASA) | Public domain (NASA) |
| 9 | March on Washington 1963 | Public domain (NARA) |
| 10 | Reagan at the Brandenburg Gate 1987 | Public domain (Reagan Library/NARA) |

### Two follow-ups
- **Unit 6** — the app's Unit 6 hero is Joe Rosenthal's Iwo Jima flag-raising,
  which the Associated Press holds in copyright. It was **not** embedded on the
  commercial cover. Recommended public-domain WWII substitute: "Into the Jaws
  of Death" (D-Day, Robert F. Sargent, U.S. Coast Guard, public domain), or
  another NARA WWII photo — to be sourced and dropped into
  `Unit6_Claude_Core/analysis/assets/hero.jpg`, then rebuild.
- **Unit 5** — the canonical template; it has no build scripts in this system,
  so its cover/workbook were not regenerated. Migrant Mother (Lange, FSA 1936,
  public domain) is the natural hero if/when Unit 5 is rebuilt on this pipeline.
