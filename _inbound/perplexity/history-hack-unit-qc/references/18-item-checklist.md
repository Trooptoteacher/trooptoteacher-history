# The 18-Item QC Checklist — Full Spec

Reference for every item in the Schedule F QC workflow. Each entry includes: file path, JSON pattern, verification rule, and common pitfalls observed during Unit 1 QC.

---

## Critical Items (3)

### C1. Standards Alignment Guide PDF

**File**: `docs/adoption/unit-{N}-standards-alignment-guide.pdf`
**Builder**: `/home/user/workspace/hh-eval/build_alignment_guide.py`
**Pages**: 14 (~94 KB)
**Format**: ReportLab, TDOE Schedule F reviewer-facing
**Sections required**:
- Cover page with unit title, standards range, version, date
- Standards overview (US.XX–US.YY listed with category tags C/E/G/H/P)
- Section-by-section standards alignment table
- SSP alignment matrix
- DOK distribution chart (bar chart from item bank data)
- Five-band differentiation summary
- Cornell notes index
- C3 Framework dimension coverage
- Primary sources list
- TDOE Table 3 rubric trace

**Verification**: PDF builds without errors, file size 80-110 KB, all data values pulled from live JSON (not hardcoded).

**Data bundle**: Builder reads `/tmp/hh-pdf/alignment-data.json` or builds directly from `public/data/...` files.

---

### C2. Vocabulary Boundary Leaks

**File**: `data/vocabulary.ts`
**Pattern**: TypeScript array of `{id, term, definition, unit, ...}` objects

**Audit query**:
```python
# Find vocab terms whose content maps to a different unit than their `unit` field
# Common leak: term introduced in Unit N narrative but tagged `unit: 'unit-{M}'`
```

**Fix**: Flip `unit` field on mistagged terms. On Unit 1, found 15 terms incorrectly tagged `unit-1` that belonged in `unit-2`.

**Verification**: After fix, re-run audit. All terms' `unit` field should match the section where they are first introduced.

**Also check for duplicate IDs** across units (Unit 1 had 16 cross-unit duplicates — flag these but do NOT fix unless user approves cross-unit refactor).

---

### C3. I Can ↔ Textbook Section Linking

**Files**:
- `public/data/ican/unit-{N}.json` — add `textbookSectionId` to each statement
- `public/data/textbook/unit-{N}.json` — add `icanStatementIds` array to each section

**Pattern**:
```json
// ican/unit-N.json statement
{
  "id": "ican-usXX",
  "statement": "I can...",
  "standardCode": "US.XX",
  "textbookSectionId": "s2",   // NEW
  ...
}

// textbook/unit-N.json section
{
  "id": "s2",
  "title": "...",
  "standardCodes": ["US.02"],
  "icanStatementIds": ["ican-us02", "ican-us02b"],  // NEW
  ...
}
```

**Verification**: Every I Can statement references a valid `sectionId`, every section lists its I Can IDs. Cross-reference is bidirectional and complete.

---

## High Items (5) — Differentiation Depth

### H4. WIDA Sentence Frames on I Can Statements

**File**: `public/data/ican/unit-{N}.json`
**Pattern**:
```json
{
  "id": "ican-usXX",
  "sentenceFrames": {
    "L1L2": "The ___ is ___.",
    "L3L4": "The ___ was important because ___.",
    "L5L6": "The ___ contributed to ___ by ___, which led to ___."
  }
}
```

**Every I Can statement gets 3 frames banded by WIDA ELD level.** Unit 1 has 7 I Can statements × 3 frames = 21 frames.

---

### H5. Printable Graphic Organizers

**Location**: `public/printables/unit-{N}/`
**Format**: Standalone HTML files with print-optimized CSS
**Required for Unit 1** (adapt for other units as standards demand):
- `cause-effect-organizer.html` — multi-cause single-effect fishbone style
- `sapa-primary-source-organizer.html` — Sourcing, Analysis, Perspective, Argumentation
- `timeline-{unit-theme}.html` — era-specific timeline (e.g., Reconstruction→Gilded Age)
- `venn-{compare-contrast-topic}.html` — two-circle compare/contrast

**Pattern**: Each HTML file has:
- `<title>` with unit + organizer name
- Inline CSS with `@media print` rules for letter-size printing
- Student-fillable fields (wide lines, labeled sections)
- Teacher answer key at the bottom (hidden with `.teacher-only` class)

**Verification**: Open each in headless Chrome and confirm print layout at letter size.

---

### H6. IEP/504 Accommodations Crosswalk

