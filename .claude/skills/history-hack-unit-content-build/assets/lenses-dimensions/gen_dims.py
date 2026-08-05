# -*- coding: utf-8 -*-
"""Dimension (strand) Coverage Crosswalk — PROOF OF COVERAGE.
Canonical per-standard TDOE dimension tags (C/E/G/H/P/T/TCA), sourced verbatim
from Live-US-History-Standards-in-order-1-95.docx. Renders (1) the course-wide
coverage crosswalk grouped by unit + a coverage matrix, and (2) a mock of the
per-standard pill row as it will appear on the workbook opener / deck divider.
"""
import os, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = os.environ.get("CHROME_BIN", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
C = json.load(open(os.path.join(HERE, "standard_to_dimensions.json")))
LEG = C["_legend"]; STD = C["standards"]
NAVY, RED, GOLD, CREAM = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF"
UNIT_TITLE = {1:"The Rise of Industrialization",2:"The Progressive Era",3:"Imperialism & WWI",4:"The 1920s",
  5:"Great Depression & New Deal",6:"World War II",7:"Cold War",8:"A Nation in Transition",
  9:"Civil Rights Movement",10:"The Modern United States"}
ORDER = ["C","E","G","H","P","T","TCA"]

def pill(code):
    bg = {"T":GOLD,"TCA":RED}.get(code, NAVY)
    fg = NAVY if code=="T" else "#fff"
    return f'<span class="pill" style="background:{bg};color:{fg}">{code}</span>'

def pills(codes):
    return "".join(pill(c) for c in ORDER if c in codes)

def legend_row():
    return " ".join(f'{pill(c)}<span class="lgt">{LEG[c]}</span>' for c in ORDER)

def coverage_counts():
    from collections import Counter
    cnt = Counter(x for s in STD.values() for x in s["dimensions"])
    return cnt

def crosswalk_html():
    cnt = coverage_counts()
    cov = " ".join(f'{pill(c)}<b>{cnt.get(c,0)}</b><span class="cvl">/95</span>' for c in ORDER)
    rows = []
    for u in range(1, 11):
        us = [(k, v) for k, v in STD.items() if v["unit"] == u]
        us.sort(key=lambda kv: kv[0])
        rows.append(f'<tr class="uh"><td colspan="3">Unit {u} &middot; {UNIT_TITLE[u]}</td></tr>')
        for code, v in us:
            rows.append(f'<tr><td class="c">{code}</td><td class="t">{v["title"]}</td>'
                        f'<td class="p">{pills(v["dimensions"])}</td></tr>')
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    @page{{size:8.5in 11in;margin:0;}} *{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:"Helvetica Neue",Arial,sans-serif;color:{NAVY};}}
    .page{{width:8.5in;padding:0.45in 0.5in;}}
    .kick{{font-size:8.5pt;letter-spacing:.13em;font-weight:800;color:{RED};text-transform:uppercase;}}
    h1{{font-family:Georgia,serif;font-size:20pt;margin-top:2px;}}
    .sub{{font-size:9.5pt;color:#5A6579;font-weight:600;margin-top:3px;}}
    .pill{{display:inline-block;min-width:15px;text-align:center;font-size:8pt;font-weight:800;
      padding:1.5px 5px;border-radius:9px;margin-right:3px;}}
    .legend{{margin:10px 0;background:{CREAM};border-left:5px solid {GOLD};border-radius:0 5px 5px 0;
      padding:8px 12px;font-size:8.6pt;line-height:2;}} .lgt{{margin:0 12px 0 2px;color:#2c3446;}}
    .cov{{margin:8px 0 12px;padding:8px 12px;border:1.5px solid {NAVY};border-radius:6px;font-size:9pt;}}
    .cov b{{font-size:11pt;}} .cov .cvl{{color:#5A6579;font-size:7.5pt;margin-right:14px;}}
    .cov .lbl{{font-weight:800;color:{NAVY};text-transform:uppercase;font-size:8pt;letter-spacing:.05em;margin-right:10px;}}
    table{{width:100%;border-collapse:collapse;table-layout:fixed;}}
    td{{border:1px solid #CBD2DE;padding:4px 8px;font-size:8.6pt;vertical-align:top;}}
    tr.uh td{{background:{NAVY};color:#fff;font-weight:800;font-size:9pt;border:1px solid {NAVY};padding:5px 8px;}}
    td.c{{width:12%;font-weight:800;color:{NAVY};}} td.t{{width:58%;color:#2c3446;}} td.p{{width:30%;}}
    .foot{{margin-top:12px;padding-top:6px;border-top:1px solid #CBD2DE;display:flex;justify-content:space-between;font-size:7.5pt;color:#5A6579;}}
    .foot b{{color:{NAVY};}}
    </style></head><body><div class="page">
      <div class="kick">Standards &middot; Disciplinary Dimensions &middot; Coverage</div>
      <h1>US History &mdash; Dimension Coverage Crosswalk <span style="font-size:13pt;color:{RED}">proof</span></h1>
      <div class="sub">Every standard's TDOE disciplinary dimensions (C/E/G/H/P/T/TCA), sourced verbatim from the Tennessee standards</div>
      <div class="legend"><b style="color:{NAVY}">Legend &mdash; </b>{legend_row()}</div>
      <div class="cov"><span class="lbl">Coverage across 95 standards</span>{cov}</div>
      <table>{''.join(rows)}</table>
      <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
      <span>Dimension Coverage Crosswalk &middot; sourced from Live US History Standards 1&ndash;95</span></div>
    </div></body></html>"""

def pill_mock_html():
    """How the per-standard Coverage pill row looks on the workbook opener / deck divider."""
    ex = STD["US.03"]
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    *{{box-sizing:border-box;margin:0;padding:0;font-family:"Helvetica Neue",Arial,sans-serif;}}
    body{{background:#8a8f99;padding:20px;}}
    .card{{width:6.6in;background:{CREAM};border:1px solid #CBD2DE;border-top:5px solid {NAVY};
      border-radius:6px;padding:16px 20px;margin:0 auto;}}
    .code{{font-family:Georgia,serif;font-size:15pt;font-weight:700;color:{NAVY};}}
    .std{{font-size:9.5pt;color:#2c3446;margin:4px 0 10px;line-height:1.35;}}
    .row{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:8px;}}
    .rl{{font-size:7.6pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#5A6579;}}
    .pill{{display:inline-block;font-size:8.2pt;font-weight:800;padding:2px 8px;border-radius:10px;}}
    .pd{{display:inline-flex;align-items:center;gap:4px;}}
    .pd small{{font-size:7.6pt;color:#5A6579;font-weight:600;}}
    </style></head><body>
    <div class="card">
      <div class="code">US.03</div>
      <div class="std">{ex['title']} &mdash; Explain the impact of the Compromise of 1877 (Jim Crow, disenfranchisement, Exodusters, <i>Plessy v. Ferguson</i>).</div>
      <div class="row"><span class="rl">Lenses</span>
        {' '.join(f'<span class="pd">{pill(c)}<small>{LEG[c].split("/")[0].split(" (")[0]}</small></span>' for c in ORDER if c in ex['dimensions'])}
      </div>
    </div></body></html>"""

if __name__ == "__main__":
    def render(html, base, win_h=1180):
        hp = os.path.join(HERE, base + ".html"); open(hp, "w").write(html)
        pdf = os.path.join(HERE, base + ".pdf")
        subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
            "--disable-dev-shm-usage","--no-pdf-header-footer","--print-to-pdf="+pdf,"file://"+hp],
            stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        from PIL import Image
        raw=os.path.join(HERE,"_"+base+".png")
        subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
            "--disable-dev-shm-usage","--force-device-scale-factor=2",f"--window-size=816,{win_h}",
            "--screenshot="+raw,"file://"+hp],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        Image.open(raw).convert("RGB").save(os.path.join(HERE,base+".png")); os.remove(raw)
        return pdf
    render(crosswalk_html(), "HH_Dimension_Coverage_Crosswalk", 1180)
    render(pill_mock_html(), "pill_mock", 360)
    # verifier
    VALID=set("C E G H P T TCA".split())
    bad=[k for k,v in STD.items() if not v["dimensions"] or any(x not in VALID for x in v["dimensions"])]
    print("standards:",len(STD),"| invalid:",bad,"| VERIFY:", "OK" if not bad else "FAIL")
    print("coverage:", dict(coverage_counts()))
