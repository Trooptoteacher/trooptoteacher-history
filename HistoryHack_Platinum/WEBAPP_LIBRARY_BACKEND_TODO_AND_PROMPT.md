# Library — Backend / Infra TODO + Ready Prompt

The web app frontend + models are essentially ready (see WEBAPP_LIBRARY_EXTENSION_SPEC.md).
The remaining blockers live in Azure and the Hono backend, which are NOT reachable from the
Claude Code environment that built the deliverables. Hand the prompt below to a Claude Code
session (or engineer) that has: the `historyhack-auth` backend repo, and Azure credentials for
the `sthistoryhackprod` storage account (`workbooks` container / decks paths).

## TODO checklist
- [ ] **Upload PDFs** to `books/unitNN/` for units 01–10:
      `HH_UnitNN_Reader.pdf` (narrative), `HH_UnitNN_Worksheets.pdf` (student workbook),
      `HH_UnitNN_TeacherKey.pdf` (teacher guide).
- [ ] **Upload decks** to `decks/unitNN/`: `HH_UnitNN_LectureDeck.pptx` (teacher/full deck),
      `HH_UnitNN_DeckAnswerKey.pdf`, and — if the student-deck tier ships — `HH_UnitNN_StudentDeck.pptx`.
      Source files: `trooptoteacher-history` → `HistoryHack_Platinum/deliverables_unitNN/`
      (map: `Unit N_Student_Workbook_CourseStandard.pdf` → Worksheets; `..._Teacher_HowToUse_and_MTSS_Guide.pdf`
      → TeacherKey; `..._Teacher_Deck_CourseStandard.pptx` → LectureDeck; `..._Student_Deck_CourseStandard.pptx`
      → StudentDeck; narrative textbook from its own repo → Reader).
- [ ] **Backend tier contract** (`historyhack-auth`): add `StudentDeck` to the deck SAS route + role
      gate (student-allowed), in lock-step with the frontend `DeckTier`.
- [ ] **Feature flags**: enable `library-reader` and `lecture-decks` for the target audience.
- [ ] **Entitlement**: replace the `isEntitled` STUB (currently returns true for everyone) with a
      real license/order lookup before commercial launch.
- [ ] **Verify**: signed-in student sees student editions only; teacher sees all; every view audited;
      SAS links expire (~60s); PPTX decks download (not inline-viewed).

## Ready-to-paste prompt (for the backend/infra session)

> You are working on the History Hack platform. The web app frontend already models a Digital
> Library with PDF tiers (`lib/storage/library-blob-path.ts`: Reader, Worksheets, TeacherKey, DBQ)
> and deck tiers (`lib/storage/deck-blob-path.ts`: LectureDeck, DeckAnswerKey), served via
> short-lived Azure SAS with `canAccessTier`/`canAccessDeckTier` role gating and per-view audit.
> A new `StudentDeck` deck tier has been added on the frontend (student-facing lean deck).
>
> Do the following, keeping frontend and backend tier lists in lock-step:
> 1. In the `historyhack-auth` Hono backend, add `StudentDeck` to the deck view/SAS route and its
>    role gate (allow student + above; it is student-safe, no answer reveals). Mirror how
>    `LectureDeck` is handled.
> 2. Upload the Course Standard files from the `trooptoteacher-history` repo folder
>    `HistoryHack_Platinum/deliverables_unitNN/` to Azure Blob (`sthistoryhackprod`), using the
>    canonical paths: `books/unitNN/HH_UnitNN_Worksheets.pdf`, `HH_UnitNN_TeacherKey.pdf`,
>    `HH_UnitNN_Reader.pdf`; `decks/unitNN/HH_UnitNN_LectureDeck.pptx`, `HH_UnitNN_StudentDeck.pptx`,
>    `HH_UnitNN_DeckAnswerKey.pdf`. Units 01–10.
> 3. Enable the `library-reader` and `lecture-decks` feature flags for the intended audience.
> 4. Replace the entitlement stub in `lib/library/entitlement.ts` (`isEntitled`) with a real
>    license lookup against the order/catalogue DAL before any paid launch.
> 5. Verify end to end: student vs teacher visibility, SAS expiry, audit rows written, PPTX
>    download behavior. Report what you changed and any contract drift between FE and BE.
