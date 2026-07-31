# Troubleshooting — recurring failures and their fixes

Every entry here is a problem that actually happened while building these workbooks, with the fix that
worked. Check here first when something looks wrong.

## Writing lines are invisible / faint on screen
- Cause: line color `C9C2B4` (the old brand value) renders almost invisibly in Spire and on screen.
- Fix: use `8892A0`, size 8, for all in-flow ruled lines. Keep `C9C2B4` only if matching a legacy
  table that must not change — but for anything a student writes on, use `8892A0`.

## Multiple ruled lines collapse into ONE thick line
- Cause: Word/Spire **merge adjacent paragraphs that share an identical bottom border** and suppress
  the internal borders.
- Fix: the `ruled(n)` helper inserts a border-less **anti-merge spacer** paragraph between each line.
  Never emit stacked bordered paragraphs directly — always go through `ruled()`.

## An activity bleeds onto a second, nearly-empty page
- Cause: content taller than one page — usually because a standard's close-read passage or item count
  is longer than the one you tested, and Word renders taller than Spire.
- Fix: render the **fullest** standard (longest `close`), not the first. Compress the overflowing
  element (fewer/inline lines, tighter `rowH`, drop an extra write box), then re-render the worst case.
  The Close-Read self-check was reduced from 3 stacked lines + writeBox to **2 inline checkbox lines**
  for exactly this reason.

## `pagefit.py` flags the `(front)` segment as BLEED
- Cause: the front matter uses **run-level page breaks** (`new PageBreak()` inside a paragraph), which
  the estimator can't see, so it lumps all front matter into one oversized segment.
- Fix: ignore the `(front)` flag. Only act on **activity** segments (those begin with `H {brk:true}` =
  `pageBreakBefore`, which the estimator does detect).

## `Error: Cannot find module 'docx'` on some units
- Cause: only `unit1/` (or one unit) has `node_modules`; others don't.
- Fix: build with `NODE_PATH="../unit1/node_modules" node build_workbook.js`. Point at whichever unit
  actually has the docx dependency installed.

## All `build_workbook.js` files are 0 bytes / wiped
- Recovery: restore the **tracked** builders from git —
  `git checkout -- <course>/BUILD/{engine,unit2,unit3,unit4,unit5,unit6,unit7}/build_workbook.js`.
- Then reconstruct `unit1/build_workbook.js` (commonly **.gitignored**) by copying a restored unit and
  swapping the header references: `unit2_content`→`unit1_content`, `unit2_images`→`unit1_images`,
  `unit2_exit_tickets`→`unit1_exit_tickets`, `Unit2_PREVIEW`→`Unit1_PREVIEW`,
  `Unit2_Student_Workbook`→`Unit1_Student_Workbook`. Syntax-check all: `node --check`.
- The `.docx` deliverables are tracked, so built output is not lost even when the unit1 script is.

## Edit applied to one unit but not the others (drift)
- Cause: the per-standard `block()` and helpers are duplicated across `unit2..7` + `engine`; editing
  one file leaves the rest inconsistent.
- Fix: apply every layout change with a **single string-replace pass over all 8 files** (a small
  python script that asserts the anchor matches exactly once per file), then regenerate unit1 from
  unit2. Never hand-edit a single unit for a shared-helper change.

## Bolding part of a callout/line doesn't work
- Cause: passing a plain string to `callout`/`P` styles the whole line uniformly.
- Fix: pass an **array of runs** as the line — `[[R('Label: ',{b:true}),R(rest)]]` for a callout, or
  `P([R(...),R(...)])` inline. The callout helper detects non-strings and forwards them to `P()`.

## `SendUserFile` / Drive can't take the file
- `SendUserFile` caps at ~30 MiB; the Drive connector passes bytes through context (impractical for
  large docx/zip). Deliver large bundles as ≤29 MB zip parts, or build a single-standard `ONLYSTD`
  preview for phone/quick review.

## Large-print edition looks identical in byte size
- Not a bug. `LARGEPRINT=1.5` changes `sz` values via `SZ()`; the number of XML elements is unchanged,
  so file size barely moves. Confirm by rendering — text is visibly larger.
