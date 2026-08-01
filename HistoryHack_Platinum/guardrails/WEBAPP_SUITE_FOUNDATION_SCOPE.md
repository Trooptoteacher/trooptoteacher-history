# Web-App Suite Foundation — Scope (for go-ahead)

**Goal:** one login, one gradebook, all courses. Credentialing is already solved
(SSO/OneRoster). This scope is the *entitlement + data-scoping* work that lets
Government / World / Tennessee / 8–6 grade plug into the existing platform.

**Repo:** `history-hack-web-app` (separate from the content repo). Do this on a new
branch `claude/suite-foundation`; PR when approved. **No auth rewrite** — auth is done.

## Already in place (do NOT rebuild)
- Auth / SSO / rostering: `lib/sso/session.ts`, `app/auth/callback`, `app/sign-in`, OneRoster.
- Entitlement/edition system: `lib/product-edition/` (`require-capability`, `registry.data`,
  `server-edition`, `build-isolation`).
- Subject registry: `lib/subjects.ts` (currently 3 subjects) + `[subject]` routes + subject context.
- Per-subject data namespaces under `public/data/{subject}/`.

## The work (small, because the platform is already multi-course)

### 1. Register all courses — `lib/subjects.ts`
- Add `SubjectId` + `SubjectMeta` for: `government` (GC), `world-history` (W, already present),
  `tennessee-history`, `grade-8-history`, `grade-7-history`, `grade-6-history`.
- Set `standardsPrefix`, `rcPrefix`, `contentReady` (false until content lands), `accentToken`.
- Create `lib/standards/{subject}-standards.ts` per course (from the TDOE PDFs).
- Wire each into the subject picker (`app/page.tsx`).

### 2. Entitlement — `lib/product-edition/`
- Add a per-course access capability so a district/user login grants the courses they own
  (e.g. `capability: "course:world-history"`). Gate `[subject]` routes with
  `require-capability`. Default new courses OFF until licensed/ready.

### 3. Subject-scope the data stores  ← the real backend task
- Stores that hold student/teacher data must key by `subject` so courses don't collide:
  `progress-store`, `portfolio-store`, `grading-categories-store`, `extended-response-store`,
  `cornell-unlock-store`, `primary-sources-store`, `last-game-store`, `pacing-version-store`.
- Add a `subject` dimension to each key/record; migrate existing US-History rows to
  `subject="us-history"`. Verify no cross-course read/write leakage.

### 4. Testing DB + tests per course
- Seed the testing database with per-subject fixtures; parameterize the existing vitest/axe
  suites by subject so every course runs the same green tests.

## Risk / sequencing
- Items 1–2 are low-risk (config + gating). Item 3 touches student data — do it behind a
  migration with tests, verify US-History data integrity first. Item 4 gates release.
- Suggested order: **1 → 2 → 3 (with migration + tests) → 4**, each its own PR.

## Decision needed
Approve this scope and I open `claude/suite-foundation` and start with #1 (registry +
entitlements), which is safe and unblocks course content. #3 (data-store scoping) gets its
own PR with a migration + tests before anything ships.

---
© 2026 TroopToTeacher Technologies, LLC · Social Studies Hack suite.
