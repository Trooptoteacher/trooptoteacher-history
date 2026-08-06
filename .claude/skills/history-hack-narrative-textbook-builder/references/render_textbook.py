#!/usr/bin/env python3
"""
Proof renderer for "To Form a More Perfect Union" — Part 1.
content -> HTML -> WeasyPrint -> PDF. Layout governed entirely by style.css
(the B&W-safe print contract). This is the Unit 1 + front-matter PROOF that
demonstrates the redesign + Sean's edit list before rolling to Units 2-3.
"""
from pathlib import Path
from weasyprint import HTML

BASE = Path(__file__).parent
A = "assets"

CREW = [
    ("crew_archive.png",   "Archive", "Call sign “J. Troop” · Pilot & Mission Commander",
     "Flew real C-130s; a historian who refuses to tell you what to think — she picks the year, frames the question, keeps the crew honest to the sources."),
    ("crew_spark.png",     "Spark", "Engagement Specialist",
     "Drops a real primary source in your hands at every stop and asks the one question that matters: “What do you notice?”"),
    ("crew_copilot.png",   "Co-Pilot", "Differentiation",
     "A medic meets the person in front of them — and if the first way in fails, there are three more. Nobody gets left behind."),
    ("crew_navigator.png", "Navigator", "ELL / ESS Specialist",
     "An interpreter who lived between two languages. Makes sure nobody gets lost — not in the history, not in the language."),
    ("crew_notetaker.png", "Notetaker", "Record-Keeper",
     "After every mission someone writes down what actually happened — your end-of-stop check. Never tells you what to conclude."),
    ("__SAM__",            "Sam Calloway", "House Author & Tennessee Guide",
     "Lands the national story at home — “where does this touch Tennessee?” — and keeps your eye on the whole arc of the Union."),
    ("__MUCK__",           "MSgt “Muck”", "Debriefer · POL / Fuels",
     "Won’t let you lift off until you can say, in one plain sentence, what the stop cost and what it bought. Highest standards on the flight line."),
]

STANDARDS = [
    ("US.01","Impact of the Homestead Act and the Transcontinental Railroad on westward settlement."),
    ("US.02","Federal Indian policy — reservations, assimilation, and off-reservation boarding schools."),
    ("US.03","How the Compromise of 1877 ended Reconstruction and enabled the rise of Jim Crow."),
    ("US.04","Gilded Age politics and economics — political machines and the capital–labor divide."),
    ("US.05","Inventions, business innovations, and industrial leaders that transformed American life."),
    ("US.06","Growth of industrial centers — urbanization and labor conditions."),
    ("US.07","‘Old’ vs. ‘new’ immigrants and nativist responses to immigration."),
]

VOCAB = [
    ("homestead","A claim of public land (usually 160 acres) a settler could earn by living on and improving it."),
    ("assimilation","Forcing a people to abandon their own culture and adopt the dominant one."),
    ("Jim Crow","State and local laws that enforced racial segregation and stripped Black Americans of rights."),
    ("political machine","An organization (e.g., Tammany Hall) that controlled a city’s politics through favors."),
    ("Gospel of Wealth","Carnegie’s idea that the rich had a duty to use their fortunes for public good."),
    ("nativism","Hostility toward immigrants and a preference for the native-born."),
]

def img(path): return f'{A}/{path}'

def crew_card(c):
    fn,nm,rl,ds=c
    if fn=="__SAM__":
        pic='<div class="ph"><span class="mono">SC</span><small>add photo</small></div>'
    elif fn=="__MUCK__":
        pic='<div class="ph"><span class="mono">MM</span><small>add photo</small></div>'
    else:
        pic=f'<img src="{img(fn)}" alt="{nm}">'
    return f'<div class="crew">{pic}<div><div class="nm">{nm}</div><div class="rl">{rl}</div><div class="ds">{ds}</div></div></div>'

def sec(eyebrow,title):
    return f'<div class="sec"><div class="eyebrow">{eyebrow}</div><h2>{title}</h2><div class="u"></div></div>'

# ── WHITE-SPACE VALUE RULE ───────────────────────────────────────────────────
# Any page left with meaningful bottom gap must earn its space with pedagogy —
# a check-in, self-assessment, prediction, reflection, or Future-Ready/ACT tie.
# These reusable value blocks are how we honor that rule.
def _ag_row(stmt):
    return (f'<div class="ag-row"><span class="st">{stmt}</span>'
            f'<span class="boxes"><span class="cb"></span>Agree &nbsp;<span class="cb"></span>Disagree</span></div>')

