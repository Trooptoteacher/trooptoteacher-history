# Code Audit Checklist — React/Next.js Components

**Load this reference when `artifact_type: code`.**

Applies to History Hack web app (Trooptoteacher/history-hack-web-app). Every component must pass each applicable criterion OR be scored Unverified with specific evidence needed.

---

## Pre-Audit Setup

Before auditing any component, verify:

- [ ] The file has been fully read in this session (not summarized, not excerpted)
- [ ] You know the component's purpose (header, modal, form, quiz item, etc.)
- [ ] You've checked for axe-core / jest-axe coverage of this component in the repo
- [ ] You've checked git blame / recent PR activity — is this file part of PR #40/#41/#43?

If PR coverage exists: reference the PR and scope your audit to the current committed state (do not re-flag issues being remediated in an open PR).

---

## Section A — Keyboard Operability (WCAG 2.1.x)

| ID | Criterion | Evidence required |
|---|---|---|
| K-01 | All interactive elements reachable via Tab (2.1.1 Keyboard, A) | File path + element; Tab order traced |
| K-02 | No keyboard traps (2.1.2 No Keyboard Trap, A) | Focus can enter AND leave every modal/dialog |
| K-03 | Custom controls handle Enter AND Space (2.1.1) | Event handlers include both keys |
| K-04 | Escape closes modals/menus (2.1.2) | onKeyDown includes Escape handling |
| K-05 | Tab order matches visual order (2.4.3 Focus Order, A) | DOM source order vs. CSS-positioned order |
| K-06 | Focus returns to trigger after modal close (2.4.3) | useRef on trigger, focus() in cleanup |
| K-07 | Visible focus indicator on every interactive element (2.4.7 Focus Visible, AA) | CSS outline or box-shadow; 3:1 contrast against adjacent colors |
| K-08 | Focus not obscured by sticky headers/footers (2.4.11, AA, new in 2.2) | scroll-padding or equivalent when focusing offscreen element |

**Common violations to check:**
- `<div onClick={...}>` without `role` + `tabIndex` + keyboard handler (fails K-01, K-03)
- Modal without focus trap (fails K-02)
- `autoFocus` on mount (violates user expectation; AAA but usually flagged)
- `outline: none` without replacement (fails K-07)

---

## Section B — Semantic Markup (WCAG 1.3.x, 4.1.x)

| ID | Criterion | Evidence required |
|---|---|---|
| S-01 | Use native HTML elements over ARIA where possible (1.3.1 Info and Relationships, A) | `<button>` not `<div role="button">`; `<nav>` not `<div role="navigation">` |
| S-02 | Heading hierarchy has no skips (1.3.1) | h1 → h2 → h3 in DOM order |
| S-03 | Every form control has an associated label (1.3.1, 3.3.2, 4.1.2) | `<label htmlFor>` or `aria-labelledby` or `aria-label` |
| S-04 | Lists use `<ul>` / `<ol>` / `<li>` (1.3.1) | Not divs styled as lists |
| S-05 | Tables use `<th scope>` and `<caption>` (1.3.1) | Data tables only; layout tables forbidden |
| S-06 | Landmarks present: main, nav, header, footer (1.3.1, 2.4.1 Bypass Blocks, A) | One `<main>` per page |
| S-07 | `aria-*` attributes reference valid IDs (4.1.2 Name Role Value, A) | aria-describedby points to existing element |
| S-08 | Dynamic content updates announced (4.1.3 Status Messages, AA) | aria-live region or role="status" |

**Common violations to check:**
- `<div role="button">` instead of `<button>` (fails S-01)
- h3 under h1 with no h2 (fails S-02)
- Placeholder used as label (fails S-03)
- `aria-describedby="tooltip"` with no element id="tooltip" (fails S-07)

---

## Section C — Images, Media, and Non-Text Content (WCAG 1.1.x, 1.2.x, 1.4.x)

| ID | Criterion | Evidence required |
|---|---|---|
| M-01 | Every `<img>` has alt attribute (1.1.1 Non-text Content, A) | alt="" for decorative; descriptive for informative |
| M-02 | Decorative images have alt="" AND aria-hidden="true" (1.1.1) | Both attributes present |
| M-03 | Informative SVGs have `<title>` element (1.1.1) | Inline SVG with title child |
| M-04 | Icon-only buttons have accessible name (4.1.2) | aria-label or visually-hidden text |
| M-05 | Video has captions (1.2.2 Captions Prerecorded, A) | <track kind="captions"> present |
| M-06 | Audio controls are accessible (1.4.2 Audio Control, A) | User can pause; doesn't autoplay >3 sec |
| M-07 | Images of text avoided (1.4.5, AA) | Text is real text, not baked into images |

---

## Section D — Color and Contrast (WCAG 1.4.x)

| ID | Criterion | Evidence required |
|---|---|---|
| C-01 | Text contrast ≥ 4.5:1 (normal), ≥ 3:1 (large/bold 18pt+) (1.4.3, AA) | Computed foreground/background values; ratio calculation |
| C-02 | UI component borders / icons ≥ 3:1 (1.4.11 Non-text Contrast, AA) | Border color vs. adjacent surface |
| C-03 | Focus indicators ≥ 3:1 (1.4.11) | Focus ring color vs. unfocused background |
| C-04 | Information not conveyed by color alone (1.4.1 Use of Color, A) | Error states have icon/text, not just red |
| C-05 | Text remains readable at 200% zoom (1.4.4 Resize Text, AA) | No horizontal scroll at 200% on 1280×1024 |
| C-06 | Content reflows at 320 CSS px width (1.4.10 Reflow, AA) | Mobile viewport simulation |

