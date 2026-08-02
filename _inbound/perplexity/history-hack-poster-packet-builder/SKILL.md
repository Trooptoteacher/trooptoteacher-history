---
name: history-hack-poster-packet-builder
description: "Platinum-standard builder and reusable template for U.S. History Hack Unit Poster and Activity Packets (TroopToTeacher Technologies LLC). Produces a unit wall set: 13 large-format 24x36 vector wall posters (Track A), Letter station activities (Track B), three teacher guides (Standards Alignment Map, Print Guide, Facilitation Guide), and two assembled bundle PDFs (Wall Set and Complete Bundle with branded cover and dividers). Enforces the locked brand kit (navy/red/gold palette, DM Sans/Inter, sketch-note fonts for flagship anchor charts), copyright footer on every page, WCAG 2.2 AA, historian-verified citations, bilingual EN/ES plus 5-band differentiation, and no AI imagery. Use when the user says: build the Unit N poster packet, build the wall set, mirror the Unit 1 Platinum pattern, build the anchor chart, word wall, timeline, or station, assemble the bundle, add Platinum Plus guides, or save the poster packet to Google Drive."
license: "Proprietary — TroopToTeacher Technologies LLC. Internal use."
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.0'
---

# U.S. History Hack — Poster & Activity Packet Builder (Platinum Standard)

This skill captures the gold-standard workflow used to build the **Unit 1 Platinum bundle**
(April–June 2026) and turns it into a reusable template for every subsequent unit. It is the
production discipline for the product brand **"U.S. History Hack — Unit [N] Poster & Activity
Packet"** · tagline **"Walls that teach. Stations that stick."**

## When to Use This Skill

Load this skill when the user asks to:

- Build a Unit N poster packet / wall set / station pack to Platinum standard.
- Mirror the Unit 1 Platinum pattern for a new unit.
- Build or revise a specific piece: anchor chart (flagship), word wall, timeline, key people,
  key events, primary source, maps, data/economics, debate wall, Tennessee connection,
  "Whose Story?" perspectives, HIPP station, or a student note sheet.
- Add the Platinum Plus teacher guides (Standards Alignment Map, Print & Display Guide,
  Facilitation Guide).
- Assemble the combined Wall Set + Complete Bundle PDFs.
- Save the finished packet to Google Drive in an organized folder.

## Non-Negotiable Standing Constraints

These are LOCKED. Never violate them in any artifact:

1. **Copyright on EVERY page.** Every generated page (poster, station, guide, cover, divider)
   must show the copyright line. Source of truth is `brand.py`:
   `© 2026 TroopToTeacher Technologies LLC. All rights reserved.` (and `COPYRIGHT_SHORT`).
2. **NO AI-generated imagery.** All visuals are hand-built ReportLab vector or pre-cleared
   photos in `poster_assets/img/`. Never generate or insert AI images into these documents.
3. **Brand palette (America-250 / Air Force One livery):** NAVY `#0A1F3C`, NAVY2 `#14315A`,
   RED `#B22234`, RED_D `#8E1B29`, GOLD `#C8A04B`, GOLD_L `#E8C97A`, INK `#1C1C1C`,
   SLATE `#4A5568`, PAPER `#F7F5EF`, LINE `#D8D2C4`.
4. **Typography:** Display = DM Sans Bold; body = Inter. Flagship sketch-note anchor charts add
   the handwriting family: Bangers (Marker), Kalam-Bold (HandBold), Kalam (Hand),
   Patrick Hand (HandPrint), Caveat (HandScript). The handwriting fonts are intentional for the
   flagship look — keep them even though generic design guidance discourages them.
5. **WCAG 2.2 AA contrast**, gradeable, historian-verified & Chicago-citable, provenance / AI-disclosure
   footer, full **bilingual EN/ES**, **5-band differentiation**.
