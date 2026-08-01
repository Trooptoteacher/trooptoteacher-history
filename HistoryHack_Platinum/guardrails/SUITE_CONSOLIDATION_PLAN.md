# Social Studies Hack — Suite Consolidation Plan

**Purpose.** Existing course builds are fragmented across branches and two
directory conventions, and none are on `main`. This plan defines ONE canonical
structure and the safe path to merge each course into it. Adopted after the
"consolidate & verify first" decision.

## Current state (verified)

| Course | Status | Location | Convention |
|---|---|---|---|
| US History | ✅ shipped (reference) | `HistoryHack_Platinum/` (main) | `build_unit*/` + `deliverables_unit*/` |
| **Government** | ✅ **built & QC'd** (7 units, ~800 MB) | branch `claude/history-hack-course-rebuild-jko587` → `courses/foundations-constitutional-government/` | numbered `00_START_HERE…07_DEPLOY` |
| World History | 🟡 partial (Unit 1-level) | branch `claude/world-history-platinum-build-mv5z17` | US-scaffold |
| TN / registry | ⬜ Phase-0 only | branch `claude/unit-5-platinum-pilot-jcubu6` → `courses/{government,world-history,tennessee-history}/` | `standards/` registry |

## Canonical structure (the single convention)

```
courses/<subject-id>/                 # subject-id = web-app registry id
  00_START_HERE/                      # brand kit, deliverables index, unit map
  01_STUDENT_PACKETS/  02_TEACHER_PACKET/
  03_TEXTBOOK_UNITS/   04_ASSESSMENTS/
  05_STANDARDS_ALIGNMENT/            # ← verbatim standards + sourcing live here
  06_COMPLIANCE_INTERNAL/            # UDL audit, MTSS map, Schedule F, accessibility
  07_DEPLOY/                         # final print-ready district package
```

- **`<subject-id>` uses the web-app registry id, not a unit name.** So the
  Government course dir is **`courses/government/`** — NOT
  `courses/foundations-constitutional-government/` (that is only Unit 1's title).
  Rename on migration. ids: `government`, `world-history`, `tennessee-history`,
  `us-history`.
- **US History** stays at `HistoryHack_Platinum/` for now (working build; do not
  disturb). It is `courses/us-history` *logically*; a physical move is a separate,
  later task.
- **The Phase-0 registry** (`courses/<id>/standards/*.json`, `*_images.json`,
  `course.json`, WCS pacing anchor) folds into **`05_STANDARDS_ALIGNMENT/`** of the
  same course. The verbatim TDOE standards JSON I ingested is the canonical
  standards source; reconcile any older `government_standards_source.json` against
  it (keep the verbatim one).

## Binary-handling strategy  ← the decision that gates "merge to main"

Each finished course is **~800 MB** (workbooks, decks, deploy PDFs), and roughly
half is regenerable `BUILD/` intermediates. Putting 4–7 courses of raw binaries in
`main` would bloat the repo to multiple GB — slow clones, capped disk here, no LFS
budget assumed. Options:

| Option | What's in `main` git | Binaries | Trade-off |
|---|---|---|---|
| **A — source-lean (recommended)** | source: content JSON, builders (`.py`/`.js`), standards, compliance `.md`, `07_DEPLOY` **manifest** (filenames + SHA-256) | `BUILD/` git-ignored; final `07_DEPLOY` PDFs delivered via **GitHub Release** or the Drive deploy folder, referenced by manifest | lean, cloneable, reproducible; binaries one link away |
| B — Git-LFS | source + LFS-tracked deliverables | LFS pointers | needs LFS quota/budget; still large |
| C — full binaries in git | everything | committed | multi-GB repo; risks disk cap here |
| D — leave on branches | nothing new | stays per-branch | fragmentation persists (the thing we're fixing) |

**Recommendation: A.** `main` carries everything needed to *rebuild and verify* a
course (source + guardrail-checkable content) plus a signed manifest of the
deploy binaries; the heavy print artifacts live as release/Drive assets. This is
the only option that respects the disk cap and keeps the suite repo usable.

## Per-course migration (once binary strategy is chosen)

1. **Verify** against CORE guardrails (Government audit in progress).
2. Extract **source + content** (not `BUILD/` binaries) from the course branch
   into `courses/<id>/` with the canonical numbered layout, renamed to the
   subject-id.
3. Fold the Phase-0 registry into `05_STANDARDS_ALIGNMENT/` (dedupe standards +
   sourcing; keep verbatim).
4. Add `.gitignore` for `BUILD/`; write `07_DEPLOY/DELIVERABLES_MANIFEST.json`
   (filenames, sizes, SHA-256, release/Drive URL).
5. Commit to the working branch → PR to `main`.
6. Repeat: Government (now) → World History (finish first) → Tennessee (greenfield).

## Order

1. **Government** — verify → migrate source → manifest → PR to main.
2. **World History** — finish the partial build to all units, then migrate.
3. **Tennessee** — greenfield Phase 1 → build → migrate.

---
© 2026 TroopToTeacher Technologies, LLC · Social Studies Hack suite · Consolidation.
