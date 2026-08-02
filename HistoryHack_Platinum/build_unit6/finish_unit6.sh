#!/usr/bin/env bash
# FINISH UNIT 6 — run this ONCE on a box where LibreOffice conversion works
# (the standard History Hack build box). It closes out the render-dependent
# steps the remote web session could not do: PDF export + the mandatory deck
# render-QC, then re-runs the automated text gates.
#
# Prereqs: soffice (LibreOffice), python3 with python-docx/python-pptx/pypdfium2,
#          poppler-utils (pdftoppm) OR pypdfium2 for rasterizing.
# Run from the repo root:  bash HistoryHack_Platinum/build_unit6/finish_unit6.sh

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DEL="$ROOT/HistoryHack_Platinum/deliverables_unit6"
SKILLS="$ROOT/.claude/skills"
QC="$ROOT/scratch_unit6_qc"; mkdir -p "$QC"
export HOME="${HOME:-/root/lohome}"; mkdir -p "$HOME"

echo "== 1/4  Export every master to PDF =="
bash "$ROOT/HistoryHack_Platinum/build_unit6/build_pdfs.sh" "$DEL"

echo "== 2/4  Rasterize both decks for the MANDATORY overflow/clipping read =="
for deck in Unit6_Teacher_Deck_CourseStandard Unit6_Student_Deck_CourseStandard; do
  if [ -f "$DEL/$deck.pdf" ]; then
    mkdir -p "$QC/$deck"
    pdftoppm -r 110 -png "$DEL/$deck.pdf" "$QC/$deck/slide" 2>/dev/null || \
      python3 - "$DEL/$deck.pdf" "$QC/$deck" <<'PY'
import sys,pypdfium2 as p
doc=p.PdfDocument(sys.argv[1])
for i in range(len(doc)):
    doc[i].render(scale=1.5).to_pil().save(f"{sys.argv[2]}/slide-{i+1:03}.png")
print("rendered",len(doc),"slides")
PY
    echo "  -> images in $QC/$deck  (READ every one: no clipped/overflowing text)"
  fi
done

echo "== 3/4  Re-run automated text gates (expect 0 blockers) =="
python3 "$SKILLS/history-hack-text-integrity-qc/scripts/scan_text_integrity.py" \
  "$DEL/Unit6_Student_Workbook_CourseStandard.docx" \
  "$DEL/Unit6_Teacher_Deck_CourseStandard.pptx" \
  "$DEL/Unit6_Student_Deck_CourseStandard.pptx" | tail -1 || true
python3 "$SKILLS/history-hack-lesson-flow-qc/scripts/build_alignment_maps.py" \
  "$DEL/Unit6_Teacher_Deck_CourseStandard.pptx" \
  "$DEL/Unit6_Student_Deck_CourseStandard.pptx" \
  "$DEL/Unit6_Student_Workbook_CourseStandard.docx" | tail -1 || true

echo "== 4/4  Manual checklist (see UNIT6_PLATINUM_STATUS.md) =="
cat <<'EOF'
  [ ] Read every deck slide image in scratch_unit6_qc/ — fix any overflow/clipping
      (129 overflow LEADS were flagged; confirm or fix each).
  [ ] Confirm the student-deck vocab reorder (KEY VOCABULARY now before DIRECT
      INSTRUCTION) reads correctly on each standard's slides.
  [ ] Remaining 14 lesson-flow majors = DI-segment parity (teacher 4 vs student 3).
      Resolve by adding the missing student-deck DI review slides — ideally via a
      reproducible deck build script (see status doc).
  [ ] Zero blank pages on every rendered PDF; notebook lines visible on ruled pages.
  [ ] Schedule F self-score, as-built, >= 80% per section and unit.
EOF
echo "Done. PDFs are in $DEL ; deck images in $QC."
