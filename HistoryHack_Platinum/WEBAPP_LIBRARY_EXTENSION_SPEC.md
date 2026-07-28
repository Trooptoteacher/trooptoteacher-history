# Web App — Adding Documents to the Per-Unit Resource Sets (Digital Library)

**Goal:** make each unit's document set (workbook, teacher guide, narrative textbook,
student packet, decks, and anything added later) available on the History Hack web app,
and make adding a new document a one-entry change going forward.

**Key finding:** the app ALREADY has this system — the gated **Digital Library**
(`/library`), backed by Azure Blob + short-lived SAS links + auth/entitlement + per-view
audit. Do NOT build a public downloads page; it would bypass licensing/audit. Extend the
Library instead. (This is exactly how the DBQ Workbook/Teacher-Guide pair was added.)

Repo: `trooptoteacher/history-hack-web-app`

---

## The three pieces to add ONE new document edition ("tier")

### 1. Frontend registry  (I can author this)
- `lib/storage/library-blob-path.ts`
  - Add the token to the `LibraryTier` union and `LIBRARY_TIERS`.
  - If it's only live for some units yet, add an availability list (mirror `LIBRARY_DBQ_UNITS` / `isTierAvailableForUnit`) so cards only render where a file exists — this is what prevents dead cards.
  - Blob leaf follows the convention: `books/unitNN/HH_UnitNN_<Tier>.pdf`.
- `app/library/page.tsx`
  - Add a `TIER_META` entry: `{ tier, slug, labelEn, labelEs, teacherOnly }`.
  - `teacherOnly: true` hides it from students (like `TeacherKey` / `DBQ_TeacherGuide`).

### 2. Azure backend contract  (your infra — I cannot reach it)
- The production SAS minter is the Hono backend (`historyhack-auth`), path
  `${NEXT_PUBLIC_API_URL}/api/library/:unit/:tier/view`.
- Add the same new tier token there so the SAS mint + role gate accept it.
- Keep frontend and backend tier lists in lock-step (the code comments call this out).

### 3. Upload the file  (your infra — I cannot reach it)
- Upload the PDF to the `workbooks` container (account `sthistoryhackprod`, East US),
  path `books/unitNN/HH_UnitNN_<Tier>.pdf`.
- This mirrors the authoring repo `Trooptoteacher/History-Hack-US-History-Workbooks`.

Once all three are in place, the card lights up for that unit and opens through the
secure viewer, audited per view.

---

## Mapping your documents

| Your document | Edition (tier) | Action |
|---|---|---|
| Narrative textbook | **`Reader`** ("Source Reader") — already exists | Just upload the blob (step 3). No code change. Confirm whether Reader is already populated per unit. |
| Student packet | **New tier** e.g. `StudentPacket` (student-facing, `teacherOnly: false`) | Steps 1 + 2 + 3. |
| Course Standard Student Workbook (this session) | Optional new tier e.g. `CourseStandard_Workbook` | Only if you want the platinum line in the licensed Library too. |
| Course Standard Teacher Guide | Optional `CourseStandard_TeacherKey` (teacherOnly) | Same. |
| Student / Teacher Decks (.pptx) | Optional `StudentDeck` / `TeacherDeck` | Note: the viewer today mints INLINE PDF views; PPTX would need either a PDF companion for in-browser view or an attachment-download variant. Decide viewer behavior first. |

Note: the **Course Standard / Platinum** products I built this session live in a DIFFERENT
source repo (`trooptoteacher-history`) than the Library's existing workbooks
(`History-Hack-US-History-Workbooks`). Adding them to the Library is a product decision, not
just a code change — confirm you want the platinum line in the paid Library.

---

## "Add to the sets as we go" — the steady-state workflow
For every future document, per unit:
1. Add/confirm the tier in the frontend registry + backend contract (once per new tier).
2. Upload `HH_UnitNN_<Tier>.pdf` to the `workbooks` blob container.
3. Add the unit to that tier's availability list (frontend) if it's unit-scoped.

That's it — no page rewrites. `TIER_META` + the blob-path builder are the single source of truth.

---

## What I can do next from here
- **Author the frontend registry diff** for the new editions you choose (Student Packet, and
  optionally the platinum line / decks), availability-gated so nothing breaks before the
  blobs exist — delivered as a ready-to-apply change to `history-hack-web-app`.
- I **cannot** update the Azure backend contract or upload blobs (no infra access from here);
  those are your pipeline / dev.

Decide which editions you want, and whether the platinum products belong in the paid Library,
and I'll stage the frontend piece.