6. **Naming / privacy:** App name = "U.S. History Hack 1877–Present"
   (App Store id6757368709). Website https://www.trooptoteacher.com. Author = Sean Reynolds,
   Founder/CEO, USAF veteran, M.Ed. NEVER use a school name or county/district name in public
   materials ("Franklin, Tennessee" as the LLC location is OK). Never use the word "viral".
7. **Content source of truth:** Always check the GitHub repo `Trooptoteacher/history-hack-web-app`
   FIRST for unit content (CLI: `bash` with `api_credentials=["github"]`) before authoring.
8. **Track definitions:** Track A = Wall Posters (finished, zero fill-in). Track B = Station
   Activities. Do not use the phrases "scenario-based" or "classroom system".

## Workspace Layout (the working tree this skill produces/uses)

Work happens under `tpt_launch/`:

```
tpt_launch/
├── brand.py                       # palette + register_fonts() + copyright constants (single source of truth)
├── fonts/                         # DM Sans, Inter, Kalam, Caveat, Patrick Hand, Bangers, Architects Daughter
├── poster_assets/
│   ├── poster_engine.py           # P01–P11 engine (24x36 master)
│   ├── sketchnote_engine.py       # P13 flagship sketch-note engine (handwriting fonts, icon dispatcher)
│   ├── engine_v2.py               # provenance_footer + vector icons (P12, P06)
│   ├── station_engine.py          # Letter-size Track B station engine
│   ├── platinum_plus.py           # the 3 teacher guides
│   ├── assemble_bundle.py         # Wall Set + Complete Bundle assembler
│   ├── unitN_content.py           # per-unit content single source of truth
│   ├── img/                       # pre-cleared photos only (NO AI imagery)
│   └── p01_overview.py … p11_tennessee.py, proof1_whose_story.py (→P12),
│       proof2_word_wall.py (→P06), proof3_hipp_station.py (→HIPP),
│       proof4_anchor_chart.py (→P13), proof4_note_sheet.py (→AnchorNotes)
├── posters/                       # output: P01..P13 .pdf (24x36)
├── stations/                      # output: ST_*.pdf (Letter)
├── guides/                        # output: Unit1_Standards_Alignment_Map / Print_Guide / Facilitation_Guide
├── assembled/                     # output: UnitN_Wall_Set.pdf, UnitN_Complete_Bundle.pdf
└── assets/                        # QC PNGs
```

## The 13-Poster Wall Set (Track A)

| # | File | Poster | Engine |
|---|------|--------|--------|
| P01 | P01_Unit_Overview | Unit Overview | poster_engine |
| P02 | P02_Timeline | Unit Timeline | poster_engine |
| P03 | P03_Learning_Targets | Learning Targets (I-can) | poster_engine |
| P04 | P04_Key_People | Key People | poster_engine |
| P05 | P05_Key_Events | Key Events & Turning Points | poster_engine |
| P06 | P06_Word_Wall | Bilingual Word Wall | engine_v2 |
| P07 | P07_Primary_Source | Primary Source Spotlight | poster_engine |
| P08 | P08_Maps_Geography | Maps & Geography | poster_engine |
| P09 | P09_Data_Economics | Data & Economics | poster_engine |
| P10 | P10_Debate_Wall | Debate Wall | poster_engine |
| P11 | P11_Tennessee_Connection | The Tennessee Connection | poster_engine |
| P12 | P12_Whose_Story | "Whose Story?" Perspectives | engine_v2 |
| P13 | P13_Anchor_Chart | Sketch-Note Anchor Chart (FLAGSHIP) | sketchnote_engine |

Track B stations (Letter, gradeable): student note sheet companion to the anchor chart
(`ST_USxx_AnchorNotes.pdf`) and a HIPP primary-source station (`ST_USxx_HIPP_*.pdf`).

## Step-by-Step Workflow for a New Unit

1. **Pull content from GitHub.** Read the unit's standards, narrative, vocab, people, events,
   timeline, primary sources, and TN connection from `Trooptoteacher/history-hack-web-app`
   (`api_credentials=["github"]`). Verify every date/number/name/statute/case against primary
   sources (see `references/historian-facts.md` for the Unit 1 verified set as a model).
