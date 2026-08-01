# Social Studies Hack — Course Trees

The expanding suite. Each course here is built to the **U.S. History Hack**
platinum standard, inheriting the shared foundation in
[`../HistoryHack_Platinum/guardrails/`](../HistoryHack_Platinum/guardrails/)
(core guardrails, cradle-to-grave workflow, sourcing allowlist, asset crosswalk,
geo provenance) and the format layer in `SKILL.md`.

## Layout convention

```
courses/<subject-id>/
  course.json            # course manifest (id, standards prefix, status)
  standards/             # official TN standards, verbatim (text + codes)
  build_unit1/ …         # per-unit content JSONs + builders (added at Phase 1)
  deliverables_unit1/ …  # rendered DOCX/PDF/PPTX (added at Phase 3)
```

Subject ids match the web-app registry (`history-hack-web-app/lib/subjects.ts`):
`us-history`, `government`, `world-history`, `tennessee-history`,
`grade-8-history`, `grade-7-history`, `grade-6-history`.

## Reference course (the template)

**U.S. History Hack** is not under `courses/` — it lives at
[`../HistoryHack_Platinum/`](../HistoryHack_Platinum/) (the original tree, left in
place to avoid disturbing the working 254-file build). Treat it as
`courses/us-history` logically: it is the platinum reference every course matches.

## High-school build priority

1. **Government** (`GC.xx`) — sourcing list complete in Drive.
2. **World History** (`W.xx`) — Unit 1 authored in the web app; WH item bank exists.
3. **Tennessee History** — standards ingest pending.

(Middle grades — 8th → 7th → 6th — follow the high-school courses.)
