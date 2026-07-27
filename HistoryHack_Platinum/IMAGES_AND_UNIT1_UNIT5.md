# Public-domain images in every workbook + Units 1 & 5 on the shared pipeline

## Embedded primary-source images & political cartoons (all units)
Every workbook's Activity 5 (HIPPO primary-source analysis) now shows a real, **public-domain**
image or political cartoon where one is available, with a full Library-of-Congress / National-
Archives Chicago citation. Source: the app's verified image bank
(`public/data/us-history/primary-sources/images/unit-N.json`) — every record is Public Domain.

- `build/gen_images.py N` picks one image per standard (cartoons preferred), copies the file into
  the unit workspace, and writes `unitN_images.json`. Standards with no bank image keep a cited
  text primary source.
- **Every image was eye-verified on a labeled contact sheet.** The bank's rights are sound but a
  few records are mislabeled — the file doesn't match its title. The `BLOCK` set in
  `gen_images.py` drops them. Two were not just wrong but **inappropriate for a classroom**:
  U1's `freedmens_bureau_1868.jpg` is actually a Pictorialist **nude art photo**, and
  `nast_union_as_it_was_1874.jpg` is a DC landscape print — both blocklisted. This is why unseen
  images are never embedded.

Coverage (standards with an embedded image): U1 7/7 · U2 3/11 · U3 3/9 · U4 9/11 · U5 6/6 ·
U6 11/14 · U7 11/12 · U8 7/7 · U9 5/5 · U10 13/13.

## All 10 covers use public-domain hero art
Unit 6's hero was the AP-copyrighted Iwo Jima photo — replaced with the bank's public-domain
D-Day "Into the Jaws of Death" (U.S. Coast Guard). Every other hero is a federal/LoC/FSA/NASA
public-domain photo. **No copyrighted images remain.**

## Units 1 & 5 rebuilt on the shared pipeline
Both were off-format (U1 used the old pre-merge close-read; U5 had no JS build scripts). They were
rebuilt by cloning Unit 4's `_uN` pipeline so all ten units are now identical in format:
- **Unit 1 — "The Rise of Industrialization, 1877–1900"** (US.01–US.07, 76 pp). Golden Spike hero,
  Geographer's Lens on the transcontinental railroad/Homestead Act (US.01), Williamson County /
  Buffalo Soldiers TN connection, embedded cartoons (Bosses of the Senate, "Next!" Standard Oil
  octopus, Nast) and photos (sod house, Tom Torlino, Ellis Island, Riis).
- **Unit 5 — "The Great Depression & New Deal, 1929–1941"** (US.39–US.44, 67 pp). Migrant Mother
  hero, Geographer's Lens on the Dust Bowl (US.40), TVA Tennessee connection, embedded photos/
  poster (Black Tuesday, Dust Bowl, Bonus Army, CCC, WPA "Work Pays America").

## Whitespace / build fixes rolled across all units
- Close Read final formula: shrink long-passage font, cap the Evidence Lab at 2–3 rows, `noSplit`
  rows so nothing splits across a page — the whole Close Read fits ONE page, no front-to-back split.
- Dropped the per-standard quiz STRETCH and the launch ruled-fill (each spilled one element to a
  near-empty page). Result: 8/10 workbooks have zero >85%-blank pages; the two remaining are a
  back-matter reflection table (U5) and a long auto-TOC (U6) — structural, not content bleeds.
- Build gotcha documented in the skill: `pkill -9 soffice; sleep 1` before every `uno_fields.py`
  bake (races produce stale PDFs); `rm -rf /tmp/wsa` before every whitespace audit.