def value_before_you_fly():
    rows="".join(_ag_row(s) for s in [
        "1. Settling the West mostly meant moving onto empty land.",
        "2. In an industrializing economy, hard work was enough to get ahead.",
        "3. “Separate but equal” was a reasonable compromise for its time.",
    ])
    return f'''<div class="value">
  <div class="vh"><span class="tag">Before You Fly</span><h4>Set your heading — predict, commit, self-check</h4></div>
  <p><b>Anticipation guide.</b> Agree or disagree on instinct. You’ll revisit these at <i>The Arc of the Union</i> and see whether the evidence moved you.</p>
  {rows}
  <p style="margin-top:9px"><b>Set your goal (SMART).</b> One thing you’ll master this unit:</p>
  <div class="write"><div class="ln"></div></div>
  <div class="fr-tie"><b>Future-Ready · ACT-Ready.</b> Predicting from limited evidence, then revising when the data comes in, is exactly what the ACT reading section — and every real decision — asks of you. &nbsp;Rate your starting knowledge of US.01–US.07: <span class="rate">1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;5</span></div>
</div>'''

def value_your_seat():
    opts=[
        "Notice like <b>Spark</b> — catch the detail everyone else misses.",
        "Question the source like <b>Archive</b> — who made this, and why?",
        "Find another way in like <b>Co-Pilot</b> — when I get stuck.",
        "Make it make sense like <b>Navigator</b> — say it in my own words.",
        "Capture it like <b>Notetaker</b> — organized notes I can study from.",
        "Debrief like <b>Muck</b> — one honest sentence on what it cost and bought.",
    ]
    rows="".join(f'<div class="ag-row"><span class="boxes"><span class="cb"></span></span><span class="st">{o}</span></div>' for o in opts)
    return f'''<div class="value tight">
  <div class="vh"><span class="tag">Your Seat on the Crew</span><h4>Which job is <i>your</i> job this year?</h4></div>
  <p>Every crew role is a thinking skill you’ll practice all year. Check your <b>growth edge</b> — the muscle you most want to build this unit.</p>
  <div class="two-col">{rows}</div>
</div>'''

def value_ready_check():
    return '''<div class="value tight">
  <div class="vh"><span class="tag">Ready-Graduate Check</span><h4>Why this makes you ACT-ready</h4></div>
  <p><b>Source it → hear every side → weigh the evidence → make your call.</b> That’s the exact move the ACT reading section rewards and every real decision demands. <b>Reflect:</b> which move feels hardest for you right now — and why?</p>
  <div class="write"><div class="ln"></div><div class="ln"></div></div>
</div>'''

def value_predict():
    return '''<div class="value">
  <div class="vh"><span class="tag">Make Your Call</span><h4>Predict before you land</h4></div>
  <p>Six people, one industrializing nation. <b>Predict:</b> as America builds railroads, factories, and cities from 1877–1900, whose America is being built — and who do you expect to gain, and who to lose? Commit now; you’ll test it against the evidence at every stop.</p>
  <div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
  <div class="fr-tie"><b>Why this matters.</b> Naming a claim <i>before</i> you have all the evidence — then revising it honestly — is the core habit of a historian, an analyst, and a Ready Graduate. That’s the skill this book trains.</div>
</div>'''

# ---- PAGE 1: TOC (redesigned, B&W-safe) ----
toc_rows = [
    ("0","Before the First Mission","Chapter Zero · the crew’s troops-to-teachers origin story",""),
    ("1","The Nation Turns West — and the Cities Rise","The Rise of Industrialization · 1877–1900 · 7 stops","US.01–US.07"),
    ("2","Turning the Light On","The Progressive Era · 1890–1920 · 7 stops","US.08–US.18"),
    ("3","On the Menu","Imperialism & World War I · 1898–1919 · 6 stops","US.19–US.27"),
    ("★","The Arc of the Union","A standalone section — plot the whole climb and make your call",""),
]
toc="".join(
    f'<div class="toc-row"><div class="toc-num">{n}</div>'
    f'<div class="toc-body"><div class="toc-title">{t}</div><div class="toc-meta">{m}</div></div>'
    f'<div class="toc-std">{s}</div></div>'
    for n,t,m,s in toc_rows)
page_toc = f'''<section class="page">{sec("To Form a More Perfect Union","Contents")}
{toc}
<div class="callout" style="margin-top:16px"><b>How to read this book.</b> Each unit is a flight. The crew (below) guide you; the era-friends you meet on the ground actually lived the year you land in. Every stop hands you a real source and ends with your call — there is no answer key.</div>
<figure class="fit" style="margin-top:16px"><img src="{img('u1_railroad.png')}" alt="Golden Spike, 1869"><figcaption style="text-align:center">Golden Spike Ceremony, Promontory Summit, Utah, May 10, 1869 — the year this book opens. <i>A. J. Russell / National Archives.</i></figcaption></figure>
</section>'''

