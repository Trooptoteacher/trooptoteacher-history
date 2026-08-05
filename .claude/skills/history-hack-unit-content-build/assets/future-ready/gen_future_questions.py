# -*- coding: utf-8 -*-
"""Future Ready — embedded reflective questions + the loan-cost math/chart.
(1) A recurring 'Future Ready Question' callout, shown tied to REAL U.S. History
    standards (the historical content sets up the student's own after-HS decision).
(2) 'The Real Cost of Borrowing' — an accurate, computed student-loan chart (SVG),
    a do-the-math box, and FAFSA/scholarship literacy. Data-viz per WORKBOOK §7.11:
    original + sourced + honest axes + alt text + plain-table fallback.
America 250 palette; Chromium --print-to-pdf.
"""
import os, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = os.environ.get("CHROME_BIN", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
NAVY, RED, GOLD, CREAM, LINE = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF", "#9AA0AB"

# Single source of truth for time-sensitive figures (see future_ready_data.json /
# verify_future_ready_currency.py). Never hard-code a rate below — read it here.
DATA = json.load(open(os.path.join(HERE, "future_ready_data.json")))
_TS = DATA["time_sensitive"]
RATE_BY_YEAR = _TS["direct_loan_rates_undergrad"]["by_year"]
EXAMPLE_APR = _TS["chart_example_apr"]["value"]
PELL_MAX = _TS["pell_max"]["value"]
PELL_AS_OF = _TS["pell_max"]["as_of"]
RATE_HISTORY = " &middot; ".join(
    f'<b>{v:.2f}%</b> (\'{yr[2:4]}&ndash;{yr[5:7]})' for yr, v in sorted(RATE_BY_YEAR.items()))

# ---- loan math (federal Direct Loan example rate) -------------------------
def pay(P, r, months):
    i = r/12
    return P*i/(1-(1+i)**-months)
P, R = 30000, EXAMPLE_APR/100.0
TERMS = [5,10,15,20]
LOAN = []
for y in TERMS:
    m=y*12; M=pay(P,R,m); tot=M*m
    LOAN.append(dict(yrs=y, M=M, total=tot, interest=tot-P, pct=100*(tot-P)/P))

# ---- SVG stacked-bar chart: principal (same) + interest (grows) -----------
def svg_chart():
    W,Hh = 660, 232
    padL,padB,padT,padR = 52, 40, 16, 14
    plotH = Hh-padB-padT; plotW = W-padL-padR
    ymax = 60000
    def y(v): return padT+plotH*(1-v/ymax)
    bars=[]
    n=len(LOAN); slot=plotW/n; bw=slot*0.5
    # gridlines
    grid=[]
    for gv in range(0,60001,15000):
        gy=y(gv)
        grid.append(f'<line x1="{padL}" y1="{gy:.1f}" x2="{W-padR}" y2="{gy:.1f}" stroke="#E1E5EC" stroke-width="1"/>')
        grid.append(f'<text x="{padL-7}" y="{gy+3:.1f}" text-anchor="end" font-size="9" fill="#5A6579">${gv//1000}k</text>')
    for k,d in enumerate(LOAN):
        cx=padL+slot*k+slot/2; x0=cx-bw/2
        yP=y(P); yT=y(d['total'])
        # principal segment (bottom)
        bars.append(f'<rect x="{x0:.1f}" y="{yP:.1f}" width="{bw:.1f}" height="{(padT+plotH-yP):.1f}" fill="{NAVY}"/>')
        # interest segment (top)
        bars.append(f'<rect x="{x0:.1f}" y="{yT:.1f}" width="{bw:.1f}" height="{(yP-yT):.1f}" fill="{RED}"/>')
        # total label
        bars.append(f'<text x="{cx:.1f}" y="{yT-5:.1f}" text-anchor="middle" font-size="10.5" font-weight="700" fill="{NAVY}">${d["total"]/1000:.1f}k</text>')
        # interest callout inside red
        bars.append(f'<text x="{cx:.1f}" y="{(yT+ (yP-yT)/2 +3):.1f}" text-anchor="middle" font-size="8.5" font-weight="700" fill="#fff">+${d["interest"]/1000:.1f}k</text>')
        # x label
        bars.append(f'<text x="{cx:.1f}" y="{padT+plotH+16:.1f}" text-anchor="middle" font-size="9.5" font-weight="700" fill="{NAVY}">{d["yrs"]} yrs</text>')
        bars.append(f'<text x="{cx:.1f}" y="{padT+plotH+28:.1f}" text-anchor="middle" font-size="8" fill="#5A6579">${d["M"]:.0f}/mo</text>')
    axis=(f'<line x1="{padL}" y1="{padT}" x2="{padL}" y2="{padT+plotH}" stroke="{NAVY}" stroke-width="1.5"/>'
          f'<line x1="{padL}" y1="{padT+plotH}" x2="{W-padR}" y2="{padT+plotH}" stroke="{NAVY}" stroke-width="1.5"/>')
    leg=(f'<rect x="{padL}" y="0" width="11" height="11" fill="{NAVY}"/><text x="{padL+15}" y="9.5" font-size="9" fill="#2c3446">What you borrowed ($30k)</text>'
         f'<rect x="{padL+165}" y="0" width="11" height="11" fill="{RED}"/><text x="{padL+180}" y="9.5" font-size="9" fill="#2c3446">Interest you add on top</text>')
    return (f'<svg viewBox="0 0 {W} {Hh+16}" width="100%" role="img" '
            f'aria-label="Stacked bar chart: a $30,000 student loan at 6.5%. Total repaid is $35k over 5 years, '
            f'$41k over 10 years, $47k over 15 years, and $54k over 20 years. The longer the term, the more interest you add.">'
            f'<g transform="translate(0,4)">{leg}</g><g transform="translate(0,14)">{"".join(grid)}{axis}{"".join(bars)}</g></svg>')

# ---- Future Ready Question callouts, tied to REAL standards ----------------
QCARDS = [
  ("US.05", "Unit 1 &middot; Gilded Age",
   "Carnegie arrived poor, learned a trade, then built the richest company in America.",
   ["What's <b>your</b> path after high school &mdash; trade, college, or military?",
    "If a trade: <b>which one</b>, and have you looked up what it pays?"]),
  ("US.33", "Unit 5 &middot; The New Deal",
   "The CCC <i>paid</i> young people to work <i>and</i> learn a skill &mdash; debt-free.",
   ["Could an <b>apprenticeship</b> be your fast, low-debt path?",
    "Have you looked at <b>free-college</b> or work-study programs in Tennessee?"]),
  ("US.58", "Unit 6 &middot; WWII &amp; the GI Bill",
   "By 1956 the 1944 GI Bill sent <b>7.8 million</b> WWII veterans to school &mdash; for free.",
   ["Your version is the <b>FAFSA</b> + scholarships + military benefits.",
    "Have you <b>started your FAFSA</b>? Do you know when it opens?"]),
  ("US.68", "Unit 7 &middot; Cold War / Space Race",
   "After Sputnik, the U.S. poured billions into math &amp; science <b>scholarships</b>.",
   ["What scholarships do <b>you</b> qualify for <i>right now</i>?",
    "Do you know <b>how to find them</b> (counselor, college aid office)?"]),
  ("US.25", "Unit 4 &middot; The 1920s",
   "The Roaring Twenties ran on &ldquo;buy now, pay later&rdquo; &mdash; and helped crash the economy.",
   ["Before you sign a <b>student loan</b>, do you know what $30,000 really costs?",
    "Are you planning a <b>gap / travel year</b>? Where, why, and how paid for?"]),
  ("US.71", "Unit 8 &middot; A Nation in Transition",
   "Every generation re-decides how it serves the country.",
   ["Do you plan on <b>joining the military</b>? If so, which <b>branch</b> &mdash; and why?",
    "What would that path pay for that another path wouldn't?"]),
]

def qcard(std, unit, hook, qs):
    ql = "".join(f'<li>{q}</li>' for q in qs)
    return f"""<div class="q">
      <div class="qtop"><span class="qtag">Future Ready&nbsp;?</span><span class="qstd">tied to {std}</span><span class="qunit">{unit}</span></div>
      <div class="qhook">{hook}</div>
      <ul class="qq">{ql}</ul>
      <div class="qjot">Jot a first thought &rarr; <span class="ln"></span></div>
    </div>"""

def questions_html():
    cards = "".join(qcard(*c) for c in QCARDS)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Future Ready &middot; Embedded Questions</div>
    <h1>Future Ready Questions &mdash; the pop-up that ties history to <i>your</i> next move</h1>
    <div class="sub">A small callout that surfaces every few lessons. It hangs the student's own after-high-school decision on the <b>exact standard</b> being taught &mdash; no new class time, real reflection.</div></div>
    <div class="stamp"><span>ASK</span><b>?</b></div></div>
  <div class="qgrid">{cards}</div>
  <div class="rulebar"><b>Placement rule (build plan):</b> seed <b>2&ndash;3 per unit</b>, only on standards whose
    content gives a natural hook (wealth &amp; mobility, the GI Bill, the Space Race, consumer debt). Never force one
    onto every standard. Each rolls up to the student's <i>My SMART Goals</i> &amp; Debrief reflection.</div>
  <div class="qsrc"><b>Sources for the historical hooks.</b> GI Bill &mdash; 7.8M WWII veterans used education/training
    benefits by 1956, of 15.4M eligible (U.S. Dept. of Veterans Affairs; National Archives, <i>Servicemen's Readjustment Act</i>).
    NDEA of 1958 funded post-Sputnik student loans &amp; science/math/language scholarships (U.S. House, History &amp; Archives).
    CCC employed ~3M young men, 1933&ndash;42, with camp education/vocational training (National Archives, RG 35). Carnegie &mdash;
    <i>Autobiography of Andrew Carnegie</i>.</div>
  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>Future Ready &middot; UDL 3.0 (CAST 2024) &middot; Embedded Questions</span></div>
</div></body></html>"""

def loan_html():
    l10 = next(d for d in LOAN if d['yrs']==10)
    tbl = "".join(f'<tr><td>{d["yrs"]} years</td><td>${d["M"]:,.0f}</td><td>${d["total"]:,.0f}</td>'
                  f'<td>${d["interest"]:,.0f}</td><td>{d["pct"]:.0f}%</td></tr>' for d in LOAN)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Future Ready &middot; Money Math</div>
    <h1>The Real Cost of Borrowing &mdash; Do the Math Before You Sign</h1>
    <div class="sub">Tied to <b>US.25 &middot; the 1920s</b> (buy-now-pay-later). A loan isn't the sticker price &mdash; it's the sticker price <i>plus interest, for years</i>. Read the chart, then run the numbers yourself.</div></div>
    <div class="stamp"><span>OWE</span><b>$$</b></div></div>

  <div class="bigstat">Borrow <b>$30,000</b> at <b>6.5%</b> for <b>10 years</b> &rarr; you pay back
    <b class="rd">${l10['total']:,.0f}</b> &mdash; that's <b class="rd">${l10['interest']:,.0f}</b> of interest,
    <b>{l10['pct']:.0f}% more</b> than you borrowed.</div>

  <div class="card wide"><div class="h">What a $30,000 loan really costs <span class="scale">same loan, different payoff terms &middot; 6.5% APR</span></div>
    {svg_chart()}
    <div class="sources"><div class="sh">Sources &amp; Method &mdash; the evidence behind this chart</div>
      <div class="sgrid">
        <div><b>Interest-rate data.</b> Federal Direct Loan rates are <i>fixed</i>, set each May by Congress
          (10-yr Treasury + a set margin) and published by the U.S. Dept. of Education &mdash; Federal Student Aid.
          Recent undergraduate (Direct Subsidized/Unsubsidized) rates: {RATE_HISTORY}.
          Chart uses <b>{EXAMPLE_APR}%</b> as a representative example.
          <span class="cite">studentaid.gov &middot; fsapartners.ed.gov (EA 2025-05-30)</span></div>
        <div><b>Method.</b> Fixed-rate amortization &mdash; <span class="mono">M = P&middot;i&frasl;(1&minus;(1+i)<sup>&minus;n</sup>)</span>,
          where P = $30,000, <b>i = APR &divide; 12</b> (monthly rate), <b>n = number of monthly payments</b>.
          Total repaid = M&middot;n; interest = total &minus; P. No loan fees or interest capitalization modeled.</div>
        <div><b>Computed figures (USD).</b> {" &middot; ".join(f'{d["yrs"]} yr &rarr; ${d["total"]:,.0f} (int ${d["interest"]:,.0f})' for d in LOAN)}.
          Single $30,000 loan; a student's actual rate, fees &amp; repayment plan will differ.</div>
      </div>
      <div class="verif">Figures corroborated against U.S. Dept. of Education / Federal Student Aid, the U.S. Dept. of
        Veterans Affairs, and the National Archives; exact page values get a final human source-check at publish (Policy 2.600).</div>
    </div>
  </div>

  <div class="two">
    <div class="card"><div class="h">Your Turn &mdash; Run the Numbers</div>
      <div class="frm">Monthly payment: <span class="mono">M = P &times; i &frasl; (1 &minus; (1+i)<sup>&minus;n</sup>)</span><br>
        <small>P = amount borrowed &middot; i = APR &divide; 12 &middot; n = months</small></div>
      <div class="lab">A friend borrows <b>$15,000</b> at <b>6.5%</b> for <b>10 years</b> (n = 120):</div>
      <div class="rowk"><span class="k">Monthly payment M &asymp; $</span><span class="ln2"></span></div>
      <div class="rowk"><span class="k">Total paid (M &times; 120) &asymp; $</span><span class="ln2"></span></div>
      <div class="rowk"><span class="k">Interest (total &minus; 15,000) &asymp; $</span><span class="ln2"></span></div>
      <div class="key">Self-check: M &asymp; $170 &middot; total &asymp; $20,439 &middot; interest &asymp; <b>$5,439</b></div>
    </div>
    <div class="card"><div class="h">Free Money First &mdash; FAFSA &amp; Scholarships</div>
      <ul class="fa">
        <li>The first <b>F</b> in FAFSA is <b>Free</b> &mdash; <b>never pay</b> to file it.</li>
        <li><b>Grants &amp; scholarships</b> are money you <b>don't pay back</b>. Chase these <i>before</i> loans.</li>
        <li>The <b>Pell Grant</b> maximum was <b>${PELL_MAX:,}</b> ({PELL_AS_OF}) &mdash; free money the FAFSA unlocks. <span class="cite">Source: Federal Student Aid</span></li>
        <li>Find scholarships through your <b>school counselor</b> and each <b>college's financial-aid office</b>.</li>
      </ul>
      <div class="chkline">☐ I made my FSA&nbsp;ID &nbsp; ☐ I started my FAFSA &nbsp; ☐ I found 3 scholarships</div>
    </div>
  </div>

  <details class="alt"><summary>Data table (accessible fallback)</summary>
    <table class="rub"><thead><tr><th>Term</th><th>Monthly</th><th>Total repaid</th><th>Interest</th><th>Extra vs borrowed</th></tr></thead>
      <tbody>{tbl}</tbody></table></details>

  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>Future Ready &middot; Money Math &middot; tied to US.25</span></div>
</div></body></html>"""

CSS = f"""
@page {{ size:8.5in 11in; margin:0; }}
*{{box-sizing:border-box;margin:0;padding:0;font-family:"Helvetica Neue",Arial,sans-serif;}}
body{{color:{NAVY};background:#fff;}}
.page{{width:8.5in;min-height:11in;padding:0.4in 0.5in 0.35in;}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2.5px solid {NAVY};padding-bottom:7px;}}
.kick{{font-size:8pt;letter-spacing:.14em;font-weight:800;color:{RED};text-transform:uppercase;}}
h1{{font-family:Georgia,serif;font-size:17.5pt;margin-top:1px;color:{NAVY};line-height:1.08;max-width:6.4in;}}
.sub{{font-size:8.8pt;color:#5A6579;font-weight:600;margin-top:4px;max-width:6.4in;line-height:1.32;}}
.stamp{{text-align:center;background:{NAVY};color:#fff;border-radius:7px;padding:6px 12px;min-width:0.9in;}}
.stamp span{{display:block;font-size:7pt;letter-spacing:.12em;font-weight:800;opacity:.85;}}
.stamp b{{font-family:Georgia,serif;font-size:18pt;line-height:1;}}
.card{{border:1.4px solid #CBD2DE;border-radius:8px;padding:10px 12px;}} .card.wide{{margin-top:11px;}}
.h{{font-size:10pt;font-weight:800;color:{NAVY};border-left:5px solid {GOLD};padding-left:8px;margin-bottom:8px;
   display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px;}}
.scale{{font-size:7.4pt;font-weight:700;color:#5A6579;}}
.lab{{font-size:8.4pt;font-weight:700;color:#2c3446;margin:7px 0 4px;}}
.rowk{{display:flex;align-items:flex-end;gap:8px;margin:5px 0;}} .k{{font-size:8.5pt;font-weight:700;color:{NAVY};white-space:nowrap;}}
.ln,.ln2{{flex:1;border-bottom:1.3px solid {LINE};min-width:60px;height:12px;}} .ln{{display:inline-block;width:52%;vertical-align:middle;}}
/* embedded questions */
.qgrid{{margin-top:11px;display:grid;grid-template-columns:1fr 1fr;gap:10px;}}
.q{{border:1.5px solid #CBD2DE;border-left:6px solid {RED};border-radius:8px;padding:9px 12px;background:#fff;}}
.qtop{{display:flex;align-items:center;gap:7px;margin-bottom:5px;flex-wrap:wrap;}}
.qtag{{background:{RED};color:#fff;font-size:8pt;font-weight:800;letter-spacing:.04em;padding:2px 9px;border-radius:11px;}}
.qstd{{background:{NAVY};color:#fff;font-size:7.4pt;font-weight:800;padding:2px 7px;border-radius:9px;}}
.qunit{{font-size:7.6pt;font-weight:700;color:#5A6579;}}
.qhook{{font-size:8.6pt;color:#2c3446;line-height:1.35;font-style:italic;}} .qhook b{{font-style:normal;color:{NAVY};}}
.qq{{list-style:none;margin:6px 0 6px;}} .qq li{{position:relative;padding:2px 0 2px 15px;font-size:8.8pt;color:{NAVY};line-height:1.3;}}
.qq li:before{{content:"?";position:absolute;left:2px;color:{RED};font-weight:800;}}
.qjot{{font-size:7.8pt;font-weight:700;color:#5A6579;display:flex;align-items:center;gap:6px;}}
.qjot .ln{{flex:1;border-bottom:1.2px solid {LINE};height:11px;width:auto;}}
.rulebar{{margin-top:11px;background:{CREAM};border-left:5px solid {GOLD};border-radius:0 6px 6px 0;
   padding:8px 12px;font-size:8.5pt;color:#2c3446;line-height:1.4;}} .rulebar b{{color:{NAVY};}}
/* loan */
.bigstat{{margin-top:9px;background:{NAVY};color:#fff;border-radius:8px;padding:9px 14px;font-size:10.5pt;line-height:1.35;}}
.bigstat b{{color:{GOLD};}} .bigstat .rd{{color:#FFD7DA;}}
.card.wide{{margin-top:9px;}} .two{{margin-top:9px !important;}} .alt{{margin-top:8px !important;}}
.sources{{padding:7px 11px !important;}}
.src{{font-size:7pt;color:#5A6579;margin-top:6px;line-height:1.35;font-style:italic;}}
.sources{{margin-top:9px;border:1.2px solid #CBD2DE;border-top:3px solid {NAVY};border-radius:6px;padding:8px 11px;background:#FBFCFD;}}
.sources .sh{{font-size:8.4pt;font-weight:800;color:{NAVY};text-transform:uppercase;letter-spacing:.03em;margin-bottom:5px;}}
.sources .sgrid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;}}
.sources .sgrid>div{{font-size:7.4pt;color:#2c3446;line-height:1.42;}} .sources .sgrid b{{color:{NAVY};}}
.sources .mono{{font-family:Georgia,serif;font-weight:700;}}
.sources .cite{{display:block;margin-top:3px;font-size:6.8pt;color:{RED};font-weight:700;}}
.sources .verif{{margin-top:7px;padding-top:5px;border-top:1px dashed #CBD2DE;font-size:6.9pt;color:#5A6579;font-style:italic;line-height:1.35;}}
.qsrc{{margin-top:8px;font-size:7pt;color:#5A6579;line-height:1.4;padding:6px 10px;background:#FBFCFD;border:1px solid #E1E5EC;border-radius:5px;}}
.qsrc b{{color:{NAVY};}}
ul.fa li .cite{{font-size:6.8pt;color:{RED};font-weight:700;}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:11px;}}
.frm{{background:{CREAM};border:1.2px solid {GOLD};border-radius:6px;padding:7px 10px;font-size:8.6pt;color:{NAVY};line-height:1.5;}}
.frm .mono{{font-family:Georgia,serif;font-weight:700;}} .frm small{{color:#5A6579;font-weight:600;}}
.key{{margin-top:8px;background:#EEF1F7;border-radius:5px;padding:5px 9px;font-size:8pt;color:#2c3446;}} .key b{{color:{RED};}}
ul.fa{{list-style:none;}} ul.fa li{{position:relative;padding:3px 0 3px 15px;font-size:8.6pt;color:#2c3446;line-height:1.35;}}
ul.fa li:before{{content:"";position:absolute;left:2px;top:8px;width:5px;height:5px;background:{GOLD};border-radius:50%;}}
ul.fa li b{{color:{NAVY};}}
.chkline{{margin-top:7px;font-size:8pt;font-weight:700;color:{NAVY};}}
table.rub{{width:100%;border-collapse:collapse;margin-top:6px;}}
table.rub th{{background:{NAVY};color:#fff;font-size:8pt;font-weight:800;padding:4px 7px;text-align:left;border:1px solid {NAVY};}}
table.rub td{{border:1px solid #CBD2DE;padding:4px 7px;font-size:8.3pt;color:#2c3446;}}
.alt{{margin-top:10px;font-size:8.5pt;}} .alt summary{{font-weight:800;color:{NAVY};cursor:pointer;}}
.foot{{margin-top:11px;padding-top:6px;border-top:1px solid #CBD2DE;display:flex;justify-content:space-between;
   font-size:7.4pt;color:#5A6579;}} .foot b{{color:{NAVY};}}
"""

def render(html, base, win_h):
    hp=os.path.join(HERE,base+".html"); open(hp,"w").write(html)
    pdf=os.path.join(HERE,base+".pdf")
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
        "--disable-dev-shm-usage","--no-pdf-header-footer","--print-to-pdf="+pdf,"file://"+hp],
        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    from PIL import Image
    raw=os.path.join(HERE,"_"+base+".png")
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
        "--disable-dev-shm-usage","--force-device-scale-factor=2",f"--window-size=816,{win_h}",
        "--screenshot="+raw,"file://"+hp],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    Image.open(raw).convert("RGB").save(os.path.join(HERE,base+".png")); os.remove(raw)

if __name__ == "__main__":
    render(questions_html(), "FutureReady_Questions", 1056)
    render(loan_html(), "FutureReady_Loan_Math", 1056)
    print("rendered questions + loan math")
    for d in LOAN: print(d)
