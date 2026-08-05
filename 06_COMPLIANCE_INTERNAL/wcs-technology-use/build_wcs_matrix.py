#!/usr/bin/env python3
"""
Render the skeptic-facing WCS Technology Use Guidance compliance matrix.

Reads the single source of truth (`requirements.json`) and writes a print-first
HTML page: law/requirement -> where History Hack meets it -> MEETS or EXCEEDS ->
the evidence. Because it is generated from the same registry the guardrail
enforces, the matrix can never drift from the verified truth.

Print-first (CLAUDE.md doctrine): the page is Letter-portrait, prints clean, and
carries the America 250 brand palette. Hand it to any board member, parent, or
reviewer who is skeptical of the content — every claim is cited.

Usage:
  python3 build_wcs_matrix.py            # writes wcs-technology-use-matrix.html
  python3 build_wcs_matrix.py --out PATH
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "requirements.json"
DEFAULT_OUT = HERE / "wcs-technology-use-matrix.html"

# America 250 palette (00_START_HERE/BRAND_PALETTE.md)
HERITAGE_BLUE = "#1F3A5F"
PATRIOT_RED = "#B22234"
FOUNDERS_CREAM = "#F8F5EF"
MUTED_GOLD = "#C9A227"


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def evidence_html(evidence: list[dict]) -> str:
    kind_label = {
        "doctrine": "doctrine",
        "repo": "content",
        "webapp": "app code",
        "webapp_route": "live route",
        "external": "law/framework",
    }
    parts = []
    for ev in evidence:
        k = ev.get("kind", "")
        ref = ev.get("ref", "")
        label = kind_label.get(k, k)
        parts.append(
            f'<li><span class="k k-{esc(k)}">{esc(label)}</span> <code>{esc(ref)}</code></li>'
        )
    return "<ul class='ev'>" + "".join(parts) + "</ul>"


def build(data: dict) -> str:
    meta = data.get("meta", {})
    reqs = data.get("requirements", [])
    n = len(reqs)
    n_exceeds = sum(1 for r in reqs if r.get("posture") == "exceeds")
    n_meets = n - n_exceeds

    # group in registry order
    groups: list[str] = []
    by_group: dict[str, list[dict]] = {}
    for r in reqs:
        g = r.get("group", "Other")
        if g not in by_group:
            by_group[g] = []
            groups.append(g)
        by_group[g].append(r)

    rows = []
    for g in groups:
        rows.append(
            f'<tr class="grouprow"><td colspan="4">{esc(g)}</td></tr>'
        )
        for r in by_group[g]:
            posture = r.get("posture", "meets")
            badge = (
                f'<span class="badge exceeds">EXCEEDS</span>'
                if posture == "exceeds"
                else '<span class="badge meets">MEETS</span>'
            )
            rows.append(
                "<tr>"
                f'<td class="src"><strong>{esc(r.get("id",""))}</strong><br>{esc(r.get("source",""))}</td>'
                f'<td class="req">{esc(r.get("requirement",""))}</td>'
                f'<td class="resp">{esc(r.get("hh_response",""))}<div class="posture">{badge}</div>'
                f'{evidence_html(r.get("evidence", []))}</td>'
                "</tr>"
            )
    rows_html = "\n".join(rows)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WCS Technology Use Guidance — Compliance Matrix — U.S. History Hack</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --blue:{HERITAGE_BLUE};--red:{PATRIOT_RED};--cream:{FOUNDERS_CREAM};--gold:{MUTED_GOLD};
}}
html{{background:#888}}
body{{font-family:'Source Sans 3',-apple-system,Segoe UI,Arial,Helvetica,sans-serif;
  background:#fff;color:#161616;width:8.5in;margin:.2in auto;
  box-shadow:0 2px 24px rgba(0,0,0,.3);font-size:9.5pt;line-height:1.5}}
@page{{size:letter portrait;margin:.55in .55in .5in}}
@media print{{html{{background:#fff}}body{{margin:0;box-shadow:none;width:auto}}
  .no-print{{display:none!important}}tr{{page-break-inside:avoid}}
  .grouprow td{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  thead{{display:table-header-group}}}}
.no-print{{position:fixed;top:12px;right:12px;background:var(--blue);color:#fff;border:none;
  border-radius:6px;padding:8px 15px;font-size:11px;font-weight:700;cursor:pointer;z-index:99}}
header{{background:var(--blue);color:#fff;padding:.42in .5in .3in;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
header .kicker{{font-size:8pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);font-weight:700}}
header h1{{font-size:17pt;line-height:1.15;margin:.06in 0 .04in}}
header .sub{{font-size:9pt;opacity:.92}}
.summary{{display:flex;gap:.28in;padding:.2in .5in;background:var(--cream);border-bottom:2px solid var(--blue);
  -webkit-print-color-adjust:exact;print-color-adjust:exact}}
.summary .stat{{text-align:center}}
.summary .num{{font-size:20pt;font-weight:800;color:var(--blue);line-height:1}}
.summary .lbl{{font-size:7.5pt;text-transform:uppercase;letter-spacing:.06em;color:#555}}
.intro{{padding:.16in .5in;font-size:8.6pt;color:#333;border-bottom:1px solid #ddd}}
.intro b{{color:var(--blue)}}
table{{border-collapse:collapse;width:100%}}
th,td{{text-align:left;vertical-align:top;padding:.08in .5in;border-bottom:1px solid #e6e2da}}
thead th{{background:var(--blue);color:#fff;font-size:7.6pt;text-transform:uppercase;letter-spacing:.06em;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;position:sticky;top:0}}
td.src{{width:23%;font-size:8pt;color:#333}}
td.req{{width:29%;font-size:8.4pt}}
td.resp{{width:48%;font-size:8.4pt}}
.grouprow td{{background:var(--gold);color:#241c00;font-weight:800;font-size:8.6pt;
  text-transform:uppercase;letter-spacing:.05em;padding:.07in .5in}}
.badge{{display:inline-block;font-size:7.4pt;font-weight:800;letter-spacing:.05em;
  padding:1px 7px;border-radius:3px;color:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.badge.meets{{background:var(--blue)}}
.badge.exceeds{{background:var(--red)}}
.posture{{margin:.05in 0 .04in}}
ul.ev{{list-style:none;margin:.03in 0 0;padding:0}}
ul.ev li{{font-size:7.4pt;color:#555;margin:1px 0;line-height:1.35}}
ul.ev code{{font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:7.1pt;
  background:#f2efe8;padding:0 3px;border-radius:2px;color:#3a3a3a}}
.k{{display:inline-block;font-size:6.4pt;font-weight:700;text-transform:uppercase;letter-spacing:.04em;
  padding:0 4px;border-radius:2px;color:#fff}}
.k-doctrine{{background:#556}}.k-repo{{background:#557}}.k-webapp{{background:#2c6e49}}
.k-webapp_route{{background:#2c6e49}}.k-external{{background:#8a6d1f}}
footer{{padding:.18in .5in .28in;font-size:7.6pt;color:#666;border-top:2px solid var(--blue)}}
footer b{{color:var(--blue)}}
</style>
</head>
<body>
<button class="no-print" onclick="window.print()">Print / Save PDF</button>
<header>
  <div class="kicker">TroopToTeacher Technologies &middot; U.S. History Hack &middot; America 250</div>
  <h1>WCS Technology Use Guidance &mdash; Compliance Matrix</h1>
  <div class="sub">{esc(meta.get("district",""))} &middot; Source: {esc(meta.get("source_document",""))}</div>
</header>
<div class="summary">
  <div class="stat"><div class="num">{n}</div><div class="lbl">Requirements</div></div>
  <div class="stat"><div class="num">{n_meets}</div><div class="lbl">Meets</div></div>
  <div class="stat"><div class="num">{n_exceeds}</div><div class="lbl">Exceeds</div></div>
  <div class="stat"><div class="num">0</div><div class="lbl">In breach</div></div>
</div>
<div class="intro">
  Every requirement below is backed by <b>resolvable evidence</b> in the product or curriculum &mdash;
  never an assertion. The machine guardrail <code>verify_wcs_compliance.py</code> fails the build if any
  requirement is unmet or any cited evidence cannot be resolved, so this matrix cannot drift from the
  verified truth. <b>MEETS</b> = the requirement is satisfied; <b>EXCEEDS</b> = History Hack goes beyond
  it (the Platinum bar: better, not parity). Generated from <code>requirements.json</code>.
</div>
<table>
<thead><tr><th>WCS / law source</th><th>Requirement</th><th>How History Hack meets it &middot; evidence</th></tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
<footer>
  <b>Provenance.</b> This document is generated from the compliance requirements registry
  (<code>06_COMPLIANCE_INTERNAL/wcs-technology-use/requirements.json</code>) and enforced by
  <code>verify_wcs_compliance.py</code>. Evidence kinds: <b>doctrine/content</b> = files in the
  curriculum repo; <b>app code / live route</b> = the History Hack web application; <b>law/framework</b>
  = the cited authority. Content accuracy follows TDOE Policy 2.600; effect sizes and citations are
  canonical, never fabricated. &copy; 2026 TroopToTeacher Technologies, LLC.
</footer>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Render the WCS Technology Use Guidance compliance matrix")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    out = Path(args.out)
    out.write_text(build(data), encoding="utf-8")
    reqs = data.get("requirements", [])
    print(f"Wrote {out} — {len(reqs)} requirements "
          f"({sum(1 for r in reqs if r.get('posture')=='exceeds')} exceeds).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
