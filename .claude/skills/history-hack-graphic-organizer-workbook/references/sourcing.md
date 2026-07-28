# Sourcing — where content comes from, and how to match the student materials

The organizer workbook is **not** a standalone product. It must align with the rest of the U.S. History
Hack ecosystem: the **student workbook chapters**, the **student packets**, and the **student & teacher
slide decks**. The organizers exist to be pre-made for the **high-impact areas** those materials
emphasize, dropped in where they best fit. Sourcing is therefore two jobs: (1) get the *facts* right from
the canonical standards, and (2) *align* to what the unit's student/teacher materials actually teach.

Do this research **before** building. Record the source of every fact you print.

## 1. Canonical standards & per-standard content (the facts)

These files in the repo are the source of truth for what each unit/standard covers. Read them per unit:

- **`07_DEPLOY/unit_standard_map.json`** — the canonical Unit → Standard map (which US.xx standards belong
  to each unit; e.g., Unit 1 = US.REC, US.01–US.07). Start here to know the unit's standard list.
- **`05_STANDARDS_ALIGNMENT/eoc-validation.html`** and **`standards-matrix.html`** — per-standard topic
  lists and EOC alignment (e.g., US.01 = Homestead Act, Transcontinental Railroad, Buffalo Soldiers; US.06
  = Boston/Chicago/NYC/Pittsburgh/San Francisco). These give you the concrete nouns to pre-load onto a
  labeled organizer.
- **`Unit1_Claude_Core/analysis/unit1_content.json`** and **`analysis/tn_standards_source.json`** (per the
  product handoff) — verbatim standards + learning targets + TN connections when available. Treat these
  as canonical when present; they are the authoritative wording.
- The **`history-hack-course-standard-builder`** skill's references (`frameworks-and-item-writing.md`,
  `primary-source-bank.md`, `cradle-to-grave-workflow.md`) — frameworks, the primary-source bank (for
  HIPPO/source-analysis organizers), and the standards workflow.

TN Social Studies Practices (SSP) names, sourced from the teacher-packet docs
(`02_TEACHER_PACKET/`, `05_STANDARDS_ALIGNMENT/`): SSP.01 Collect Information · SSP.02 Critically Examine
Sources · SSP.03 Synthesize Data · SSP.04 Construct & Communicate with Evidence · SSP.05 Develop
Historical Awareness (chronology, cause/effect, change over time) · SSP.06 Develop Geographic Awareness.

## 2. Alignment to the student workbook, packets, and slide decks (the fit)

Read the unit's student-facing materials to learn which moments the curriculum treats as high-impact —
those are exactly where a pre-made organizer belongs. Match vocabulary, figures, and framing to them so a
teacher moving between the slide deck, the workbook, and the organizer sees one coherent product.

- **`03_TEXTBOOK_UNITS/unit-<N>.html`** — the unit chapter / student workbook: its sections, formative &
  summative assessments (e.g., the DBQ), retrieval-practice questions, glossary, and "critical content /
  common misconceptions" notes. The DBQ prompt and the comparison/cause-effect moments it leans on are
  prime candidates for a labeled organizer.
- **`01_STUDENT_PACKETS/`** — `activities.html` (differentiated A/B/C worksheets), `packet-a-skills.html`,
  `packet-b-inquiry.html`, `graphic-organizers.html`, `ell-support.html`, `differentiation-toolkit.html`.
  These show the tasks students actually do and the differentiation language to mirror.
- **Student & teacher slide decks** — these live outside this repo (commonly in Google Drive or built with
  the Gamma connector). Ask the user for the deck link(s) if you don't have them, then read them to match
  the unit's emphasis, section titles, and figure choices. If a deck is unavailable, align to the
  workbook chapter and packets and note the deck wasn't consulted.

**Match, don't drift:** use the same figures, terms, dates, and framing the student materials use. If the
workbook calls them "old vs. new immigrants," the organizer says the same. If the deck highlights a
particular DBQ document, key an organizer to it. Consistency across the workbook, packets, decks, and
organizers is what makes it a *product*, not a pile of files.

## 3. Tennessee connections (sourced only)

Only print a TN tie you can source. Unit 1's came from the standards inventory + instructional guide:
- **US.01 — George Jordan, Williamson County, TN** (Buffalo Soldier, 9th U.S. Cavalry, Medal of Honor);
  confirmed in `05_STANDARDS_ALIGNMENT/eoc-validation.html`.
- **US.03 — T.C.A. § 49-6-1006** (Tennessee law requiring this instruction), per the instructional guide.
Look for each unit's sourced TN people/places/laws the same way; never manufacture one for effect.

## What to capture before building (checklist)

- [ ] Unit's standard list (from `unit_standard_map.json`).
- [ ] Per-standard topics/figures/dates (from eoc-validation / standards-matrix / unit_content JSON).
- [ ] Verbatim learning targets where available.
- [ ] The high-impact moments from the unit chapter + packets + slide decks (what to pre-make).
- [ ] Sourced Tennessee connections for the unit.
- [ ] A note, per printed fact, of which file it came from (so it's auditable for district adoption).
