# -*- coding: utf-8 -*-
"""FUTURE READY — employability / Future-Ready bookend (pilot, Unit 1).
Two per-unit sheets that make the named skills VISIBLE (each is printed and named)
and MEASURABLE (a number, a tally, or a dated 1-4 rubric score with a growth delta):
  1) LAUNCH  (student completes BEFORE the unit): grade & missing-items check,
     pre-unit goal, hireability self-baseline (10-trait rubric), voice-to-email setup.
  2) DEBRIEF (student completes AFTER the unit): goal check-in, grade delta,
     timeliness tally (late-to-class marks -> total), hireability re-score (+delta),
     next-unit commitment.
America 250 palette; Chromium --print-to-pdf; matches the workbook opener geometry.
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = os.environ.get("CHROME_BIN", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
NAVY, RED, GOLD, CREAM, LINE = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF", "#9AA0AB"

# 10 employability traits + a concrete, observable look-for (grounds the score).
TRAITS = [
  ("Timeliness",          "In seat & ready when the bell rings; work turned in on time."),
  ("Integrity",           "Own words & own work; honest about what I did and didn't do."),
  ("Work ethic",          "Effort all period; push through hard tasks without quitting."),
  ("Adaptability",        "Adjust when plans change; try a new strategy when stuck."),
  ("Lifelong learning",   "Ask questions; act on feedback; learn past the grade."),
  ("Organization",        "Materials, notes & deadlines tracked; can find my work."),
  ("Reliability",         "Do what I said I'd do; teammates can count on me."),
  ("Civic responsibility","Contribute to the class community; respect people & space."),
  ("Teamwork",            "Share the load; listen; help the group reach the goal."),
  ("Leadership",          "Set the example; step up; help others without being asked."),
]

def scorebox(vals=(1,2,3,4)):
    # circle-the-number cell
    return '<span class="sb">' + "".join(f'<i>{n}</i>' for n in vals) + '</span>'

def line(w="100%"):
    return f'<div class="wl" style="width:{w}"></div>'

def launch_html():
    rubric = "".join(
        f'<tr><td class="tn">{name}</td><td class="tl">{look}</td>'
        f'<td class="ts">{scorebox()}</td></tr>' for name, look in TRAITS)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Future Ready &middot; Employability</div>
    <h1>Future Ready &mdash; Unit Launch</h1>
    <div class="sub">Get hired-ready while you learn history. Fill this in <b>before</b> the unit &mdash; you'll re-check it at the end.</div></div>
    <div class="stamp"><span>UNIT</span><b>1</b></div></div>

  <div class="grid2">
    <div class="card"><div class="h">1 &middot; Grade &amp; Missing-Items Check</div>
      <div class="rowk"><span class="k">Current grade</span>{line("1.1in")}
        <span class="k">Missing items</span>{line("0.7in")}</div>
      <div class="lab">List what's missing &amp; when I'll turn it in:</div>
      {line()}{line()}{line()}
      <div class="chk">☐ I checked the gradebook myself today.</div>
    </div>
    <div class="card"><div class="h">2 &middot; Set Your SMART Goal
        <span class="scale">new to SMART? use the support sheet on the back &rarr;</span></div>
      <div class="pick2">This goal is: &nbsp;☐ academic &nbsp;&nbsp; ☐ employability skill</div>
      <div class="smart">
        <div class="sr"><span class="tag">S</span><span class="sl"><b>Specific</b> &mdash; exactly what I'll do</span></div>{line()}
        <div class="sr"><span class="tag">M</span><span class="sl"><b>Measurable</b> &mdash; the number or proof</span></div>{line()}
        <div class="sr"><span class="tag">A&middot;R</span><span class="sl"><b>Achievable &amp; Relevant</b> &mdash; why it fits me</span></div>{line()}
        <div class="sr"><span class="tag">T</span><span class="sl"><b>Time-bound</b> &mdash; by when</span></div>{line("2.4in")}
      </div>
    </div>
  </div>

  <div class="card wide"><div class="h">3 &middot; Hireability Baseline &mdash; score yourself honestly
      <span class="scale">1 Not yet &middot; 2 Developing &middot; 3 Proficient &middot; 4 Exemplary</span></div>
    <table class="rub"><thead><tr><th>Skill</th><th>What it looks like</th><th>My score</th></tr></thead>
      <tbody>{rubric}</tbody></table>
    <div class="tot">Baseline total <b>____ / 40</b> &nbsp;&middot;&nbsp; circle one number per row &middot; keep it real &mdash; growth is the point.</div>
  </div>

  <div class="card wide voice"><div class="h">4 &middot; Voice-to-Email Your Teacher</div>
    <div class="vtwo">
      <div><div class="lab">Use your phone/computer <b>voice-to-text</b> to draft a real email. Say it, check it, send it.
        Follow up if you don't hear back in <b>2 school days</b>.</div>
        <div class="chk">☐ I sent one email to my teacher this unit.</div>
        <div class="rowk"><span class="k">Date sent</span>{line("1.2in")}
          <span class="k">Reply by</span>{line("1.2in")}</div></div>
      <div class="frame"><div class="fh">Email structure</div>
        <ol><li><b>Greeting</b> &mdash; "Dear Mr./Ms. ____,"</li>
          <li><b>Purpose</b> &mdash; one clear sentence: why you're writing.</li>
          <li><b>Details</b> &mdash; the specifics (assignment, date, question).</li>
          <li><b>The ask</b> &mdash; exactly what you need.</li>
          <li><b>Sign-off</b> &mdash; "Thank you, [Full name, Class period]"</li></ol></div>
    </div>
  </div>

  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>Future Ready &middot; UDL 3.0 (CAST 2024) &middot; Unit Launch</span></div>
</div></body></html>"""