**File**: `public/data/textbook/unit-{N}.json`
**Path**: `differentiationPlan.tier3Intensive.accommodationsCrosswalk.accommodations`
**Pattern**: Array of 10 entries:
```json
{
  "accommodation": "Extended time (1.5x)",
  "iepCategory": "Timing/Scheduling",
  "standardAlignment": "Applies to all US.{N} items",
  "implementation": "Provide extended time on all formative assessments and the summative.",
  "tdoeIndicator": "Table 3, 3.3"
}
```

10 entries typical: extended time, chunked assignments, preferential seating, read-aloud, graphic organizer provided, reduced answer choices, word bank, frequent breaks, digital text, audio support.

---

### H7. 504 Band Between Tier 2 and Tier 3

**File**: `public/data/textbook/unit-{N}.json`
**Path**: `differentiationPlan.section504Accommodations`
**Pattern**:
```json
{
  "section504Accommodations": {
    "description": "...",
    "strategies": [
      {"strategy": "...", "implementation": "...", "indicator": "..."},
      // 6 strategies typical
    ],
    "keyDistinction": "Unlike Tier 3 intensive, 504 accommodations remove barriers without modifying curriculum content. Students access the same instructional objectives with adjusted environmental or procedural supports."
  }
}
```

**`keyDistinction` field is REQUIRED** — distinguishes 504 from Tier 3 for TDOE reviewers.

---

### H8. C3 Dimension 4 Civic-Action Extension

**File**: `public/data/textbook/unit-{N}.json`
**Path**: `differentiationPlan.extensionsAdvanced.strategies`
**Pattern**: Add one strategy with full C3 metadata:
```json
{
  "strategy": "C3 Dimension 4: Taking Informed Action — '{Unit-Specific Civic Action}'",
  "implementation": "Students ... [full task description]",
  "c3Dimension": "D4",
  "ssp": ["SSP.3", "SSP.5", "SSP.6"],
  "standards": ["US.XX"],
  "duration": "2-3 class periods"
}
```

Unit 1 example: "Policy Memo from 1882 to Today" — students connect Chinese Exclusion Act analysis to modern immigration policy and write a policy memo to their representative.

Every unit must have at least ONE D4 extension.

---

## Medium Items (5-6)

### M9. Spanish `readingContentEs` on I Can

**File**: `public/data/ican/unit-{N}.json`
**Pattern**: For each statement, add `readingContentEs` mirroring the English `readingContent`:
```json
{
  "id": "ican-usXX",
  "statement": "I can...",
  "statementEs": "Puedo...",
  "readingContent": "...",
  "readingContentEs": "..."
}
```

**Quality**: Latin American neutral Spanish, Grade 10-11 level, preserve proper nouns.

---

### M10. Stimulus Field on Document-Based DOK-3 Items

**File**: `public/data/questions/unit-{N}/dok-3.json`
**Pattern**: Every item with primary source content must have:
```json
{
  "id": "US.XX-Q...",
  "stimulus": {
    "type": "primary_source",
    "citation": "Author, Title, Date. Collection.",
    "text": "Full quoted passage..."
  },
  "stem": "Based on the excerpt above, ..."
}
```

**Audit**: Items whose stem references "the excerpt", "the passage", "the source", or "the document" but lack `stimulus` field. On Unit 1 found 18 such items.

---

### M11. DOK-3 Retagging (D2 → D3/D4)

**File**: `public/data/questions/unit-{N}/dok-3.json`
**Pattern**: Audit items tagged `c3Dimension: "D2"` that are actually asking students to evaluate, corroborate, or argue from evidence.
- Analysis of sources → `D3`
- Action/policy recommendation → `D4`

On Unit 1 found 16 mistagged items. Use `scripts/fix_dok3_bank.py` as a template.

---

### M12. Cornell Notes Coverage

**File**: `lib/cornell-notes-data.ts`
**Pattern**: Each standard in the unit should have at least one Cornell note entry:
```typescript
{
  id: 'us-NN',
  title: 'Topic',
  standardCode: 'US.XX',
  cues: [...],
  notes: [...],
  summary: '...'
}
```

**Coverage target**: All unit standards covered. Unit 1 ended with 9 notes covering US.01–US.05 + US.07 (US.06 noted as gap but not flagged critical).

---

### M13. Honors Acceleration Track

**File**: `public/data/textbook/unit-{N}.json`
**Path**: `differentiationPlan.honorsAcceleration`
**Pattern**:
```json
{
  "honorsAcceleration": {
    "description": "...",
    "strategies": [
      {"strategy": "...", "implementation": "...", "duration": "..."},
      // 5 strategies typical
    ],
    "distinctionFromExtensions": "Honors acceleration replaces regular coursework for advanced learners rather than adding to it..."
  }
}
```