2. **Author `unitN_content.py`** — the single source of truth for that unit (STANDARDS list,
   TIMELINE, PEOPLE, EVENTS, VOCAB EN/ES, DATA, MAPS, TN_CONNECTION, SOURCES). Mirror the shape
   of `unit1_content.py`.
3. **Build posters** by running each builder (`python3 p01_overview.py` … `python3 p11_tennessee.py`,
   then `proof1_whose_story.py`, `proof2_word_wall.py`, `proof4_anchor_chart.py`). Each builder
   ends with a `qc_render()` to a PNG.
4. **Build stations** (`proof3_hipp_station.py`, `proof4_note_sheet.py`).
5. **Build Platinum Plus guides:** `python3 platinum_plus.py`.
6. **MANDATORY visual QC** (see below) at poster scale on every page.
7. **Assemble:** `python3 assemble_bundle.py` → Wall Set + Complete Bundle.
8. **Save to Google Drive** in an organized folder (see Google Drive section).
9. **Share** each deliverable with `share_file` (`should_validate=false` for posters/stations —
   they pass internal QC and the validator over-flags large-format vector art).

See `references/engine-reference.md` for the exact ReportLab engine API (frame, header band,
auto-fit text wrapping, image cover/contain, photo cards, chips, footer with copyright, QC render)
and `references/workflow-recipes.md` for the build/QC/assemble command recipes.

## Mandatory Visual QC Gate

Before sharing or saving ANY page, render it to PNG and inspect closely for:

- Copyright line present and legible on every page.
- Text that wraps wrong, breaks mid-word, overflows, or is truncated.
- Titles/important text split or broken.
- Text color too close to background (e.g. dark on navy header).
- On the flagship anchor chart: captions dodge subjects, the subtle corporate mark is legible,
  no top logo, no overflow.

Engines auto-fit text (`wrap_fit`, `fit_single`, `para` with `simpleSplit`) to prevent overflow —
but you must still visually verify. If you see ANY issue, fix the layout/zones and re-render.
Never share a page with broken or wrapped text.

## Save to Google Drive

Use the `gws` CLI via `bash` with `api_credentials=["gws"]` (load the `gws-best-practices` skill
for the full contract). Create one parent folder named
`U.S. History Hack — Unit [N] Poster & Activity Packet` with four subfolders:
`01 — Wall Posters (Track A)`, `02 — Station Activities (Track B)`, `03 — Teacher Guides`,
`04 — Assembled Bundles`. Then upload each PDF.

```bash
# create folder
gws drive files create --json '{"name":"...","mimeType":"application/vnd.google-apps.folder"}'
# create subfolder
gws drive files create --json '{"name":"...","mimeType":"application/vnd.google-apps.folder","parents":["<parent-id>"]}'
# upload a PDF (path RELATIVE to cwd)
gws drive files create --upload posters/P01_Unit_Overview.pdf --upload-content-type application/pdf \
  --json '{"name":"P01_Unit_Overview.pdf","parents":["<subfolder-id>"]}'
```

On exit 2 (auth) → `call_external_tool(tool_name="connect", source_id="google_drive")`; do not
blind-retry. Never permanently delete (trash + confirm only).

## Pricing & Launch (reference, locked)

Single $5.50 / $3.50; Unit Bundle $39 / $24.50; Full Course $599 / $349; Free Sampler $0.
TpT setup is paused per the user's instruction — do not publish to TpT without an explicit go.

## References

- `references/engine-reference.md` — full ReportLab engine API and design DNA.
- `references/workflow-recipes.md` — exact build / QC / assemble / Drive command recipes.
- `references/historian-facts.md` — Unit 1 verified primary-source facts (citation model).
- `assets/brand.py` — the locked brand kit (palette, fonts, copyright constants) to copy into a new tree.
