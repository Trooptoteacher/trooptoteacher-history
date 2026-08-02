# Spanish Translation Subagent — Ready-to-Use Brief

Copy the template below into a `run_subagent` call when translating textbook narratives. Substitute `{N}` with the unit number.

## Subagent Configuration

- **subagent_type**: `general_purpose`
- **preload_skills**: `["ell-bilingual-review-specialist"]`
- **task_name**: `Translate Unit {N} narratives`

## Objective Template

```
Translate {X} English textbook narratives to Spanish for History Hack Unit {N} (Tennessee U.S. History, high school, Grade 11). Your Spanish must be suitable as primary instructional text for bilingual and ELL learners, not for native-only adult readers.

## INPUT FILES
- /home/user/workspace/hh-eval/translation-work/s1-en.txt
- /home/user/workspace/hh-eval/translation-work/s2-en.txt
- ...
(one per section, write the narrative to a file first before spawning)

## OUTPUT
For each section, write the Spanish translation to:
- /home/user/workspace/hh-eval/translation-work/s{N}-es.txt

DO NOT modify the source JSON. A downstream script will inject translations as narrativeEs fields. Just produce clean UTF-8 Spanish text files with paragraph structure matching the English.

## TRANSLATION REQUIREMENTS (non-negotiable)

1. **PRESERVE ALL STRAND MARKERS EXACTLY** — markers like [Strand: Economics, Geography] must appear in Spanish output in the EXACT same position with EXACT same English text inside brackets. Do NOT translate strand labels. Count before and after to verify.

2. **PRESERVE ALL PROPER NOUNS, DATES, AND STATISTICS**:
   - People: keep English spelling (Abraham Lincoln, Andrew Carnegie, etc.)
   - Place names: standard Spanish forms where they exist (Estados Unidos, Nueva York, Nueva Inglaterra, Misuri)
   - Laws/acts: keep English name + Spanish parenthetical on FIRST mention only
   - Numbers: preserve all dates, acreage, dollar amounts exactly

3. **REGISTER AND READING LEVEL**:
   - Target Grade 10-11 Spanish (Lexile 1000-1100 equivalent)
   - Third-person expository (no direct address)
   - Neutral Latin American Spanish
   - Prefer shorter clearer sentences; one conceptual idea per sentence

4. **STANDARDIZED HISTORICAL TERMINOLOGY** (locked glossary):
   - "formerly enslaved people" → "personas anteriormente esclavizadas"
   - "sharecropping" → "aparcería (sharecropping on first mention)"
   - "Jim Crow laws" → "leyes Jim Crow"
   - "Reconstruction" → "la Reconstrucción"
   - "Gilded Age" → "la Era Dorada (Gilded Age on first mention)"
   - "robber barons" → "barones ladrones"
   - "captains of industry" → "capitanes de la industria"
   - "Great Plains" → "las Grandes Llanuras"
   - "Native Americans" → "los pueblos nativos americanos"
   - "westward expansion" → "la expansión hacia el oeste"
   - "monopoly"/"trust" → "monopolio"/"trust"
   - "vertical integration" → "integración vertical"
   - "nativism" → "el nativismo"
   - "Ellis Island"/"Angel Island" → keep English
   - "disenfranchisement" → "privación del derecho al voto"
   - "poll tax" → "impuesto electoral"
   - "literacy test" → "prueba de alfabetización"
   - Amendments → "13.ª Enmienda", "14.ª Enmienda", etc.

5. **PARAGRAPH STRUCTURE**: One-to-one with English. No merging, splitting, or reordering.

6. **QUOTES**: Translate quoted historical text with "(texto original en inglés)" parenthetical on first appearance.

7. **NO EDITORIALIZING**: Faithful translation, not summary or elaboration.

## WORKFLOW

1. Read each s{X}-en.txt completely. Count [Strand: ...] markers.
2. Translate following all rules. Preserve paragraph breaks.
3. Count [Strand: ...] markers in Spanish — must match.
4. Write s{X}-es.txt.
5. After all done, report:
   - Character count of each Spanish file
   - Strand marker count verification table (EN vs ES)
   - Confirmation all files written

## CRITICAL REMINDERS

- Use `write` or `edit` tool, not bash heredocs
- Primary instructional text — quality over speed
- Longest file typically s4 (~20K chars) — budget accordingly
- Never produce a summary — always full translation
```

## Pre-Subagent Setup (parent agent runs this)

```python
# Extract narratives to files for the subagent
import json, os
os.makedirs('/home/user/workspace/hh-eval/translation-work', exist_ok=True)
with open('public/data/textbook/unit-{N}.json') as f:
    tb = json.load(f)
for s in tb['sections']:
    with open(f'/home/user/workspace/hh-eval/translation-work/{s["id"]}-en.txt', 'w') as f:
        f.write(s['narrative'])
```

## Post-Subagent Injection (parent agent runs this)

```python
# Inject Spanish translations back into JSON and verify strand markers
import json, re
with open('public/data/textbook/unit-{N}.json') as f:
    tb = json.load(f)
pattern = r'\[Strand:[^\]]+\]'
for s in tb['sections']:
    with open(f'/home/user/workspace/hh-eval/translation-work/{s["id"]}-es.txt') as f:
        s['narrativeEs'] = f.read()
    en_count = len(re.findall(pattern, s['narrative']))
    es_count = len(re.findall(pattern, s['narrativeEs']))
    status = "PASS" if en_count == es_count else "FAIL"
    print(f"  {s['id']}: EN={en_count} ES={es_count} [{status}]")
tb['version'] = "{NEW_VERSION}"
tb['lastUpdated'] = "{TODAY}"
with open('public/data/textbook/unit-{N}.json', 'w') as f:
    json.dump(tb, f, indent=2, ensure_ascii=False)
```

## Expected Output Ratios (from Unit 1)

Spanish-to-English character ratio: **1.12× – 1.18×**. Flag if outside this range.