**`distinctionFromExtensions` is REQUIRED** — differentiates honors from extensions.

---

### M13b. Spanish `narrativeEs` on Textbook Sections

**File**: `public/data/textbook/unit-{N}.json`
**Pattern**: Each section gets a `narrativeEs` field next to `narrative`:
```json
{
  "id": "sN",
  "narrative": "English text...",
  "narrativeEs": "Spanish text..."
}
```

**This is the most expensive item** — full narrative translation (~12K words on Unit 1). Spawn a dedicated translation subagent. See `translation-subagent-brief.md`.

**Strand markers MUST be preserved verbatim** (`[Strand: Economics, Geography]` etc.) — do NOT translate the bracketed content.

---

## Low Items (5)

### L14. Boundary Vocabulary `ellSupportNote`

**File**: `data/vocabulary.ts`
**Pattern**: For high-frequency / cross-unit terms, add `ellSupportNote` with etymology anchor:
```typescript
{
  id: 'vocab-reconstruction',
  term: 'Reconstruction',
  definition: '...',
  ellSupportNote: 'Reconstruction was the effort after the Civil War (1865–1877) to rebuild the South... Remember: to reconstruct means to build again.',
  ...
}
```

Pick 3-5 most important cross-unit terms per unit.

---

### L15. DOK-1 Tier 2/3 Entry-Point Items

**File**: `public/data/questions/unit-{N}/dok-1.json`
**Count**: 3-4 new items per unit
**Pattern**:
```json
{
  "id": "US.XX-E01",
  "stem": "...simplified stem...",
  "stemEs": "...Spanish stem...",
  "itemType": "mcq",
  "correctAnswer": "...",
  "explanation": "...",
  "explanationEs": "...",
  "difficultyEstimate": "entry",
  "dokLevel": 1,
  "standardCodes": ["US.XX"],
  "choices": [...],
  "irtParameters": {"a": 1.0, "b": -1.5, "c": 0.2},
  "instructionalPurpose": "tier23_entry_point",
  "tier2Entry": true,
  "tier3Entry": true,
  "scaffolds": {
    "simplifiedLanguage": true,
    "chunkedStem": true,
    "wordBank": false,
    "wida": "L1-L3"
  }
}
```

**Characteristics**:
- Low IRT difficulty (b between -1.5 and -1.8)
- Stem pre-teaches the key concept or vocabulary
- 4 short options
- Full English + Spanish

---

### L16. SSP Codes on Extension Strategies

**File**: `public/data/textbook/unit-{N}.json`
**Path**: `differentiationPlan.extensionsAdvanced.strategies[*]`
**Pattern**: Every strategy must have an `ssp` array:
```json
{
  "strategy": "...",
  "implementation": "...",
  "ssp": ["SSP.3", "SSP.5"]
}
```

**Audit**: Count strategies without `ssp` field. Unit 1 ended with 5/5 tagged.

---

### L17. Standalone Economic + Geographic Reasoning Activities

**File**: `public/data/textbook/unit-{N}.json`
**Path**: `differentiationPlan.standaloneReasoningActivities`
**Pattern**:
```json
{
  "standaloneReasoningActivities": {
    "description": "...",
    "economicReasoning": [
      {
        "id": "econ-uN-01",
        "title": "...",
        "standards": ["US.XX"],
        "tdoeIndicator": "Table 3, 3.6",
        "c3Dimension": "D2",
        "duration": "35-45 minutes",
        "task": "...",
        "deliverable": "...",
        "scaffolds": {
          "tier2": "...",
          "tier3": "...",
          "section504": "...",
          "extensions": "..."
        },
        "assessment": "..."
      },
      // 2 total
    ],
    "geographicReasoning": [
      // same structure, 2 total
    ],
    "implementationNote": "...",
    "tdoeAlignmentNote": "Satisfies TDOE Textbook Commission Scoring Rubric Table 3, Indicator 3.6 (economic reasoning) and Indicator 3.7 (geographic reasoning)..."
  }
}
```

**Required**: 2 econ + 2 geo per unit.

---

### L18. Pacing Guide Audit

**File**: `public/data/pacing-guide.json`
**Path**: `units[{N-1}]`
**Check**:
- `totalDays` matches sum of `sections[*].days`
- Every unit standard (US.XX–US.YY) appears in at least one section's `standards` array
- Every section has `dayBreakdown` with per-day descriptions referencing specific activities, vocabulary, and CFU checks

**Unit 1 ended**: 18 days total, all 7 standards (US.01–US.07) covered, 5 sections with complete dayBreakdown arrays.

If any gaps exist, fill them with the same format as the Unit 1 sections (see `unit-1-reference-state.md`).
