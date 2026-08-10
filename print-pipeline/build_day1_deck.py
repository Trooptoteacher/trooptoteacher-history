#!/usr/bin/env python3
"""
Day One — 20-minute welcome + norms deck (America 250 brand).
Introduces the teacher and the year, walks the Schoology/syllabus agenda, then
lands the ONE RULE (RESPECT) and hands the class the pen to co-write the norms
under it. Rendered HTML -> PDF via WeasyPrint (16:9, 13.333x7.5in).
Editable teacher fields are marked [like this].
"""
import sys
from weasyprint import HTML

# America 250
NAVY="#1F3A5F"; RED="#B22234"; GOLD="#C9A227"; GOLDINK="#846009"
CREAM="#F8F5EF"; TINT="#F3ECD6"; INK="#1F2430"; COOL="#EAF0F7"

CSS = f"""
@page {{ size: 1280px 720px; margin: 0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
.slide {{ position:relative; width:1280px; height:720px; background:#fff;
  page-break-after:always; font-family:'Carlito','Calibri',sans-serif; color:{INK};
  overflow:hidden; }}
.bar {{ position:absolute; top:0; left:0; width:1280px; height:16px; background:{NAVY}; }}
.pad {{ position:absolute; top:52px; left:70px; right:70px; bottom:56px; }}
.kicker {{ color:{RED}; font-weight:700; letter-spacing:2px; font-size:19px; text-transform:uppercase; }}
h1 {{ font-family:'Liberation Serif','Georgia',serif; color:{NAVY}; font-size:60px;
  line-height:1.04; margin:6px 0 14px; }}
h1.big {{ font-size:78px; }}
.sub {{ font-size:26px; color:#33475b; line-height:1.3; }}
.foot {{ position:absolute; left:70px; bottom:20px; font-size:15px; color:#8a94a3; }}
.time {{ position:absolute; right:70px; bottom:16px; background:{TINT}; color:{GOLDINK};
  border:1.5px solid {GOLD}; border-radius:18px; padding:6px 16px; font-weight:700; font-size:17px; }}
.card {{ background:{CREAM}; border:1.5px solid #e4dcc6; border-left:7px solid {GOLD};
  border-radius:10px; padding:18px 20px; }}
.cardnavy {{ background:{NAVY}; color:#fff; border-radius:10px; padding:18px 20px; }}
.big-num {{ font-family:'Liberation Serif',serif; font-size:34px; color:{GOLD}; font-weight:700; }}
.row {{ display:flex; gap:18px; }}
.col {{ flex:1; }}
ol.agenda {{ list-style:none; }}
ol.agenda li {{ display:flex; align-items:center; gap:18px; font-size:30px; margin:14px 0;
  background:{COOL}; border-radius:12px; padding:14px 22px; }}
ol.agenda .n {{ background:{NAVY}; color:#fff; font-weight:700; border-radius:50%;
  width:44px; height:44px; display:flex; align-items:center; justify-content:center; font-size:22px; flex:none; }}
ol.agenda .t {{ margin-left:auto; color:{GOLDINK}; font-weight:700; font-size:20px; }}
.steps {{ font-size:30px; line-height:1.5; }}
.steps b {{ color:{NAVY}; }}
.code {{ display:inline-block; background:#fff; border:2.5px dashed {RED}; color:{RED};
  font-weight:800; letter-spacing:4px; font-size:40px; padding:8px 26px; border-radius:10px; }}
.buckets {{ display:flex; gap:16px; margin-top:14px; }}
.bucket {{ flex:1; background:{CREAM}; border:1.5px solid #e4dcc6; border-top:6px solid {NAVY};
  border-radius:10px; padding:16px; }}
.bucket h3 {{ color:{NAVY}; font-size:23px; margin-bottom:8px; }}
.line {{ border-bottom:1.5px dotted #b9c2cf; height:30px; }}
.stem {{ background:{TINT}; border-radius:10px; padding:16px 20px; font-size:24px; color:{GOLDINK};
  font-weight:600; margin-top:16px; }}
.hint {{ font-size:20px; color:#5a6675; margin-top:12px; font-style:italic; }}
.tt {{ display:flex; gap:18px; margin-top:18px; }}
.tt .c {{ flex:1; background:{COOL}; border-radius:12px; padding:20px; font-size:24px; min-height:170px; }}
.tt .c .n {{ font-family:'Liberation Serif',serif; font-size:40px; color:{RED}; font-weight:700; }}
.edit {{ color:#94794f; font-size:16px; font-style:italic; }}
"""

