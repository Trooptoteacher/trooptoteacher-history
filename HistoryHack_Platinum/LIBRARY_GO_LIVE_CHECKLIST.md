# Digital Library — Go-Live Checklist

Everything that can be built in code IS built. What remains is review + infra. This is the
single hand-off: give it to whoever manages the web app / Azure.

## ✅ Done (code complete, tested)
| Piece | Where | Status |
|---|---|---|
| Frontend: StudentDeck tier + decks on `/library` | web-app **PR #561** | tests green, ESLint clean |
| Backend: deck download endpoint (SAS + audit + gating) | historyhack-auth **PR #54** | 36 unit tests green, tsc clean |
| FE ↔ BE contract (slugs, paths, tier lists) | verified aligned | ✓ |
| Turnkey upload script | `HistoryHack_Platinum/upload_library_blobs.sh` | 40/40 deliverables mapped |

The PDF editions (narrative Reader, Student Workbook → Worksheets, Teacher Guide → TeacherKey)
already had a working backend; the **decks** were the gap and now have a full, reviewed-ready
implementation on both sides.

## ⬜ Remaining — review + infra (not code)

### 1. Review + merge the two PRs
- [ ] `history-hack-web-app` **#561** (frontend)
- [ ] `historyhack-auth` **#54** (backend — auth/licensing service; human review recommended)
- [ ] Follow-up noted in #54: add a route-level integration test mirroring `library-routes.test.ts` (couldn't run in the build env — no deps installed).

### 2. Upload the files to Azure Blob
- [ ] `az login` with access to the `sthistoryhackprod` / `workbooks` account
- [ ] Run `HistoryHack_Platinum/upload_library_blobs.sh` (workbooks + decks, units 1–10)
- [ ] Separately upload the **narrative textbook** → `books/unitNN/HH_UnitNN_Reader.pdf` (from its own repo)

### 3. Flip the flags (backend env)
- [ ] `LIBRARY_READER_ENABLED=true`
- [ ] `LECTURE_DECKS_ENABLED=true`

### 4. Light up the units in the UI
- [ ] Extend `DECK_AVAILABLE_UNITS` (both `history-hack-web-app/lib/storage/deck-blob-path.ts` and
      `historyhack-auth/backend/library/deck-blob-path.ts`) from `[1]` to every uploaded unit — keep
      the two lists in lock-step.

### 5. Before commercial launch (licensing)
- [ ] Replace the `isEntitled` stub (returns true for everyone) with a real license/order lookup in
      both `entitlement.ts` files.

## Reference docs (this folder)
- `WEBAPP_LIBRARY_EXTENSION_SPEC.md` — how the Library models editions + the "add a doc = one entry" workflow
- `WEBAPP_LIBRARY_BACKEND_TODO_AND_PROMPT.md` — the backend/infra prompt (now mostly satisfied by PR #54)
- `upload_library_blobs.sh` — the upload commands
