# Operational Checklist — History Hack District Edition Restructure

This is the executable checklist for the restructure. It expands the 13 gates
(0–12) referenced in `SKILL.md` into concrete tasks, required evidence, and
acceptance criteria. Work gate-by-gate, in order. Do not skip a gate because a
later gate "seems more urgent" — later gates assume earlier evidence exists.

Read `edition-contract.md` before starting Gate 0. Every gate below assumes the
contract is already loaded and treated as locked.

## How to use this checklist

- Each gate has: **Tasks**, **Required evidence artifacts**, **Acceptance
  criteria**, and **STOP conditions**.
- An **evidence artifact** is a concrete, inspectable thing — a file, a CI run
  URL, a screenshot, a diff, a test report — not a claim in prose. "I verified
  X" is not evidence. A pasted command output, log, or file path is evidence.
- Do not mark a gate complete in the STATUS block (see `SKILL.md`) until every
  acceptance criterion has a corresponding evidence artifact recorded.
- If a gate cannot be completed because of a missing dependency (access,
  credentials, a decision from the user), stop, record it as a STOP condition,
  and surface it rather than improvising a workaround.

---

## Gate 0 — Baseline and change-control

**Tasks**

1. Confirm the exact repository (or repositories) in scope. Record remote URL(s).
2. Confirm default branch name(s).
3. Locate and record the status of open PRs **#41** and **#507** — do not
   assume they are unrelated; read their diffs and determine if they touch
   routes, build config, or entitlement logic that this restructure will also
   touch. Record merge conflicts risk.
4. Confirm current production deployment state (what's live, where).
5. Explicitly confirm: **no production deploy will happen without human
   approval**, at any point in this workflow. This is a standing rule, not a
   one-time check.
6. Record a rollback point: exact commit SHA / tag on the default branch
   before any restructure work begins.
7. If the user has proposed forking/cloning into an independent repo to
   achieve isolation, run the tradeoff review (below) before proceeding with
   that path. Otherwise, confirm the one-repo/two-editions default and move on.

**Fork/clone tradeoff review (only if user proposes it)**

Document, at minimum: maintenance burden of two codebases, drift risk between
editions, CI/CD duplication cost, how shared packages/data would sync, and why
static-export + entitlement isolation (Gates 3–4) is insufficient for the
user's stated need. This review must be written down and the user's explicit
override recorded before any fork/clone action is taken. Absent this, the
default (one repo, two editions) stands.

**Required evidence artifacts**

- Repo URL(s) and default branch name(s) recorded in the STATUS block.
- PR #41 and PR #507 status summary (open/closed/merged, files touched,
  conflict risk) recorded in the STATUS block or a linked note.
- Rollback commit SHA recorded in the STATUS block.
- (If applicable) written fork/clone tradeoff review with explicit user
  sign-off, saved as a file.

**Acceptance criteria**

- [ ] Repo(s) and branch(es) identified and recorded.
- [ ] PR #41 and PR #507 reviewed and their status/impact recorded.
- [ ] No-production-deploy-without-approval rule acknowledged in STATUS block.
- [ ] Rollback commit SHA recorded.
- [ ] Fork/clone default upheld, or override documented with sign-off.

**STOP conditions**

- Cannot access the repository or determine the default branch.
- PR #41 or #507 cannot be read/resolved and materially conflicts with planned
  route/build changes.
- User proposes forking/cloning without agreeing to complete the tradeoff
  review.

---

## Gate 1 — Inventory and classification

**Tasks**

1. Enumerate every route in the application (page routes, API routes,
   server actions/functions).
2. Enumerate every distinct data domain/table/collection the app reads or
   writes.
3. Classify **every single route and API endpoint** into exactly one of:
   `district`, `full`, `shared`, `internal`. No route may remain unclassified.
4. Classify supporting features (not just routes) the same way — e.g. a
   feature might be implemented across multiple routes; classify the feature
   and confirm consistency across its routes.
5. Produce an inventory table: route/endpoint, classification, owning
   feature, data domains touched, current auth requirement (if any).

**Required evidence artifacts**

- A complete inventory file (e.g. `route-inventory.csv` or `.md` table) listing
  every route/endpoint with its classification.
