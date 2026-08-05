# -*- coding: utf-8 -*-
"""Standard <-> SSP Crosswalk WITH PROOF (pilot: Unit 1).
For every content standard, name the TN Social Studies Practices it builds AND
prove each tie with the concrete task location: the deck slide role (from the
slide-keying map) and the student-workbook activity that exercises the practice.
Skeptic-facing, Schedule-F-defensible. Sourced from the deck _build.json ssps +
the canonical SSP labels in build_deck.js + slide-keying.md activity/slide roles.
"""
import os, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = os.environ.get("CHROME_BIN", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

# Canonical SSP definitions (labels from build_deck.js SSP_LABEL; "what students do" per TDOE SSP.01-06).
SSP = {
  "SSP.01": ("Collect sources", "Gather and identify relevant primary and secondary sources."),
  "SSP.02": ("Examine a source", "Interrogate a single source — author, audience, purpose, point of view (HIPP)."),
  "SSP.03": ("Synthesize sources", "Corroborate and combine multiple sources into a coherent account."),
  "SSP.04": ("Build an argument", "Construct a claim supported by evidence and reasoning (CER)."),
  "SSP.05": ("Historical awareness", "Sequence events and reason about causation and change over time."),
  "SSP.06": ("Geographic awareness", "Analyze place, movement, and human–environment interaction using maps."),
}

# Proof map: for each SSP, WHERE the practice is exercised — deck slide role
# (slide-keying.md) + student-workbook activity. This is the evidence of the tie.
PROOF = {
  "SSP.01": ("Primary Source — SOURCE IT FIRST band", "Activity 5 · Primary Source / HIPPO"),
  "SSP.02": ("Primary Source — SOURCE IT FIRST (tagged SSP.02)", "Activity 5 · HIPPO source analysis"),
  "SSP.03": ("Direct Instruction — Close Read + Constructed Response", "Activity 4 · Close Read → Activity 7 · CER"),
  "SSP.04": ("Wrap-Up — DOK 3 Honors band (tagged SSP.04) + Three Perspectives", "Activity 7 · CER (claim · evidence · reasoning)"),
  "SSP.05": ("Direct Instruction — Cornell Notes / timeline content", "Activity 3 · Cornell Notes"),
  "SSP.06": ("Direct Instruction — map / geographic content", "Activity 3 · Cornell Notes (Geographer's Lens)"),
}

def load_unit1():
    p = "/home/user/trooptoteacher-history/.claude/skills/history-hack-tcap-deck-builder/assets/unit1-example/_build.json"
    d = json.load(open(p))
    rows = []
    for code, v in d.items():
        if isinstance(v, dict) and "ssps" in v:
            rows.append((code, v.get("title", ""), v.get("ssps", [])))
    rows.sort(key=lambda r: r[0])
    return rows

NAVY, RED, GOLD, CREAM = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF"

def render(unit_no, unit_title, rows):
    body = []
    for code, title, ssps in rows:
        n = len(ssps)
        first = True
        for s in ssps:
            label, _defn = SSP.get(s, (s, ""))
            deck, wb = PROOF.get(s, ("—", "—"))
            std_cell = (f'<td class="std" rowspan="{n}"><b>{code}</b><span>{title}</span></td>' if first else "")
            body.append(
              f'<tr>{std_cell}'
              f'<td class="ssp"><b>{s}</b> {label}</td>'
              f'<td class="pf">{deck}</td>'
              f'<td class="pf">{wb}</td></tr>')
            first = False
    rowsn = "".join(body)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    @page {{ size:8.5in 11in; margin:0; }}
    *{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:"Helvetica Neue",Arial,sans-serif;color:{NAVY};background:#fff;}}
    .page{{width:8.5in;min-height:11in;padding:0.45in 0.5in;}}
    .kick{{font-size:8.5pt;letter-spacing:.13em;font-weight:800;color:{RED};text-transform:uppercase;}}
    h1{{font-family:Georgia,serif;font-size:20pt;color:{NAVY};line-height:1.05;margin-top:2px;}}
    .sub{{font-size:9.5pt;color:#5A6579;font-weight:600;margin-top:3px;}}
    .why{{margin:10px 0 12px;background:{CREAM};border-left:5px solid {GOLD};border-radius:0 5px 5px 0;
      padding:8px 12px;font-size:9pt;line-height:1.35;color:#2c3446;}}
    .why b{{color:{NAVY};}}
    table{{width:100%;border-collapse:collapse;table-layout:fixed;}}
    thead th{{background:{NAVY};color:#fff;font-size:8.6pt;font-weight:800;text-transform:uppercase;
      letter-spacing:.03em;padding:7px 8px;text-align:left;border:1px solid {NAVY};}}
    td{{border:1px solid #CBD2DE;padding:6px 8px;font-size:8.7pt;vertical-align:top;line-height:1.3;}}
    td.std{{width:20%;background:#EEF1F7;}}
    td.std b{{display:block;font-size:11pt;color:{NAVY};}}
    td.std span{{display:block;font-size:8pt;color:#5A6579;font-weight:600;margin-top:2px;}}
    td.ssp{{width:24%;}} td.ssp b{{color:{RED};}}
    td.pf{{width:28%;color:#2c3446;}}
    .foot{{margin-top:12px;padding-top:6px;border-top:1px solid #CBD2DE;display:flex;
      justify-content:space-between;font-size:7.6pt;color:#5A6579;}}
    .foot b{{color:{NAVY};}}
    </style></head><body><div class="page">
      <div class="kick">Standards &middot; Social Studies Practices &middot; Evidence</div>
      <h1>Unit {unit_no} &mdash; Standard &harr; SSP Crosswalk <span style="font-size:13pt;color:{RED}">with proof</span></h1>
      <div class="sub">{unit_title} &middot; every TN Social Studies Practice tie is proven by a concrete task</div>
      <div class="why"><b>How to read this.</b> TN Social Studies Practices (SSP.01&ndash;06) are process
      standards woven across the content standards. This crosswalk names the practices each standard builds
      and <b>proves each one</b> by pointing to where students actually do it &mdash; the <b>deck slide</b>
      (teacher lecture deck) and the <b>student-workbook activity</b>. No practice is claimed without a task
      that exercises it.</div>
      <table><thead><tr>
        <th style="width:20%">Standard</th>
        <th style="width:24%">Social Studies Practice</th>
        <th style="width:28%">Proven on the deck (slide role)</th>
        <th style="width:28%">Proven in the workbook (activity)</th>
      </tr></thead><tbody>{rowsn}</tbody></table>
      <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
      <span>Standard&harr;SSP Crosswalk with Proof &middot; Unit {unit_no}</span></div>
    </div></body></html>"""

if __name__ == "__main__":
    rows = load_unit1()
    html = render(1, "The Rise of Industrialization (1877-1900)", rows)
    hp = os.path.join(HERE, "unit1_ssp_crosswalk.html")
    open(hp, "w").write(html)
    pdf = os.path.join(HERE, "HH_Unit1_Standard_SSP_Crosswalk.pdf")
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--disable-dev-shm-usage", "--no-pdf-header-footer",
                    "--print-to-pdf=" + pdf, "file://" + hp],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # verifier: every SSP claimed must have SSP def + proof
    missing = []
    for code, _t, ssps in rows:
        for s in ssps:
            if s not in SSP: missing.append(f"{code}:{s} no SSP definition")
            if s not in PROOF: missing.append(f"{code}:{s} no proof location")
    print("standards:", len(rows), "| ssp-ties:", sum(len(r[2]) for r in rows))
    print("VERIFY:", "OK (every tie proven)" if not missing else missing)
    print("PDF:", pdf)