# ---- PAGE 2: Meet the Crew (ONE page, deduped) ----
page_crew = f'''<section class="page">{sec("Chapter Zero","Meet the Crew")}
<p class="lead">Seven seats. Seven people. The crew are the time-travelers — <b>they guide.</b> The era-friends you meet when the ramp drops actually lived the year you land in. And the newest crew on this plane? That’s <b>you.</b></p>
<div class="crew-grid">{''.join(crew_card(c) for c in CREW)}</div>
{value_your_seat()}
<p class="small" style="margin-top:7px">The Flight Crew are fictional characters (™) of TroopToTeacher Technologies LLC.</p>
</section>'''

# ---- PAGE 3: How This Book Works + pedagogy matrix ----
matrix=[
 ("Source It First","Every stop opens with a real primary source (Spark).","C3 Inquiry; DBQ","Reading/writing across the curriculum"),
 ("Steelman, then weigh","Each side gets its strongest hearing before any critique.","CER; argument","ELA — argument & evidence"),
 ("The Arc of the Union","Students predict & decide: did this move the country toward its promise, or away?","Historical reasoning","Civics — founding ideals"),
 ("Notes & Debrief","Cornell-style capture (Notetaker) + one-sentence debrief (Muck).","Retrieval practice (Hattie d≈0.70)","Metacognition / SEL"),
 ("Multiple ways in","Entry / On-Level / Extension paths; EN/ES vocabulary (Co-Pilot, Navigator).","UDL 3.0; WIDA","MTSS / ELL"),
]
mrows="".join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in matrix)
page_how=f'''<section class="page">{sec("Start here","How This Book Works")}
<p class="lead">Six things are true of every unit, so you only learn them once. This book isn’t a lecture — it’s a method: <b>look at the evidence, hear every side fairly, then make your own call.</b></p>
<div class="tint" style="margin:6px 0 14px"><b>The through-line — the Arc of the Union.</b> The Constitution’s first line sets the goal: to “form a more perfect union.” At every stop you’ll <b>predict and decide</b> whether the country climbed toward that promise or slipped back — and defend it with evidence. That habit of reasoned judgment is the whole point.</div>
<div class="sec" style="border-left-color:var(--gold)"><div class="eyebrow">Evidence-based · cross-curricular</div><h2 style="font-size:14pt">What’s working under the hood</h2></div>
<table class="mx"><thead><tr><th>Move</th><th>What students do</th><th>Research base</th><th>Cross-curricular tie</th></tr></thead><tbody>{mrows}</tbody></table>
<p class="small" style="margin-top:8px">Research base: CAST UDL 3.0 (2024) · Hattie’s <i>Visible Learning</i> · C3 Framework · WIDA ELD. Classroom-formative · pre-field-test.</p>
{value_ready_check()}
</section>'''

# ---- PAGE 4: Unit 1 divider (Arabic numeral, B&W-safe standards) ----
stds="".join(f'<div class="std"><span class="chip">{c}</span><span class="txt">{t}</span></div>' for c,t in STANDARDS)
page_div=f'''<section class="page">
<div style="border-top:3px solid var(--rule);border-bottom:3px solid var(--rule);padding:14px 0;margin-bottom:6px">
  <div style="font:700 10pt 'DejaVu Sans';letter-spacing:.2em;color:var(--red)">UNIT 1</div>
  <h1 style="font-size:30pt;margin:4px 0 2px">The Nation Turns West — and the Cities Rise</h1>
  <div class="toc-meta" style="font-size:11pt">The Rise of Industrialization · 1877–1900</div>
</div>
<div class="std-list">{stds}</div>
<div class="callout"><b>Essential Question.</b> As America industrialized, the same forces — the railroad, the factory, the open door — meant opportunity for some and loss for others. <b>Whose America was being built, and at whose expense?</b> Hold this question the whole unit.</div>
{value_before_you_fly()}
</section>'''

# ---- PAGE 5: Who you'll travel with (era-friends strip, own page) ----
friends=[
 ("Anna Halvorsen","A homestead claim on the plains — her family crossed an ocean for one sheet of paper."),
 ("Chaska","A young Dakota man watching the same acres named ‘empty’ that his nation calls home."),
 ("Isaiah","A Black Southerner navigating the end of Reconstruction and the rise of Jim Crow."),
 ("Rosa","A tenement seamstress in the roaring industrial city."),
 ("Frankie","A precinct kid learning how a political machine really runs a city."),
 ("Nora Doyle","A ‘new’ immigrant stepping off the boat at Ellis Island."),
]
fr="".join(f'<div class="friend"><div><div class="fn">{n}</div><div class="fd">{d}</div></div></div>' for n,d in friends)
page_friends=f'''<section class="page">{sec("Unit 1","Who you’ll travel with")}
<p class="lead">Six era-friends carry this unit. They are <b>composite characters</b> — invented from the documented record and marked as fiction throughout. Real historical figures appear only in their own recorded words.</p>
{fr}
<div class="tint" style="margin-top:10px"><b>🦬 Witness Lens — the Buffalo.</b> Not a person, not a side. The great herds — tens of millions — are a witness to what the railroad and the plow changed. Watch for the Witness Lens at key stops.</div>
{value_predict()}
</section>'''

