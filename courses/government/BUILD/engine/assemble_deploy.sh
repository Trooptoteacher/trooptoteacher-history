#!/usr/bin/env bash
# Assemble the district print package into 07_DEPLOY/ from rendered PDFs.
# Classroom-facing PDFs get clean names; production cover-kits are quarantined
# in a clearly-labeled subfolder so no one photocopies spine-spec sheets.
set -u
C="/home/user/trooptoteacher-history/courses/foundations-constitutional-government"
D="$C/07_DEPLOY"
UNIT_TITLES=( "" \
  "Foundations-of-Constitutional-Government" "Citizen-Participation" \
  "The-Legislative-Branch" "The-Executive-Branch" "The-Judicial-Branch" \
  "Civil-Liberties" "Tennessee-State-and-Local-Government" )

cp_if(){ [ -f "$1" ] && cp -f "$1" "$2" && echo "  + $(basename "$2")" || echo "  ! MISSING: $1"; }

rm -rf "$D"/Unit-* 2>/dev/null
for n in 1 2 3 4 5 6 7; do
  U="$D/Unit-${n}_${UNIT_TITLES[$n]}"
  mkdir -p "$U/STUDENT" "$U/TEACHER" "$U/PRINT-SHOP_COVERS"
  dl="$C/BUILD/unit$n/deliverables"
  echo "Unit $n:"
  # STUDENT
  cp_if "$dl/Unit${n}_Student_Workbook_CourseStandard.pdf"        "$U/STUDENT/Unit${n}_Student_Workbook.pdf"
  cp_if "$dl/Unit${n}_Student_Workbook_CourseStandard_LargePrint.pdf" "$U/STUDENT/Unit${n}_Student_Workbook_LargePrint.pdf"
  cp_if "$C/01_STUDENT_PACKETS/pdf/unit-${n}-graphic-organizers.pdf"  "$U/STUDENT/Unit${n}_Student_Graphic_Organizers.pdf"
  cp_if "$C/BUILD/decks/Unit${n}_Student_Deck/exports/Unit${n}_Student_Deck.pdf" "$U/STUDENT/Unit${n}_Student_Deck.pdf"
  # TEACHER
  cp_if "$dl/Unit${n}_Teacher_HowToUse_and_MTSS_Guide.pdf"        "$U/TEACHER/Unit${n}_Teacher_Guide_HowToUse_and_MTSS.pdf"
  cp_if "$dl/Unit${n}_Assessment_Book_Teacher.pdf"               "$U/TEACHER/Unit${n}_Assessment_Book_Teacher.pdf"
  cp_if "$C/BUILD/decks/Unit${n}_Teacher_Deck/exports/Unit${n}_Teacher_Deck.pdf" "$U/TEACHER/Unit${n}_Teacher_Deck.pdf"
  cp_if "$C/BUILD/organizers/Unit${n}_Teacher_Graphic_Organizer_Toolkit/exports/Unit${n}_Government_Hack_Graphic_Organizer_Toolkit.pdf" "$U/TEACHER/Unit${n}_Teacher_Graphic_Organizer_Toolkit.pdf"
  # COVERS (production kits)
  for c in Assessment_Book Organizer_Toolkit Student_Workbook Teacher_Edition; do
    cp_if "$dl/Unit${n}_Cover_${c}.pdf" "$U/PRINT-SHOP_COVERS/Unit${n}_Cover_${c}.pdf"
  done
done
# course-level
mkdir -p "$D/COURSE"
cp_if "$C/06_COMPLIANCE_INTERNAL/udl-mtss-framework.pdf" "$D/COURSE/UDL-MTSS-Framework.pdf"
echo "DEPLOY_ASSEMBLED total=$(find "$D" -name '*.pdf' | wc -l) pdfs, $(du -sh "$D" | cut -f1)"