def slide(kicker, body, foot="U.S. History Hack · Don't just learn history. Hack it.", time=None):
    t = f'<div class="time"> {time}</div>' if time else ""
    return (f'<div class="slide"><div class="bar"></div><div class="pad">'
            f'<div class="kicker">{kicker}</div>{body}</div>'
            f'<div class="foot">{foot}</div>{t}</div>')

SL = []

# 1 — WELCOME / bell-ringer
SL.append(slide("U.S. History Hack · Day One",
  f"""<h1>Welcome aboard.</h1>
  <div class="sub">Find your seat, open your Chromebook, and take a breath.<br>
  We're about to hack a whole century — together.</div>
  <div class="card" style="margin-top:26px; font-size:27px;">
   <b>Bell-ringer:</b> On the sticky note at your seat, write <b>one word</b> for how
  you feel about history right now. Stick it on the board on your way in.</div>""",
  time="as you enter"))

# 2 — AGENDA
SL.append(slide("Agenda · 20 minutes",
  """<h1>Today's flight plan</h1>
  <ol class="agenda">
    <li><span class="n">1</span> Log into Schoology <span class="t">4 min</span></li>
    <li><span class="n">2</span> Quick tour — where everything lives <span class="t">3 min</span></li>
    <li><span class="n">3</span> Syllabus <span class="t">2 min</span></li>
    <li><span class="n">4</span> Our one rule <span class="t">1 min</span></li>
    <li><span class="n">5</span> You write the rules <span class="t">3 min</span></li>
  </ol>""", time="1 min"))

# 3 — MEET THE TEACHER (two truths and a lie)
SL.append(slide("Meet your pilot",
  f"""<h1>Mr. Reynolds — Two Truths &amp; a Lie</h1>
  <div class="sub">Two of these are true. One is a bald-faced lie. <b>Vote with your hands.</b></div>
  <div class="tt">
    <div class="c"><span class="n">1</span><br><span class="edit">[ write something true about you ]</span></div>
    <div class="c"><span class="n">2</span><br><span class="edit">[ write the lie — make it believable ]</span></div>
    <div class="c"><span class="n">3</span><br><span class="edit">[ write something true about you ]</span></div>
  </div>
  <div class="hint">Teacher: fill these three in with your real facts before class.</div>""",
  time="3 min"))

# 4 — THE YEAR AHEAD
SL.append(slide("The year ahead",
  f"""<h1 class="big">Don't just learn history. Hack it.</h1>
  <div class="row" style="margin-top:14px;">
    <div class="col card"><div class="big-num"></div><b style="font-size:24px;color:{NAVY}">You're the historian.</b>
      <div style="font-size:21px;margin-top:6px;">You'll weigh real primary sources and <b>make your own call</b> — there's no answer key.</div></div>
    <div class="col card"><div class="big-num"></div><b style="font-size:24px;color:{NAVY}">1877 → today.</b>
      <div style="font-size:21px;margin-top:6px;">Ten stops, one flight across modern America — every unit builds on the last.</div></div>
    <div class="col card"><div class="big-num"></div><b style="font-size:24px;color:{NAVY}">It's about you.</b>
      <div style="font-size:21px;margin-top:6px;">Different experiences, same journey. Your voice is part of the story.</div></div>
  </div>""", time="2 min"))

# 5 — LOG INTO SCHOOLOGY
SL.append(slide("Step 1",
  f"""<h1>Log into Schoology</h1>
  <div class="steps">
  <p><b>1.</b> Go to <b>[ app.schoology.com ]</b> <span class="edit">(or your district portal)</span></p>
  <p><b>2.</b> Sign in with your <b>school Google account</b></p>
  <p><b>3.</b> Join our class with the access code:</p>
  </div>
  <div style="text-align:center;margin-top:14px;"><span class="code">[ ____ – ____ ]</span></div>
  <div class="hint">We'll do this together — thumbs up when you're in.</div>""",
  time="4 min"))

