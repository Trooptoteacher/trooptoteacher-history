# Practice-quiz sourcing from the authoritative bank

The Activity 6 practice quizzes must be **standard-aligned and historically correct**. The
auto-assembled quizzes shipped with the workbook were unreliable (off-topic / mis-standardized
items, only 3 per standard). Rebuild them from the authoritative bank.

## The bank
Repo: `history-hack-web-app` (attach via `add_repo` + shallow clone if not in session).
Path: `public/data/us-history/questions/unit-N/dok-{1,2,3}.json` — ~4,760 items total, each with:
`id, stem, stemEs, itemType (mcq), bankTier (student), correctAnswer, choices[{id,text,textEs}],
dokLevel, difficultyEstimate, irtParameters, distractorTags, standardCodes, explanation`.

## CRITICAL: the bank's `standardCodes` use an OLDER numbering — match by CONTENT, not code
The bank's `US.46` items are New Deal / court-packing; its `US.57` mixes UN and Vietnam. Do **not**
select by `standardCodes`. Instead:
1. Load all MCQ, student-tier, 4-choice items across all units.
2. For each workbook standard, define **tight content keywords + exclusions** (kill cross-era
   homonyms: "Eisenhower's presidency", "1920s women", "Iron Curtain", "SDI", "Vietnam").
3. **Read the candidates** and hand-verify each is on the correct WWII sub-topic and era.
4. Pick 4 with a DOK spread (e.g., 1·2·2·3). Use the bank's `correctAnswer` verbatim.
- The genuine WWII items cluster under bank ids `us-40…us-45`, `q-us45…q-us58` (with `-b`/`-u6`
  suffixes marking the WWII items inside otherwise-New-Deal families), and `U6-…`, `dok3-gen-u6-…`.
- Gaps happen (Unit 6 had no clean "WWII leaders" family for US.49) — search broadly
  (`Eisenhower`+`d-day`, `Marshall`, `MacArthur`+`Pacific`) and verify; if the bank truly lacks
  items, author fact-checked ones and **say so** — never silently.

## Selection sketch
```python
import json, glob
items=[]
for f in glob.glob('public/data/us-history/questions/unit-*/dok-*.json'):
    items += json.load(open(f))['questions']
mc=[q for q in items if q.get('itemType')=='mcq' and q.get('bankTier')=='student' and len(q.get('choices',[]))==4]
# keyword include/exclude per workbook standard -> read candidates -> hand-pick 4 by id.
# Persist final picks as {code: [{id,dok,stem,choices{A..D},ans,explanation}]}.
```

## Building the quiz into the workbook
Clone the reference exemplar's Activity 6 item block (tag paragraph, question paragraph, A–D
option paragraphs) and its answer-key block, then fill text. Per standard:
- Remove the old items between the RESPONSE CHOICE intro table and the Activity 7 header.
- Insert 4 items: `[DOK n · item <id>]`, `n. <stem>`, `A.–D. <choice>`.
- Add the on-page self-check key: `CHECK YOURSELF — quiz answer key` /
  `Commit your answers first, then check:  1. X  2. Y  3. Z  4. W` / `Missed one? Reread…`.
- Keep the locked reference standard's quiz as-is (it's already aligned).

## Exit-ticket keys (for the Teacher Guide)
Exit-ticket items live in the workbook (one per standard). Their distractors carry hedging
"tells" ("which contradicts the primary source…", "lacks supporting historical evidence"); the
**correct answer is the single substantive, non-hedged option**. Detect it by filtering out hedged
options, then **verify each against the historical record** before publishing the key.
