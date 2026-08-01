# Platinum build + PDF preflight (run in an environment with working LibreOffice)

The docx packets are built here (node + docx-js). **PDF rendering + pagination preflight
run in your environment / CI**, because this repo's build sandbox has a non-functional
headless LibreOffice (it hangs converting even a trivial docx). Everything below works on a
normal machine (macOS/Linux) or CI image with LibreOffice installed.

## One-time setup
- **LibreOffice** (provides `soffice` + the python-`uno` bridge)
  - macOS: `brew install --cask libreoffice`
  - Debian/Ubuntu: `sudo apt-get install -y libreoffice libreoffice-script-provider-python`
- **Python**: `pip install pdfminer.six`
- **Node** + the docx builder deps: from a unit build dir, `npm install docx`

## Build a unit's packets (docx)
From a unit build dir that contains `analysis/<unit>_content.json` (+ `node_modules`):
```bash
mkdir -p deliverables
node ../engine/build_workbook.js          # Student Workbook
# (teacher guide / assessment book / organizer toolkit / cover builders as they are added)
```
All builders read unit metadata from `C.unit` (course_name, code, title, standards_range,
perspectives, tn_connection) — course-agnostic, no hardcoded content.

## Render PDF + preflight pagination
```bash
python3 ../engine/render_pdf.py \
    deliverables/Unit1_Student_Workbook_CourseStandard.docx \
    deliverables/Unit1_Student_Workbook_CourseStandard.pdf --pages
```
- Renders via the LibreOffice UNO socket bridge (updates the TOC first), with
  `JAVA_TOOL_OPTIONS` unset for the soffice subprocess (proxy JVM opts hang headless soffice).
- `--pages` prints a **pagination report**: total pages, which page each `Activity`/`Standard`
  header lands on, and **flags any Activity that spans more than one page** (a "bleed").
- **Print-preflight gate:** the report must show `✓ no activity spans more than one page`
  before a packet is released. If an activity bleeds, tighten it in the content JSON
  (shorten the close-read passage) or in the builder (row heights) and re-render.

## Also run the release preflight
```bash
python3 preflight.py    # 11 platinum checks: standards verbatim, no answer leak, de-bias,
                        # citations+alt, crosswalks, disclosures, no source-district label
```

## Assessment banks (no LibreOffice needed)
```bash
python3 ../unit<N>/author_unit<N>_items.py            # or the v2 item generator
python3 ../unit1/assessment_rigor_check.py <bank.json>  # must report 0 flags
```