def debrief_html():
    rescore = "".join(
        f'<tr><td class="tn">{name}</td>'
        f'<td class="tb">{scorebox()}</td><td class="tb">{scorebox()}</td>'
        f'<td class="td_"><span class="delta">▲ ▬ ▼</span></td></tr>' for name, _ in TRAITS)
    # 12 class-day tally cells for the timeliness log
    days = "".join('<span class="day"><i>On&nbsp;time</i><i>Late</i></span>' for _ in range(12))
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Future Ready &middot; Employability</div>
    <h1>Future Ready &mdash; Unit Debrief</h1>
    <div class="sub">Fill this in <b>at the end</b> of the unit. Compare it to your Launch page &mdash; that difference is your growth.</div></div>
    <div class="stamp"><span>UNIT</span><b>1</b></div></div>

  <div class="grid2">
    <div class="card"><div class="h">1 &middot; Goal Check-In</div>
      <div class="rowk"><span class="k">My goal was</span>{line("2.0in")}</div>
      <div class="pick">☐ Met &nbsp; ☐ Partly &nbsp; ☐ Not yet</div>
      <div class="lab">Evidence / what happened:</div>{line()}{line()}
    </div>
    <div class="card"><div class="h">2 &middot; Grade &amp; Missing Re-Check</div>
      <div class="rowk"><span class="k">Grade now</span>{line("0.9in")}
        <span class="k">Change</span>{line("0.9in")}</div>
      <div class="rowk"><span class="k">Missing now</span>{line("0.9in")}</div>
      <div class="lab">Still to turn in:</div>{line()}{line()}
    </div>
  </div>

  <div class="card wide"><div class="h">3 &middot; Timeliness Tally
      <span class="scale">mark each class this unit &mdash; then total your lates</span></div>
    <div class="days">{days}</div>
    <div class="tot">Total <b>on-time ____</b> &nbsp;&middot;&nbsp; <b>late ____</b> &nbsp;&middot;&nbsp; goal next unit: <b>____ or fewer lates</b></div>
  </div>

  <div class="card wide"><div class="h">4 &middot; Hireability Re-Score
      <span class="scale">1 Not yet &middot; 2 Developing &middot; 3 Proficient &middot; 4 Exemplary</span></div>
    <table class="rub"><thead><tr><th>Skill</th><th>Baseline</th><th>Now</th><th>Growth</th></tr></thead>
      <tbody>{rescore}</tbody></table>
    <div class="tot">Baseline <b>____ / 40</b> &rarr; Now <b>____ / 40</b> &nbsp;&middot;&nbsp; circle ▲ grew, ▬ same, ▼ slipped.</div>
  </div>

  <div class="card wide commit"><div class="h">5 &middot; My Commitment for the Next Unit</div>
    <div class="lab">One employability skill I'll level up, and my first move:</div>{line()}{line()}</div>

  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>Future Ready &middot; UDL 3.0 (CAST 2024) &middot; Unit Debrief</span></div>
