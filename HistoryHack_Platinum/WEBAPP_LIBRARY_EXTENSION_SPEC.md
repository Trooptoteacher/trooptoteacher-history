# Web App — Per-Unit Resource Sets in the Digital Library

**Reality check after reading the code:** the History Hack web app (`trooptoteacher/history-hack-web-app`)
ALREADY has the full infrastructure for this — for both PDFs and decks. Almost nothing new is
needed on the *model* side; the real work is uploading files to Azure Blob and turning on the flags.

## What already exists

### PDF library editions — `lib/storage/library-blob-path.ts`
Blob layout `books/unitNN/HH_UnitNN_<Tier>.pdf`, served via short-lived SAS with auth + entitlement + audit.
- `Reader` → **Source Reader** (the narrative textbook) ✅
- `Worksheets` → **Student Worksheets** (student workbook) ✅
- `TeacherKey` → **Teacher Key** (teacher guide, teacher-only) ✅
- `DBQ_Workbook` / `DBQ_TeacherGuide` (units 1–3) ✅

UI: `app/library/page.tsx` renders `UNITS × TIER_META`; teacher-only tiers hidden from students
(`canAccessTier` in `lib/library/entitlement.ts`). Feature flag: `library-reader`.

### Deck editions — `lib/storage/deck-blob-path.ts`
Blob layout `decks/unitNN/HH_UnitNN_<Tier>.(pptx|pdf)`, own SAS (`deck-sas.ts`), downloads
(`deck-downloads.ts`), gating (`canAccessDeckTier`), feature flag `lecture-decks`.
- `LectureDeck` → the `.pptx` (teacher-only today) ✅
- `DeckAnswerKey` → printable `.pdf` key (teacher-only) ✅

## How our documents map

| Document (this session / yours) | Existing edition | New work? |
|---|---|---|
| Narrative textbook | `Reader` | Upload blob only |
| Student Workbook (platinum) | `Worksheets` | Upload blob only |
| Teacher Guide (How-to-Use & MTSS) | `TeacherKey` | Upload blob only |
| Teacher (Full) Deck | `LectureDeck` | Upload blob only |
| Teacher Answer Key (deck) | `DeckAnswerKey` | Upload blob only |
| **Student (Lean) Deck** | — (LectureDeck is teacher-only) | **NEW student-facing deck tier** (small FE+BE change) |

So the ONLY genuinely-new model piece is a **student-facing deck tier** (e.g. `StudentDeck`,
`.pptx` or a PDF render) so the Lean deck can reach students. Everything else already has a home.

## The remaining work, by owner

### Frontend (I can do)
1. Add a `StudentDeck` tier to `DeckTier` + `DECK_TIERS` + extension/mime maps + `canAccessDeckTier`
   (student-allowed) + `normalizeDeckTierParam` — mirrors the existing `LectureDeck` entry.
2. Surface **deck editions** in `app/library/page.tsx` (today it lists only PDF tiers) — a deck
   group per unit, availability-gated so cards only show where a blob exists (mirror `LIBRARY_DBQ_UNITS`).
3. Add availability lists for the platinum editions so they light up per unit as blobs land.

### Backend / infra (NOT reachable from this environment — see TODO + prompt)
1. Azure Hono backend (`historyhack-auth`): add the `StudentDeck` tier to the deck SAS route +
   role gate so it stays in lock-step with the frontend.
2. Upload the actual files to Azure Blob:
   - `books/unitNN/HH_UnitNN_Reader.pdf` (narrative)  · `HH_UnitNN_Worksheets.pdf` · `HH_UnitNN_TeacherKey.pdf`
   - `decks/unitNN/HH_UnitNN_LectureDeck.pptx` · `HH_UnitNN_DeckAnswerKey.pdf` · `HH_UnitNN_StudentDeck.pptx`
   Source files are in `trooptoteacher-history` → `HistoryHack_Platinum/deliverables_unitNN/`.
3. Turn on feature flags (`library-reader`, `lecture-decks`) for the audience.
4. Replace the entitlement STUB (`isEntitled` returns true for everyone) with a real license lookup
   before commercial launch.

## Steady-state: "add a document as we go"
Per new document, once its tier exists: drop `HH_UnitNN_<Tier>.<ext>` in the right blob container,
add the unit to that tier's availability list. No page rewrites — `TIER_META` + the blob-path
builders are the single source of truth.