# ---- STOPS 1–7 (data-driven from the canonical banks) ----
import json as _json, html as _html
_ROOT = BASE.parents[1]                                  # history-hack-web-app
_NARR = _json.load(open(_ROOT/"content-build/us-history/narrative/unit-01.json"))
_READER = _json.load(open(_ROOT/"public/data/us-history/textbook/unit-1.json"))
_VOCAB = {t["term"]: t["definition"] for t in _json.load(open(_ROOT/"public/data/us-history/vocabulary/unit-1.json"))}
def _esc(s): return _html.escape(str(s or ""), quote=False)
def _spread(n): return next((s for s in _NARR["spreads"] if s.get("spreadNumber")==n), {})
def _src(n):
    for s in _READER.get("spreads",[]):
        if s.get("spreadNumber")==n: return (s.get("primarySource") or {}).get("image") or {}
    return {}

# Per-stop presentation metadata (image asset, short title, Word-Wall terms, WHO/WHEN/WHY, TN tie).
# TN ties marked verified are historian-confirmable facts; the rest are honest inquiry prompts
# pending a tn-content-specialist / historian-factcheck fill.
STOP_META = {
 1:{"title":"Free Land — and Whose Land?","img":"u1_railroad","terms":["Homestead Act","Transcontinental Railroad","Exodusters"],
    "who":"Andrew J. Russell — a Union Pacific photographer on assignment.","when":"May 10, 1869 — the rails meet at Promontory Summit.","why":"To document a national triumph: coast joined to coast by rail.",
    "closer":"Who is <i>in</i> this photo — and who isn’t? Whose land did these tracks cross?",
    "tn":"<b>★ Tennessee Connection.</b> Nashville’s Pap Singleton led the ‘Exodusters’ west as Reconstruction collapsed; Buffalo Soldier George Jordan, born in Tennessee, earned the Medal of Honor on this frontier."},
 2:{"title":"Made to Vanish","img":"u1_carlisle","terms":["Reservation System","Dawes Act","Assimilation"],
    "who":"John N. Choate — the Carlisle school’s official photographer.","when":"1882 and 1885 — ‘before’ and ‘after’ portraits of Tom Torlino (Navajo).","why":"To advertise assimilation as a success and win support for the boarding-school program.",
    "closer":"What does the ‘before/after’ framing want you to believe — and what does it hide?",
    "tn":"<b>★ Tennessee Connection.</b> Red Clay, Tennessee, was the last seat of the Cherokee national government before the 1838 Removal — the same assimilation-or-remove logic this federal policy carried forward."},
 3:{"title":"The Refs Walk Off","img":"u1_freedmen","terms":["Compromise of 1877","Jim Crow Laws","Plessy v. Ferguson","Disenfranchisement"],
    "who":"Alfred R. Waud — a <i>Harper’s Weekly</i> illustrator.","when":"July 25, 1868 — a Freedmen’s Bureau officer holding two mobs apart.","why":"To show a national audience the Bureau standing between freedpeople and violence.",
    "closer":"When the federal ‘referee’ leaves in 1877, who gets to write the rules next?",
    "tn":"<b>★ Tennessee Connection.</b> Tennessee passed one of the nation’s earliest separate-car (segregation) laws in 1881 — Jim Crow taking legal shape at home."},
 4:{"title":"The Group Chat You’re Not In","img":"u1_trust","terms":["Gilded Age","Political Machines","Spoils System","Pendleton Act"],
    "who":"Joseph Keppler — cartoonist for <i>Puck</i>.","when":"January 23, 1889 — “The Bosses of the Senate.”","why":"To argue that industrial trusts, not voters, controlled the Senate.",
    "closer":"Why draw the trusts as giants and the senators as tiny? Where is the ‘People’s Entrance’?",
    "tn":"<b>★ Tennessee Connection — investigate.</b> How did machine politics take root in a Tennessee city (start with Memphis)? Find one local example. <i>[pending historian-verified fill]</i>"},
 5:{"title":"Gospel — and Its Price","img":"u1_octopus","terms":["Robber Barons/Captains of Industry","Monopoly","Trust","Vertical Integration"],
    "who":"Udo J. Keppler — cartoonist for <i>Puck</i>.","when":"September 7, 1904 — “Next!”","why":"To depict Standard Oil as an octopus strangling industry and government.",
    "closer":"Carnegie’s ‘Gospel of Wealth’ and this cartoon describe the same men. Which is true — or are both?",
    "tn":"<b>★ Tennessee Connection.</b> Tennessee ended convict leasing in 1896 after the Coal Creek War, when miners rose against prisoners being leased into the mines — industrial labor’s fight, fought at home."},
 6:{"title":"The City That Can’t House Its Workers","img":"u1_ellis","terms":["Urbanization","Ellis Island","New Immigrants","Push-Pull Factors"],
    "who":"Detroit Publishing Company.","when":"ca. 1910–1920 — the Ellis Island inspection room.","why":"To document the processing point where more than twelve million immigrants entered.",
    "closer":"What do the benches, rails, and scale of the room say about how the country saw the people passing through?",
    "tn":"<b>★ Tennessee Connection — investigate.</b> How did Nashville and Memphis grow as rail-and-industry hubs in these years? Find one example of who did the work. <i>[pending historian-verified fill]</i>"},
 7:{"title":"‘Expat’ or ‘Immigrant’?","img":"u1_riis","terms":["Old Immigrants","New Immigrants","Nativism","Chinese Exclusion Act"],
    "who":"Jacob Riis — police reporter and reformer.","when":"1889 — “Five Cents a Spot,” a Bayard Street lodging house.","why":"To expose tenement conditions in <i>How the Other Half Lives</i> and force reform.",
    "closer":"Riis wanted reform — but whose gaze is the camera? How might the people in the room have told it?",
    "tn":"<b>★ Tennessee Connection — investigate.</b> Which immigrant communities put down roots in Tennessee in this era, and how were they received? <i>[pending historian-verified fill]</i>"},
}

