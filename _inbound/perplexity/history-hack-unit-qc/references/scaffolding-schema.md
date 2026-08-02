# Unit 1 In-Text Scaffolding Marker Schema (v1.1)

**Purpose**: Define inline markers for embedded differentiation, SSP tracing, vocabulary support, and chunked retrieval in History Hack U.S. History textbook narratives.

**Design principles**:
1. **Render-agnostic** — markers are valid text until a renderer is built; never break existing UI
2. **Parallel to existing `[Strand: ...]`** — same bracket syntax, same insertion rules
3. **Language-parity required** — every marker in English MUST appear in matching position in Spanish
4. **Minimal surface** — 6 marker types total, no nesting, no complex syntax

---

## Marker Types

### 1. `[[Vocab]]` or `[[narrative|canonical]]` — Double-bracket Vocabulary Highlight

**Purpose**: Trigger click-to-define popup with Spanish translation, audio, Tier 2/3 simplified definition.

**Two syntaxes (GOLD STANDARD, v1.1)**:

**Syntax A — simple wrap** (when narrative text == canonical vocab term):
```
[[Homestead Act]]
```
The wrapped text IS the canonical key used to look up the vocab entry in `data/vocabulary.ts`.

**Syntax B — pipe-alias** (when narrative text differs from canonical vocab term):
```
[[narrative_form|canonical_vocab_term]]
```
The text BEFORE the pipe is the exact narrative phrase (preserves case, pluralization, original wording). The text AFTER the pipe is the canonical key the renderer uses to resolve the vocab entry.

**When to use pipe-alias**:
- Narrative uses a shortened form: `[[Jim Crow|Jim Crow Laws]]`
- Spanish narrative keeps the English proper noun but vocab entry is Spanish: `[[Ellis Island|Isla Ellis]]`, `[[Angel Island|Isla Angel]]`
- Narrative uses a synonym or common phrasing: `[[ethnic neighborhoods|Ethnic Clusters]]`
- Narrative is a plural or inflected form of a singular canonical entry: `[[sharecroppers|Sharecropping]]`

**Rules**:
- Wraps the exact term as it appears in the narrative — NEVER modify the narrative text
- First occurrence in each section (per canonical key) gets wrapped; subsequent occurrences are bare
- Term text before pipe is never modified (preserves case, pluralization, accents)
- Canonical key after pipe must match a `term` or `termEs` field in `data/vocabulary.ts`
- The renderer MUST support both syntaxes — parse `[[X|Y]]` as narrative=X, canonical=Y; parse `[[Z]]` as narrative=canonical=Z

**Example**:
```
English: The [[Homestead Act]] of 1862 offered settlers 160 acres... Later, [[Jim Crow|Jim Crow Laws]] codified segregation.
Spanish: La [[Homestead Act]] de 1862 ofreció a los colonos 160 acres... Los inmigrantes llegaban a [[Ellis Island|Isla Ellis]].
```

---

### 2. `[SSP: N,M]` — Social Studies Practice Marker

**Purpose**: Tag where specific SSPs are actively modeled in the prose for reviewer trace and teacher pedagogy.

**Rules**:
- Placed immediately after the sentence or clause where the practice is demonstrated
- SSP numbers 1-6 (TN Social Studies Practices)
  - SSP.1: Gather information from primary/secondary sources
  - SSP.2: Evaluate source credibility and perspective
  - SSP.3: Synthesize information from multiple sources
  - SSP.4: Construct and communicate arguments
  - SSP.5: Develop historical awareness
  - SSP.6: Develop cultural awareness
- 1-2 SSPs per marker max (comma-separated, no spaces)
- Approximately 1 marker per 2-3 paragraphs — do not over-tag
- English and Spanish markers are IDENTICAL (same numbers, same positions)

**Example**:
```
English: The Homestead Act's promise of free land drew settlers from Scandinavia, Germany, and Ireland, fundamentally reshaping the cultural geography of the Great Plains. [SSP: 5,6]
Spanish: La promesa de tierra gratuita de la Homestead Act atrajo a colonos de Escandinavia, Alemania e Irlanda, transformando fundamentalmente la geografía cultural de las Grandes Llanuras. [SSP: 5,6]
```

---

### 3. `[CHUNK: Quick Check — question]` — Chunk Break + Retrieval Prompt

**Purpose**: Break long passages into digestible units with embedded retrieval practice (Rosenshine Principle 1, 6; Roediger & Karpicke testing effect).

**Rules**:
- Placed between sub-topics within a section (2-4 per section typical)
- Format: `[CHUNK: Quick Check — {question text}]`
- Question is 10-20 words, answerable from preceding 2-4 paragraphs
- Answerable at DOK 1 or DOK 2 (recall or basic reasoning)
- Spanish version translates the question but keeps `[CHUNK: Quick Check — ]` wrapper identical
- Acts as a visual + cognitive pause for all learners; Tier 2/3 students may answer aloud before proceeding

**Example**:
```
English: [CHUNK: Quick Check — What three conditions did settlers have to meet to claim Homestead Act land?]
Spanish: [CHUNK: Quick Check — ¿Qué tres condiciones tenían que cumplir los colonos para reclamar tierras bajo la Homestead Act?]
```

---

### 4. `[SUMMARY-L1L3: text]` and `[SUMMARY-L4L6: text]` — Tiered Summary Anchors

**Purpose**: Banded summaries at sub-section and section level so WIDA L1-L3 students get simplified recap while L4-L6 students get denser synthesis. Aligns to WIDA ELD Standards Framework 2020 and UDL Principle 1 (multiple means of representation).

