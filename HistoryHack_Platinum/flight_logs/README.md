# Flight Logs — drop folder

The **Flight Log** is the student companion to the narrative Reader (students fill it in),
paired with a **teacher answer key**. Drop both files here — **you do NOT need to split them
by unit.** Claude will split per-unit here, or model a course-level edition if they don't
split cleanly.

## What to drop
Two files (any of these forms is fine — PDF preferred, but a zip like the narratives works too):

| Drop this | It is | Who sees it in the Library |
|---|---|---|
| the **student** flight log | the fill-in booklet | **all roles** (students + teachers) |
| the **teacher answer key** | the completed / annotated key | **teachers only** |

Helpful (not required) names so Claude can tell them apart at a glance:
- `FlightLog_Student.pdf`
- `FlightLog_TeacherKey.pdf`

If they're named something else, just drop them and say which is which.

## What happens next
- Per-unit split → `books/unitNN/HH_UnitNN_FlightLog.pdf` + `…_FlightLogKey.pdf`, **or**
- Course-level → a single Flight Log / Flight Log Key edition.

Then it rides the same `upload_library_blobs.sh` → Azure pipeline as everything else, and a
small code change adds the two new tiers (student = everyone, key = teacher-only). No page
rewrites — the tier list + blob-path builder are the single source of truth.