</div></body></html>"""

SMART = [
  ("S","Specific","What exactly will I do?"),
  ("M","Measurable","What number or proof shows I did it?"),
  ("A","Achievable","Can I really do this in one unit?"),
  ("R","Relevant","Why does it matter to me &amp; my future?"),
  ("T","Time-bound","By when?"),
]

def smart_support_html():
    deftbl = "".join(
        f'<tr><td class="L">{L}</td><td class="W">{w}</td><td class="Q">{q}</td></tr>'
        for L, w, q in SMART)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Future Ready &middot; Support Tool</div>
    <h1>SMART Goals &mdash; Set It, Then Follow Up</h1>
    <div class="sub">Learn the SMART frame here, then set your <b>short-, mid-, and long-term</b> goals on the <i>My SMART Goals</i> page. Print on the back of Launch, or your teacher may assign it.</div></div>
    <div class="stamp"><span>SET</span><b>&#10003;</b></div></div>

  <div class="why2"><b>Why this matters.</b> A goal you write down and can <b>measure</b> is a goal you can win.
    People who set specific, measurable goals &mdash; and <b>check them</b> &mdash; reach them far more often than people who just
    &ldquo;try harder.&rdquo; That's why we <b>set</b> it on the Launch page and <b>follow up</b> on the Debrief.</div>

  <div class="two">
    <div class="card"><div class="h">A &middot; What SMART Means</div>
      <table class="def"><tbody>{deftbl}</tbody></table></div>
    <div class="card"><div class="h">B &middot; See What It Looks Like</div>
      <div class="model">
        <div class="mg">&ldquo;I will raise my U.S. History grade from a <b>74</b> to an <b>80 or higher</b> by the end of Unit 1 by turning in every assignment on time and asking one question in class each week.&rdquo;</div>
        <div class="mb"><b>S</b> raise my history grade &middot; <b>M</b> 74 &rarr; 80+ &middot; <b>A</b> 6 points is reachable
          &middot; <b>R</b> keeps me on track &amp; eligible &middot; <b>T</b> by the end of Unit&nbsp;1</div>
      </div>
      <div class="mb" style="margin-top:7px"><b>Employability version:</b> &ldquo;I will be in my seat, ready to work, <b>before the bell for all 12 class days</b> this unit.&rdquo;</div>
    </div>
  </div>

  <div class="card wide"><div class="h">C &middot; Now You Try &mdash; Build Your Goal <span class="scale">draft it here, then copy the best version onto your Launch page</span></div>
    <div class="builder"><div class="bframe">
      I will <u>&nbsp;</u> <small>Specific &mdash; what I'll do</small>
      from <u>&nbsp;</u> to <u>&nbsp;</u> <small>Measurable &mdash; start &rarr; target (a number or proof)</small>
      by <u>&nbsp;</u> <small>Time-bound &mdash; the deadline</small>
      because <u>&nbsp;</u> <small>Relevant &mdash; why it matters to me</small>
    </div></div>
    <div class="bank"><b>Measurable verbs:</b> raise &middot; complete &middot; reach &middot; reduce &middot; attend &middot; submit &middot; score &nbsp;&nbsp;
      <b>Time words:</b> by Friday &middot; each week &middot; daily &middot; by the end of the unit</div>
  </div>

  <div class="card wide"><div class="h">D &middot; Follow Up &mdash; A Goal You Don't Check Is a Wish</div>
    <ul class="foll">
      <li><b>Halfway through the unit &mdash; quick check:</b> Am I on track? What's one number that shows my progress? What's my next move this week?</li>
      <li><b>End of the unit &mdash; on the Debrief page:</b> mark <b>Met / Partly / Not yet</b>, write your evidence, and set your next goal.</li>
      <li><b>If I'm off track:</b> don't quit &mdash; shrink the goal or change the step, <b>not</b> the finish line.</li>
    </ul></div>

  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>Future Ready Support &middot; UDL 3.0 (CAST 2024) &middot; SMART Goals</span></div>
</div></body></html>"""