# HVT — "High-Value Target": the single must-know takeaway per standard (EOC-tested
# core). A concise summary-label of the LOCKED standard, not new narrative.
HVT = {
 1:"The transcontinental railroad and Homestead Act opened the West for settlers <b>and</b> drove the dispossession of Native nations — one expansion, two outcomes.",
 2:"Reservations, the Dawes Act, and boarding schools were one coordinated policy to break up Native land and erase culture — assimilation by force.",
 3:"The Compromise of 1877 ended Reconstruction; <i>Plessy v. Ferguson</i> (1896) made ‘separate but equal’ the law — the legal foundation of Jim Crow.",
 4:"In the Gilded Age, trusts and political machines held the real power; the Pendleton Act began replacing the spoils system with merit.",
 5:"Industrial titans built the modern economy through monopoly and vertical/horizontal integration — hailed as ‘Captains of Industry,’ condemned as ‘Robber Barons.’",
 6:"Industrial jobs plus mass immigration exploded the growth of cities — and packed workers into crowded, dangerous tenement conditions.",
 7:"‘New immigrants’ from Southern & Eastern Europe and Asia met nativism and exclusion laws — including the Chinese Exclusion Act (1882).",
}
def _wordwall(terms):
    cells=[]
    for t in terms:
        d=_VOCAB.get(t)
        if d: cells.append(f'<div class="v"><span class="t">{_esc(t)}</span> — {_esc(d)}</div>')
    return "".join(cells)

def stop_page(n):
    sp=_spread(n); m=STOP_META[n]; im=_src(n)
    code=", ".join(sp.get("standardCodes") or [f"US.0{n}"])
    lo=_esc(sp.get("learningObjective"))
    hook=_esc(sp.get("engagementHook"))
    cap=_esc(im.get("caption")); cite=_esc(im.get("citation"))
    # Deterministic page-fill: scale the primary-source image height inversely to the
    # stop's content weight (hook + vocab), so every stop self-levels to ~92-96%.
    weight = len(sp.get("engagementHook") or "") + sum(len(_VOCAB.get(t,"")) for t in m["terms"])
    img_h = 3.1 if weight<1000 else 3.05 if weight<1100 else 2.8
    terms = m["terms"][:3] if weight>1130 else m["terms"]   # trim the single densest stop so the cue fits
    return f'''<section class="page">
<div class="stop-hd"><span class="n">{n}</span><span class="t">{_esc(m["title"])}</span></div>
<p class="small"><b>Standard {code} · Learning target:</b> {lo}</p>
<div class="callout"><b>Spark asks:</b> {hook} <b>What do you notice?</b></div>
<div class="stop-media">
  <figure><img src="{img(m["img"]+".png")}" alt="{_esc(cap)[:120]}" style="height:{img_h}in"><figcaption>{cap} <i>{cite}</i></figcaption></figure>
  <div class="src-col">
    <div class="source-band"><h4>Source It First</h4>
      <dl><dt>WHO</dt><dd>{m["who"]}</dd><dt>WHEN</dt><dd>{m["when"]}</dd><dt>WHY</dt><dd>{m["why"]}</dd></dl>
      <div class="small"><b>Read it closer:</b> {m["closer"]}</div>
    </div>
    <div class="hvt"><div class="hvt-hd"><span class="hvt-badge">◎ HVT</span> High-Value Target — lock this in</div><p>{HVT[n]}</p></div>
  </div>
</div>
<div class="sec" style="border-left-color:var(--gold);margin:8px 0 6px"><div class="eyebrow">Word Wall · EN/ES</div></div>
<div class="vocab">{_wordwall(terms)}</div>
<div class="tint cool" style="margin-top:10px">{m["tn"]}</div>
<div class="fl-cue">▶ Now make your call — capture Stop {n} on the next page (your Flight Log).</div>
</section>'''

