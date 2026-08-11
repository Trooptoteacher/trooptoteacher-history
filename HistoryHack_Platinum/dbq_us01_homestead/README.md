# U.S. History Hack™ — US.01 Homestead Act DBQ (standalone SKU)

**Investigation:** *The Homestead Act of 1862 — Who Gained a Homestead, and Who Lost a Homeland?*
**Standard:** US.01 — *Explain how the Homestead Act and the Transcontinental Railroad impacted the settlement of the West* (verbatim TDOE).
**Built:** 2026-08-11 (UTC) · print-first via the WeasyPrint print-pipeline (no .docx).
**Generator:** `print-pipeline/gen_dbq_us01_homestead.py`

## Deliverables (print these)
1. **`US01_Homestead_DBQ_Workbook_*.pdf`** — student DBQ (13 pp): what-is-a-DBQ how-to, US.01 + SSP crosswalk, pre-reading Activate & Predict page, 6-document set, Tennessee Connection, evidence organizer, CER essay + rubric.
2. **`US01_Homestead_DBQ_Scaffold_Supports_*.pdf`** — Scaffold & Language-Access Companion (4 pp) for the three inclusion sections: DBQ checklist, worked HIPPO + OPTIC models, EN/ES word bank, sentence stems, bucketing organizer, thesis builder. Works **alongside — never in place of** — a student's IEP/504.
3. **`US01_Homestead_DBQ_Teacher_Guide_*.pdf`** — teacher guide + answer key (5 pp): at-a-glance, pacing, source notes, model thesis + annotated exemplar, 20-pt AP-aligned rubric, differentiation plan (3 inclusion / 2 honors), honest disclosure.

Supporting files: `manifest.json` (document-set manifest for the guardrail) · `us01-homestead-sources.json` (verbatim statute-excerpt corpus, committed so the primary-source text lives in a durable file, not only inside the PDF).

## Document set (2 text/HIPPO + 4 visual/OPTIC — all public domain)
| Doc | Kind | Source (provenance) | Date |
|---|---|---|---|
| A | text / HIPPO | Homestead Act §1–2 (eligibility, affidavit) — 12 Stat. 392, RG 11, U.S. National Archives | 1862 |
| B | text / HIPPO | Homestead Act §3 (five-year residence, proof, reversion) — 12 Stat. 392 | 1862 |
| C | visual / OPTIC | Golden Spike, Promontory — A. J. Russell, Yale Coll. of Western Americana | 1869 |
| D | visual / OPTIC | Railroad Systems of the U.S., 1890 (Plate 60) — Gannett / U.S. Census, LOC G&M | 1890 |
| E | visual / OPTIC | Rawding family sod house, Custer Co., NE — S. D. Butcher; LC-USZ62-8276 | 1886 |
| F | visual / OPTIC | Tom Torlino, Navajo, Carlisle (before/after) — J. N. Choate; Beinecke, Yale | 1882/85 |

Statute text verified verbatim against the U.S. National Archives, NPS Homestead National Historical Park, Gilder Lehrman, and the State Historical Society of North Dakota transcript. The Act has **8 sections**; approved **May 20, 1862**.

## QC results
- **Image-content gate (mandatory):** every image was rendered and inspected against its caption, tasks, and medium — Rawding sod house (photo), Golden Spike (photo), 1890 rail map (Census map), Tom Torlino (photos): all **Y/Y/Y**.
- **verify_dbq — Part B (document-set balance + provenance):** PASS (≥1 text + ≥1 visual, 6 docs, every doc has source + date).
- **verify_dbq — Part A (corpus file):** flags `.claude/skills/history-hack-dbq-workbook/assets/unit-1-sources.json` missing. That check guards the **ReportLab** engine (`build_workbook_template.py`), which this build does not use; the `.claude/skills/` tree is main-owned/read-only on work branches. The verbatim excerpts instead live inline in the workbook **and** in the committed `us01-homestead-sources.json`, satisfying the gate's intent (no excerpts trapped only inside a PDF). **Reconciliation:** update `verify_dbq.py` to accept the WeasyPrint/print-pipeline path (a committed workspace corpus) via a **skills-only PR to `main`** — flagged per `BUILD_PREFLIGHT.md` §"Format note."
- **Layout:** 13 / 4 / 5 pp (≤120 cap); body 10.6 pt (≥10.5); no orphan headings, no sparse/near-empty pages; America 250 palette; ™ (not ®); ISBN "[to be assigned]"; version timestamp in filename + on-page.

## Differentiation (3 inclusion sections + 2 honors sections)
- **Inclusion (★ Entry):** workbook **+** the Scaffold Companion; Plain-Language boxes + read-aloud; pre-taught EN/ES word bank; full HIPPO/OPTIC frames may stay in use; minimum 2 documents to meet the standard.
- **Honors (▲ Extension):** workbook only; the ▲ Honors extension question under each document plus the historiography prompt; independent sourcing from Doc B onward.
- Scaffold fading is built in: Docs A–B full frames → C–E reduced cues → F independent.