# Three-horizon SMART exemplars — authentic voice of a high-school junior.
# Each: label, timeframe, natural-voice quote, and a COMPLETED frame
# (specific, start, target, by-when, because) so students see it filled in.
HORIZONS = [
  ("SHORT-TERM", "this unit &middot; ~3 weeks",
   "I will raise my U.S. History grade from a 74 to an 80 or higher by the end of this unit by turning in every assignment on time and asking at least one question in class each week.",
   ("raise my U.S. History grade", "a 74", "an 80 or higher", "the end of this unit", "it keeps me eligible to play")),
  ("MID-TERM", "this semester &middot; ~this year",
   "By the end of this semester I'll get my GPA up to a 3.0 so I stay eligible for soccer, by keeping every class at a C or better and checking my grades every Friday.",
   ("raise my GPA", "a 2.6", "a 3.0", "the end of this semester", "I have to stay eligible for soccer")),
  ("LONG-TERM", "graduation &amp; beyond",
   "By the time I graduate in two years I'll be ready to start a welding apprenticeship, so this year I'll pass all my classes, keep my attendance above 95%, and earn my OSHA-10 card by next spring.",
   ("get welding-job-ready", "no certification", "OSHA-10 certified", "next spring", "it's my plan after I graduate")),
]

def filled_frame(f):
    s, a, b, t, r = f
    return (f'I will <span class="fv">{s}</span> from <span class="fv">{a}</span> to '
            f'<span class="fv">{b}</span> by <span class="fv">{t}</span> because '
            f'<span class="fv">{r}</span>.')

def my_smart_goals_html():
    cards = []
    for label, tf, quote, filled in HORIZONS:
        cards.append(f"""
      <div class="gcard"><div class="gtop"><span class="chip">{label}</span><span class="gtime">{tf}</span></div>
        <div class="ex"><span class="exk">A real junior:</span> <i>&ldquo;{quote}&rdquo;</i></div>
        <div class="filled"><span class="fl">Completed example</span>{filled_frame(filled)}</div>
        <div class="build2"><span class="nl">Now you try:</span>
          <span class="bl">I will <u>&nbsp;</u> <small>Specific</small></span>
          <span class="bl">from <u>&nbsp;</u> to <u>&nbsp;</u> <small>Measurable</small></span>
          <span class="bl">by <u>&nbsp;</u> <small>Time-bound</small></span>
          <span class="bl">because <u>&nbsp;</u> <small>Relevant</small></span>
        </div></div>""")
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Future Ready &middot; Goals</div>
    <h1>My SMART Goals &mdash; Short &middot; Mid &middot; Long</h1>
    <div class="sub">Every big goal is built from smaller ones. Write all three &mdash; each unit's goal ladders up to your long-term goal. Use the SMART support sheet if you need the how-to.</div></div>
    <div class="stamp"><span>GOALS</span><b>3</b></div></div>
  <div class="glist">{''.join(cards)}</div>

  <div class="card wide reflect"><div class="h">Reflect &amp; Commit &mdash; the part that makes a goal stick</div>
    <div class="rgrid">
      <div class="rcol">
        <div class="lab">Connect the ladder &mdash; how does my <b>short-term</b> goal move me toward my <b>long-term</b> goal?</div>{line()}{line()}
        <div class="rowk"><span class="k">My accountability partner (who checks on me)</span>{line("1.4in")}</div>
      </div>
      <div class="rcol">
        <div class="lab">One thing that could get in my way:</div>{line()}
        <div class="lab">My plan for when it does:</div>{line()}
        <div class="rowk"><span class="k">My first step &mdash; this week</span>{line("1.7in")}</div>
      </div>
    </div>
    <div class="motto">A goal without a plan is just a wish &mdash; a goal you <b>write, ladder, and check</b> is a plan.</div>
  </div>

  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>Future Ready &middot; UDL 3.0 (CAST 2024) &middot; My SMART Goals</span></div>
