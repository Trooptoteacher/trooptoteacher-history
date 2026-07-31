# Platinum Reference Build — Unit 6 Student Workbook (Course Standard)

This is the **locked reference implementation** of the U.S. History Hack Course Standard
student workbook. Every future unit/standard is built to match it.

- `Unit6_Student_Workbook_CourseStandard.docx` — editable master (174 pp).
- `Unit6_Student_Workbook_CourseStandard.pdf` — rendered, QC'd print copy.

**Spec:** `../STUDENT_WORKBOOK_PLATINUM_STANDARD.md` (LOCKED). Geometry, typography,
palette, section anatomy, and all guardrails are derived from and verified against this build.

**Reference standard inside the unit:** US.45 is polished end-to-end and is the per-standard
model (§7.6 of the spec). US.46–US.58 are produced by propagating US.45's anatomy.

**Rendering/QC:** `soffice --headless --convert-to pdf` (requires `libreoffice-writer`) +
`pypdfium2` to render pages; inspect every page (§7.5 QC gate). No workbook ships with a
blank/near-empty page, a stranded response prompt, or a bled/split box.
