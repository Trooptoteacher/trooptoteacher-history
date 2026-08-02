# History Hack Bilingual Architecture — Technical Reference

## Repository Structure

**Web App**: `Trooptoteacher/history-hack-web-app`
**iOS App** (reference): `Trooptoteacher/rork-u.s.-history-hack-1877-present-084`

## Core Bilingual Components

### 1. LanguageProvider (`components/providers/language-provider.tsx`)

```typescript
type Language = "en" | "es";

interface LanguageContextValue {
  language: Language;
  setLanguage: (lang: Language) => void;
  toggleLanguage: () => void;
}
```

- Persists to localStorage under key `hh-language`
- Default: `"en"`
- Sets `document.documentElement.lang` on change
- SSR-safe: defaults to English, hydrates from storage in useEffect

**Usage pattern in pages:**
```typescript
const { language } = useLanguage();
// Inline bilingual: {language === "es" ? "Vocabulario" : "Vocabulary"}
```

### 2. BilingualText Component (`components/accessibility/bilingual-text.tsx`)

```typescript
interface BilingualTextProps {
  en: string;           // Always required
  es?: string;          // Optional Spanish translation
  as?: WrapperElement;  // "h1" | "h2" | "h3" | "p" | "div" | "span"
  className?: string;
  showBoth?: boolean;   // Side-by-side mode
}
```

**Behavior:**
- English mode → renders `en` text with `lang="en"`
- Spanish mode with `es` available → renders `es` text with `lang="es"`
- Spanish mode without `es` → renders `en` text with `(English only)` indicator
- `showBoth` mode → renders both with EN/ES labels

**Review checklist for BilingualText usage:**
- [ ] All user-facing headings use `<BilingualText en="..." es="..." as="h2" />`
- [ ] All paragraph content uses `<BilingualText>` when translations exist
- [ ] The `as` prop matches semantic HTML requirements
- [ ] `showBoth` is only used where dual-language display is pedagogically valuable

### 3. ReadAloudButton (`components/accessibility/read-aloud-button.tsx`)

```typescript
interface ReadAloudButtonProps {
  text: string;        // Text to read aloud
  language: string;    // "en" or "es"
  size?: "sm" | "md";
  label?: string;      // aria-label
}
```

**Review checklist:**
- [ ] `text` prop contains the ACTIVE language version (not always English)
- [ ] `language` prop matches the language of the `text` prop
- [ ] Button is present for vocabulary terms, definitions, and key instructions
- [ ] aria-label describes the action ("Read definition aloud")

### 4. Content Translation Framework (`lib/content-translations.ts`)

**Registry system for content-level translations (not UI labels):**

```typescript
type ContentCategory = "cornell" | "ican" | "game-cipher" | "vocabulary" | "textbook";

// Register translations at module load:
registerTranslations("cornell", "unit-1", {
  "us-01": { topic: "Reconstrucción", cueQuestions: [...] },
});

// Use in components:
const { t, tArray, language, isSpanish } = useContentTranslation();
const topic = t("cornell", "unit-1", "us-01", "topic") ?? note.topic;
```

**Review checklist:**
- [ ] All content categories have registered translations for all 10 units
- [ ] Translation data files import correctly and register at module load
- [ ] `isEllActive()` correctly gates ELL-specific UI features

### 5. Reading Settings Provider (`components/providers/reading-settings-provider.tsx`)

```typescript
interface ReadingSettings {
  fontSize: "small" | "medium" | "large" | "xlarge";
  fontFamily: "system" | "serif" | "openDyslexic";
  lexileLevel: "simplified" | "standard";
  focusMode: boolean;
  sentenceHighlighting: boolean;
}
```

**ELL-relevant settings:**
- `lexileLevel`: Controls simplified vs. standard definitions. Should be synced to vocabulary page's simplified toggle.
- `fontSize`: Must be tested with bilingual content at all sizes — Spanish text is typically 10-20% longer than English
- `openDyslexic`: Font must render correctly for Spanish characters (ñ, accented vowels)

### 6. Vocabulary Data (`data/vocabulary.ts`)

```typescript
interface VocabTerm {
  id: string;
  term: string;
  termEs?: string;
  definition: string;
  definitionEs?: string;
  simplifiedDefinition?: string;
  example?: string;
  exampleEs?: string;
  primarySource?: string;
  primarySourceEs?: string;
  ellSupportNote?: string;
  relatedStandards?: string[];
  unitId: string;
}
```

**315 terms across 10 units. Review each term for:**
- [ ] `termEs` present (100% required)
- [ ] `definitionEs` present (100% required)
- [ ] `simplifiedDefinition` present (100% required)
- [ ] `exampleEs` present (100% required)
- [ ] `primarySourceEs` present (100% required)
- [ ] `ellSupportNote` present (100% required)
- [ ] `relatedStandards` correctly maps to TN standards

## iOS App ELL Features (Reference for Parity)

### ELL Settings Screen (`app/ell-settings.tsx`)
The iOS app has a dedicated ELL settings screen with:
- Enable/disable ELL supports toggle
- Proficiency level selector (WIDA levels 1-6)
- Native language selector
- Advanced settings (sentence stems, visual supports, audio speed)

### Bilingual Coverage QC (`utils/bilingual-coverage-qc.ts`)
Automated quality control system that:
- Defines coverage policies per content family
- Measures English:Spanish field parity
- Reports pass/fail with percentage thresholds
- Should be replicated or referenced for web app audits

### Vocab Visual Support (`utils/vocab-visual-support.ts`)
Maps vocabulary terms to historical images/maps for visual reinforcement — particularly valuable for ELLs who benefit from dual-coding.

## Pages Using Bilingual Features (80+ files)

All pages under `app/` directory use `useLanguage()`. Key pages to audit:

**Student-facing (highest priority):**
- `app/vocabulary/page.tsx` — Vocabulary with flashcards and list view
- `app/practice/page.tsx` — Quiz practice with question content
- `app/dashboard/page.tsx` — Student home with recent activity
- `app/units/[id]/unit-journey-client.tsx` — Unit learning path
- `app/textbook/[unit]/textbook-unit-client.tsx` — Textbook reader
- `app/resources/cornell-notes/student/page.tsx` — Cornell Notes
- `app/practice/ican/page.tsx` — I Can statement practice
- All game pages under `app/games/` and `app/trivia/`

**Teacher-facing (medium priority):**
- `app/teacher-tools/parallel-tests/page.tsx` — Test generator
- `app/teacher-tools/question-viewer/page.tsx` — Question bank viewer
- `app/teacher-dashboard/page.tsx` — Teacher analytics

**Informational (lower priority):**
- `app/accessibility/page.tsx` — Accessibility statement
- `app/privacy/page.tsx` — Privacy policy
- `app/terms/page.tsx` — Terms of service

## Unit Color Map (for consistent visual scaffolding)

```typescript
{
  1: "#1976D2",  // Reconstruction & Industrialization
  2: "#0E918C",  // Progressive Era & Imperialism
  3: "#5C6BC0",  // WWI & 1920s
  4: "#D4752E",  // Great Depression & New Deal
  5: "#8D6E63",  // World War II
  6: "#2E7D32",  // Cold War
  7: "#C62828",  // Civil Rights
  8: "#6A1B9A",  // Vietnam & Social Movements
  9: "#E65100",  // End of Cold War & Conservatism
  10: "#00695C"  // Modern America
}
```

Colors should be used consistently in bilingual content to provide visual anchoring that reduces language-dependent navigation.
