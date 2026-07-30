# -*- coding: utf-8 -*-
"""Generate the district-facing UDL 3.0 + MTSS alignment crosswalk (HTML) from
udl_mtss_alignment.json. One source of truth -> the machine-readable map (data)
and this human-readable adoption-defensibility document."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "05_STANDARDS_ALIGNMENT", "udl_mtss_alignment.json")
OUT = os.path.join(HERE, "udl-mtss-framework.html")
A = json.load(open(DATA))

def esc(x): return html.escape(str(x), quote=False)
BADGE = {"present_strong": ('s2','Designed in'), "present_weak": ('s1','Partial'), "absent": ('s0','Gap')}

def rows_for(section):
    out = []
    for gkey, gval in section.items():
        if gkey in ("principle",): continue
        gname = gkey.split("_", 2)[-1].replace("_", " ").title()
        gnum = gkey.split("_")[1]
        first = True
        cons = [(k, v) for k, v in gval.items()]
        for ckey, cval in cons:
            cls, lbl = BADGE[cval["score"]]
            cnum = ckey.split("_")[0]
            cname = " ".join(ckey.split("_")[1:]).replace("-", " ").title()
            ev = "".join(f"<li>{esc(e)}</li>" for e in cval["evidence"])
            glabel = f'<td rowspan="{len(cons)}" class="gl"><b>{gnum}. {esc(gname)}</b></td>' if first else ""
            out.append(f'<tr>{glabel}<td class="cn">{esc(cnum)} {esc(cname)}</td>'
                       f'<td><span class="{cls}">{lbl}</span></td><td><ul>{ev}</ul></td></tr>')
            first = False
    return "\n".join(out)

def principle_block(key, title):
    sec = A["udl"][key]
    return f"""<h2>{title}</h2>