# 6 — TOUR
SL.append(slide("Step 2",
  f"""<h1>Where everything lives</h1>
  <div class="buckets">
    <div class="bucket"><h3> Materials</h3><div style="font-size:20px">Lessons + your <b>Flight Log</b> (where all your writing goes)</div></div>
    <div class="bucket"><h3> Calendar</h3><div style="font-size:20px">What's due, and when</div></div>
    <div class="bucket"><h3> Grades</h3><div style="font-size:20px">How you're doing — check it weekly</div></div>
    <div class="bucket"><h3> Messages</h3><div style="font-size:20px">The fastest way to reach me</div></div>
  </div>
  <div class="stem"> Challenge: find the <b>Unit 1</b> folder and open the <b>Flight Log</b>. Thumbs up when you see it.</div>""",
  time="3 min"))

# 7 — SYLLABUS
SL.append(slide("Step 3",
  f"""<h1>The syllabus</h1>
  <div class="row">
    <div class="col card"><b style="font-size:23px;color:{NAVY}">Bring every day</b>
      <div style="font-size:21px;margin-top:6px;">Charged Chromebook · something to write with · your brain</div></div>
    <div class="col card"><b style="font-size:23px;color:{NAVY}">How grades work</b>
      <div style="font-size:21px;margin-top:6px;">[ grading + redo/retake policy — edit ]</div></div>
    <div class="col card"><b style="font-size:23px;color:{NAVY}">Reach me</b>
      <div style="font-size:21px;margin-top:6px;">[ email / Schoology message / room # — edit ]</div></div>
  </div>
  <div class="stem"> Skim it now and <b>star ONE question</b> you want answered before you leave.</div>""",
  time="2 min"))

# 8 — THE ONE RULE (full navy)
SL.append(f"""<div class="slide" style="background:{NAVY};">
  <div class="pad" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
    <div style="color:{GOLD};font-weight:700;letter-spacing:3px;font-size:24px;">OUR ONE RULE</div>
    <div style="font-family:'Liberation Serif',serif;color:{GOLD};font-size:190px;font-weight:700;line-height:1;margin:6px 0 10px;">RESPECT</div>
    <div style="color:{CREAM};font-size:34px;">We have exactly one rule. <b>Everything else fits under it.</b></div>
  </div>
  <div class="time" style="background:transparent;border-color:{GOLD};color:{GOLD};"> 1 min</div></div>""")

# 9 — WHAT DOES RESPECT LOOK LIKE
SL.append(slide("Turn &amp; talk",
  f"""<h1>What does respect look like — <span style="color:{RED}">here?</span></h1>
  <div class="buckets">
    <div class="bucket"><h3>Yourself</h3></div>
    <div class="bucket"><h3>Each other</h3></div>
    <div class="bucket"><h3>This room</h3></div>
    <div class="bucket"><h3>Our learning</h3></div>
  </div>
  <div class="stem"> With your partner (60 sec): "Respect <b>looks like</b> ______ and <b>sounds like</b> ______."</div>""",
  time="2 min"))

# 10 — YOU WRITE THE RULES
SL.append(slide("You make the call",
  f"""<h1>You write the rules — under RESPECT</h1>
  <div class="sub">Every rule we keep has to pass one test: <b>does it show respect?</b> You propose them. We adopt them. They're <i>ours</i>.</div>
  <div class="buckets" style="margin-top:12px;">
    <div class="bucket"><h3>Yourself</h3><div class="line"></div><div class="line"></div></div>
    <div class="bucket"><h3>Each other</h3><div class="line"></div><div class="line"></div></div>
    <div class="bucket"><h3>This room</h3><div class="line"></div><div class="line"></div></div>
    <div class="bucket"><h3>Our learning</h3><div class="line"></div><div class="line"></div></div>
  </div>
  <div class="stem" style="text-align:center;"> Wheels up. Welcome to the year.</div>""",
  time="3 min"))

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(SL)}</body></html>"
out = sys.argv[1] if len(sys.argv) > 1 else "Day1_Welcome_Respect_Deck.pdf"
HTML(string=html).write_pdf(out)
print(f"WROTE {out} ({len(SL)} slides)")
