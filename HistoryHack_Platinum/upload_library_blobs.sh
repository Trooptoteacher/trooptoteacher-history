#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# History Hack — Digital Library blob upload
# Uploads the Course Standard deliverables to the canonical blob paths the
# backend serves (books/unitNN/…  and  decks/unitNN/…).
#
# PREREQS: az CLI logged in (az login) with access to the workbooks storage
# account, and the two vars below set. Run from the repo root (paths are
# repo-relative to HistoryHack_Platinum/).
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail
: "${ACCOUNT:=sthistoryhackprod}"      # AZURE_WORKBOOKS_STORAGE_ACCOUNT
: "${CONTAINER:=workbooks}"            # AZURE_WORKBOOKS_CONTAINER
up() { # up <local> <blob>
  if [ -f "$1" ]; then
    echo "→ $2"
    az storage blob upload --account-name "$ACCOUNT" --container-name "$CONTAINER" \
      --file "$1" --name "$2" --overwrite --only-show-errors
  else echo "SKIP (missing source): $1"; fi
}

# ── Unit 1 ──
up "deliverables_unit1/Unit1_Student_Workbook_CourseStandard.pdf" "books/unit01/HH_Unit01_Worksheets.pdf"
up "deliverables_unit1/Unit1_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit01/HH_Unit01_TeacherKey.pdf"
up "deliverables_unit1/Unit1_Teacher_Deck_CourseStandard.pptx" "decks/unit01/HH_Unit01_LectureDeck.pptx"
up "deliverables_unit1/Unit1_Student_Deck_CourseStandard.pptx" "decks/unit01/HH_Unit01_StudentDeck.pptx"

# ── Unit 2 ──
up "deliverables_unit2/Unit2_Student_Workbook_CourseStandard.pdf" "books/unit02/HH_Unit02_Worksheets.pdf"
up "deliverables_unit2/Unit2_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit02/HH_Unit02_TeacherKey.pdf"
up "deliverables_unit2/Unit2_Teacher_Deck_CourseStandard.pptx" "decks/unit02/HH_Unit02_LectureDeck.pptx"
up "deliverables_unit2/Unit2_Student_Deck_CourseStandard.pptx" "decks/unit02/HH_Unit02_StudentDeck.pptx"

# ── Unit 3 ──
up "deliverables_unit3/Unit3_Student_Workbook_CourseStandard.pdf" "books/unit03/HH_Unit03_Worksheets.pdf"
up "deliverables_unit3/Unit3_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit03/HH_Unit03_TeacherKey.pdf"
up "deliverables_unit3/Unit3_Teacher_Deck_CourseStandard.pptx" "decks/unit03/HH_Unit03_LectureDeck.pptx"
up "deliverables_unit3/Unit3_Student_Deck_CourseStandard.pptx" "decks/unit03/HH_Unit03_StudentDeck.pptx"

# ── Unit 4 ──
up "deliverables_unit4/Unit4_Student_Workbook_CourseStandard.pdf" "books/unit04/HH_Unit04_Worksheets.pdf"
up "deliverables_unit4/Unit4_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit04/HH_Unit04_TeacherKey.pdf"
up "deliverables_unit4/Unit4_Teacher_Deck_CourseStandard.pptx" "decks/unit04/HH_Unit04_LectureDeck.pptx"
up "deliverables_unit4/Unit4_Student_Deck_CourseStandard.pptx" "decks/unit04/HH_Unit04_StudentDeck.pptx"

# ── Unit 5 ──
up "deliverables_unit5/Unit5_Student_Workbook_CourseStandard.pdf" "books/unit05/HH_Unit05_Worksheets.pdf"
up "deliverables_unit5/Unit5_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit05/HH_Unit05_TeacherKey.pdf"
up "deliverables_unit5/Unit5_Teacher_Deck_CourseStandard.pptx" "decks/unit05/HH_Unit05_LectureDeck.pptx"
up "deliverables_unit5/Unit5_Student_Deck_CourseStandard.pptx" "decks/unit05/HH_Unit05_StudentDeck.pptx"

# ── Unit 6 ──
up "deliverables_unit6/Unit6_Student_Workbook_CourseStandard.pdf" "books/unit06/HH_Unit06_Worksheets.pdf"
up "deliverables_unit6/Unit6_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit06/HH_Unit06_TeacherKey.pdf"
up "deliverables_unit6/Unit6_Teacher_Deck_CourseStandard.pptx" "decks/unit06/HH_Unit06_LectureDeck.pptx"
up "deliverables_unit6/Unit6_Student_Deck_CourseStandard.pptx" "decks/unit06/HH_Unit06_StudentDeck.pptx"

# ── Unit 7 ──
up "deliverables_unit7/Unit7_Student_Workbook_CourseStandard.pdf" "books/unit07/HH_Unit07_Worksheets.pdf"
up "deliverables_unit7/Unit7_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit07/HH_Unit07_TeacherKey.pdf"
up "deliverables_unit7/Unit7_Teacher_Deck_CourseStandard.pptx" "decks/unit07/HH_Unit07_LectureDeck.pptx"
up "deliverables_unit7/Unit7_Student_Deck_CourseStandard.pptx" "decks/unit07/HH_Unit07_StudentDeck.pptx"

# ── Unit 8 ──
up "deliverables_unit8/Unit8_Student_Workbook_CourseStandard.pdf" "books/unit08/HH_Unit08_Worksheets.pdf"
up "deliverables_unit8/Unit8_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit08/HH_Unit08_TeacherKey.pdf"
up "deliverables_unit8/Unit8_Teacher_Deck_CourseStandard.pptx" "decks/unit08/HH_Unit08_LectureDeck.pptx"
up "deliverables_unit8/Unit8_Student_Deck_CourseStandard.pptx" "decks/unit08/HH_Unit08_StudentDeck.pptx"

# ── Unit 9 ──
up "deliverables_unit9/Unit9_Student_Workbook_CourseStandard.pdf" "books/unit09/HH_Unit09_Worksheets.pdf"
up "deliverables_unit9/Unit9_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit09/HH_Unit09_TeacherKey.pdf"
up "deliverables_unit9/Unit9_Teacher_Deck_CourseStandard.pptx" "decks/unit09/HH_Unit09_LectureDeck.pptx"
up "deliverables_unit9/Unit9_Student_Deck_CourseStandard.pptx" "decks/unit09/HH_Unit09_StudentDeck.pptx"

# ── Unit 10 ──
up "deliverables_unit10/Unit10_Student_Workbook_CourseStandard.pdf" "books/unit10/HH_Unit10_Worksheets.pdf"
up "deliverables_unit10/Unit10_Teacher_HowToUse_and_MTSS_Guide.pdf" "books/unit10/HH_Unit10_TeacherKey.pdf"
up "deliverables_unit10/Unit10_Teacher_Deck_CourseStandard.pptx" "decks/unit10/HH_Unit10_LectureDeck.pptx"
up "deliverables_unit10/Unit10_Student_Deck_CourseStandard.pptx" "decks/unit10/HH_Unit10_StudentDeck.pptx"

# ── NOT in the Course Standard deliverables set (upload from their own source) ──
# Narrative textbook  → books/unitNN/HH_UnitNN_Reader.pdf   (from the narrative-textbook repo)
# Deck answer key      → decks/unitNN/HH_UnitNN_DeckAnswerKey.pdf   (optional; platinum has no separate deck key)

echo "Done. After upload, set LIBRARY_READER_ENABLED=true and LECTURE_DECKS_ENABLED=true,"
echo "and extend DECK_AVAILABLE_UNITS / LIBRARY availability to the uploaded units."