- A written note of how the inventory was generated (e.g. "walked
  `app/` directory tree + grep for API route handlers on <date>") so it can be
  regenerated/audited later.

**Acceptance criteria**

- [ ] Inventory covers 100% of discovered routes/endpoints — zero rows with a
      blank or "TBD" classification.
- [ ] Each classification is one of the four allowed values only.
- [ ] Data domains touched are recorded per route where applicable.
- [ ] Inventory file is committed to the repo (or saved to workspace) and
      linked from the STATUS block.

**STOP conditions**

- A route's correct classification is ambiguous and cannot be resolved from
  the edition contract alone (e.g. it's unclear if a feature is "shared" or
  "full-only") — stop and ask the user rather than guessing.
- Route discovery tooling cannot enumerate all routes (e.g. dynamic route
  generation not statically analyzable) — stop and flag, do not assume
  completeness.

---

## Gate 2 — Product Edition Registry

**Scope boundary (read first):** Gate 2 is a **Phase A, no-runtime-behavior-change**
gate. It establishes the registry as the single source of truth and wires in
the presentation-layer consumers that are already in scope (navigation/hub and
package presentation), without pruning build output or enforcing API
authorization. **Build-output pruning is Gate 3's job. API authorization
enforcement is Gate 4's job.** Gate 2 is complete when the registry exists,
is exhaustively mapped, is consumed wherever already-in-scope presentation
logic exists, has no competing allowlist anywhere in the codebase, and
exposes stable adapters that Gates 3 and 4 are contractually required to
consume later. Gate 2 does **not** require build config or API middleware to
exist yet or to read the registry — those are later gates' deliverables, not
Gate 2's.

**Tasks**

1. Design and implement a single, canonical **Product Edition Registry** —
   one source of truth (a typed config module, table, or schema) that maps:
   edition → allowed routes → allowed capabilities → allowed roles → LTI
   availability. Define it with a real type/schema (not a loose object) so
   Gates 3 and 4 can consume it without re-deriving its shape.
2. Produce an **exhaustive inventory mapping**: cross-check the registry
   against the Gate 1 inventory so that every classified route/capability has
   exactly one corresponding registry entry, with zero gaps and zero
   duplicates.
3. Wire the registry into **navigation and package/hub presentation** —
   i.e., whatever already renders the five-hub navigation or determines which
   packages/hubs a user sees today — so that this presentation now reads from
   the registry instead of any prior hardcoded list. This must be done
   **without changing current public behavior**: the set of routes/hubs a
   given real-world user sees before and after this change must be identical.
   This task is about swapping the data source underneath existing
   presentation logic, not about introducing new isolation behavior.
4. **Prohibit competing edition allowlists.** No other file, module, or
   config in the codebase may maintain a second list of "district routes,"
   "full routes," or equivalent, for any purpose, including build config and
   API middleware that will be written in later gates. If such lists already
   exist anywhere (including in code that predates this gate), they must be
   removed or refactored to delegate to the registry now, even though the
   build/API enforcement that will use them is not implemented until Gates
   3 and 4.
5. Design and implement **owner override** as a registry concept, with its
   activation path restricted to **server-side entitlement only** — never a
   client flag, query parameter, cookie the client can set, or build-time
   toggle a non-owner could flip. The override mechanism itself is defined
   here even though no build/API enforcement consumes it yet.
6. **Expose stable adapters/functions** on top of the registry — e.g.
   `getAllowedRoutesForEdition(edition)`, `isCapabilityAllowed(edition, role,
   capability)`, `getLtiAvailability(edition)` — with a documented, versioned
   interface. These adapters are the explicit hand-off point: Gate 3's build
   isolation and Gate 4's API authorization **must** call these adapters
   rather than reimplementing registry lookups. Treat any change to these
   adapter signatures after Gate 3/4 begin consuming them as a breaking
   change requiring coordination.
7. **Explicitly defer, and record as deferred:**
   - Build-output pruning / static-export allowlisting → **Gate 3**.
   - API/session entitlement enforcement (403s, per-capability middleware
     checks) → **Gate 4**.
   Record both as **required downstream consumers** of the Gate 2 adapters in
   the evidence artifact below — this is not an open question to revisit
   later, it is a committed dependency that Gates 3 and 4 must satisfy.

**Required evidence artifacts**

- The registry source/schema file(s) (path recorded), including the type/
  schema definition.
- The exhaustive inventory-to-registry mapping (e.g. a generated report or
  test) showing 100% of Gate 1 rows have exactly one registry entry, with any
  discrepancies listed and resolved.
- A diff or grep showing navigation/hub presentation now reads from the
  registry, plus a before/after behavior check (e.g. a snapshot test or
  manual walkthrough) confirming no visible change in what routes/hubs are
  shown to any existing user class.
- A repo-wide grep/audit showing zero competing route allowlists/denylists
  remain anywhere in the codebase (including any pre-existing ones that were
  removed as part of this gate).
- A test (unit or integration) proving owner override cannot be triggered by
  any client-controllable input.
- A written adapter contract (function signatures + description) for the
  stable adapters Gate 3 and 4 must consume, saved as a reference doc or
  code-level interface/type file, explicitly labeled as the Gate 3/Gate 4
  hand-off surface.
- A short deferral note recording that build-output pruning (Gate 3) and API
  enforcement (Gate 4) are intentionally not implemented in this gate, and
  that both are logged as required downstream consumers of the adapters above.

**Acceptance criteria**

- [ ] Registry exists as a single canonical, typed source; file path recorded.
- [ ] 100% of Gate 1 inventory rows have exactly one matching registry entry;
      zero gaps, zero duplicates.
- [ ] Navigation/hub presentation consumes the registry; a before/after check
      confirms zero change in current public behavior.
- [ ] Zero competing edition allowlists remain anywhere in the codebase.
- [ ] Owner override is server-entitlement-gated only; test proves this.
- [ ] Stable adapters/functions are implemented, documented, and versioned as
      the Gate 3/Gate 4 consumption surface.
- [ ] Build-output pruning and API enforcement are explicitly recorded as
      deferred to Gates 3 and 4 respectively, with both logged as required
      downstream consumers of the Gate 2 adapters (not silently dropped).

Do not require, as a Gate 2 acceptance criterion, that build config or API
middleware already read the registry — that is what Gates 3 and 4 verify.
Gate 2 is only responsible for the registry, the inventory mapping, the
in-scope presentation wiring, the prohibition on competing allowlists, and
the stable adapter contract those later gates must use.

**STOP conditions**

- Any existing code path determines edition access from a client-supplied
  value (URL param, header the client sets, localStorage) — this must be
  fixed before Gate 2 is considered complete, not deferred.
- A competing edition allowlist is found anywhere in the codebase (including
  inside code that will later become Gate 3/4's implementation) and is left
  in place instead of being removed or refactored to delegate to the
  registry.
- Navigation/hub presentation is wired to the registry in a way that changes
  current public behavior — this is a Gate 2 violation (no-runtime-behavior-
  change is a hard constraint for this gate), not an acceptable side effect.
- Gate 3 or Gate 4 work begins by reimplementing registry lookups instead of
  calling the Gate 2 adapters — stop and correct the dependency direction
  before continuing.

---

## Gate 3 — Static-export build isolation

**Dependency on Gate 2:** this gate is the first required downstream consumer
of the Gate 2 registry adapters. Build config must call the stable adapters
exposed in Gate 2 (e.g. `getAllowedRoutesForEdition(edition)`) rather than
reimplementing a route list. If the adapters don't yet cover something build
config needs, extend them in Gate 2's registry/adapter layer — do not create a
parallel allowlist inside build config to work around a gap.

**Tasks**

1. Configure the district build to statically export **only** allowlisted
   routes, sourced from the Gate 2 registry via its stable adapters — not
   from a new or separately maintained list.
2. Verify excluded routes are **absent from the built JS bundles and the
   `out/` (or equivalent export) directory** — not just hidden from
   navigation. Search built output for excluded route strings/chunk names.
3. Configure a **real 404** response for any excluded route requested
   directly (not a client-side redirect that still ships the page's JS).
4. Verify the static host's `navigationFallback` / SPA-fallback rewrite rule
   **cannot** serve an excluded route's content (a common leak: a catch-all
   fallback silently serving the full-platform shell which then
   client-side-routes into an excluded page).
5. Add a **CI assertion** (automated check, not manual) that fails the build
   if any excluded route/chunk is present in the district export.

**Required evidence artifacts**

- Build config diff showing the allowlist-driven static export.
- A grep/scan report (saved as a file) of the district `out/` directory
  showing zero matches for excluded route paths or their associated chunk
  identifiers.
- A recorded manual or automated test hitting an excluded route on the
  deployed/preview district artifact and observing a real 404.
- The CI job definition (e.g. workflow YAML) implementing the automated
  route-leak assertion, plus a link to a CI run where it executed.

**Acceptance criteria**

- [ ] District export contains only allowlisted routes — verified by file
      system scan, not visual inspection of the nav menu.
- [ ] Excluded route JS chunks are absent from the district bundle.
- [ ] Direct navigation to an excluded route returns a real 404 on the
      district artifact.
- [ ] `navigationFallback`/rewrite rules tested and confirmed not to expose
      excluded content.
- [ ] CI assertion exists, is green, and would fail on a deliberate
      regression (prove this by temporarily reintroducing a leak in a scratch
      branch and confirming CI catches it, then reverting).

**STOP conditions**

- Any excluded route content, string, or JS chunk is found in the district
  build output — this is a release blocker, not a note for later.
- The static host does not support a real 404 for unmatched deep routes and
  only supports fallback-to-index — flag this as an infrastructure gap
  requiring a decision before proceeding.

---

## Gate 4 — API/session entitlement enforcement

**Dependency on Gate 2:** this gate is the second required downstream
consumer of the Gate 2 registry adapters. All per-capability checks must call
the stable adapters exposed in Gate 2 (e.g. `isCapabilityAllowed(edition,
role, capability)`) rather than reimplementing capability lookups against the
registry's underlying data. If the adapters don't yet expose what API
middleware needs, extend them in Gate 2's registry/adapter layer — do not
build a second capability-resolution path inside API middleware.

**Tasks**

1. Implement server-side claims (session/JWT/etc.) that encode edition and
   role, issued only by the server.
2. Implement **per-capability checks** at the API layer — every endpoint
   checks the registry-defined capability requirement (via the Gate 2
   adapters) against the caller's claims, not just a coarse "is this a
   district user" boolean, and not a re-derived local copy of the registry.
3. Write **403 tests**: for every district-excluded capability, a request from
   a district-scoped session must receive 403, not 404-masking-as-403 or a
   silent empty response.
4. Implement and test **tenant isolation** — a district user's session must
   not be able to read/write another tenant's (district's) data, verified with
   cross-tenant test requests.
5. Confirm **no code path grants privilege based on a query parameter or a
   client-supplied/client-maintained allowlist**. This includes feature flags
   that a client can set unless the flag's value is itself re-validated
   server-side against the registry.

**Required evidence artifacts**

- Middleware/handler code implementing per-capability checks (path recorded).
- A test suite file/report showing 403 tests for every excluded capability,
  with pass status.
- A tenant-isolation test report showing cross-tenant access attempts are
  rejected.
- A grep/audit note confirming no query-param or client-allowlist privilege
  grants exist (or documenting and then fixing any found).

**Acceptance criteria**

- [ ] Claims are server-issued only; no client can mint or elevate its own
      claims.
- [ ] Every registry capability has an automated 403 test for
      unauthorized callers, and all pass.
- [ ] Tenant isolation tests pass for at least one realistic cross-tenant
      attempt per data domain identified in Gate 1.
- [ ] No privilege-granting code path depends on client-controlled input.

**STOP conditions**

- A capability exists with no corresponding test.
- Any discovered privilege-escalation path via query param, header, or
  client-writable storage — treat as a blocking security issue, fix before
  continuing.

---

## Gate 5 — Separate deployments

**Tasks**

1. Stand up separate subdomains for district and full editions (e.g.
   `district.example.org` and `app.example.org` — use the project's actual
   domain).
2. Configure separate environment variables/config per deployment (district
   deployment must not carry full-platform secrets/config it doesn't need,
   and vice versa where relevant).
3. Confirm both deployments build from the **same repository** and share
   packages/data layers per the one-repo/two-editions default — separate
   deployment does not mean separate codebase.
4. Define and test a rollback procedure for each deployment independently
   (rolling back district must not force-rollback full, and vice versa,
   unless they share a release train intentionally).

**Required evidence artifacts**

- Deployment configuration (infra-as-code, hosting dashboard config export,
  or equivalent) for both subdomains.
- Confirmation both deployments reference the same repo/commit lineage
  (e.g. both deployment records show commits from the same branch history).
- A documented rollback runbook or tested rollback action with before/after
  state recorded.

**Acceptance criteria**

- [ ] District and full editions are reachable on separate subdomains.
- [ ] Environment/config separation confirmed (no leaked secrets across
      editions).
- [ ] Shared codebase confirmed — no divergent forked source.
- [ ] Rollback tested for at least one deployment and documented.

**STOP conditions**

- Any shared secret/config that would let a district deployment access
  full-platform-only resources it shouldn't.
- Rollback procedure is undefined or untested at release time.

---

## Gate 6 — Schoology mapping

**Tasks**

1. Verify the exact `deployment_id` and `tenant` values Schoology assigns and
   confirm this mapping is bound to the **district edition** specifically
   (not accidentally shared with or defaulting to the full platform).
2. Implement/verify LTI launch flow end-to-end for the district edition.
3. Implement/verify deep-linking (content selection from within Schoology).
4. Confirm role mapping (teacher/student/admin roles from Schoology map
   correctly to History Hack roles/entitlements).
5. Confirm **NRPS** (roster) and **AGS** (grades) integration **only where
   configured** — do not assume every district has AGS enabled; the app must
   detect and gracefully handle its absence.
6. Implement clear **readiness errors** — if a district's Schoology
   configuration is incomplete (missing deployment_id, misconfigured keys),
   the failure must be a clear, actionable error, not a silent fallback that
   masks misconfiguration.

**Required evidence artifacts**

- Recorded `deployment_id`/tenant mapping configuration (redacted of secrets
  as needed) tied to the district edition.
- A successful end-to-end LTI launch trace/log (from Schoology into the
  district edition).
- A deep-linking test trace.
- A test case demonstrating graceful behavior when AGS is not configured.
- A test case demonstrating a readiness error surfaces correctly for a
  deliberately broken/incomplete config.

**Acceptance criteria**

- [ ] `deployment_id`/tenant verified and scoped to district edition only.
- [ ] LTI launch works end-to-end in at least one test environment.
- [ ] Deep-linking verified.
- [ ] Roles map correctly for teacher, student, and admin.
- [ ] AGS-absent case handled gracefully (no crash, no false grade data).
- [ ] Readiness errors are clear and actionable, verified with a deliberately
      broken config.

**STOP conditions**

- `deployment_id`/tenant cannot be verified — do not guess or hardcode a
  plausible-looking value.
- LTI launch fails silently with no diagnosable error.

---

## Gate 7 — Five-hub UX and UDL/MTSS framework presentation

**Tasks**

1. Implement the five hubs exactly as named in `edition-contract.md` Section
   1.2, in that order, as the complete top-level navigation.
2. Design for **low cognitive load**: minimize simultaneous choices, use
   consistent layout patterns across hubs, avoid dense/cluttered screens.
3. Implement **contextual** (not global-only) support tools: read-aloud,
   bilingual toggling, display adjustments (e.g. font size/contrast), focus
   mode, and print-friendly views — available where relevant to the content
   being viewed, not buried in a disconnected settings page only.
4. Ensure UDL/MTSS framing is presented as foundational throughout (per
   contract Section 1.1) — check copy on hub landing pages specifically for
   "overlay/add-on/layer" language and correct it.
5. Implement **teacher governance** UI for the Approve/Modify/Defer/Decline
   actions (contract Section 2.2) wherever a system recommendation is shown
   to a teacher.

**Required evidence artifacts**

- Screenshots or recorded UI walkthroughs of all five hubs.
- Copy audit note confirming no "overlay/add-on/layer" language remains.
- Screenshot/trace of the Approve/Modify/Defer/Decline control in context.
- Accessibility-relevant screenshots of read-aloud/bilingual/display/focus/
  print controls in at least one real content context each.

**Acceptance criteria**

- [ ] All five hubs implemented, named exactly, in the specified order.
- [ ] Contextual accessibility/support tools present in real content
      contexts (not only a settings page).
- [ ] No overlay/add-on/layer language describing UDL/MTSS anywhere in
      shipped copy.
- [ ] Teacher governance controls (Approve/Modify/Defer/Decline) present
      everywhere a recommendation is surfaced; no automatic Tier 3 path;
      no student-facing tier labels found in audit.

**STOP conditions**

- Any discovered automatic tier assignment or student-visible tier label —
  blocking, must be fixed before this gate closes.
- A sixth top-level nav item appears without a documented contract change.

---

## Gate 8 — Standards Mastery System integrity

**Tasks**

1. Audit every place mastery percentages, item counts, or standards coverage
   are displayed or exported. Confirm the 5,056-item count and US.01–US.95
   alignment claims are only shown where actually true of the current bank.
2. Confirm mastery calculation logic **excludes** games and pretests, per
   contract Section 2 — trace the actual calculation code, don't rely on
   comments.
3. Confirm remediation-gating and teacher-authorization are enforced in code
   for retake eligibility (not just described in copy).
4. Confirm persistence status is accurately reflected in the UI/docs for
   MTSS plans, spaced-repetition state, and retake reflection (localStorage/
   pilot/local-only, per contract Section 3) — no copy implies
   server-side persistence for these.
5. Sweep all District Edition copy, docs, and exported reports for
   overclaims (e.g. claiming full World History coverage, claiming Hess CRM
   tagging, claiming complete Spanish parity) and correct any found.

**Required evidence artifacts**

- Code trace/reference showing mastery calculation excludes games/pretests.
- Code trace showing retake eligibility requires remediation + teacher
  authorization.
- A copy/docs audit log listing every capability claim found and its
  resolution (kept-as-is-with-caveat, corrected, or removed).

**Acceptance criteria**

- [ ] Mastery calculation verified in code to exclude games/pretests.
- [ ] Retake path verified to require remediation gate + teacher
      authorization; no bypass path found.
- [ ] Every honesty caveat from `edition-contract.md` Section 3 has a
      corresponding, correctly-labeled UI/doc statement (or the capability is
      not mentioned at all).
- [ ] No overclaim (Hess CRM, full World History, complete metadata/Spanish
      parity) found in shipped copy after audit.

**STOP conditions**

- Mastery calculation code cannot be located/verified — do not assume it's
  correct; escalate.
- Any found overclaim in customer/district-facing copy is a blocking issue
  for release, not a "note for later."

---

## Gate 9 — District-review personas

**Tasks**

1. Create test accounts/personas for: district reviewer/admin, teacher,
   student, and owner/full-platform user.
2. Walk through the district edition as each non-owner persona, confirming
   the experience matches their intended entitlement (e.g. student cannot see
   teacher governance controls; district admin cannot see full-platform-only
   features).
3. **The owner must review the district host using non-owner test personas**
   — not their own owner-privileged session. This is mandatory: an owner
   reviewing via their own elevated session can mask isolation failures
   (owner override could silently grant access that a real district user
   would not have).

**Required evidence artifacts**

- List of test persona accounts created (role, scope, edition).
- Walkthrough notes or recordings for each persona on the district host.
- Explicit confirmation (with screenshot/log) that the owner's review was
  conducted through a non-owner-scoped session on the district host, not
  through their default owner session.

**Acceptance criteria**

- [ ] All four personas tested on the district host.
- [ ] Owner review explicitly conducted via non-owner test persona(s), not
      owner's own session — documented.
- [ ] No persona observes capabilities outside their registry-defined
      entitlement.

**STOP conditions**

- Owner review was only performed via the owner's own elevated session —
  this gate is not complete until re-done via a non-owner test persona.
- Any persona observes an out-of-scope capability — blocking.

---

## Gate 10 — Verification matrix

Run and record results for each of the following, on the district artifact
unless noted otherwise:

| Check | Method | Evidence to record |
|---|---|---|
| Route artifact scan | Filesystem/bundle scan for excluded routes | Scan output file |
| 404 checks | Direct navigation to excluded routes | HTTP status + trace |
| 403 checks | Direct API calls to excluded capabilities | HTTP status + trace |
| RBAC | Per-role capability walkthrough | Persona test notes (Gate 9) |
| LTI | End-to-end launch + deep-linking | Trace/log (Gate 6) |
| a11y / WCAG 2.2 AA | Automated + manual accessibility audit | Audit report |
| iframe embedding | Confirm district content behaves correctly when iframed by Schoology (framing headers, responsive layout, no broken auth) | Test notes/screenshots |
| Automated tests | Full test suite run | CI run link, pass/fail summary |
| Static build | Confirm district static export builds cleanly and matches Gate 3 criteria | Build log |
| Claims/counts freshness | Re-check every numeric/factual claim (item counts, standards range, coverage) against current bank — no stale numbers | Audit note with date |

**Acceptance criteria**

- [ ] Every row in the matrix has a recorded evidence artifact and a pass
      result.
- [ ] Any failing row blocks progression to Gate 11 until resolved.
- [ ] Claims/counts freshness check is dated to the same review cycle as
      release — do not reuse a stale check from an earlier phase without
      re-verifying.

**STOP conditions**

- Any row fails and cannot be immediately fixed — record as a blocker, do not
  mark the gate complete.

---

## Gate 11 — Documentation and approval-copy sync

**Tasks**

1. Confirm the WCS packet (or equivalent district-facing packet) explicitly
   remains in **draft** status and uses only interest-only language per
   contract Section 4.
2. Produce/update: architecture diagram, data-flow diagram, and a permission
   matrix (role × capability × edition) reflecting the actual Gate 2 registry
   contents — documentation must match code, not aspiration.
3. Maintain a **versioned change log** for this restructure — every gate's
   completion, every contract-relevant decision, dated and attributed.

**Required evidence artifacts**

- WCS packet (or link/path) with draft status and interest-only language
  confirmed by direct read-through.
- Architecture diagram, data-flow diagram, and permission matrix files.
- Change log file with dated entries.

**Acceptance criteria**

- [ ] WCS packet reviewed and confirmed draft/interest-only; no
      approval/adoption language found.
- [ ] Architecture/data-flow/permission-matrix docs exist and match the
      actual registry and deployment topology.
- [ ] Change log exists, is versioned, and is up to date through the current
      gate.

**STOP conditions**

- WCS packet or any district-facing material contains approval, adoption, or
  endorsement language — this is a blocking correction, not a style note.
- Documentation contradicts the actual implemented registry/permissions —
  fix the mismatch before proceeding (favor correcting docs to match
  verified code, or fixing code if code is wrong — determine which via
  evidence, don't assume).

---

## Gate 12 — Release gates

**Tasks**

1. Open PR(s) with a clear description referencing which gates/evidence they
   close.
2. Ensure CI is green (all automated checks from Gates 3, 4, and 10 pass in
   CI, not just locally).
3. Obtain human review — a human reviewer, not just the agent, must review
   the PR.
4. Obtain **explicit merge approval** and **explicit deploy approval** —
   these are two separate approvals; merging to default branch does not imply
   deploy approval.
5. After deploy, run a **post-deploy smoke test** against the live district
   and full deployments.
6. Confirm the rollback point/procedure from Gate 0/Gate 5 is current and
   ready to execute if the smoke test fails.

**Required evidence artifacts**

- PR link(s) with gate references in the description.
- CI run link showing green status.
- Recorded human review (approval comment/sign-off).
- Recorded explicit merge approval and explicit deploy approval (can be the
  same approver, but both approvals must be recorded distinctly).
- Post-deploy smoke test results.

**Acceptance criteria**

- [ ] PR(s) reference the gates/evidence they close.
- [ ] CI green on the exact commit being merged.
- [ ] Human review recorded.
- [ ] Merge approval and deploy approval both explicitly recorded (not
      inferred from merge itself).
- [ ] Post-deploy smoke test passed, or failure triggered documented
      rollback.

**STOP conditions**

- No human review recorded — do not self-approve or treat CI green as
  sufficient.
- Deploy approval was not explicitly given — merging code is never, by
  itself, authorization to deploy.
- Post-deploy smoke test fails — execute rollback, do not "wait and see."

---

## STATUS block template (also in SKILL.md)

Use this exact structure at the end of every working session and whenever
progress is reported to the user:

```
STATUS: History Hack District Edition Restructure
Repo: <url> | Branch: <name> | Rollback SHA: <sha>
Open PRs tracked: #41 (<status>), #507 (<status>)
Current gate: <0-12> — <gate name>
Gate completion: [0:done] [1:done] [2:in-progress] [3:blocked] ... [12:not-started]
Evidence recorded this session: <bullet list with file paths/links>
Blockers / STOP conditions active: <list, or "none">
Next action: <single concrete next step>
Awaiting human approval for: <deploy/merge/none>
```

Do not omit any line. If a field is not yet applicable, write `n/a` rather
than deleting the line.
