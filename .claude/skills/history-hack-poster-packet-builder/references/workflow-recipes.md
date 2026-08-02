# Workflow Recipes — exact commands

All commands run from `tpt_launch/` (cwd). Python deps: `reportlab`, `pypdf`, `pypdfium2`.

## 0. Pull unit content from GitHub (source of truth)

```bash
# via bash with api_credentials=["github"] — repo Trooptoteacher/history-hack-web-app
# Read the unit's standards, narrative, vocab, people, events, timeline, primary sources, TN tie-in.
```

Author `unitN_content.py` mirroring the shape of `unit1_content.py` (STANDARDS, TIMELINE, PEOPLE,
EVENTS, VOCAB EN/ES, DATA, MAPS, TN_CONNECTION, SOURCES). This is the per-unit single source of truth.

## 1. Build the 13 wall posters (Track A)

```bash
cd tpt_launch/poster_assets
for b in p01_overview p02_timeline p03_learning_targets p04_key_people p05_key_events \
         p07_primary_source p08_maps_geography p09_data_economics p10_debate_wall p11_tennessee; do
  python3 ${b}.py
done
python3 proof2_word_wall.py     # -> P06_Word_Wall.pdf
python3 proof1_whose_story.py   # -> P12_Whose_Story.pdf
python3 proof4_anchor_chart.py  # -> P13_Anchor_Chart.pdf (flagship)
```

## 2. Build the stations (Track B)

```bash
python3 proof3_hipp_station.py  # -> ../stations/ST_USxx_HIPP_*.pdf  (2 pages, no blank 3rd page)
python3 proof4_note_sheet.py    # -> ../stations/ST_USxx_AnchorNotes.pdf
```

## 3. Build Platinum Plus teacher guides

```bash
python3 platinum_plus.py
# -> ../guides/Unit1_Standards_Alignment_Map.pdf
# -> ../guides/Unit1_Print_Guide.pdf
# -> ../guides/Unit1_Facilitation_Guide.pdf
```

## 4. Mandatory visual QC

Each builder calls `qc_render()` and writes a `*_qc.png` into `../assets/`. Use the `read` tool on
each PNG and inspect for: copyright present, no text overflow/wrap-break/truncation, header text
legible against navy, flagship caption zones dodge subjects. Fix and re-render anything that fails.

```bash
ls ../assets/*_qc.png
```

## 5. Assemble the bundle

```bash
python3 assemble_bundle.py
# -> ../assembled/UnitN_Wall_Set.pdf        (13 posters)
# -> ../assembled/UnitN_Complete_Bundle.pdf (cover + dividers + guides + posters + stations)
```

## 6. Share with the user

Use `share_file` with `should_validate=false` for posters/stations (large-format vector art trips
the generic validator even when QC-clean). Reuse the same `name` to version-update an asset.

## 7. Save to Google Drive (organized)

Load `gws-best-practices`. Use `bash` with `api_credentials=["gws"]`. Upload paths must be RELATIVE
under cwd.

```bash
# parent
gws drive files create --json '{"name":"U.S. History Hack — Unit N Poster & Activity Packet","mimeType":"application/vnd.google-apps.folder"}'
# subfolders (parents=[<parent-id>])
for s in "01 — Wall Posters (Track A)" "02 — Station Activities (Track B)" \
         "03 — Teacher Guides" "04 — Assembled Bundles"; do
  gws drive files create --json "{\"name\":\"$s\",\"mimeType\":\"application/vnd.google-apps.folder\",\"parents\":[\"<parent-id>\"]}"
done
# upload (loop a file list per subfolder)
gws drive files create --upload posters/P01_Unit_Overview.pdf --upload-content-type application/pdf \
  --json '{"name":"P01_Unit_Overview.pdf","parents":["<posters-subfolder-id>"]}'
# get the shareable link
gws drive files get --params '{"fileId":"<parent-id>","fields":"id,name,webViewLink"}'
```

Auth failure (exit 2) → `call_external_tool(tool_name="connect", source_id="google_drive")`, then
stop and let the user click the surfaced button. Never blind-retry; never permanently delete.

## Common pitfalls (learned on Unit 1)

- A double `c.showPage()` at the end of a station's student page creates a blank trailing page —
  remove the stray one.
- Keep stderr separate when parsing `gws` JSON: `gws ... 2>gws.err` then parse stdout only.
- Posters are huge (24x36 vector); the Complete Bundle can be ~40 MB — that is expected.
- Re-render ALL pages after any change to `brand.py` (palette/copyright) so every footer matches.
