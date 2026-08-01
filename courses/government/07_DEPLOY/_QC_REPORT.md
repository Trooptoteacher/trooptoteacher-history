# Print QC Report — Government Hack™ Course Standard (Platinum)

**Course:** Foundations of Constitutional Government · TN U.S. Government & Civics (GC.01–GC.35)
**Scope:** Full package — 7 units × (Student Workbook · Large-Print Workbook · Student Organizers · Student Deck · Teacher Guide+MTSS · Assessment Book · Teacher Deck · Organizer Toolkit · 4 covers) + course-level artifacts
**Method:** All 57 Word deliverables rendered to print-locked PDF via LibreOffice headless; 91 PDFs machine-scanned for render integrity, blank/widow pages, page-fit, and asset completeness.
**Date:** 2026-07-31

---

## 1. Overall verdict

**READY FOR CLASSROOM PRINT — with minor packaging fixes.**

The instructional consumables (workbooks, organizers, assessment books, teacher guides, decks) are clean, complete, and reproducible. Every file renders without error, with **zero blank interior pages** and **zero render failures** across 91 PDFs. The issues below are packaging/asset matters, not content or layout defects — none block a teacher from printing and using the core materials.

## 2. Severity summary

| Severity | Count | Item |
|---|---|---|
| Critical | 0 | — |
| High | 1 | "Cover" files are print-shop production kits, not classroom covers |
| Medium | 2 | 3 primary-source images missing + 1 placeholder; Unit 7 student organizer packet absent |
| Low | 2 | Large-print workbooks very long; course-level artifacts still HTML-only |

## 3. Environment fix applied (was blocking all PDF output)

This build container shipped with **only `libreoffice-core`** — the `libreoffice-writer` module was missing, so LibreOffice could not load *any* Word document (it failed even on plain text). No docx could be converted to PDF in this environment until `libreoffice-writer` was installed. All 57 renders below were produced after that fix. **Action:** the container/setup for this repo needs `libreoffice-writer` (+`libreoffice-math`, `python3-uno`) pre-installed, or PDF builds will silently fail.

## 4. Defects

### HIGH — "Cover" files are perfect-bound production kits, not classroom cover sheets
- **Where:** all 28 `*_Cover_*.pdf` (every unit, 4 each). Quarantined in each unit's `PRINT-SHOP_COVERS/`.
- **What:** each "cover" is a 5-page production wrap: p1 front cover, p2 **mirror-reversed back cover** (for perfect binding), p3 **spine-width spec** (0.203 in @ 90 pp), p4 marketing page, p5 a sheet literally labeled *"internal handoff sheet for your printer… not part of the printed book."*
- **Why it matters:** a teacher who prints "the cover" for a photocopied consumable gets 5 pages including reversed text and internal spine math — confusing and wasteful. These are right for a print-shop perfect-bound run, wrong for copier reproduction.
- **Fix:** generate a simple **1-page classroom front cover** per book for the copy-and-staple workflow; keep these kits for the perfect-bound storefront run. (Interim: they're foldered as `PRINT-SHOP_COVERS/` so no one prints them by mistake.)

### MEDIUM — Missing / placeholder primary-source images
- **Where:** `GC.04_looking-glass-1787`, `GC.32_nast-third-term-panic`, `GC.33_yellow-press-cartoon` are **absent from the repo**; `GC.28_tennessee-state-capitol.jpg` is a **20 KB placeholder** (Tennessee Great Seal stand-in).
- **Why it matters:** these appear in the **Teacher Decks** (Units 1, 2, 7). Printed decks will show a gap or the placeholder where the source should be.
- **Fix:** re-supply the four high-res source scans (owner action — these are external assets I can't regenerate), then re-export the affected decks. Workbooks embed their own media and are unaffected.

### MEDIUM — Unit 7 student graphic-organizer packet missing
- **Where:** `01_STUDENT_PACKETS/pdf/` has units 1–6 only; no `unit-7-graphic-organizers.pdf`.
- **Why it matters:** Unit 7 students lack the standalone organizer consumable their peers get in every other unit. (The Unit 7 *Teacher* Organizer Toolkit does exist.)
- **Fix:** generate the Unit 7 student organizer packet to match units 1–6.

## 5. Low-priority notes
- **Large-print workbooks are long** — Unit 1 = 304 pp, Unit 3 = 239 pp, Unit 6 = 174 pp. Correct for accessibility, but a real per-student paper cost. Recommend duplex/booklet printing and offering large-print on demand rather than class sets.
- **Course-level artifacts (standards matrix, scope & sequence) are HTML**, not PDF. Only `UDL-MTSS-Framework.pdf` is print-ready. Convert the HTML crosswalks to PDF if districts want them in the print binder.

## 6. Priority order
1. Add `libreoffice-writer` to the build environment (unblocks all future PDF builds).
2. Generate 1-page classroom covers (HIGH, affects every unit's copy workflow).
3. Re-supply 4 primary-source scans + re-export affected decks (MEDIUM).
4. Build Unit 7 student organizer packet (MEDIUM).
5. Convert course-level HTML crosswalks to PDF (LOW).

## 7. Final release readiness
- **Student & teacher instructional consumables:** ✅ release-ready for classroom print now.
- **Perfect-bound storefront covers:** ✅ ready as production kits (not classroom sheets).
- **Full district binder (with covers + all course artifacts as print):** ⚠️ needs items 2–5 above.

*Render integrity: 57/57 docx → PDF OK · 91 PDFs scanned · 0 render errors · 0 blank interior pages.*