**Tools:** axe-core reports contrast failures with exact ratio; cite that line.

---

## Section E — Forms and Inputs (WCAG 3.3.x, 4.1.2)

| ID | Criterion | Evidence required |
|---|---|---|
| F-01 | Every input has a visible, persistent label (3.3.2 Labels or Instructions, A) | `<label>` element, not just placeholder |
| F-02 | Required fields indicated beyond color (3.3.2) | "(required)" text or `aria-required` |
| F-03 | Error messages are specific (3.3.1 Error Identification, A) | "Email must contain @" not "Invalid" |
| F-04 | Error suggestions provided (3.3.3 Error Suggestion, AA) | "Did you mean example@…" |
| F-05 | Autocomplete tokens on personal info inputs (1.3.5 Identify Input Purpose, AA) | autoComplete="given-name" etc. |
| F-06 | Redundant entry avoided (3.3.7 Redundant Entry, A, new in 2.2) | Don't ask for same info twice |
| F-07 | Status messages announced (4.1.3) | role="status" or aria-live on success/error |

---

## Section F — Timing and Motion (WCAG 2.2.x, 2.3.x)

| ID | Criterion | Evidence required |
|---|---|---|
| T-01 | Timed content can be paused/extended/disabled (2.2.1 Timing Adjustable, A) | Speed Challenge must have pause; Unit tests check this |
| T-02 | Moving/auto-updating content can be paused (2.2.2 Pause Stop Hide, A) | Carousels, animations |
| T-03 | No content flashes >3 times per second (2.3.1 Three Flashes, A) | CSS animations / transitions |
| T-04 | prefers-reduced-motion respected (2.3.3 Animation from Interactions, AAA — we aim for it anyway) | @media (prefers-reduced-motion: reduce) CSS |

---

## Section G — Language and Internationalization (WCAG 3.1.x)

| ID | Criterion | Evidence required |
|---|---|---|
| L-01 | `<html lang>` is set (3.1.1 Language of Page, A) | lang="en" or lang="es" |
| L-02 | `<html lang>` updates on language toggle (3.1.1) | EN/ES toggle updates the attribute |
| L-03 | Language of parts marked (3.1.2 Language of Parts, AA) | Spanish quote in English text: `<span lang="es">` |

---

## Section H — Targets and Pointer (WCAG 2.5.x)

| ID | Criterion | Evidence required |
|---|---|---|
| P-01 | Target size ≥ 24×24 CSS px (2.5.8, AA, new in 2.2) | Measured via browser inspector |
| P-02 | Pointer gestures have single-pointer alternative (2.5.1, A) | No swipe-only interactions |
| P-03 | Dragging has single-pointer alternative (2.5.7, AA, new in 2.2) | Drag-and-drop also keyboard-operable |
| P-04 | Pointer cancellation supported (2.5.2, A) | Click fires on up-event, not down-event |

---

## Section I — Tool Integration (History Hack Specific)

| ID | Criterion | Evidence required |
|---|---|---|
| I-01 | axe-core has coverage for this component | jest-axe test exists in `__tests__` or `.test.tsx` |
| I-02 | eslint-plugin-jsx-a11y errors at zero | `npm run lint` output for the file |
| I-03 | Component tested with keyboard only | Manual or CI test record |
| I-04 | Component tested with screen reader (NVDA minimum) | Test log or deferred with specific target date |
| I-05 | Reduced motion respected via CSS `prefers-reduced-motion` | Media query present |
| I-06 | Reading Preferences context honored | Component respects font scale, spacing, theme tokens from PR #40 |

---

## Scoring Rubric for Code

| Grade | Criteria |
|---|---|
| **A** | 100% Pass on applicable criteria; zero Unverified; zero violations in axe-core; eslint-jsx-a11y clean |
| **B** | ≤2 High findings being remediated in an open PR; all other criteria Pass; zero Critical |
| **C** | 1-2 Critical OR 3-6 High, with clear remediation path |
| **D** | 3+ Critical OR widespread Medium issues; not submission-ready |
| **F** | Keyboard inaccessible, screen reader unusable, or fails a lawsuit-adjacent criterion (1.1.1, 1.4.3, 2.1.1, 4.1.2 at scale) |

## Finding Template (for Code)

```markdown
### Finding C-[seq] — [short title]

**Severity:** Critical / High / Medium / Low
**Standard(s):** WCAG 2.2 SC [X.Y.Z] [Title] ([A|AA]); also cited under Section 508 E[xxx.x], ADA Title II
**Location:** [file path]:[line range]
**Evidence:**
```
[exact code quote]
```
**Finding:** [what is wrong, in plain language]
**User impact:** [who is affected and how]
**Remediation:** [specific fix with code or approach]
**Estimated effort:** [S / M / L]
**Related PR:** [if being fixed in open PR, cite]
```
