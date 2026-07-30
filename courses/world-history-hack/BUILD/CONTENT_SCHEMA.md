# Content JSON contract (what the engines consume)

Each unit's `BUILD/unitN/analysis/unitN_content.json` is the source of truth for every generator.
Field names below are the **exact** keys `build_workbook.js` (and siblings) read — match them precisely.

```jsonc
{
  "unit": {
    "code": "Unit 7",                       // "Unit N"
    "title": "World War I",
    "brand": "World History Hack",          // REQUIRED (else builder falls back to a Gov string)
    "course_name": "World History & Geography",
    "standards_range": "W.29–W.38",
    "quarter": "Q2",
    "suggested_days": 12,
    "essential_question": "…",
    "cover_era": "1910s–1920s",
    "cover_title_lines": ["World War I"],
    "cover_image": "W.31_somme-trench.jpg",
    "tn_connection_label": "TENNESSEE CONNECTION",
    "tn_connection": "…real TN tie or ''…",
    "tn_connection_task": "…World-History-appropriate task (override the Gov default)…",
    "perspectives_title": "Multiple Perspectives",
    "perspectives_intro": "…",
    "publisher": "TroopToTeacher Technologies LLC",
    "footer": "…",
    "frameworks": { "udl_designed_in": true, "mtss": true },
    "belief_check": "…", "play": "…", "spiral": "…", "discussion_norms": ["…"]
  },
  "order": ["W.29","W.30", "…"],             // standard codes, teaching order
  "standards": {
    "W.29": {
      "title": "…short teaching title…",
      "standard": "…VERBATIM state text…",
      "ican": "…primary I-can (string; builder strips leading 'I can ')…",
      "targets": ["…","…"],                  // learning targets (array); or "target" (string)
      "vocab": [ {"term":"…","say":"…","es":"…","def":"…"} ],   // EN/ES + pronunciation
      "sources": [ {"title":"…","who":"…","date":"…","repo":"…","url":"…","quote":"…"} ],
      "cfu": { "stem":"…", "options":{"A":"…","B":"…","C":"…","D":"…"}, "dok":2, "key":"C" },  // key TEACHER-SIDE; debias A/B/C/D across standards
      "cues": ["…Cornell cue questions…"],
      "hook": "…provocative, standard-specific question…",
      "lenses": ["…C/E/G/H/P analytical lenses…"],
      "ref": { "range": "W.29" },
      "ssp_focus": "SSP.02",
      "tn_connection": "…only where genuinely part of the standard…",
      "auth": {                              // activity pack (a = s.auth)
        "frayer": ["term1","term2"],         // terms to Frayer-model
        "close": { "passage":"…authored close-read (label as WHH-authored synthesis)…", "lexile":"…" },
        "tdq": ["…text-dependent questions…"],
        "quiz": [ {"stem":"…","opts":{"A":"…","B":"…","C":"…","D":"…"},"key":"B","dok":2} ],
        "cer": { "prompt":"…", "frames":["…sentence/argument frames…"] }
      },
      "geo": "…geographic hook where G-dimension…"
    }
  }
}
```

Notes:
- `s.auth` (a.k.a. the activity pack) drives Close Read, Frayer, Practice Quiz, CER. `s.vocab`, `s.cfu`,
  `s.cues`, `s.hook`, `s.sources` drive the other activities → the **seven-activity cycle** per standard.
- Keys (`cfu.key`, `auth.quiz[].key`) are TEACHER-SIDE; never surface them in student output.
- `sources[]` maps to the Phase-2 bank (`primary_source_sourcing.json`); `url`=page_url, cite repo+rights.

## ⚠️ Engine de-leak required before rendering World History docx/PDF (Phase 5–7 prerequisite)
The copied builders bake in Government-course text that must be parameterized from `U.*` (geometry stays
untouched). Rendered-output leaks to fix (NOT the harmless `.js` comments):
- `build_workbook.js` L153 "UNITED STATES GOVERNMENT & CIVICS (GC) …", L159/L173 "Tennessee U.S.
  Government & Civics Standards", L420 "Civics"; fallbacks L12/L14 → neutral.
- `build_cover.js` — pervasive ("GOVERNMENT HACK", "Government & Civics", "Foundations of Constitutional
  Government", "GC"): parameterize the whole cover from `U.*`.
- `build_organizer_toolkit.js` — "GC" reporting-category labels + "Government Hack" footer → drive from `U.*` / RC-WH{N}.
- `build_assessment_book.js` L40/L45, `build_teacher_guide.js` L133 → `U.*`.
Verify: render a unit, strip base64, grep `word/*.xml` for the forbidden strings → 0 hits.
