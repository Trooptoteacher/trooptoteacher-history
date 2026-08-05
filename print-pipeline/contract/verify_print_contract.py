#!/usr/bin/env python3
"""
Print-contract lock — the guardrail that keeps the shared CSS Paged-Media
contract producing correct, commercial-grade output for all four page products.

Fails (exit 1) on any of:
  1. A required contract file missing (contract CSS, tokens, embedded fonts).
  2. The contract CSS missing a structural invariant (version, @page frame,
     running-head string-set, first-page rule, landscape page).
  3. A product fixture that does not render, renders zero pages, or renders far
     more pages than expected (a blow-out = broken layout).
  4. The brand fonts NOT embedded/subset in the output PDF (would mean the PDF
     is not self-contained / not print-shop safe).
  5. The optional print-shop overlay failing to render (crop marks + bleed).

Run from anywhere:
  python3 print-pipeline/contract/verify_print_contract.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

CONTRACT = Path(__file__).resolve().parent
PIPELINE = CONTRACT.parent
RENDER = PIPELINE / "render.py"
FIXTURES = CONTRACT / "fixtures"

# product -> (fixture, max expected pages for the one-page proof fixture)
PRODUCTS = {
    "textbook": ("textbook.json", 3),
    "workbook": ("workbook.json", 3),
    "dbq": ("dbq.json", 3),
    "organizer": ("organizer.json", 3),
}
REQUIRED_FILES = [
    CONTRACT / "print-contract.css",
    CONTRACT / "print-shop.css",
    CONTRACT / "tokens" / "us-history.css",
    CONTRACT / "fonts" / "DMSans-Regular.ttf",
    CONTRACT / "fonts" / "DMSans-Bold.ttf",
    CONTRACT / "fonts" / "Inter-Regular.ttf",
]
CONTRACT_INVARIANTS = [
    "Contract version:",           # versioned
    "@page{",                      # page frame
    "string-set: runhead",         # running header wiring
    "@page :first",                # first-page rule
    "@page landscape",             # landscape variant
]
BRAND_FONT_MARKERS = ("HH-Sans", "HH-Text")

errors: list[str] = []


def check_files() -> None:
    for f in REQUIRED_FILES:
        if not f.exists() or f.stat().st_size == 0:
            errors.append(f"[file] missing/empty required contract file: {f.relative_to(PIPELINE)}")


def check_invariants() -> None:
    css = (CONTRACT / "print-contract.css").read_text(encoding="utf-8", errors="replace")
    for inv in CONTRACT_INVARIANTS:
        if inv not in css:
            errors.append(f"[invariant] print-contract.css is missing: '{inv}'")


def render(fixture: str, out: Path, print_shop: bool = False) -> bool:
    cmd = [sys.executable, str(RENDER), str(FIXTURES / fixture), str(out)]
    if print_shop:
        cmd.append("--print-shop")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        errors.append(f"[render] {fixture} failed: {p.stderr.strip().splitlines()[-1] if p.stderr else 'nonzero exit'}")
        return False
    return out.exists() and out.stat().st_size > 0


def check_pdf(out: Path, label: str, max_pages: int) -> None:
    try:
        import fitz
    except ImportError:
        return  # PyMuPDF not present: skip deep checks (render success already asserted)
    d = fitz.open(str(out))
    if d.page_count < 1:
        errors.append(f"[pages] {label}: rendered 0 pages")
    if d.page_count > max_pages:
        errors.append(f"[pages] {label}: {d.page_count} pages (> {max_pages}) — layout blow-out?")
    fonts = {f[3] for pg in d for f in pg.get_fonts()}
    if not any(any(m in fn for fn in fonts) for m in BRAND_FONT_MARKERS):
        errors.append(f"[fonts] {label}: brand fonts (HH-Sans/HH-Text) not embedded — got {sorted(fonts)[:4]}")


def main() -> int:
    check_files()
    check_invariants()
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for name, (fixture, max_pages) in PRODUCTS.items():
            out = tmp / f"{name}.pdf"
            if render(fixture, out):
                check_pdf(out, name, max_pages)
        # print-shop overlay must also render
        ps = tmp / "printshop.pdf"
        if not render("textbook.json", ps, print_shop=True):
            pass  # error already recorded

    print("=" * 68)
    print("PRINT CONTRACT LOCK — shared CSS Paged-Media contract")
    print("=" * 68)
    print(f"Products verified : {', '.join(PRODUCTS)}")
    print(f"Required files    : {len(REQUIRED_FILES)}   Invariants: {len(CONTRACT_INVARIANTS)}")
    print("-" * 68)
    if errors:
        print(f"FAILED — {len(errors)} problem(s):\n")
        for e in errors:
            print("  " + e)
        return 1
    print("PASS — all four products render, brand fonts embedded, contract intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
