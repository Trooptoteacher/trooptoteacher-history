# History Hack — repo memory & guardrails

## Canonical banks live in THIS repo (source of truth)
For ANY History Hack deliverable (workbooks, teacher guides, decks, **assessment books**, **graphic
organizer toolkits**, comics, printables) pull primary sources, images, citations, and assessment items
from here — never source ad hoc, never invent a citation.

- **Image primary sources:** `public/data/us-history/primary-sources/images/unit-<N>.json` (116; each has
  `standardIds`, `src`, `alt`/`altEs`, `hostingInstitution`, `rightsLabel`, `rightsStatementVerbatim`,
  `citationChicago`, `commercialUse`, `verifiedAt`).
- **Text primary sources:** `public/data/us-history/primary-sources/unit-<N>.json` (309; HIPP scaffolds, SSP, bilingual).
- **Question / item bank:** `public/data/us-history/questions/unit-<N>/dok-<1..4>.json` (~300/unit; MCQ + CR + DBQ;
  `irtParameters`, `dokRationale`, per-distractor explanations, `reportingCategory`, `tdoeTags`, bilingual).
  Items are **pre-calibration** until field-run — always disclose "classroom-formative · pre-field-test."
- **Image files:** `public/images/textbook/unit-<N>/…`. **Schemas:** `lib/primary-sources/schema.ts`, `lib/question-data`.

## Guardrails (apply to every build)
1. Source of truth only; fabricate nothing. Standards + dimension tags from official standards; "I can"
   learning targets from the instructional guide's right-hand column — **verbatim**. **Never print "WCS."**
2. Answer keys and "What's Next" reteach are teacher-side only.
3. Accessibility: alt text (EN/ES), WCAG AA, ≥9 pt, bilingual, UDL response choice; grayscale-legible in print.
6. **Print-safe images (B&W default).** The interior prints in black-and-white — prefer photographs, engravings,
   and line cartoons (color is decorative, meaning survives grayscale). When color *encodes* meaning
   (choropleth/shaded maps, color-keyed charts), flag the image `colorKey:true`: the build prints a
   "view the full-color version on the projection slide" note, and the color original must live in the deck.
   Never rely on a color-only distinction in a printed page.
7. Deliverables per unit also include a **sale-ready Cover Wrap** (front · spine · back + print/listing spec):
   trademark, copyright, business, ISBN/barcode zone, UDL/MTSS/framework selling copy, trim + spine-width math.
4. De-bias answer positions, synced across all surfaces.
5. Verify by rendering; run the preflight before packaging.

## The platinum system (full memory)
Lives in the Claude skill **`history-hack-course-standard-builder`** and in `HistoryHack_Platinum/`:
- `references/cradle-to-grave-workflow.md` — 6-phase pipeline + gates + agent registry + folder taxonomy.
- `references/prompt-library.md` — ready-to-run Claude prompts (with the guardrail preamble) per phase.
- `references/frameworks-and-item-writing.md` — CER, UDL 3.0, MTSS, HIPPO, C3, SSP, Cornell, Frayer, DOK,
  Bloom, Hattie, Marzano, WIDA, SEL + the full item-writing standard.
- `references/primary-source-bank.md` + `references/primary-source-procurement-validation.md` — the banks + the how.
- `references/handoff-organizer-toolkit-canva.md` — the Canva organizer-toolkit build.
Deliverables per unit: Student Workbook · Teacher Guide · Student Deck · Teacher Deck · **Graphic Organizer
Toolkit** · **Unit Assessment Book** · **Cover Wrap (front/spine/back + listing spec)**. Scaffold a new subject with `scaffold_subject.py`.
Also mirrored to Google Drive.