**Rules**:
- Two anchors always appear as a pair
- L1L3: 1-2 sentences, 15-25 words, simple SVO structures, concrete nouns
- L4L6: 1-2 sentences, 25-40 words, academic vocabulary, complex-compound structures
- Placed at the end of each sub-topic cluster (2-4 pairs per section)
- Spanish versions must match L1L3/L4L6 register distinctions
- Stays within the same paragraph break structure

**Example**:
```
English:
[SUMMARY-L1L3: The Homestead Act gave settlers 160 acres of free land. They had to live on the land and farm it for five years.]
[SUMMARY-L4L6: The Homestead Act of 1862 accelerated westward expansion by offering 160 acres to any citizen or prospective citizen who agreed to reside on and improve the land for five years.]

Spanish:
[SUMMARY-L1L3: La Homestead Act dio a los colonos 160 acres de tierra gratuita. Tenían que vivir en la tierra y cultivarla por cinco años.]
[SUMMARY-L4L6: La Homestead Act de 1862 aceleró la expansión hacia el oeste al ofrecer 160 acres a cualquier ciudadano o aspirante a ciudadano que aceptara residir y mejorar la tierra durante cinco años.]
```

---

### 5. `[PROMPT: question]` — Pause-and-Reflect Prompt

**Purpose**: Trigger brief metacognitive reflection after complex or emotionally weighty passages. Aligned to Rosenshine Principle 7 (obtain high success rate) and culturally responsive pedagogy.

**Rules**:
- Placed after paragraphs involving ethical weight, perspective-taking, or analytical complexity
- 1-2 per section max — reserve for genuine reflection moments
- Question is open-ended, no single right answer
- 10-25 words
- Spanish version translates verbatim

**Example**:
```
English: [PROMPT: Think about the word "displacement." What does it mean to be removed from a place that your ancestors have lived for generations?]
Spanish: [PROMPT: Piensa en la palabra "desplazamiento". ¿Qué significa ser removido de un lugar donde tus antepasados han vivido durante generaciones?]
```

---

### 6. `[CONTEXT: setup text]` — Primary Source Pre-Reading

**Purpose**: 2-3 sentence pre-reading context before quoted primary sources, so all learners can access the source cognitively. Mayer multimedia learning principle (pre-training).

**Rules**:
- Placed immediately BEFORE any primary source quotation in the narrative
- 2-3 sentences, 30-60 words
- Provides: author's background + date/occasion + why the source matters
- Spanish version translated verbatim

**Example**:
```
English: [CONTEXT: In 1889, Andrew Carnegie — one of the wealthiest industrialists of the Gilded Age — published "The Gospel of Wealth," an essay arguing that wealthy people had a moral obligation to use their fortunes for the public good. Read his words carefully and consider who he leaves out of his argument.]

"The problem of our age is the proper administration of wealth..."
```

---

## Marker Placement Rules

1. **Marker density cap**: No more than 3 markers in any single paragraph
2. **Order when adjacent**: `[[Vocab]]` is inline; `[Strand: ...]` and `[SSP: ...]` follow the clause; `[CHUNK]`, `[PROMPT]`, `[CONTEXT]` appear on their own line; `[SUMMARY-L1L3]` and `[SUMMARY-L4L6]` appear as a paired block on their own lines.
3. **Nesting exception**: `[[vocab]]` MAY appear inside `[SUMMARY-L1L3: ...]` or `[SUMMARY-L4L6: ...]` blocks. Parsers must use bracket-depth-aware block extraction (see `reconstruct4.py` `_strip_block()`). No other nesting is allowed.
4. **EN-ES parity**: Every marker in English MUST appear in the matching position in Spanish (except `[[Vocab]]` first-occurrence rule).
5. **NARRATIVE TEXT UNCHANGED (CRITICAL)**: Stripping all markers (including pipe-alias `|canonical` portions) from the scaffolded text MUST produce byte-identical output to the original narrative. Verify with `reconstruct4.py`.

## JSON Schema Impact

No JSON schema changes needed. All markers are inline text within the `narrative` and `narrativeEs` string fields. A future renderer parses them via regex.

### Renderer parsing pseudocode

```
# Vocab (handle both syntaxes)
for match in re.finditer(r'\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]', narrative):
    display_text = match.group(1)
    canonical = match.group(2) or match.group(1)
    vocab_entry = vocabulary.lookup(canonical)  # try term, then termEs
    render_as_clickable(display_text, vocab_entry)

# Other markers — own-line or trailing-clause extraction
# [SSP: N,M], [CHUNK: ...], [SUMMARY-L1L3: ...], [SUMMARY-L4L6: ...], [PROMPT: ...], [CONTEXT: ...]
```

## Counting/Validation

Per section, expected marker counts:
| Marker | s1 (8,978 ch) | s4 (20,535 ch) |
|---|---|---|
| `[[Vocab]]` first-occurrence | 5-10 | 12-18 |
| `[SSP: ...]` | 3-5 | 7-10 |
| `[CHUNK: Quick Check]` | 2-3 | 4-5 |
| `[SUMMARY-L1L3]` + `[SUMMARY-L4L6]` pairs | 2-3 pairs | 4-5 pairs |
| `[PROMPT: ...]` | 1-2 | 1-2 |
| `[CONTEXT: ...]` | 0-2 | 1-3 |

Validation script verifies EN marker count = ES marker count for each type.

## Version History

- **v1.0** (2026-04-17): Initial 6-marker schema
- **v1.1** (2026-04-17): Added pipe-alias vocab syntax `[[narrative|canonical]]` for narrative/canonical mismatches. Applied to Unit 1 (textbook v2.5). All v3 files verified byte-equal to originals via `reconstruct4.py`.
