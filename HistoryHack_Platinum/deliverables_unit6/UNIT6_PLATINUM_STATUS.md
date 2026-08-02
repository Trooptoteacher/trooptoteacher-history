# Unit 6 (WWII · US.45–US.58) — Platinum remediation status

_Snapshot of the remediation that took Unit 6 from "almost Platinum" toward the Platinum bar.
This is the intended template unit for US.01–US.95._

## Fixed at the source (verified clean in this session)

| Area | Defect (before) | Fix | Verified |
|---|---|---|---|
| `build_unit6/unit6_content.json` | 34 fields truncated mid-word with `…` (vocab defs + C/E/G/H/P lens statements) | 31 lens statements recovered sentence-complete from each standard's own reading passage; 3 vocab defs (Communism, Appeasement) completed from the SME vocab bank | `scan_text_integrity` → **0** truncations |
| `build_unit6/derive_unit6.py` | `content[:110] + "…"` cut lens blurbs mid-clause | replaced with `sentence_complete()` (whole-sentence, never mid-word) | future re-derive is clean |
| `build_unit6/build_workbook_u6.js` | `ImageRun` had no `type:` → 12 images written as `*.undefined`, invalid OOXML (would not open in strict tools) | `imgType()` helper + explicit `type:` on every `ImageRun` | rebuilt workbook: **0** `.undefined`, opens in python-docx |
| `build_unit6/build_cover_u6.js` | same `.undefined` defect on the cover hero (all 4 covers) | explicit `type:'jpeg'` on the hero `ImageRun` | 4 covers rebuilt: **0** `.undefined`, open OK |
| Student Workbook `.docx` | invalid package + truncated word-wall defs | **rebuilt** from fixed source + images (pulled from `history-hack-web-app`) | text-integrity **0/0/0**; valid OOXML |
| Teacher + Student Deck `.pptx` | 16 truncated vocab defs / answer-key rationales (8 were text-integrity BLOCKERS) | each completed from the SME source (extend-only, verified `startswith`) — patched in place (no deck build script exists to rebuild) | text-integrity **0** blockers; both decks valid, slide counts intact (258 / 113) |
| Student Workbook alignment | 98 activities had **no** `▶ Deck` reference | added `▶ Deck · <Role>` to all 7 activities/standard in `build_workbook_u6.js` | lesson-flow majors **126 → 28** |

## Remaining Platinum gaps — need the LibreOffice/render build box

These could not be completed in the remote web session and are handed off:

1. **PDF re-export (all changed masters).** LibreOffice document conversion is SIGKILLed in this
   sandbox. The `.docx`/`.pptx` **masters** are the source of truth and are clean; the distribution
   **PDFs must be regenerated** with `build_unit6/build_pdfs.sh` on a box where `soffice --convert-to`
   works. The stale PDFs for the changed masters were removed so nothing mismatched ships.
2. **Deck render QC (mandatory Gate 3).** 129 overflow *leads* (assertion headlines vs. box height)
   are render-confirm only — rasterize each deck and read every slide.
3. **Student-deck structural alignment (28 lesson-flow majors, all 14 standards).**
   - Student deck presents **KEY VOCABULARY after DIRECT INSTRUCTION**; Platinum rule is vocab-first.
   - Teacher deck teaches **more DI segments than the student deck** (student review deck should cover
     100% of what was taught). Both require reordering/adding student-deck slides + a render pass —
     ideally via a reproducible deck build script (none exists in `build_unit6/` yet; Unit 10 has a
     `deck_merge_teacher.py` to model). Establishing that script is also step 1 of making Unit 6 a
     true, reproducible template.
4. **Brand palette.** Workbook/cover scripts still use legacy navy `#1B2A4A` / gold `#C89B3C`
   (retired). Migrate to America 250 (`#1F3A5F` / `#C9A227`, cream `#F8F5EF`) across all unit scripts
   as one coherent change before templatizing.

## Reproducibility note (for templatizing to other units)

`build_unit6/` is **not yet self-contained**: `derive_unit6.py` reads from
`history-hack-web-app/public/data/us-history/` and images from `public/images/textbook/unit-6/`,
and the deck build step is missing entirely. To make Unit 6 THE template, vendor (or script the
pull of) the source data + images, add the deck build/merge script, and pin the node `docx`
dependency.
