# HANDOFF — Build World History Hack (start a new chat)

This is the one-page handoff to build **World History Hack** in a fresh chat, to the exact
platinum standard of the U.S. History flagship and the just-completed **Government Hack**
(`courses/foundations-constitutional-government/`). The full workflow, prompts, skills,
QC gate, copyright procedure, brand-lock, and suite integration are in
**`courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md`** — this page tells you how
to start and what to have ready.

---

## Why a new chat (not this one)
- **Skills are not session-bound** — every build skill (`history-hack-course-standard-builder`,
  `tn-assessment-specialist`, `tcap-item-writer-v2`, `udl-cast-expert`,
  `copyright-integrity-accreditation`, `history-hack-website-builder`, …) is available in **any**
  chat on this repo. A new chat has the same toolbox.
- A full course build is large; a fresh chat gets a **full context budget** instead of fighting a
  nearly-full one. Everything needed is captured on disk (below), so nothing is lost.

## The context that matters (tell the new chat this)
World History Hack ships **in addition to** the main History Hack web app, which is becoming a
**multi-course Social Studies Suite**: one platform, entitlement-gated course editions —
U.S. History (flagship) · Government & Civics · **World History** · future (Economics, Geography).
It is a **course edition, not a new app or a fork.** Reuse the platform's brand, tokens, and
manifest schema; add World History to the course switcher; keep teacher keys entitlement-gated.

---

## Have these TWO inputs ready before you start
1. **The official TN World History & Geography standards** (verbatim text + codes) — paste at Phase 1.
2. **A Google Drive folder of the primary-source images**, one genuine **public-domain** source per
   standard, each named **exactly** `{{STD}}_slug.ext` (e.g. `W.14_magna-carta.jpg`). You already have
   the **WH.08–WH.37 TCAP Assessment Items** in Drive — point the chat at those too. Get direct
   downloadable links + rights from LoC / Wikimedia Commons / National Archives / Smithsonian OA /
   Met OA / NYPL / Gallica / Rijksmuseum / Internet Archive (table in the playbook, Phase 2).
   Re-export anything > 10 MB to ≤ 10 MB (~2000 px); pull images ≥ ~1200 px so they route through the
   on-disk decode path.

## Then paste this into the new chat
> Build a new licensable "World History Hack" course edition to the platinum standard of
> `courses/foundations-constitutional-government`, following
> `courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md` phase by phase — produce EVERYTHING in
> its Deliverables Inventory, copy the reusable Government assets (question-bank toolkit, the
> **brand-locked** `BUILD/engine/` docx builders, deck builder, `sync_images.py`, compliance
> templates), and register the edition in the Social Studies Suite. Use the one-shot kickoff prompt at
> the bottom of the playbook. I'll paste the TN World History & Geography standards now and drop the
> sourced PD images in a Drive folder at Phase 2. STOP and show me the standards→unit map before authoring.

(The playbook's **"One-shot kickoff prompt"** at the bottom is the full version — it names every skill,
the guardrails, the brand-lock, and the QC gate. Use it verbatim.)

---

## What's already on disk to reuse (nothing to rebuild)
- **Playbook** — `courses/_playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md` (13 phases + prompts, full skills roster, GUARDRAILS block, UDL/MTSS wording block, sourcing table, **⭐ Workbook Brand-Lock**, **Copyright & Rights Clearance**, **Master QC Gate**, **Social Studies Suite** integration).
- **Proven template** — `courses/foundations-constitutional-government/` (a complete platinum course: 7 units, 35 standards, decks, workbooks + large-print, teacher guides, organizer toolkits, assessment books, 700-item question bank, parallel-test generator, 9/9 UDL audit, compliance pack).
- **Brand-lock reference** — `courses/foundations-constitutional-government/REFERENCE/{USHistory_Unit8_Student_Workbook.docx, README.md}` — the owner's actual U.S. History Hack workbook + the exact locked settings (margins 1224 · width 9792 · Cornell 2448|7344 · ruled line C9C2B4). **The student workbook must come out identical to this.**
- **Reusable builders/toolkit** — `BUILD/engine/build_*.js` (brand-locked), `08_QUESTION_BANK/*.py`, `BUILD/decks/*/build_deck.py`, `BUILD/sync_images.py`, `06_COMPLIANCE_INTERNAL/*`, `05_STANDARDS_ALIGNMENT/*`.

## Definition of Done (per the playbook's Deliverables Inventory)
Per unit: content JSON · teacher + student decks (tagged PDF) · student workbook + large-print · teacher
guide · organizer toolkit · assessment book (keys/psychometrics/UDL teacher-side) · DBQ book · 4 covers.
Course-wide: 20-item/standard question bank w/ psychometrics + UDL + remediation · parallel-test generator
· inventory + standards crosswalk · primary-source bank · **9/9 CAST UDL 3.0 audit** · MTSS map ·
accessibility statement · **rights-clearance log + NOTICES** · compliance pack (matrix, scope & sequence,
Schedule F) · **Master QC Gate passed (12 checks)** · web edition manifests registered in the Suite ·
master index · district ZIP. Guardrails hold everywhere; verify + commit + push each phase.
