# District-Ready Unit Folder Architecture

Use a predictable structure for every unit:

```text
History Hack U.S. History/
  Unit NN - Unit Title/
    00 Start Here/
      Unit Overview.docx
      Unit Pacing Guide.docx
      Standards Alignment and Crosswalk.docx
      Unit File Inventory.xlsx-or-csv
      README.txt
    01 Unit Presentation/
      History-Hack-Unit-NN-Teacher-Deck.pptx
      Teacher Deck Usage Guide.docx
    02 Lessons/
      US.xx - Lesson Title/
        Teacher Materials/
        Student Materials/
        Print-Ready PDFs/
      US.yy - Lesson Title/
        Teacher Materials/
        Student Materials/
        Print-Ready PDFs/
    03 Assessments/
      Formative/
      Exit Tickets/
      Unit Assessment/
      Answer Keys/
    04 Primary Sources/
      Student Editions/
      Teacher Guides/
      Citation and Rights Ledger/
    05 Differentiation and Accessibility/
      UDL-WIDA Overview.docx
      Accommodation Crosswalk.docx
      Spanish and Multilingual Supports/
    06 Optional Extensions/
    99 Archive - Superseded Files/
```

## Rules

- Use numeric prefixes so folders sort in teacher workflow order.
- Keep the unit deck only in `01 Unit Presentation`.
- Keep authoritative editable files in the lesson or shared-content location where teachers expect them.
- Do not duplicate authoritative Word files across folders.
- PDF exports may appear in print-ready folders because they are delivery copies, not editable authorities.
- Archive superseded versions rather than mixing them with current files.
- No shortcuts.
- Use consistent names: `US.xx - Material Name - Student.docx` and `US.xx - Material Name - Teacher.docx`.
- Include version/date only when formal version control is needed; avoid filename clutter.

## Complete-Unit Download Structure

The app ZIP may be flatter than the district Drive:

```text
README.txt
US.xx/
  Student Materials/
  Teacher Materials/
US.yy/
  Student Materials/
  Teacher Materials/
Unit Presentation/
  History-Hack-Unit-NN-Teacher-Deck.pptx
```

Every file in the ZIP must be physical, unique, and extractable. The README explains editable originals, PDFs, deck location, and support labels.

