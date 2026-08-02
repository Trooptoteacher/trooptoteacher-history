#!/usr/bin/env bash
# Re-export every Unit 6 master (.docx/.pptx) to its distribution PDF.
#
# WHY THIS SCRIPT EXISTS: the remote web session that repaired these masters
# cannot run LibreOffice conversion (the sandbox SIGKILLs any soffice document
# load). The masters were fixed there; the PDFs must be regenerated here, on a
# box where `soffice --convert-to` works (the standard History Hack build box).
#
# Usage:  cd HistoryHack_Platinum/deliverables_unit6 && bash ../build_unit6/build_pdfs.sh
# (Run from the deliverables_unit6 folder, or pass it as $1.)

set -euo pipefail
DIR="${1:-.}"
export HOME="${HOME:-/root/lohome}"
mkdir -p "$HOME"

echo "Re-exporting Unit 6 masters in: $DIR"
for f in \
  Unit6_Student_Workbook_CourseStandard.docx \
  Unit6_Teacher_HowToUse_and_MTSS_Guide.docx \
  Unit6_Teacher_Graphic_Organizer_Toolkit.docx \
  Unit6_Assessment_Book_Teacher.docx \
  Unit6_Cover_Student_Workbook.docx \
  Unit6_Cover_Teacher_Edition.docx \
  Unit6_Cover_Assessment_Book.docx \
  Unit6_Cover_Organizer_Toolkit.docx \
  Unit6_Teacher_Deck_CourseStandard.pptx \
  Unit6_Student_Deck_CourseStandard.pptx \
; do
  if [ -f "$DIR/$f" ]; then
    echo "  -> $f"
    soffice --headless --convert-to pdf --outdir "$DIR" "$DIR/$f" >/dev/null
  else
    echo "  (skip, missing) $f"
  fi
done
echo "Done. Verify page counts and, for the decks, run the MANDATORY render QC"
echo "(pdftoppm to images, read every slide for overflow/clipping)."