def writing_page(n):
    sp=_spread(n); m=STOP_META[n]
    cc=sp.get("comprehensionCheck"); cc=cc if isinstance(cc,dict) else {}
    prompt=_esc(cc.get("question")) or "Make the call on this stop, and defend it with evidence from the source."
    nxt = f"fly to Stop {n+1}." if n<7 else "head to the Arc of the Union."
    claim="".join('<div class="ln"></div>' for _ in range(7))
    eviA="".join('<div class="ln"></div>' for _ in range(4)); eviB="".join('<div class="ln"></div>' for _ in range(4))
    deb="".join('<div class="ln"></div>' for _ in range(3))
    return f'''<section class="page">{sec("MSgt “Muck” · Debrief", _esc(m["title"])+" — Make Your Call")}
<p class="lead">{prompt} <b>Claim first, then prove it — a detail from each side.</b></p>
<div class="wlabel">Your claim — one sentence:</div>
<div class="write">{claim}</div>
<div class="two-ev">
  <div><div class="wlabel">Evidence — first perspective:</div><div class="write">{eviA}</div></div>
  <div><div class="wlabel">Evidence — the other:</div><div class="write">{eviB}</div></div>
</div>
<div class="sec" style="border-left-color:var(--gold);margin:12px 0 5px"><div class="eyebrow">Self-grade before you fly</div></div>
<table class="rubric"><thead><tr><th>4 — Cleared</th><th>3 — Airworthy</th><th>2 — Pre-flight</th><th>1 — Grounded</th></tr></thead>
<tbody><tr>
<td>Clear claim + evidence from <b>both</b> sides; names the tension between them.</td>
<td>Claim + evidence from both; tension implied, not stated.</td>
<td>Claim with evidence from only one side.</td>
<td>An opinion, no evidence yet.</td>
</tr></tbody></table>
<div class="wlabel" style="margin-top:10px">Muck’s debrief — in ONE sentence: what did this stop cost, and what did it buy?</div>
<div class="write">{deb}</div>
<div class="app"><span class="badge">Web · Writing Lab</span> &nbsp;Now go to <b>History Hack online → Writing Lab</b>, type your response, and check it against this rubric for <b>instant feedback</b>. Revise here, then {nxt}</div>
</section>'''

stops_html = "".join(stop_page(n)+writing_page(n) for n in range(1,8))

# ---- COVER (full-bleed hero art) ----
page_cover = f'<section class="cover-page"><img src="{img("cover.png")}" alt="To Form a More Perfect Union — cover"></section>'

# ---- FOREWORD (Sean's why & vision — DRAFT in the founder's voice) ----
page_foreword = f'''<section class="page fw">
<div class="kicker">Foreword</div>
<h1>Why We Built This</h1>
<div class="sub">A note on the why — and the vision.</div>
<p>I spent years in the back of a C-130, watching history happen to people up close — with the smoke still in the air. I learned what it actually costs when a country makes a choice, because I was standing where the choice landed. Then I came home and did what a lot of us did: I walked into a classroom.</p>
<div class="pull">The most dangerous thing in the world is a generation that never learned to see its own history clearly — and the most powerful thing in the world is one that did.</div>
<p>That conviction is why this book exists. The big publishers were built to make money. We were built to make a difference — <b>mission over margin</b> — and every page is measured against one question: does this actually teach, and is it better for a student than anything else on the market?</p>
<p>So we made a different kind of history book. We don’t tell you what to think. Every claim is tied to a real source you can check. We give every side its strongest, fairest hearing <i>before</i> anyone answers it. And we end with a question, not a verdict — because the weighing is yours to make, from the evidence.</p>
<p>That’s the whole flight. At every stop you’ll ask the question that runs the length of this book: is the Union bending toward its founding promise — a <i>more perfect union</i> — or away? You decide. Then you defend it.</p>
<p>This is for the veterans who came home and became teachers. It’s for Tennessee. And it’s for every student deciding what kind of citizen to be.</p>
<p><b>Welcome aboard. Let’s fly.</b></p>
<div class="rule"></div>
<div class="sig"><div class="name">Sam Calloway</div><div class="role">Founder · TroopToTeacher Technologies LLC · U.S. History Hack</div></div>
<p style="font-family:'DejaVu Serif';font-style:italic;font-size:11pt;color:var(--ink-soft);margin-top:14px">For the veterans who came home and became teachers — and for every student deciding what kind of citizen to be.</p>
</section>'''

