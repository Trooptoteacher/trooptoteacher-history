# Sourcing — the APPROVED source of truth (read this first, every unit)

The organizer workbook must be built from the **approved Course Standard (Platinum)** source only.
Getting this wrong mislabels units and pulls the wrong standards. There is exactly one approved source
for unit titles, standard ranges, and learning targets — use it and nothing else.

## 1. Approved source of truth (Google Drive)

**"_LIVE — History Hack — Platinum UDL Master (2026-27)"** is the canonical source for all curriculum
content, standards, and adoption evidence. Inside it:

- **`01_Governance/standard_to_unit_map.json`** — the ONLY approved unit→standard map. Unit titles are
  **verbatim TDOE unit titles**; it defines each unit's standard range. Never re-derive unit titles or
  ranges from anywhere else.
- **Per-unit folders `Unit 1 … Unit 10`** — each holds that unit's Student Workbook, Teacher Edition,
  Assessment Book, and Organizer Toolkit, plus the derived standards content.
- The **"Course Standard (Platinum) Print Sets"** manifest (in the sibling "Print Sets" folder) is a quick
  reference for the 10 units' titles · years · standard ranges (mirror of the map).

The 10 approved units (verbatim from the Course Standard manifest — confirm against
`standard_to_unit_map.json` before printing):

| # | Unit title | Years | Standards |
|---|---|---|---|
| 1 | The Rise of Industrialization | 1877–1900 | US.01–US.07 (7) |
| 2 | The Progressive Era | 1890–1920 | US.08–US.18 (11) |
| 3 | Imperialism & World War I | 1890–1920 | US.19–US.27 (9) |
| 4 | The Roaring Twenties | 1920–1929 | US.28–US.38 (11) |
| 5 | The Great Depression & New Deal | 1929–1941 | US.39–US.44 (6) |
| 6 | World War II | 1939–1945 | US.45–US.58 (14) |
| 7 | The Cold War | 1945–1991 | US.59–US.70 (12) |
| 8 | Postwar America | 1945–1963 | US.71–US.77 (7) |
| 9 | The Civil Rights Movement | 1954–1975 | US.78–US.82 (5) |
| 10 | Modern America | 1965–2016 | US.83–US.95 (13) |

Standards + **"I can" learning targets** are taken **verbatim** from the official state standards /
instructional guide (captured in each unit's `standards_source.json`). Primary sources, images,
citations, and assessment items come from the **History Hack banks** in the `history-hack-web-app` repo
(see the Primary Source & Image Bank Registry). **Fabricate nothing.** Never print the label **"WCS"** in
any student- or teacher-facing product.

The GitHub source that regenerates the Platinum build lives in `trooptoteacher/trooptoteacher-history`,
branch **`claude/unit-5-platinum-pilot-jcubu6`**, path `HistoryHack_Platinum/build_unit1 … build_unit10`
(derive + build scripts and the derived content JSON per unit).

## 2. The Student Workbook Platinum decides WHICH worksheets to produce

**Use the unit's Student Workbook Platinum as the guide for which organizers to make.** Each unit's
workbook runs a **7-activity cycle per standard**: Vocabulary Word Bank · Vocabulary Studio (Frayer) ·
Cornell-notes direct teaching · Close Read · Primary-Source/Data **HIPPO** analysis · Practice Quiz ·
**CER** writing — plus a **Geographer's Lens** on spatially-relevant standards. Read the workbook and:

- Pre-make the organizers the workbook's activities call for (Frayer for Vocabulary Studio, HIPPO for the
  primary-source analysis, CER for the constructed response, a map/matrix for the Geographer's Lens, etc.).
- For each standard, add the **best-fit labeled organizer** for that standard's task, pre-loaded with the
  workbook's own figures, terms, dates, and framing so the organizer, workbook, and slide deck read as one
  product. Match vocabulary and examples to the workbook exactly — don't drift.
- Where the workbook flags a high-impact moment (a DBQ, a signature comparison, a cause-effect chain),
  build a labeled organizer for it.

## 3. Governing guardrails & banks (parent Drive folder)

- **Frameworks & Item-Writing Standards** — CER, UDL 3.0, MTSS, HIPPO/OPTIC, SSP.01–06, DOK. Requirements.
- **Cradle-to-Grave Product Workflow (Platinum)** — the phase pipeline and golden guardrails.
- **Primary Source & Image Bank Registry** — the only approved image/source bank; full citation + rights +
  alt text required; pull from it, never source images ad hoc.

## 4. DO NOT USE — superseded drafts

These predate the Platinum/UDL-MTSS reframe and are **wrong**. Do not read them for unit titles, standard
ranges, or content:

- `03_TEXTBOOK_UNITS/unit-*.html` in this repo (old chapter drafts).
- `07_DEPLOY/unit_standard_map.json` in this repo (old map — its titles and ranges disagree with the
  approved `standard_to_unit_map.json`).
- `05_STANDARDS_ALIGNMENT/*.html`, `01_STUDENT_PACKETS/*` (old scheme).

If you only have access to the repo and not the approved Drive source, **stop and ask** for the approved
`standard_to_unit_map.json` and the unit's Student Workbook Platinum rather than falling back to the drafts.

## Checklist before building a unit
- [ ] Confirm the unit's title + standard range from `standard_to_unit_map.json` (approved).
- [ ] Read the unit's **Student Workbook Platinum**; list the organizers its activities require + the
      high-impact moments to pre-label.
- [ ] Pull verbatim standards + "I can" targets from the unit's `standards_source.json`.
- [ ] Pull any images/primary sources from the History Hack bank (cited); never fabricate.
- [ ] Record each printed fact's source (auditable for TDOE Schedule F adoption).
