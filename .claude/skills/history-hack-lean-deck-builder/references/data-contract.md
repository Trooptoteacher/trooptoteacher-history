# Lean Deck Data Contract (`_build.json`)

`scripts/build_lean_deck.js` reads a single `_build.json` from the data dir. Top-level keys:

```jsonc
{
  "meta":      { /* free-form; unit title, version, standards list */ },
  "imageRefs": { "<image-key>": "relative/path/under/IMG_DIR.jpg", ... },
  "slides":    [ /* ordered slide objects; each has n, kind, standard, footer */ ]
}
```

- **`imageRefs`** — maps a short key to an image path **relative to `IMG_DIR`** (3rd CLI arg; defaults to `hh-web/public`). Every slide's `image` / `secondaryImage` field is a key into this map.
- **`slides`** — ordered array. `n` is the 1-based slide number (also the printed page number). `kind` selects the slide renderer. `footer` is the per-slide footer caption (`"US.01 · <topic>"`). `standard` is the `US.NN` code. `assertion` is the bold headline — a **summary-label of the locked narrative**, never new narrative.

## Slide kinds (the fixed lean sequence)

Build order is exactly the array order. `kind` values and their extra fields:

| `kind` | Renderer | Extra fields |
|---|---|---|
| `Standard Divider` | `standardDividerSlide` | `title`, `tnStandard`, `iCan` |
| `Hook` | `assertionEvidenceSlide` (default) | `image`, `wordBudget` |
| `Direct Instruction` | `assertionEvidenceSlide` (default) | `image`, `wordBudget` |
| `Primary Source Analysis` | `sourceItFirstSlide` | `image`, `sourceItFirst {who, when, why}`, `sources [{label,url}]`, `practice` |
| `Three Perspectives Synthesis` | `threePerspectivesSlide` | `framingIntro`, `perspectives [3]`, `primarySourceAnchor` |
| `We Do` | `weDoSlide` | `weDo {skill, modeledPrompt, modeled, think, thenYou}`, `image` |
| `Tennessee Connection` | `tennesseeSlide` | `image`, `secondaryImage`, `tnFacts [{claim}]`, `mapNote`, `highlight`, `emphasis` |

Any `kind` not listed falls through to `assertionEvidenceSlide` (bold assertion headline + large evidence image).

## Fixed framework wording (do not paraphrase)

The **Three Perspectives** lenses are verbatim across the whole app:

- **Who benefited?**
- **Who bore the costs?**
- **Who decided?**

## Standard-divider example

```json
{
  "kind": "Standard Divider",
  "standard": "US.02",
  "title": "Federal Policies Toward American Indians",
  "tnStandard": "US.02 – Examine federal policies toward American Indians, including ...",
  "iCan": "I can examine federal policies toward American Indians, including ...",
  "n": 10
}
```

## Tennessee Connection example (celebrated, bold)

```json
{
  "n": 9, "kind": "Tennessee Connection", "standard": "US.01",
  "assertion": "A hometown hero: George Jordan of Triune, Williamson County ...",
  "image": "williamson-county-map-1878",
  "secondaryImage": "ninth-cavalry-ncos-1889",
  "footer": "US.01 · Tennessee Connection · Williamson County",
  "highlight": true, "emphasis": "bold-celebrated",
  "tnFacts": [ { "claim": "..." }, { "claim": "..." }, { "claim": "..." } ],
  "mapNote": "1878 Williamson County map (Tennessee State Library & Archives) ..."
}
```

See `assets/unit1-lean-example/_build.json` for the complete, working 48-slide Unit 1 file (US.01–US.07).

## Image rules (locked)

- All imagery is **public-domain**, source-captioned on-slide, historian-verified (LOC / NARA / Smithsonian). **No AI-generated imagery.**
- Image slides carry a gold **ZOOM IN** pill so the teacher can zoom in while presenting.
- Never show a mismatched image; omit the image and use a clean wide-text layout instead.