# ---- ARC OF THE UNION — data-capture + coordinate plot (cross-curricular math/science) ----
ARC = [
    (1869,"Homestead Act & transcontinental railroad"),
    (1877,"Compromise of 1877 ends Reconstruction"),
    (1881,"Tennessee’s separate-car law"),
    (1882,"Chinese Exclusion Act"),
    (1887,"Dawes Act"),
    (1890,"Sherman Antitrust Act"),
    (1892,"Ida B. Wells’s anti-lynching campaign"),
    (1896,"Plessy v. Ferguson — ‘separate but equal’"),
    (1896,"Tennessee ends convict leasing"),
    (1901,"NY Tenement House Act"),
    (1911,"Standard Oil broken up"),
]
def arc_grid_svg():
    W,H,padL,padR,padT,padB = 662,332,74,12,20,44
    pw,ph = W-padL-padR, H-padT-padB
    def X(i): return padL + (i-0.5)/len(ARC)*pw
    def Y(v): return padT + (3-v)/6*ph
    s=[f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans">']
    # horizontal gridlines + Y labels
    ylab={3:"+3 Toward",2:"+2",1:"+1",0:"0  no change",-1:"−1",-2:"−2",-3:"−3 Away"}
    for v in range(-3,4):
        y=Y(v); bold = v==0
        s.append(f'<line x1="{padL}" y1="{y:.1f}" x2="{W-padR}" y2="{y:.1f}" stroke="{"#1b3a6b" if bold else "#d3d8e0"}" stroke-width="{1.4 if bold else 0.8}"/>')
        s.append(f'<text x="{padL-6}" y="{y+3:.1f}" text-anchor="end" font-size="9" fill="#41506a">{ylab[v]}</text>')
    # vertical gridlines + X labels (milestone # + year)
    for i,(yr,_) in enumerate(ARC,1):
        x=X(i)
        s.append(f'<line x1="{x:.1f}" y1="{padT}" x2="{x:.1f}" y2="{H-padB}" stroke="#eef1f6" stroke-width="0.8"/>')
        s.append(f'<text x="{x:.1f}" y="{H-padB+14:.1f}" text-anchor="middle" font-size="9" font-weight="bold" fill="#1b3a6b">{i}</text>')
        s.append(f'<text x="{x:.1f}" y="{H-padB+27:.1f}" text-anchor="middle" font-size="7.5" fill="#7a828e">{yr}</text>')
    # axis frame
    s.append(f'<line x1="{padL}" y1="{padT}" x2="{padL}" y2="{H-padB}" stroke="#1b2a41" stroke-width="1"/>')
    s.append('</svg>')
    return "".join(s)

def arc_capture_rows():
    return "".join(
        f'<tr><td class="c">{i}</td><td class="c">{yr}</td><td>{lab}</td>'
        f'<td class="call">−3 &nbsp;−2 &nbsp;−1 &nbsp;0 &nbsp;+1 &nbsp;+2 &nbsp;+3</td></tr>'
        for i,(yr,lab) in enumerate(ARC,1))

page_arc_plot = f'''<section class="page">{sec("The Arc of the Union · its own section","Chart the Nation’s Climb")}
<p class="lead">You made a call at every stop: did this moment move the country <b>toward</b> a more perfect union, or <b>away</b>? Now turn your judgments into data. <b>1)</b> Score each milestone below (−3 = far from the promise, +3 = toward it). <b>2)</b> Plot each score on the grid. <b>3)</b> Connect the dots in order — that line <i>is</i> the Arc of the Union.</p>
<table class="arc"><thead><tr><th class="c">#</th><th class="c">Year</th><th>Milestone</th><th>My call — circle one</th></tr></thead><tbody>{arc_capture_rows()}</tbody></table>
<div class="grid-wrap">{arc_grid_svg()}</div>
<p class="small" style="text-align:center;margin-top:2px">Milestone (1–11) →&nbsp;&nbsp;&nbsp;plot your call for each, then connect the points in order.</p>
</section>'''

page_arc_read = f'''<section class="page">{sec("The Arc of the Union","Read the Arc — the cross-curricular part")}
<p class="lead">A graph turns eleven separate judgments into one picture you can defend. Now read your own data like a mathematician and a scientist.</p>
<div class="xc">
  <div class="value tight"><div class="vh"><span class="tag">Math</span><h4>Trend &amp; average</h4></div>
    <p>Each call is an ordered pair — <b>(milestone, score)</b> — and your connected points are a <b>line graph</b>. Does the line mostly <b>climb</b> (positive slope) or <b>fall</b>?</p>
    <p>Add your 11 scores and divide by 11 — the <b>mean</b>. A positive mean says the nation, on balance, moved toward the promise; negative says away.</p>
    <p><b>My mean score:</b> <span class="blank">&nbsp;</span> &nbsp;·&nbsp; Overall trend (circle): &nbsp;<b>Climbing &nbsp; Falling &nbsp; Mixed</b></p>
  </div>
  <div class="value tight"><div class="vh"><span class="tag">Science</span><h4>Pattern in the data</h4></div>
    <p>Scientists plot data to reveal patterns a table hides. Your graph exposes the <b>shape</b> of this era — where it rose and where it broke.</p>
    <p>Where is the <b>steepest climb</b>? The <b>steepest drop</b>? Name one milestone where the line changes direction, and say what caused the turn.</p>
    <div class="write"><div class="ln"></div><div class="ln"></div></div>
  </div>
</div>
<div class="callout" style="margin-top:12px"><b>Make the call — with your graph as evidence.</b> Answer the unit’s Essential Question: in these years, did America move <i>toward</i> a more perfect union, or away? Defend it with the shape of your arc — the trend, the mean, and the turning point that matters most.</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="xc" style="margin-top:10px">
  <div class="value tight"><div class="vh"><span class="tag">Correlate</span><h4>Compare arcs</h4></div>
  <p>Trade graphs with a partner. Where do your two lines <b>agree</b>? Where do they <b>diverge</b> — and why can two people plot the same evidence differently? Circle the one milestone you’d most defend from the sources.</p></div>
  <div class="value tight"><div class="vh"><span class="tag">Extrapolate → Unit 2</span><h4>Predict the next arc</h4></div>
  <p>Your data stops in 1911. <b>Extend the line:</b> if the trend held, where would <b>1920</b> land? Draw a <b>dotted prediction</b> off the grid’s right edge — the Progressive Era is where you test it.</p></div>
</div>
<div class="fr-tie"><b>Cross-curricular · Future-Ready.</b> Plotting evidence, finding a trend, extrapolating, and defending a claim with data is the shared language of history, math, science, and every college and career path — same skill, different classroom.</div>
</section>'''

html = f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="style.css"></head><body>
{page_cover}{page_foreword}{page_toc}{page_crew}{page_how}{page_div}{page_friends}{stops_html}{page_arc_plot}{page_arc_read}
</body></html>'''

out = BASE/"out"/"ToFormAMorePerfectUnion_Unit1_PROOF.pdf"
HTML(string=html, base_url=str(BASE)).write_pdf(str(out))
print("WROTE", out)

# ── PAGE-FILL QC GATE ────────────────────────────────────────────────────────
# House rule: every content page must fill >= TARGET_FILL of the live area
# (below the running footer). The cover is exempt (full-bleed); the foreword is
# exempt (fills once the founder personalizes it). Everything else must earn 90%.
TARGET_FILL = 90
EXEMPT = {1: "cover (full-bleed)", 2: "foreword (fills when personalized)"}
try:
    import fitz
    doc = fitz.open(str(out)); DPI=100; FOOT=int(0.55*DPI); fails=[]
    print(f"\nPAGE-FILL QC  (target {TARGET_FILL}%):")
    for i in range(doc.page_count):
        pm=doc[i].get_pixmap(colorspace=fitz.csGRAY,dpi=DPI); W,H=pm.width,pm.height; px=pm.samples
        lim=H-FOOT; end=0
        for y in range(lim):
            if min(px[y*W:(y+1)*W])<205: end=y
        fill=100*end/lim; n=i+1
        tag = f"exempt — {EXEMPT[n]}" if n in EXEMPT else ("OK" if fill>=TARGET_FILL else "*** BELOW TARGET ***")
        if n not in EXEMPT and fill<TARGET_FILL: fails.append((n,fill))
        print(f"  p{n:>2}  {fill:5.1f}%  {tag}")
    print(("QC PASS — every non-exempt page ≥ %d%%." % TARGET_FILL) if not fails
          else ("QC FAIL — %d page(s) below %d%%: %s" % (len(fails),TARGET_FILL,", ".join(f"p{n} ({f:.0f}%)" for n,f in fails))))
    doc.close()
except ImportError:
    print("QC skipped (pymupdf not available)")