</div></body></html>"""

# CER self-grade — modeled on the College Board AP U.S. History essay rubric's own
# A/B/C/D reporting-category layout (LEQ 6 pts; extends to the 7-pt DBQ scale when
# the CER is document-based) so the format is familiar to any AP reader.
CER_ROWS = [
  ("A", "Thesis / Claim", "Claim", "0&ndash;1", (0,1),
   ["<b>1 pt</b> &mdash; Make a defensible claim that answers the prompt and sets up a line of reasoning (more than restating the question)."]),
  ("B", "Contextualization", "Context", "0&ndash;1", (0,1),
   ["<b>1 pt</b> &mdash; Describe a broader historical context &mdash; before, during, or after &mdash; that's relevant to the prompt."]),
  ("C", "Evidence", "Evidence", "0&ndash;2", (0,1,2),
   ["<b>1 pt</b> &mdash; Give at least two specific, accurate pieces of evidence relevant to the prompt.",
    "<b>2 pts</b> &mdash; <i>Use</i> that evidence to support your argument &mdash; not just list it."]),
  ("D", "Analysis &amp; Reasoning", "Reasoning", "0&ndash;2", (0,1,2),
   ["<b>1 pt</b> &mdash; Use a reasoning skill &mdash; causation, comparison, or continuity &amp; change &mdash; to structure the argument.",
    "<b>2 pts</b> &mdash; Show a complex understanding: weigh another perspective, qualify a claim, or connect across time."]),
]

def cer_rubric_html():
    rows = ""
    for L, apname, cerw, pts, vals, bullets in CER_ROWS:
        drs = "".join(f"<li>{b}</li>" for b in bullets)
        rows += (f'<tr><td class="cn"><span class="apL">{L}</span>'
                 f'<b>{apname}</b><span class="cerw">CER &middot; {cerw}</span>'
                 f'<span class="pts">{pts} pts</span></td>'
                 f'<td class="cw"><ul class="dr">{drs}</ul></td>'
                 f'<td class="cs">{scorebox(vals)}</td></tr>')
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="top"><div><div class="kick">Constructed Response &middot; Self-Grade</div>
    <h1>CER Self-Grade &mdash; AP-Aligned</h1>
    <div class="sub">Grade your own <b>Claim &middot; Evidence &middot; Reasoning</b> response the way an AP reader would &mdash; same <b>A&ndash;D</b> categories they use. Score each row, total your points, then reflect and revise.</div></div>
    <div class="stamp"><span>SCORE</span><b>/6</b></div></div>

  <div class="why2"><b>Where this comes from.</b> These are the <b>College Board AP U.S. History</b> essay
    reporting categories &mdash; <b>A</b> Thesis, <b>B</b> Contextualization, <b>C</b> Evidence,
    <b>D</b> Analysis &amp; Reasoning (the 6-point Long-Essay scale). If your CER analyzes documents,
    <b>C</b> extends to the AP <b>Document-Based (7-point)</b> scale &mdash; your teacher will say which you're on.</div>

  <table class="rub cer"><thead><tr><th>Reporting category</th><th>Scoring / decision rules</th><th>My score</th></tr></thead>
    <tbody>{rows}</tbody></table>
  <div class="tot">My total <b>____ / 6</b> &nbsp;&middot;&nbsp; circle the points you truly earned &mdash; be your own toughest reader.</div>

  <div class="card wide reflect"><div class="h">Reflect &amp; Revise &mdash; the step that actually raises your score</div>
    <div class="rgrid">
      <div class="rcol">
        <div class="lab">What my score tells me about this response:</div>{line()}{line()}
        <div class="rowk"><span class="k">My lowest category was</span>{line("1.6in")}</div>
        <div class="lab">The one change that earns that point:</div>{line()}
      </div>
      <div class="rcol">
        <div class="lab">Across my recent CERs, my weak spot is usually:</div>
        <div class="picks">☐ A Claim &nbsp; ☐ B Context &nbsp; ☐ C Evidence &nbsp; ☐ D Reasoning</div>
        <div class="lab" style="margin-top:8px">So next time I'll target:</div>{line()}
        <div class="chk">☐ I revised &amp; re-scored &mdash; new total ____ / 6</div>
      </div>
    </div></div>

  <div class="why2 tips"><b>Quick self-check.</b> Claim = a sentence a classmate could argue against &middot;
    Evidence = names, dates, terms &mdash; not &ldquo;stuff happened&rdquo; &middot; Reasoning = the word <i>because</i>
    doing real work &middot; Complexity = &ldquo;but&rdquo; / &ldquo;however&rdquo; / another side.</div>

  <div class="foot"><span><b>U.S. History Hack&trade;</b> &middot; &copy; 2026 TroopToTeacher Technologies LLC</span>
    <span>CER Self-Grade &middot; modeled on the College Board AP U.S. History rubric</span></div>
</div></body></html>"""