<p class="pp">{esc(sec['principle'])}</p>
<table><thead><tr><th style="width:20%">Guideline</th><th style="width:20%">Consideration</th><th style="width:12%">Status</th><th>Evidence in the course build</th></tr></thead>
<tbody>{rows_for(sec)}</tbody></table>"""

mtss = A["mtss"]
def mtss_block(k):
    m = mtss[k]
    ev = "".join(f"<li>{esc(e)}</li>" for e in m["evidence"])
    return f'<tr><td class="gl"><b>{esc(k.replace("_"," ").title())}</b></td><td>{esc(m["description"])}</td><td><ul>{ev}</ul></td></tr>'

contract = "".join(f"<li>{esc(c)}</li>" for c in A["design_contract"])
D = A["defensibility"]
defrows = "".join(f'<tr><td class="gl"><b>{esc(k.upper()) if len(k)<=4 else esc(k.title())}</b></td><td>{esc(v)}</td></tr>'
                  for k, v in D.items() if k != "boundary")

HTML = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>UDL 3.0 + MTSS Framework Alignment — Foundations of Constitutional Government</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,serif;background:#f5f5f3;color:#111;font-size:10.5pt;line-height:1.6}}
.topbar{{background:#1B2A4A;color:#fff;padding:10px 20px;display:flex;justify-content:space-between;align-items:center}}
.topbar .brand{{font-family:Arial,sans-serif;font-size:11px;color:rgba(255,255,255,.7)}}
.hero{{background:#1B2A4A;color:#fff;padding:26px 24px;text-align:center;border-bottom:4px solid #B22234}}
.hero h1{{font-family:Arial,sans-serif;font-size:clamp(16px,3vw,23px);font-weight:700}}
.hero .sub{{font-family:Arial,sans-serif;font-size:12px;color:#B5D4F4;margin-top:4px}}
.content{{max-width:1000px;margin:0 auto;padding:24px 20px 48px}}
h2{{font-family:Arial,sans-serif;font-size:14pt;color:#1B2A4A;margin:26px 0 4px;padding-bottom:4px;border-bottom:2px solid #1B2A4A}}
.pp{{font-style:italic;color:#3D2200;margin-bottom:8px;font-size:9.5pt}}
blockquote{{border-left:4px solid #C9A227;background:#fffdf5;padding:10px 16px;margin:12px 0;border-radius:0 4px 4px 0;font-style:italic;color:#3D2200}}
table{{width:100%;border-collapse:collapse;margin:8px 0 14px;font-size:9pt;font-family:Arial,sans-serif}}
th{{background:#1B2A4A;color:#fff;padding:7px 9px;text-align:left;font-size:8.5pt}}
td{{padding:6px 9px;border-bottom:1px solid #ddd;vertical-align:top}}
td.gl{{background:#EEF1F7;color:#1B2A4A;width:18%}}
td.cn{{font-weight:700;color:#2A3F5E;width:20%}}
ul{{margin:0 0 0 15px}} li{{margin-bottom:2px}}
.s2{{background:#1e5631;color:#fff;font-weight:700;text-align:center;border-radius:3px;padding:1px 7px;white-space:nowrap;font-size:8pt}}
.s1{{background:#C9A227;color:#3D2200;font-weight:700;text-align:center;border-radius:3px;padding:1px 7px;white-space:nowrap;font-size:8pt}}
.s0{{background:#8a2a2a;color:#fff;font-weight:700;text-align:center;border-radius:3px;padding:1px 7px;white-space:nowrap;font-size:8pt}}
.contract{{background:#fffdf5;border:1.5px solid #C9A227;border-radius:6px;padding:12px 16px 12px 30px}}
.boundary{{background:#FBEEEF;border-left:4px solid #B22234;padding:10px 14px;margin:12px 0;border-radius:0 4px 4px 0;font-size:9.5pt}}
footer{{background:#1B2A4A;color:rgba(255,255,255,.6);text-align:center;padding:16px;font-family:Arial,sans-serif;font-size:10px}}
footer strong{{color:#C9A227}}
@media print{{tr{{break-inside:avoid}}}}
</style></head><body>
<div class="topbar"><span>UDL 3.0 + MTSS Framework Alignment</span>
<span class="brand">TroopToTeacher Technologies LLC · © 2026 · District Review</span></div>
<div class="hero"><h1>Universal Design for Learning (3.0) &amp; MTSS — Framework Alignment</h1>
<div class="sub">Foundations of Constitutional Government · United States Government &amp; Civics (GC) · District adoption defensibility</div></div>
<div class="content">
<blockquote>{esc(A['_meta']['principle'])} This document maps the course's design decisions to the
<b>CAST UDL Guidelines version 3.0</b> (all nine guidelines, thirty considerations) and to a three-tier
<b>MTSS</b> model. UDL and MTSS are built in as frameworks — largely invisible on the page to teacher and
student, but explicit and reviewable here. <b>Firm goals, flexible means:</b> the means vary; the TN GC
standard and Social Studies Practices never do.</blockquote>
<p style="font-size:9pt;color:#555"><b>Sources of truth.</b> Framework map: <code>05_STANDARDS_ALIGNMENT/udl_mtss_alignment.json</code>
(machine-readable). UDL: {esc(A['_meta']['udl_citation'])} MTSS: {esc(A['_meta']['mtss_model'])}</p>

{principle_block('engagement','Principle 1 — Engagement (the WHY of learning)')}
{principle_block('representation','Principle 2 — Representation (the WHAT of learning)')}
{principle_block('action_expression','Principle 3 — Action &amp; Expression (the HOW of learning)')}

<h2>MTSS — Multi-Tiered System of Supports</h2>
<p class="pp">Supports are designed into the core materials, tiered by need, and driven by progress-monitoring data.</p>
<table><thead><tr><th style="width:18%">Tier</th><th style="width:32%">Role</th><th>Evidence in the course build</th></tr></thead>
<tbody>{mtss_block('tier_1_universal')}{mtss_block('tier_2_targeted')}{mtss_block('tier_3_intensive')}{mtss_block('progress_monitoring')}</tbody></table>

<h2>Design Contract (held on every future unit)</h2>
<ul class="contract">{contract}</ul>

<h2>Adoption Defensibility</h2>
<table><thead><tr><th style="width:14%">Population</th><th>How the design meets it</th></tr></thead><tbody>{defrows}</tbody></table>
<div class="boundary"><b>The UDL / modification boundary:</b> {esc(D['boundary'])}</div>

<p style="font-size:9pt;color:#555;margin-top:14px"><em>Internal framework-alignment document for district curriculum review. Not a claim of state, waiver, or Textbook Commission approval. UDL Guidelines © CAST, used as an alignment reference.</em></p>
</div>
<footer><strong>TroopToTeacher Technologies LLC</strong> · Foundations of Constitutional Government · UDL 3.0 + MTSS Framework Alignment · © 2026</footer>
</body></html>"""

with open(OUT, "w") as f:
    f.write(HTML)
print("wrote", OUT, f"({len(HTML)//1024} KB)")
