# Course-Binding Standard & Course Walls (the canonical wall)

**Owner:** `history-hack-new-course-builder`. **Consumed by every shared build skill** (workbook, teacher
deck, lean deck, DBQ, organizers, poster, assessment, QC, orchestrator). One wall, referenced everywhere —
never re-implemented per skill, never duplicated per course.

The History Hack platform is **one shared skillset building many walled courses**. The *machinery* (activities,
Cornell notes, organizers, deck arc, item schema, QC gates) is identical for every course. What differs is
**which course's standards and content a build is bound to**. This standard defines that binding and the hard
walls between courses so a build can never cross into the wrong course.

## The course registry (7 editions — matches the web-app `lib/subjects.ts`)

| # | Course id | displayName | Prefix | Home | Status |
|---|---|---|---|---|---|
| 1 | `us-history` | U.S. History | `US` | `HistoryHack_Platinum/` (logical `courses/us-history`) | **Flagship — protected reference & default** |
| 2 | `government` | U.S. Government & Civics | `GC` | `courses/government/` | active |
| 3 | `world-history` | World History & Geography | `W` | `courses/world-history/` | active |
| 4 | `tennessee-history` | Tennessee History | `TN` | `courses/tennessee-history/` | standards ingest |
| 5 | `grade-8-history` | 8th Grade History | (TBD) | `courses/grade-8-history/` | planned |
| 6 | `grade-7-history` | 7th Grade History | (TBD) | `courses/grade-7-history/` | planned |
| 7 | `grade-6-history` | 6th Grade History | (TBD) | `courses/grade-6-history/` | planned |

The **U.S. History flagship is the default and is protected.** Any build that does not explicitly resolve a
different course id builds US History exactly as it always has. A non-US build **never** modifies the flagship.

## Course config contract (`courses/<id>/course.json`)

Every course declares its wall in its own manifest. Shared build skills read **only** these fields — they do
not hardcode course facts.

| Key | Meaning |
|---|---|
| `id` | course id (registry key); the namespace for every output |
| `displayName` | title on covers, footers, decks |
| `standardsPrefix` / `rcPrefix` | the ONLY standard-code prefix this course may emit (e.g. `US`, `GC`, `W`, `TN`) |
| `standardsFile` | path (under this course) to the verbatim TDOE standards — the **only** standards a build may read |
| `contentRoots` | the course's content/deliverable roots (e.g. `courses/<id>/…`, `history-hack-web-app/public/data/<id>/…`) — the **only** places a build may read course content from and write deliverables to |
| `assessmentSource` | the authoritative item bank / parallel-forms for quizzes + answer keys (this course only) |
| `eocTestable` | `true` only if the course has an operational TCAP EOC (currently `us-history`). Governs EOC labels/weighting. |
| `brand` | palette/brand tokens (America 250 is shared) |
| `pacing_anchor` | district calendar for pacing |

Resolution order: an explicit course id from the request → the `course.json` in the working `courses/<id>/`
path → **default `us-history` flagship**. State the resolved id before building (Wall Rule W1).

### Course-select gate (ask when it isn't pinned)

Every build opens with a course binding. Resolve it, then **confirm before any read or write**:

1. **Unambiguous** — the request names a registry course/id (or you are working inside a single
   `courses/<id>/` tree, or it is plainly a U.S. History flagship build): resolve it, **state it**
   ("Building `world-history` (W)…"), and proceed. No prompt needed.
2. **Ambiguous** — the request names a *subject or class* without a registry id ("build the civics unit,"
   "make the world unit"), could match more than one course, or is a new/other-course build with no id
   pinned: **STOP and confirm which of the 7 registry courses to build** before touching any file. Offer the
   registry list (us-history · government · world-history · tennessee-history · grade-8/7/6-history). Do
   **not** silently fall through to the `us-history` default when a non-US or unspecified subject is in play —
   the default protects *flagship* builds, it is not a guess for an unnamed subject.

Once confirmed, the resolved `id` binds every downstream skill (workbook, decks, DBQ, organizers, assessment,
QC) for that build — they all read the same `course.json` and never re-ask.

## The walls (hard rules — enforce on every build)

- **W0 · Pull the current skill first (never build from memory).** Before you build, rebuild, format, render,
  or QC **any** artifact — workbook, slide deck, graphic organizer, poster, DBQ, assessment, worksheet, comic,
  web page, anything — **re-read the CURRENT version of the governing skill(s) from `main`.** Skills are the
  single source of truth and change only via skills-only PRs; a stale, cached, or remembered copy is **not
  valid**. A different agent or a new session must **reload** the skill, not rely on what it "knows." If you
  cannot confirm you are on the current skill, **STOP and pull it first.**
- **W1 · Declare + confirm first.** Run the **Course-select gate** above: resolve and **state the course id**
  ("Building `world-history`…") when it is unambiguous; **STOP and confirm which of the 7 courses** when it is
  not. No build proceeds on an ambiguous course, and an unnamed subject is never silently defaulted to the
  flagship.
- **W2 · Standards wall.** Read standards **only** from the resolved course's `standardsFile`. Never read or
  mix another course's standards. Emit **only** `standardsPrefix`-coded standards (a `world-history` build emits
  `W.xx` only — never `US.xx`).
- **W3 · Content wall.** Read course content and write deliverables **only** under the resolved course's
  `contentRoots`. Never read one course's narrative/sources/banks into another; never write into another
  course's tree.
- **W4 · Flagship protection.** `us-history` (`HistoryHack_Platinum/`) is the protected default. A non-US build
  **must not** read from or write to the flagship tree, and must not alter US files. US builds are unaffected by
  any of this — they resolve to the flagship exactly as before.
- **W5 · Assessment wall.** Quizzes, checks, and answer keys come **only** from the resolved course's
  `assessmentSource`. For non-EOC courses the equated parallel-forms bank is that source.
- **W6 · EOC framing by config.** "TCAP EOC" labels/weighting appear **only** when `eocTestable: true`. Non-EOC
  courses use "benchmark / Standard-Mastery" framing with identical rigor — never an EOC claim.
- **W7 · Namespace outputs.** Every deliverable, filename, and manifest entry is namespaced by `id` so two
  courses' artifacts can never collide or be confused.

## What is shared vs walled

- **Shared (identical for all courses):** the build skills themselves — the 7-activity workbook spine, guided
  Cornell notes, organizer set, deck arc, `tn-assessment-specialist` item schema + rigor, the four adoption
  gates (crosswalk + SSP, UDL 3.0 CAST 2024 back page, notebook-lined space, Rubric-F accessibility), America
  250 brand, and every QC gate. Fix a skill once → every course benefits.
- **Walled (per course, never crossed):** standards, "I Can" targets, narrative, primary sources, vocabulary,
  images, assessment banks/forms, deliverables, and the display name/prefix/EOC flag in `course.json`.

A build is correct only when the shared machinery is bound to **exactly one** course's walled content, declared
up front, with no cross-course read or write.
