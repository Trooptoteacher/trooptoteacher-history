# Unit 1 Reference State (v2.4, April 17 2026)

The gold-standard final state of Unit 1. Reference when uncertain about any data structure or to sanity-check a new unit's scope.

## Repo State
- Repo: `Trooptoteacher/history-hack-web-app` (main branch)
- Final commit: `fc91625`
- Textbook version: 2.4
- PDF: `docs/adoption/unit-1-standards-alignment-guide.pdf` (94.1 KB, 14 pages)

## Unit 1 Dimensions
- Sections: 5 (s1–s5)
- Standards: US.01–US.07
- I Can statements: 7
- Total narrative: 66,339 EN chars / 75,625 ES chars (1.14× ratio)
- Total days in pacing: 18
- Cornell notes: 9 (covering US.01–US.05 + US.07)

## Item Banks
- DOK-1: 64 items (including 4 entry-point items US.01-E01, US.02-E01, US.04-E01, US.06-E01)
- DOK-2: (unchanged)
- DOK-3: 95 items (18 with stimulus field, C3 distribution D3=58 / D4=25)

## differentiationPlan Schema (canonical)
```json
{
  "differentiationPlan": {
    "description": "...",
    "ellSupport": { ... },
    "tier1Universal": [ /* 5 strategies */ ],
    "tier2Targeted": [ /* 5 strategies */ ],
    "section504Accommodations": {
      "strategies": [ /* 6 */ ],
      "keyDistinction": "..."
    },
    "tier3Intensive": {
      "strategies": [ ... ],
      "accommodationsCrosswalk": {
        "accommodations": [ /* 10 entries */ ]
      }
    },
    "extensionsAdvanced": {
      "strategies": [ /* 5, including C3 D4 civic action */ ]
    },
    "tdoeAlignment": { ... },
    "honorsAcceleration": {
      "strategies": [ /* 5 */ ],
      "distinctionFromExtensions": "..."
    },
    "standaloneReasoningActivities": {
      "economicReasoning": [ /* 2 */ ],
      "geographicReasoning": [ /* 2 */ ],
      "tdoeAlignmentNote": "..."
    }
  }
}
```

## Graphic Organizers (public/printables/unit-1/)
- `cause-effect-organizer.html`
- `sapa-primary-source-organizer.html`
- `timeline-reconstruction-to-gilded-age.html`
- `venn-old-vs-new-immigrants.html`

## C3 Dimension 4 Extension (template)
**Title**: "Policy Memo from 1882 to Today"
**Pattern**: Students analyze a historical primary source on discriminatory policy (Chinese Exclusion Act) and draft a 2-page policy memo to a current legislator connecting the historical reasoning to a modern immigration policy question.

## Honors Acceleration Strategies (5)
1. Compacting — pre-test out of known content
2. Independent research project aligned to unit standard
3. Cross-disciplinary synthesis (e.g., economics + history + geography)
4. Peer teaching / reciprocal teaching leadership
5. Primary source original research (archives / local history)

## Pacing Guide (Unit 1 excerpt)
```
{
  "unit": 1,
  "title": "The Rise of Industrialization",
  "standards": "US.01–US.07",
  "reportingCategory": "RC1",
  "totalDays": 18,
  "sections": [
    {"section": "s1", "standards": ["US.01"], "days": 3, "dayBreakdown": [...]},
    {"section": "s2", "standards": ["US.02"], "days": 3, "dayBreakdown": [...]},
    {"section": "s3", "standards": ["US.03"], "days": 3, "dayBreakdown": [...]},
    {"section": "s4", "standards": ["US.04","US.05"], "days": 4, "dayBreakdown": [...]},
    {"section": "s5", "standards": ["US.06","US.07"], "days": 4, "dayBreakdown": [...]}
  ]
}
```

## Known Deferred Items (not blocking Schedule F)
- 16 cross-unit vocabulary duplicate IDs (needs user decision on refactor)
- US.06 Cornell note (gap but not flagged critical)
- Older DOK-1 items have empty `stemEs` stubs (most items, pending bulk translation pass)

## Commit Trail
1. Prior session: `69f9b0b` — Critical 1-3 + 6a/6b/6e
2. Medium batch: `71321e3` — 6c/6f/6g (stimulus, Cornell, D2→D3/D4 retags)
3. PDF rebuild: `ea3aaf7`
4. Low batch: `192c143` — entry-point items + standalone econ/geo activities
5. Spanish narratives: `fc91625` — 6d narrativeEs on all 5 sections

Each band commit followed by push to `origin/main`.