CSS = f"""
@page {{ size:8.5in 11in; margin:0; }}
*{{box-sizing:border-box;margin:0;padding:0;font-family:"Helvetica Neue",Arial,sans-serif;}}
body{{color:{NAVY};background:#fff;}}
.page{{width:8.5in;min-height:11in;padding:0.4in 0.5in 0.35in;}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2.5px solid {NAVY};padding-bottom:7px;}}
.kick{{font-size:8pt;letter-spacing:.14em;font-weight:800;color:{RED};text-transform:uppercase;}}
h1{{font-family:Georgia,serif;font-size:19pt;margin-top:1px;color:{NAVY};}}
.sub{{font-size:8.8pt;color:#5A6579;font-weight:600;margin-top:3px;max-width:6.2in;line-height:1.3;}}
.stamp{{text-align:center;background:{NAVY};color:#fff;border-radius:7px;padding:6px 12px;min-width:0.9in;}}
.stamp span{{display:block;font-size:7pt;letter-spacing:.12em;font-weight:800;opacity:.85;}}
.stamp b{{font-family:Georgia,serif;font-size:20pt;line-height:1;}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:11px;}}
.card{{border:1.4px solid #CBD2DE;border-radius:7px;padding:9px 11px;background:#fff;}}
.card.wide{{margin-top:10px;}}
.h{{font-size:10pt;font-weight:800;color:{NAVY};border-left:5px solid {GOLD};padding-left:8px;margin-bottom:7px;
   display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px;}}
.scale{{font-size:7.4pt;font-weight:700;color:#5A6579;letter-spacing:.02em;}}
.lab{{font-size:8.3pt;font-weight:700;color:#2c3446;margin:6px 0 3px;}}
.wl{{height:0;border-bottom:1.3px solid {LINE};margin:9px 0;}}
.rowk{{display:flex;align-items:flex-end;gap:8px;flex-wrap:wrap;margin:5px 0;}}
.k{{font-size:8.3pt;font-weight:700;color:{NAVY};white-space:nowrap;}}
.chk,.pick{{font-size:8.4pt;font-weight:700;color:{NAVY};margin-top:6px;}}
.pick{{margin-top:8px;}}
.sb{{display:inline-flex;gap:4px;}}
.sb i{{font-style:normal;width:17px;height:17px;line-height:15px;text-align:center;font-size:8.6pt;font-weight:800;
      border:1.3px solid {NAVY};border-radius:50%;color:{NAVY};}}
table.rub{{width:100%;border-collapse:collapse;table-layout:fixed;}}
table.rub th{{background:{NAVY};color:#fff;font-size:8pt;font-weight:800;text-transform:uppercase;letter-spacing:.03em;
   padding:5px 8px;text-align:left;border:1px solid {NAVY};}}
table.rub td{{border:1px solid #CBD2DE;padding:4px 8px;font-size:8.4pt;vertical-align:middle;}}
td.tn{{width:20%;font-weight:800;color:{NAVY};}}
td.tl{{width:60%;color:#2c3446;line-height:1.25;}}
td.ts{{width:20%;text-align:center;}}
td.tb{{width:16%;text-align:center;}} td.td_{{width:14%;text-align:center;}}
.delta{{font-size:9pt;letter-spacing:2px;color:{NAVY};}}
.tot{{margin-top:6px;font-size:8.5pt;font-weight:700;color:{NAVY};background:{CREAM};border-left:4px solid {GOLD};
   border-radius:0 4px 4px 0;padding:5px 9px;}}
.voice .vtwo{{display:grid;grid-template-columns:1.15fr 1fr;gap:12px;}}
.frame{{background:{CREAM};border:1.2px solid {GOLD};border-radius:6px;padding:7px 10px;}}
.fh{{font-size:8.2pt;font-weight:800;color:{NAVY};text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px;}}
.frame ol{{margin-left:14px;font-size:8pt;color:#2c3446;line-height:1.5;}}
.days{{display:grid;grid-template-columns:repeat(6,1fr);gap:5px;margin:2px 0 4px;}}
.day{{border:1.2px solid #CBD2DE;border-radius:5px;padding:5px 3px;display:flex;flex-direction:column;gap:4px;text-align:center;}}
.day i{{font-style:normal;font-size:7pt;font-weight:700;color:{NAVY};border:1px solid {LINE};border-radius:3px;padding:2px 0;}}
.commit .lab{{margin-top:2px;}}
.pick2{{font-size:8.4pt;font-weight:700;color:{NAVY};margin:2px 0 6px;}}
.smart{{margin-top:2px;}}
.sr{{display:flex;align-items:center;gap:8px;margin-top:7px;}}
.tag{{flex:0 0 auto;min-width:24px;height:20px;line-height:20px;text-align:center;background:{NAVY};color:#fff;
   font-size:8.4pt;font-weight:800;border-radius:5px;padding:0 5px;}}
.sl{{font-size:8.1pt;color:#2c3446;}} .sl b{{color:{NAVY};}}
.smart .wl{{margin:5px 0 2px;}}
/* SMART support sheet */
.two{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:11px;}}
.def{{width:100%;border-collapse:collapse;}}
.def td{{border:1px solid #CBD2DE;padding:5px 8px;font-size:8.5pt;vertical-align:top;}}
.def .L{{width:15%;background:{NAVY};color:#fff;font-weight:800;font-size:11pt;text-align:center;font-family:Georgia,serif;}}
.def .W{{width:38%;font-weight:800;color:{NAVY};}}
.def .Q{{color:#2c3446;}}
.model{{background:{CREAM};border:1.2px solid {GOLD};border-radius:6px;padding:8px 11px;margin-top:4px;}}
.model .mg{{font-size:9pt;font-style:italic;color:{NAVY};line-height:1.4;border-left:4px solid {RED};padding-left:9px;margin-bottom:7px;}}
.model .mb{{font-size:8pt;color:#2c3446;line-height:1.55;}}
.model .mb b{{color:{NAVY};}}
.why2{{background:#EEF1F7;border-radius:6px;padding:8px 11px;font-size:8.4pt;color:#2c3446;line-height:1.4;margin-top:4px;}}
.why2 b{{color:{NAVY};}}
.builder{{border:1.4px dashed {NAVY};border-radius:7px;padding:9px 11px;margin-top:4px;}}
.bframe{{font-size:9.2pt;color:{NAVY};line-height:2.2;}}
.bframe u{{text-decoration:none;border-bottom:1.3px solid {LINE};padding:0 34px;}}
.bframe small{{display:block;font-size:7.2pt;color:#5A6579;font-weight:700;letter-spacing:.02em;}}
.bank{{margin-top:7px;font-size:7.8pt;color:#2c3446;}} .bank b{{color:{NAVY};}}
.foll{{list-style:none;margin-top:3px;}}
.foll li{{font-size:8.4pt;color:#2c3446;line-height:1.4;padding:4px 0 4px 20px;position:relative;border-bottom:1px solid #E4E8F0;}}
.foll li:before{{content:"→";position:absolute;left:2px;color:{RED};font-weight:800;}}
.foll li b{{color:{NAVY};}}
/* My SMART Goals (3 horizons) */
.glist{{margin-top:11px;display:flex;flex-direction:column;gap:11px;}}
.gcard{{border:1.4px solid #CBD2DE;border-radius:8px;padding:10px 13px;border-left:6px solid {GOLD};}}
.gtop{{display:flex;align-items:center;gap:10px;margin-bottom:5px;}}
.chip{{background:{NAVY};color:#fff;font-size:8pt;font-weight:800;letter-spacing:.06em;padding:3px 10px;border-radius:11px;}}
.gtime{{font-size:8pt;font-weight:700;color:{RED};text-transform:uppercase;letter-spacing:.04em;}}
.ex{{font-size:8.8pt;color:#2c3446;line-height:1.35;}} .ex .exk{{font-weight:800;color:{NAVY};}}
.ex i{{color:{NAVY};}}
.filled{{font-size:8.8pt;color:#2c3446;line-height:1.5;margin:6px 0 7px;padding:6px 10px;
   background:{CREAM};border-left:4px solid {GOLD};border-radius:0 5px 5px 0;}}
.filled .fl{{display:inline-block;font-size:7pt;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
   color:{RED};margin-right:8px;}}
.filled .fv{{color:{NAVY};font-weight:800;border-bottom:1.4px solid {GOLD};}}
.build2{{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 22px;border:1.2px dashed {NAVY};border-radius:6px;padding:7px 10px;}}
.nl{{flex-basis:100%;font-size:7.4pt;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:{NAVY};margin-bottom:2px;}}
.bl{{font-size:8.8pt;color:{NAVY};white-space:nowrap;}}
.bl u{{text-decoration:none;border-bottom:1.2px solid {LINE};padding:0 26px;}}
.bl small{{display:block;font-size:6.8pt;color:#5A6579;font-weight:700;letter-spacing:.02em;}}
/* CER self-grade — modeled on the AP A–D reporting-category layout */
table.cer td.cn{{width:24%;color:{NAVY};position:relative;padding-left:34px;}}
table.cer td.cn .apL{{position:absolute;left:7px;top:6px;width:20px;height:20px;line-height:20px;text-align:center;
   background:{NAVY};color:#fff;font-family:Georgia,serif;font-weight:700;font-size:10pt;border-radius:4px;}}
table.cer td.cn b{{display:block;font-size:9pt;color:{NAVY};}}
table.cer td.cn .cerw{{display:block;font-size:7.4pt;color:{RED};font-weight:800;margin-top:1px;}}
table.cer td.cn .pts{{display:block;font-size:7.6pt;color:#5A6579;font-weight:700;margin-top:3px;}}
table.cer td.cw{{width:54%;color:#2c3446;}}
ul.dr{{list-style:none;}} ul.dr li{{position:relative;padding:2px 0 2px 14px;font-size:8.4pt;line-height:1.3;}}
ul.dr li:before{{content:"";position:absolute;left:2px;top:8px;width:5px;height:5px;background:{GOLD};border-radius:50%;}}
ul.dr li b{{color:{RED};}}
table.cer td.cs{{width:22%;text-align:center;}}
.tips{{margin-top:8px;font-size:8pt;}}
/* Reflection blocks (both pages) */
.reflect{{margin-top:10px;border-left:6px solid {RED};}}
.rgrid{{display:grid;grid-template-columns:1fr 1fr;gap:6px 22px;}}
.rcol{{min-width:0;}}
.picks{{font-size:8.3pt;font-weight:700;color:{NAVY};margin-top:3px;}}
.motto{{margin-top:9px;padding-top:7px;border-top:1px dashed #CBD2DE;font-size:8.4pt;font-style:italic;
   color:{NAVY};text-align:center;}} .motto b{{font-style:normal;color:{RED};}}
.foot{{margin-top:11px;padding-top:6px;border-top:1px solid #CBD2DE;display:flex;justify-content:space-between;
   font-size:7.4pt;color:#5A6579;}} .foot b{{color:{NAVY};}}
"""

def render(html, base, win_h):
    hp = os.path.join(HERE, base + ".html"); open(hp, "w").write(html)
    pdf = os.path.join(HERE, base + ".pdf")
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
        "--disable-dev-shm-usage","--no-pdf-header-footer","--print-to-pdf="+pdf,"file://"+hp],
        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    from PIL import Image
    raw = os.path.join(HERE, "_"+base+".png")
    subprocess.run([CHROME,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
        "--disable-dev-shm-usage","--force-device-scale-factor=2",f"--window-size=816,{win_h}",
        "--screenshot="+raw,"file://"+hp],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    Image.open(raw).convert("RGB").save(os.path.join(HERE, base+".png")); os.remove(raw)
    return pdf

if __name__ == "__main__":
    render(launch_html(), "FutureReady_Unit_Launch", 1056)
    render(debrief_html(), "FutureReady_Unit_Debrief", 1056)
    render(smart_support_html(), "FutureReady_SMART_Support", 1056)
    render(my_smart_goals_html(), "FutureReady_My_SMART_Goals", 1056)
    render(cer_rubric_html(), "FutureReady_CER_SelfGrade", 1056)
    print("rendered launch + debrief + smart support + my-smart-goals + cer self-grade")
