# UDL 3.0 Salvage Workflow

For teams with existing curriculum products they need to UDL-align without throwing them out.

## When to Use This Workflow

- Existing product line has been shipped and needs UDL retrofit
- Product line is generated from a source engine + content files (like History Hack) — content lives in source, not just the PDF
- Timeline forces incremental redesign rather than a rebuild
- Multiple artifact types must be evaluated (workbooks, slides, videos, worksheets, assessments)

## The Salvage Principle

CAST is explicit that existing materials don't need to be discarded — they need to be redesigned. Most existing content is 60-80% salvageable. The failure mode is not "our content is bad"; it's "our content forces a single path when it could offer multiple."

## The 6-Step Workflow

### Step 1 — Inventory

Before UDL analysis, produce a complete inventory:

- Every artifact by type (workbook, slide deck, worksheet, video, assessment, poster, primary source pack, DBQ, etc.)
- File location, size, and content ownership
- Product SKU or catalog identity
- Current usage (who's using it, in what contexts)
- Source-of-truth location (is the artifact generated from a config? edited by hand? both?)

Do not skip this step. UDL redesign without inventory produces duplication and orphans.

### Step 2 — Cluster by Artifact Family

Group artifacts into families that share the same UDL design profile:

- **Student-facing print workbooks** — heavy Representation load, moderate Action & Expression, light Engagement
- **Student-facing digital experiences** — heavy Interaction, moderate Perception, high Engagement opportunity
- **Slide decks (teacher-facing during instruction)** — heavy Representation, Engagement, and Action & Expression
- **Videos** — heavy Perception, moderate Language & Symbols, high Engagement opportunity
- **Assessments** — heavy Action & Expression, moderate Representation
- **Primary source packs / DBQs** — heavy Representation (especially 1.3, 2.3, 3.3), Action & Expression
- **Posters / activity stations** — heavy Engagement (7.1-7.3), moderate Action & Expression

Each family gets its own UDL audit criteria, because the design musts differ.

### Step 3 — Audit One Representative Artifact per Family First

Do not audit all 200 artifacts. Pick ONE representative from each family, audit it against all 9 guidelines using the `audit-template.md`, and identify the systemic patterns. If the pattern holds (as it usually does), the rest of the family shares the same gaps and the same fixes.

Save time: for a product line with 10 units × 5 tiers × 6 artifact types = 300 artifacts, one representative per artifact type per unit (~60 audits) is enough. If cross-unit patterns hold in a spot check, reduce to one representative per artifact type total (~6 audits).

### Step 4 — Distinguish Content Salvage vs. Packaging Redesign

Two very different fixes emerge from an audit:

**Content salvage** — the words on the page, the primary sources, the historical narrative, the mathematics, the concept explanations. Content is usually good and stays.

**Packaging redesign** — how the content is delivered: mode, structure, layout, choice architecture, response format, evidence stamps. Packaging is usually where UDL gaps live.

**Rule of thumb:** if a UDL gap can be closed by adding a scaffold, overlay, or alternate mode WITHOUT changing the content, it's a packaging problem. If closing it requires rewriting the content, it's a content problem. Packaging problems are cheaper to fix and should be attacked first.

### Step 5 — Layer the Fixes

Apply UDL fixes in this priority order:

1. **Perception fixes (1.1, 1.2)** — customizable display, alternate perception modes. Almost always packaging. Cheap.
2. **Language scaffolds (2.1, 2.3)** — glossaries, cognates, sentence frames. Almost always packaging. Cheap.
3. **AT compatibility (4.2)** — screen reader tags, dictation-friendly layouts, OpenDyslexic overlays. Packaging. Moderate.
4. **Choice architecture (7.1)** — building learner choice into existing tasks. Packaging + light content. Moderate.
5. **Multiple response modes (4.1, 5.1)** — accepting written, oral, visual, gestural responses. Packaging + assessment rubric changes. Moderate.
6. **Diversity of perspectives (1.3, 3.3)** — adding non-dominant voices, indigenous ways of knowing. Often content addition. Higher cost but highest equity impact.
7. **Bias audit (2.4, 5.4, 7.4)** — reviewing existing content for exclusion. Content review. Moderate.
8. **Exclusionary-practice challenge (6.5)** — restructuring how the product operates (tracking, single-mode assessment, gatekeeping). Highest impact, requires product-level decisions.

### Step 6 — Ship in Passes, Not All at Once

Ship the packaging fixes first. Ship them fast. Get the artifact defensible before you start rewriting content.

**Pass 1 (weeks):** Perception, Language, AT, Choice, Multiple Response Modes — all packaging.
**Pass 2 (months):** Diversity of perspectives, bias audit — content additions.
**Pass 3 (quarter):** Exclusionary-practice restructuring — product-level.

If you try to ship all three at once, you'll ship none.

## Salvage Decision Tree

For each artifact:

```
Is the content standards-aligned and accurate?
├── NO → REPLACE (route to curriculum reviewer, not UDL)
└── YES → Is the content representative of multiple perspectives (1.3, 3.3)?
    ├── NO → CONTENT ADDITION (Pass 2)
    └── YES → Does the artifact offer multiple perception modes (1.2)?
        ├── NO → PACKAGING FIX (Pass 1: add audio, visual, tactile)
        └── YES → Does it offer multiple response modes (4.1, 5.1)?
            ├── NO → PACKAGING FIX (Pass 1: add response alternates)
            └── YES → Does it have a Provable Design Stamp?
                ├── NO → PACKAGING FIX (Pass 1: add stamp)
                └── YES → SHIP AS-IS
```

## Common Anti-Patterns to Watch For

**"5 tier variants of the same book"** — Duplicating a base artifact 5 times with cosmetic changes is not UDL. UDL is one artifact with multiple options built into the design.

**"Accommodation as afterthought"** — Providing extra time or a scribe is not UDL. UDL is designing the artifact so extra time isn't needed to demonstrate mastery through an alternate mode.

**"Teacher will differentiate on the fly"** — If the UDL fix depends on the teacher remembering to give one kid something different, it's not a design fix. Redesign the artifact.

**"Digital version = UDL"** — A digital PDF of a paper worksheet is not UDL. UDL requires the digital version to offer options the paper version can't (display customization, AT integration, multiple response modes).

**"We have a Spanish version"** — Translation is not UDL. WIDA-aligned scaffolds (cognates, sentence frames, oral rehearsal, level tags) inside the same artifact are UDL.

**"Honors is UDL because it extends"** — Extension without redesign is a tier variant, not UDL. UDL means the same artifact contains extension paths for anyone who takes them, not a separate book for "the smart kids."
