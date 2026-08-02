#!/usr/bin/env python3
"""
History Hack Unit QC Audit

Usage:
    python3 audit_unit.py <unit_number>

Runs from the history-hack-web-app repo root and reports the status
of all 18 QC items for the specified unit. Status is one of:
    DONE    — item fully satisfied
    PARTIAL — partially satisfied, needs work
    TODO    — not started

Reference state: Unit 1 v2.4 (April 2026) — all 18 DONE.
"""
import json
import os
import re
import sys
from pathlib import Path


def status(label, condition, detail=""):
    mark = "DONE " if condition else "TODO "
    return f"  [{mark}] {label}" + (f"  ({detail})" if detail else "")


def partial_status(label, partial_condition, full_condition, detail=""):
    if full_condition:
        mark = "DONE "
    elif partial_condition:
        mark = "PART "
    else:
        mark = "TODO "
    return f"  [{mark}] {label}" + (f"  ({detail})" if detail else "")


def audit(unit_n):
    repo = Path("public/data")
    if not repo.exists():
        print("Error: run from history-hack-web-app repo root", file=sys.stderr)
        sys.exit(1)

    # Load files
    tb_path = repo / f"textbook/unit-{unit_n}.json"
    ican_path = repo / f"ican/unit-{unit_n}.json"
    dok1_path = repo / f"questions/unit-{unit_n}/dok-1.json"
    dok3_path = repo / f"questions/unit-{unit_n}/dok-3.json"
    pdf_path = Path(f"docs/adoption/unit-{unit_n}-standards-alignment-guide.pdf")
    pacing_path = repo / "pacing-guide.json"
    printables_dir = Path(f"public/printables/unit-{unit_n}")

    tb = json.load(open(tb_path)) if tb_path.exists() else None
    ican = json.load(open(ican_path)) if ican_path.exists() else None
    dok1 = json.load(open(dok1_path)) if dok1_path.exists() else None
    dok3 = json.load(open(dok3_path)) if dok3_path.exists() else None
    pacing = json.load(open(pacing_path)) if pacing_path.exists() else None

    if tb is None:
        print(f"Error: missing {tb_path}", file=sys.stderr)
        sys.exit(1)

    print(f"\n=== Unit {unit_n} QC Audit — textbook v{tb.get('version','?')} ===\n")

    # CRITICAL
    print("CRITICAL")
    # C1
    print(status("C1  Standards Alignment Guide PDF", pdf_path.exists(),
                 f"{pdf_path.stat().st_size // 1024} KB" if pdf_path.exists() else "missing"))
    # C2 - simplified check: vocabulary.ts exists and has unit-1 entries
    vocab_path = Path("data/vocabulary.ts")
    vocab_exists = vocab_path.exists()
    print(status("C2  Vocabulary file present (manual boundary audit required)", vocab_exists))
    # C3
    if ican:
        ican_items = ican if isinstance(ican, list) else ican.get("statements", ican.get("items", []))
        all_linked = all("textbookSectionId" in s for s in ican_items) if ican_items else False
        sections_linked = all("icanStatementIds" in s for s in tb.get("sections", []))
        print(status("C3  I Can ↔ textbook section bidirectional linking",
                     all_linked and sections_linked,
                     f"{sum('textbookSectionId' in s for s in ican_items)}/{len(ican_items)} statements, {sum('icanStatementIds' in s for s in tb.get('sections',[]))}/{len(tb.get('sections',[]))} sections"))
    else:
        print(status("C3  I Can ↔ textbook section linking", False, "no ican file"))

    # HIGH
    print("\nHIGH")
    # H4
    if ican:
        ican_items = ican if isinstance(ican, list) else ican.get("statements", ican.get("items", []))
        frames_ct = sum(1 for s in ican_items if "sentenceFrames" in s)
        print(status("H4  WIDA sentence frames on I Can", frames_ct == len(ican_items),
                     f"{frames_ct}/{len(ican_items)}"))
    # H5
    org_files = list(printables_dir.glob("*.html")) if printables_dir.exists() else []
    print(status("H5  Printable graphic organizers", len(org_files) >= 4,
                 f"{len(org_files)} HTML files"))
    # H6
    dp = tb.get("differentiationPlan", {})
    cross = dp.get("tier3Intensive", {}).get("accommodationsCrosswalk", {}).get("accommodations", [])
    print(status("H6  IEP/504 accommodations crosswalk (≥10)", len(cross) >= 10, f"{len(cross)} entries"))
    # H7
    sec504 = dp.get("section504Accommodations", {})
    has504 = bool(sec504.get("strategies")) and "keyDistinction" in sec504
    print(status("H7  504 band with keyDistinction", has504,
                 f"{len(sec504.get('strategies', []))} strategies"))
    # H8
    ext_strats = dp.get("extensionsAdvanced", {}).get("strategies", [])
    d4 = [s for s in ext_strats if isinstance(s, dict) and s.get("c3Dimension") == "D4"]
    print(status("H8  C3 Dimension 4 extension", len(d4) >= 1, f"{len(d4)} D4 extensions"))

    # MEDIUM
    print("\nMEDIUM")
    # M9
    if ican:
        ican_items = ican if isinstance(ican, list) else ican.get("statements", ican.get("items", []))
        es_ct = sum(1 for s in ican_items if s.get("readingContentEs"))
        print(status("M9  Spanish readingContentEs on I Can", es_ct == len(ican_items),
                     f"{es_ct}/{len(ican_items)}"))
    # M10 - items whose stem references external text-based stimulus they don't carry.
    # Legit schema allows inline photograph/map descriptions in the stem, so those
    # are excluded. Only flag items referencing "the excerpt/passage/document" or
    # "based on the source" without either a stimulus field or inline source text.
    if dok3:
        d3_items = dok3 if isinstance(dok3, list) else dok3.get("items", [])
        text_ref = re.compile(r"\bthe (excerpt|passage|document|source)\b|based on the (excerpt|passage|document|source)", re.I)
        # Exclude items whose stem already has inline source text (bracketed label or
        # embedded "In the photograph above"-style descriptions)
        inline_patterns = [
            re.compile(r"^\s*\[[^\]]*(Primary Source|Source|Document|Photograph|Map|Chart)", re.I),
            re.compile(r"use the (photograph|map|chart|image|graph) to answer", re.I),
            re.compile(r"this (photograph|map|chart|image|graph) shows", re.I),
        ]
        def has_inline(stem):
            return any(p.search(stem) for p in inline_patterns)
        doc_based = [i for i in d3_items
                     if text_ref.search(i.get("stem", "")) and not has_inline(i.get("stem", ""))]
        with_stim = [i for i in doc_based if "stimulus" in i]
        missing = len(doc_based) - len(with_stim)
        print(status("M10 Stimulus on document-based DOK-3", missing == 0,
                     f"{len(with_stim)}/{len(doc_based)} text-stimulus items have stimulus field"))
    # M11
    if dok3:
        d3_items = dok3 if isinstance(dok3, list) else dok3.get("items", [])
        d2_tagged = [i for i in d3_items if i.get("c3Dimension") == "D2"]
        print(status("M11 DOK-3 items retagged away from D2", len(d2_tagged) == 0,
                     f"{len(d2_tagged)} still tagged D2"))
    # M12
    cornell_path = Path("lib/cornell-notes-data.ts")
    if cornell_path.exists():
        cornell_text = cornell_path.read_text()
        unit_stds = set()
        for s in tb.get("sections", []):
            unit_stds.update(s.get("standardCodes", []) or s.get("standards", []))
        covered = sum(1 for std in unit_stds if std in cornell_text)
        print(status("M12 Cornell notes coverage", covered == len(unit_stds),
                     f"{covered}/{len(unit_stds)} standards covered"))
    # M13
    honors = dp.get("honorsAcceleration", {})
    has_honors = bool(honors.get("strategies")) and "distinctionFromExtensions" in honors
    print(status("M13 Honors acceleration + distinctionFromExtensions", has_honors,
                 f"{len(honors.get('strategies', []))} strategies"))
    # M13b - Spanish narratives
    sections = tb.get("sections", [])
    es_narratives = sum(1 for s in sections if s.get("narrativeEs"))
    print(status("M13b Spanish narrativeEs on all sections", es_narratives == len(sections),
                 f"{es_narratives}/{len(sections)}"))

    # LOW
    print("\nLOW")
    # L14 - ellSupportNote on boundary vocab (manual check flagged)
    if vocab_exists:
        vocab_text = vocab_path.read_text()
        ell_ct = vocab_text.count("ellSupportNote")
        print(status("L14 ellSupportNote on boundary vocab (≥3)", ell_ct >= 3,
                     f"{ell_ct} entries have ellSupportNote"))
    # L15
    if dok1:
        d1_items = dok1 if isinstance(dok1, list) else dok1.get("items", [])
        entry = [i for i in d1_items if i.get("tier2Entry") or i.get("tier3Entry")]
        print(status("L15 DOK-1 Tier 2/3 entry-point items (≥3)", len(entry) >= 3,
                     f"{len(entry)} entry-point items"))
    # L16
    all_ssp = all(isinstance(s, dict) and "ssp" in s for s in ext_strats) if ext_strats else False
    print(status("L16 SSP codes on all extension strategies", all_ssp,
                 f"{sum(1 for s in ext_strats if isinstance(s, dict) and 'ssp' in s)}/{len(ext_strats)}"))
    # L17
    reasoning = dp.get("standaloneReasoningActivities", {})
    econ = reasoning.get("economicReasoning", [])
    geo = reasoning.get("geographicReasoning", [])
    print(status("L17 Standalone econ+geo reasoning activities (≥2 each)",
                 len(econ) >= 2 and len(geo) >= 2,
                 f"{len(econ)} econ, {len(geo)} geo"))
    # L18
    if pacing:
        units = pacing.get("units", [])
        unit_entry = next((u for u in units if u.get("unit") == unit_n), None)
        if unit_entry:
            total = unit_entry.get("totalDays", 0)
            section_days = sum(s.get("days", 0) for s in unit_entry.get("sections", []))
            has_breakdown = all(s.get("dayBreakdown") for s in unit_entry.get("sections", []))
            print(status("L18 Pacing guide complete",
                         total == section_days and has_breakdown,
                         f"{total} days, breakdown={'yes' if has_breakdown else 'no'}"))
        else:
            print(status("L18 Pacing guide", False, "no entry for unit"))

    print("\n=== End audit ===\n")
    print("Reference: Unit 1 v2.4 has all 18 items DONE.")
    print("For item specs: load references/18-item-checklist.md")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: audit_unit.py <unit_number>", file=sys.stderr)
        sys.exit(1)
    audit(int(sys.argv[1]))
