# US.01 · The Homestead Act of 1862 — Teacher Resource Set (web-app publish manifest)

**Unit 1 · Standard US.01 · Primary-Source Study.** These nine handouts publish to the
History Hack **Digital Library** as a labeled US.01 teacher resource set. This folder is the
**canonical upload source**; the files are already named to the blob convention
`books/unit01/HH_Unit01_<Tier>.pdf` so they need no rename at upload time.

> All statute text is the **verbatim** Homestead Act of 1862 (Sections 1–8, correct numbering:
> five-year proof clause in **Section 2**, reversion in **Section 5**). Content-accuracy gate: passed.

## What teachers get (label · audience · file)

| # | Teacher-facing label (what they see) | Audience | Blob tier | Source file |
|---|--------------------------------------|----------|-----------|-------------|
| 1 | **Homestead Act — Close Reading (two-column, large print)** | All roles | `Homestead_Reading` | `HH_Unit01_Homestead_Reading.pdf` |
| 2 | **Homestead Act — Full Text Excerpt (by section)** | All roles | `Homestead_FullText` | `HH_Unit01_Homestead_FullText.pdf` |
| 3 | **Homestead Act — HIPP Source-Analysis Organizer** | All roles | `Homestead_HIPP` | `HH_Unit01_Homestead_HIPP.pdf` |
| 4 | **Homestead Act — Word Wall (emerging readers, ~Gr. 3–4)** | All roles | `Homestead_WordWall` | `HH_Unit01_Homestead_WordWall.pdf` |
| 5 | **Homestead Act — Leveled Close Read + Questions (~Gr. 4 Lexile, EN/ES supports)** | All roles | `Homestead_CloseReadLeveled` | `HH_Unit01_Homestead_CloseReadLeveled.pdf` |
| 6 | **Homestead Act — Primary-Source DBQ Workbook** | All roles | `Homestead_DBQ` | `HH_Unit01_Homestead_DBQ.pdf` |
| 7 | **Homestead Act — DBQ Scaffolds & UDL Supports** | All roles | `Homestead_DBQ_Scaffold` | `HH_Unit01_Homestead_DBQ_Scaffold.pdf` |
| 8 | 🔒 **Homestead Act — Teacher Plain-Language Version (NOT for student distribution)** | **Teacher-only** | `Homestead_TeacherPlain` | `HH_Unit01_Homestead_TeacherPlain.pdf` |
| 9 | 🔒 **Homestead Act — DBQ Teacher Guide + Rubric + Answer Key** | **Teacher-only** | `Homestead_DBQ_TeacherGuide` | `HH_Unit01_Homestead_DBQ_TeacherGuide.pdf` |

Items **8 and 9 are teacher-only** and must be gated with `canAccessTier` (never shown to students),
exactly like the existing `TeacherKey` / `DBQ_TeacherGuide` tiers.

## To publish (two steps — both need access this build environment does not have)

**Step 1 — Upload the files to Azure Blob** (needs `az login` with *Storage Blob Data Contributor*
on `sthistoryhackprod`):
```bash
cd HistoryHack_Platinum
./upload_library_blobs.sh        # the Homestead block is already wired in
```
Files land at `books/unit01/HH_Unit01_Homestead_*.pdf`. Missing files are skipped, so this is safe
to re-run.

**Step 2 — Register the 9 tiers in `trooptoteacher/history-hack-web-app`** (a small FE + BE PR;
mirrors the existing tier pattern — see `WEBAPP_LIBRARY_EXTENSION_SPEC.md`):
1. `lib/storage/library-blob-path.ts` — add the 9 `Homestead_*` tiers to the tier enum + `TIER_META`
   (label + description from the table above), grouped under a **"US.01 · Homestead Act (1862)"**
   section on the Unit 1 card.
2. `lib/library/entitlement.ts` — add `Homestead_TeacherPlain` and `Homestead_DBQ_TeacherGuide` to the
   teacher-only set in `canAccessTier` (the other 7 are all-roles).
3. `app/library/page.tsx` — add unit 1 to each tier's availability list so the cards light up once the
   blobs are present.
4. Backend SAS route (Azure Hono `historyhack-auth`) — add the 9 tiers to the allow-list + role gate so
   the frontend and backend stay in lock-step.

Feature flag `library-reader` must be on for the audience.

## Provenance
Generators (source of truth) in `../../print-pipeline/`:
`gen_homestead_reading_hipp.py` (reading · full text · HIPP · teacher plain), `gen_dbq_us01_homestead.py`
(DBQ workbook · scaffold · teacher guide), `gen_homestead_closeread.py` (leveled close read),
`gen_homestead_wordwall.py` (word wall). Word/`.docx` archives live beside the PDFs in
`../homestead_reading_hipp/`. Regenerate → re-copy into this folder → re-run the upload script.
