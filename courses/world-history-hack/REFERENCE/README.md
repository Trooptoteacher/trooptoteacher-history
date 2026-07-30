# Brand Reference — Workbook Layout Lock

`USHistory_Unit8_Student_Workbook.docx` is the **U.S. History Hack** Unit 8 Course
Standard Student Workbook, pulled from the owner's Google Drive as the canonical
brand layout. Every course workbook (Government Hack and beyond) must match its
document geometry and writing-activity styling exactly. These are the extracted,
locked-in settings:

| Setting | Value |
|---|---|
| Page size | 12240 × 15840 twips (8.5" × 11") |
| Margins | top/bottom **1152**, left/right **1224**, header/footer **720** |
| Printable / table width | **9792** twips (page − 1224 − 1224) |
| Body font | Calibri, 22 half-pt (11 pt) |
| Column splits | even divisions of 9792 → 4896 (2-col), 3264 (3-col), 2448 (4-col) |
| Cornell notes | grid 4896\|4896; cells **2448 (cue)** \| **7344 (notes)**; navy header `1B2A4A` white bold 20 half-pt; zebra rows `F7F5EF`/`FFFFFF`; `cantSplit`, row height `atLeast 520` |
| Ruled writing line | empty paragraph, `spacing before 80 / after 140`, bottom border `single sz6 space1 color C9C2B4` |
| Callout borders | `C9C2B4` |

The Government workbook builders (`BUILD/unit*/build_workbook.js`) are locked to
these values. To build another course, copy a builder and keep every geometry/style
constant above unchanged — only the content JSON changes.
