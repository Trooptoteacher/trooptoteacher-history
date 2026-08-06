#!/usr/bin/env python3
"""
Flight Log builder — the write-in student companion to the narrative textbook
("To Form a More Perfect Union"). Generates, per unit: a brand cover, a SMART-
goals page, and one cross-referenced log entry per stop, then an Arc-of-the-
Union capture. The log entries and the textbook's per-stop writing cues are
generated from the SAME stop data, so the cross-reference is accurate by
construction (Textbook Stop N ⇄ Flight Log Entry N).

For Units built through build_unit.py (the generalized textbook builder), the
stop index is DERIVED from build_unit.UNITS so titles/codes can never drift from
the reader. Unit 1 (rendered by render_proof.py) keeps a local stop index.

Editions:
  * Student edition  — blank write-in log (default).
  * Teacher edition  — same structure + grounded exemplar CER answers, a model
    debrief, and self-grade anchors per stop (teacher-side only, per guardrail #2).

Usage:
  python3 build_flightlog.py <unitNumber>            # student edition
  python3 build_flightlog.py <unitNumber> teacher    # teacher edition
Layout governed by style.css (+ flight-log styles; teacher-only styles inlined).
"""
import json as _json, html as _html, os, sys
from pathlib import Path
from weasyprint import HTML
import build_unit as BU   # derive stop index from the textbook builder (no-drift)

BASE = Path(__file__).parent
ROOT = BASE.parents[1]
# Cover asset. Defaults to the full-res hero art; set FL_COVER to a lighter image
# (e.g. assets/cover_web.jpg) for a smaller download build — content is identical.
COVER = os.environ.get("FL_COVER", "assets/cover.png")
def esc(s): return _html.escape(str(s or ""), quote=False)

# Unit 1 is rendered by render_proof.py (its own stop metadata); keep a local
# index here so the Flight Log matches the reader exactly. Units in BU.UNITS are
# derived from that source of truth instead (see resolve()).
STOPS_U1 = {"title":"The Nation Turns West — and the Cities Rise","years":"1877–1900",
    "stops":[(1,["US.01"],"Free Land — and Whose Land?"),(2,["US.02"],"Made to Vanish"),
             (3,["US.03"],"The Refs Walk Off"),(4,["US.04"],"The Group Chat You’re Not In"),
             (5,["US.05"],"Gospel — and Its Price"),(6,["US.06"],"The City That Can’t House Its Workers"),
             (7,["US.07"],"‘Expat’ or ‘Immigrant’?")]}

def resolve(unit):
    """Return {title, years, stops:[(n, [codes], title)]} for a unit, derived from
    the textbook builder when available so the cross-reference cannot drift."""
    if unit in BU.UNITS:
        U = BU.UNITS[unit]
        return {"title": U["title"], "years": U["years"],
                "stops": [(i+1, st["codes"], st["title"]) for i, st in enumerate(U["stops"])]}
    if unit == 1:
        return STOPS_U1
    raise SystemExit(f"No stop index for unit {unit}")

# The crew member whose narrative debrief the student writes from (the Debriefer).
DEBRIEFER = "MSgt “Muck”"

# ─────────────────────────────────────────────────────────────────────────────
# TEACHER EXEMPLARS (teacher-side only — guardrail #2). Each is a grounded model
# CER response for the stop's "Make Your Call": a claim that names the tension,
# two evidence points, and Muck's one-sentence cost/benefit debrief. Grounded in
# the stop's LOCKED HVT takeaway and Source-It-First tension; builder synthesis →
# flag for tn-content-specialist review before adoption print.
# ─────────────────────────────────────────────────────────────────────────────
EXEMPLARS = {
 1:{
  1:{"claim":"Westward expansion after 1865 was one policy with two opposite outcomes — it opened opportunity for settlers while dispossessing Native nations of their land.",
     "ev1":"The Homestead Act (1862) and the transcontinental railroad, joined in 1869 at Promontory, drew hundreds of thousands of settlers — and Exodusters — west onto 160-acre claims.",
     "ev2":"Those same rail lines and land grants cut across Native homelands, collapsing the bison herds and forcing tribes onto reservations.",
     "debrief":"It bought a settled, rail-connected continent — and it cost Native nations their land and way of life."},
  2:{"claim":"Reservations, the Dawes Act, and boarding schools were not separate events but one coordinated federal policy to break up Native land and erase Native culture.",
     "ev1":"The Dawes Act (1887) split communally held reservations into individual allotments and sold the 'surplus' to white settlers.",
     "ev2":"Schools like Carlisle used staged 'before/after' portraits to sell forced assimilation — cutting hair, banning languages, renaming children.",
     "debrief":"It bought the government cheap land and a story of 'progress' — at the cost of Native children's culture, families, and identity."},
  3:{"claim":"When federal protection withdrew in 1877, Southern states rewrote the rules to strip Black Americans of the rights Reconstruction had won.",
     "ev1":"The Compromise of 1877 pulled federal troops from the South, ending the era when a Freedmen's Bureau officer stood between freedpeople and mob violence.",
     "ev2":"Plessy v. Ferguson (1896) then made 'separate but equal' constitutional, giving Jim Crow segregation and disenfranchisement the force of law.",
     "debrief":"Ending Reconstruction bought a reunited white nation — and cost Black Americans nearly a century of legal equality."},
  4:{"claim":"In the Gilded Age the real political power sat with industrial trusts and party machines, not with ordinary voters.",
     "ev1":"Keppler's 'Bosses of the Senate' drew the trusts as giants and the senators as tiny — with the 'People's Entrance' bolted shut.",
     "ev2":"The Pendleton Act (1883) began replacing the spoils system with merit-based hiring — a first, limited check on machine power.",
     "debrief":"Machine politics bought services and order for some — at the cost of honest, representative government."},
  5:{"claim":"The same industrialists can be judged as both 'Captains of Industry' who built the modern economy and 'Robber Barons' who crushed competition.",
     "ev1":"Through trusts, monopoly, and vertical integration, men like Rockefeller controlled whole industries — Standard Oil drawn as the strangling octopus in 'Next!'",
     "ev2":"Carnegie's 'Gospel of Wealth' argued the rich had a duty to give their fortunes back, funding libraries and schools.",
     "debrief":"Consolidation bought national wealth and philanthropy — at the cost of competition and workers' bargaining power."},
  6:{"claim":"Industrial jobs and mass immigration made American cities explode in size faster than they could safely house the people who powered them.",
     "ev1":"More than twelve million immigrants entered through processing points like Ellis Island, pulled by factory work.",
     "ev2":"That growth packed workers into crowded, dangerous tenements with little light, air, or sanitation.",
     "debrief":"Urban growth bought industrial power and opportunity — at the cost of overcrowded, unsafe living conditions."},
  7:{"claim":"The 'new immigrants' from Southern and Eastern Europe and Asia were met not with welcome but with nativism and laws designed to keep them out.",
     "ev1":"Reformers like Jacob Riis exposed tenement conditions in 'How the Other Half Lives,' shaping how the public saw the newcomers.",
     "ev2":"The Chinese Exclusion Act (1882) was the first federal law to restrict immigration by nationality — barring Chinese laborers.",
     "debrief":"Immigration bought the labor that built industrial America — at the cost of the exclusion and prejudice new arrivals faced."},
 },
 2:{
  1:{"claim":"Washington and Du Bois offered two competing roadmaps for Black progress — patient economic self-help versus an immediate demand for full civil rights.",
     "ev1":"In the 1895 Atlanta Compromise, Booker T. Washington urged Black Southerners to build vocational skills and accept segregation for the time being.",
     "ev2":"W.E.B. Du Bois rejected accommodation, demanding immediate civil rights and higher education for a 'Talented Tenth.'",
     "debrief":"Washington's road bought white tolerance and jobs now — at the cost of the rights Du Bois insisted could not wait."},
  2:{"claim":"Farmers and industrial workers both organized to fight the railroads and trusts that controlled their livelihoods — and both met fierce resistance.",
     "ev1":"Farmers built the Grange, the Farmers' Alliance, and the Populist Party to demand railroad regulation and free silver.",
     "ev2":"Workers who struck Carnegie's Homestead mill in 1892 were met by armed Pinkerton guards, and the strike ended in blood.",
     "debrief":"Organizing bought a collective voice against concentrated power — at the risk, at Homestead, of violence and defeat."},
  3:{"claim":"Progressive presidents Roosevelt and Wilson both turned federal power against the trusts, though by different means.",
     "ev1":"TR's Square Deal promised to referee fairly between capital and labor through trust-busting, regulation, and conservation.",
     "ev2":"Wilson's New Freedom added the Clayton Antitrust Act, the FTC, and the Federal Reserve to regulate business and banking.",
     "debrief":"Federal regulation bought a fairer marketplace — at the cost, critics said, of a much larger, more powerful government."},
  4:{"claim":"The deadly conditions of industrial workplaces, dramatized by the Triangle fire, finally forced the nation to pass real workplace-safety laws.",
     "ev1":"On March 25, 1911, 146 garment workers — mostly young immigrant women — died at the Triangle Shirtwaist Factory behind doors locked to stop breaks and theft.",
     "ev2":"The disaster drove landmark fire-safety, child-labor, and factory-inspection reforms.",
     "debrief":"Cheap, fast production bought company profits — at the cost of 146 lives that finally moved the law."},
  5:{"claim":"Muckraking journalists exposed abuses so vividly that they forced Congress to act where years of quiet complaint had not.",
     "ev1":"Upton Sinclair's 'The Jungle' (1906) revealed filthy, dangerous conditions in the meatpacking industry.",
     "ev2":"The public outcry pushed Congress to pass the Pure Food and Drug Act and the Meat Inspection Act that same year.",
     "debrief":"Sinclair aimed for workers' hearts and hit the country's stomach — buying food-safety law at a target he hadn't aimed for."},
  6:{"claim":"Progressive reforms moved political power closer to ordinary voters and away from party bosses and wealthy interests.",
     "ev1":"The initiative, referendum, recall, and direct primary let voters make and unmake laws and candidates directly.",
     "ev2":"The 16th Amendment created a federal income tax and the 17th gave voters the direct election of senators.",
     "debrief":"These reforms bought citizens a more direct voice — at the cost of the insider control the machines had held."},
  7:{"claim":"Seventy years of organizing won women the vote in the 19th Amendment — and it came down to a single deciding state.",
     "ev1":"Suffragists like Carrie Chapman Catt and Alice Paul pressured politicians nationally, warning that stalling would carry a political price.",
     "ev2":"Tennessee cast the deciding 36th ratifying vote in August 1920 after Harry Burn changed his vote at his mother's urging.",
     "debrief":"The amendment bought half the nation the ballot — after decades of work that came down to one young legislator's vote."},
 },
 3:{
  1:{"claim":"The United States became an empire in 1898 driven by the hunt for markets, naval power, and a self-declared 'civilizing mission' — but not without opposition.",
     "ev1":"Strategists like Alfred Thayer Mahan argued the U.S. needed overseas bases and markets, and the 1898 cartoon shows Uncle Sam reading a menu of colonies.",
     "ev2":"The Anti-Imperialist League challenged empire head-on as a betrayal of the nation's founding rejection of colonial rule.",
     "debrief":"Empire bought the U.S. new markets and global reach — at the cost of the anti-colonial principle it was founded on."},
  2:{"claim":"The Spanish-American War turned the United States into an overseas empire and set the pattern for how it would project power.",
     "ev1":"Victory in 1898 handed the U.S. Puerto Rico, Guam, and the Philippines, and TR's Rough Riders became the war's iconic image.",
     "ev2":"The empire that followed was managed through TR's Big Stick, Taft's Dollar, and Wilson's Moral diplomacy.",
     "debrief":"The 'splendid little war' bought a global empire — at the cost, often out of frame, of the soldiers and colonized peoples who paid for it."},
  3:{"claim":"Long-building tensions made Europe a room full of gasoline, and the U.S. was finally pulled in by attacks on its ships and a secret German threat.",
     "ev1":"The MAIN causes — militarism, alliances, imperialism, and nationalism — set the conditions for a continental war.",
     "ev2":"Unrestricted submarine warfare and the intercepted Zimmermann Telegram, proposing a German–Mexican alliance, pushed the neutral U.S. to declare war.",
     "debrief":"Neutrality bought the U.S. years out of the war — until submarine attacks and the Zimmermann note made staying out impossible."},
  4:{"claim":"New industrial weapons made World War I catastrophically deadly, and the fresh American Expeditionary Force helped tip the balance in 1918.",
     "ev1":"Machine guns, poison gas, and tanks turned the trenches and No Man's Land into a killing ground.",
     "ev2":"The AEF — Pershing's command, heroes like Alvin C. York, and the Harlem Hellfighters — added decisive weight to the Allied side.",
     "debrief":"American entry bought the Allies victory in 1918 — at the cost of the industrialized slaughter every soldier in the ditch endured."},
  5:{"claim":"Winning the war at home meant mobilizing the whole society — and, at the same time, sharply narrowing civil liberties.",
     "ev1":"Women entered war work, citizens bought Liberty Bonds, and Creel's Committee on Public Information ran mass propaganda.",
     "ev2":"The Espionage and Sedition Acts criminalized dissent, and Schenck v. United States upheld limits on wartime speech.",
     "debrief":"Mobilization bought a unified war effort — at the cost of the free-speech rights the government suspended to get it."},
  6:{"claim":"Wilson designed a peace built on self-determination and a League of Nations — and then watched his own Senate refuse to join it.",
     "ev1":"The Fourteen Points (1918) called for open diplomacy, self-determination, and a general association of nations to keep the peace.",
     "ev2":"Led by Henry Cabot Lodge, the Senate rejected the Treaty of Versailles, and the United States never joined the League.",
     "debrief":"Wilson's vision bought the idea of collective security — at the cost of an America that, in the end, refused to lead it."},
 },
}

# Teacher-only styles, inlined so the shared style.css (which the passing units
# depend on) is never touched.
TEACHER_CSS = """<style>
.ted-band{background:#7a1020}
.tkey{border:1.4pt solid #1b3a6b;border-left:6pt solid #1b3a6b;background:#f4f7fb;
  border-radius:5px;padding:9px 12px;margin-top:7px;font-size:9.4pt;line-height:1.4}
.tkey .kl{color:#7a1020;font-weight:700;letter-spacing:.02em}
.tkey p{margin:3px 0}
.tkey .anchor{margin-top:6px;font-size:8.6pt;color:#41506a;border-top:1px dashed #b9c4d6;padding-top:5px}
.tnote{background:#fff8e6;border:1pt solid #d8b24a;border-radius:5px;padding:8px 11px;
  margin:8px 0;font-size:9pt}
.ted-tag{display:inline-block;background:#7a1020;color:#fff;font-weight:700;font-size:7.5pt;
  letter-spacing:.12em;padding:2px 7px;border-radius:3px;vertical-align:middle}
</style>"""

def build(unit, teacher=False):
    U = resolve(unit)
    ex = EXEMPLARS.get(unit, {})
    if teacher and not ex:
        raise SystemExit(f"No teacher exemplars authored for unit {unit}")
    codes = sorted({c for _, cs, _ in U["stops"] for c in cs})
    span = f'{codes[0]}–{codes[-1]}'
    ed_kick = "✈ Teacher Flight Log · Answer Key" if teacher else "✈ Student Flight Log"
    band_cls = "fl-band ted-band" if teacher else "fl-band"

    # ---- BRAND COVER (hero art + Flight Log band) ----
    cover = f'''<section class="fl-cover">
  <img src="{COVER}" alt="To Form a More Perfect Union">
  <div class="{band_cls}">
    <div class="fl-kick">{ed_kick}</div>
    <div class="fl-title">Unit {unit} · {esc(U["title"])}</div>
    <div class="fl-sub">To Form a More Perfect Union · {esc(U["years"])} · {span}</div>
    {'<div class="fl-name" style="font-size:9pt">Teacher edition — exemplars &amp; self-grade anchors. Not for student distribution.</div>' if teacher else '<div class="fl-name">NAME <span class="fl-line"></span> &nbsp; PERIOD <span class="fl-line short"></span></div>'}
  </div>
</section>'''

    # ---- SMART GOALS + HOW THE LOG WORKS ----
    if teacher:
        goals = f'''<section class="page">
<div class="sec"><div class="eyebrow">Teacher edition · how to use</div><h2>Exemplars &amp; Self-Grade Anchors</h2><div class="u"></div></div>
<p class="lead">This is the teacher companion to the Unit {unit} Student Flight Log. Every entry below carries a grounded <b>exemplar CER</b> — a model claim, two evidence points, and {DEBRIEFER}’s one-sentence debrief — plus the self-grade anchor to look for.</p>
<div class="tnote"><b>Use it as an anchor, not a script.</b> The exemplar shows one strong path to a <b>4</b> — a claim that <i>names the tension</i>, not just picks a side. Students can reach 4 by other well-evidenced routes. Read the model aloud only <i>after</i> students commit their own call, so you protect the prediction/retrieval effect.</div>
<div class="tnote"><b>Disclosure.</b> Item content is <b>classroom-formative · pre-field-test</b>. Exemplars are teacher-side only (never printed in the student edition) and are builder synthesis grounded in each stop’s locked High-Value Target — verify against your standards guide before adoption print.</div>
<div class="fr-tie" style="margin-top:12px"><b>Cross-check.</b> Each entry ties to one <b>Stop</b> in the textbook; students write from {DEBRIEFER}’s debrief on the matching Stop page. The numbers are generated from the same stop list as the reader, so Entry N always equals Stop N.</div></section>'''
    else:
        goals = f'''<section class="page">
<div class="sec"><div class="eyebrow">Before the flight</div><h2>My SMART Goals</h2><div class="u"></div></div>
<p class="lead">This log is your co-pilot’s seat in the textbook. Every stop, the crew hands you a source and asks for your call — you capture it <b>here</b>, then type it into <b>History Hack online · Writing Lab</b> for instant feedback.</p>
<div class="tint" style="margin:6px 0 12px"><b>How the cross-check works.</b> Each entry below is tied to one <b>Stop</b> in the textbook. When {DEBRIEFER} says <i>“capture this in your Flight Log,”</i> come here to the matching entry number — and the entry tells you exactly where in the narrative to write from.</div>
<div class="wlabel">Short-term goal (this unit)</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:8px">Mid-term goal (this quarter)</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:8px">Long-term goal (Ready Graduate — ACT ≥ 21 or an EPSO/credential)</div><div class="write"><div class="ln"></div></div>
<div class="fr-tie" style="margin-top:12px"><b>Reflect &amp; commit.</b> How does today’s work ladder toward the long-term goal? Name one habit you’ll hold all unit.</div>
<div class="write"><div class="ln"></div><div class="ln"></div></div></section>'''

    # ---- LOG ENTRIES (cross-referenced) ----
    def entry_student(n, cs, title):
        codestr = ", ".join(cs)
        return f'''<div class="fl-entry">
  <div class="fl-eh"><span class="fl-num">{n}</span><span class="fl-et">{esc(title)}</span><span class="fl-ec">{codestr}</span></div>
  <div class="fl-xref">↳ <b>In the textbook:</b> write from {DEBRIEFER}’s debrief on the <b>Stop {n}</b> page (Unit {unit}, {codestr}) — the “Make Your Call” prompt.</div>
  <div class="fl-cap"><b>My claim (one sentence):</b><div class="write"><div class="ln"></div></div>
  <b>My evidence (from the source):</b><div class="write"><div class="ln"></div><div class="ln"></div></div>
  <div class="fl-grade">Self-grade before you fly: <b>4</b> claim + evidence, names the tension &nbsp; <b>3</b> both, tension implied &nbsp; <b>2</b> one side &nbsp; <b>1</b> opinion only &nbsp; → <span class="fl-box"></span></div></div>
</div>'''
    def entry_teacher(n, cs, title):
        codestr = ", ".join(cs)
        e = ex.get(n, {})
        return f'''<div class="fl-entry">
  <div class="fl-eh"><span class="fl-num">{n}</span><span class="fl-et">{esc(title)}</span><span class="fl-ec">{codestr}</span> <span class="ted-tag">KEY</span></div>
  <div class="fl-xref">↳ <b>In the textbook:</b> students write from {DEBRIEFER}’s debrief on the <b>Stop {n}</b> page (Unit {unit}, {codestr}).</div>
  <div class="tkey">
    <p><span class="kl">Exemplar claim.</span> {esc(e.get("claim"))}</p>
    <p><span class="kl">Evidence 1.</span> {esc(e.get("ev1"))}</p>
    <p><span class="kl">Evidence 2.</span> {esc(e.get("ev2"))}</p>
    <p><span class="kl">{DEBRIEFER}’s debrief (model).</span> {esc(e.get("debrief"))}</p>
    <div class="anchor"><b>Self-grade anchor →</b> a <b>4</b> states the claim <i>and</i> names the tension between the two sides (cost vs. benefit); a <b>3</b> gives both evidence points but leaves the tension implied.</div>
  </div>
</div>'''
    entry = entry_teacher if teacher else entry_student
    per_page = 2 if teacher else 3
    ent = U["stops"]
    pages = []
    for i in range(0, len(ent), per_page):
        chunk = ent[i:i+per_page]
        body = "".join(entry(n, cs, t) for n, cs, t in chunk)
        eyebrow = "Answer Key · every stop" if teacher else "Flight Log · every stop"
        head = (f'<div class="sec"><div class="eyebrow">{eyebrow}</div><h2>{"Exemplars" if teacher else "Log your calls"} — Stops {chunk[0][0]}–{chunk[-1][0]}</h2><div class="u"></div></div>'
                if i == 0 else
                f'<div class="sec" style="margin-bottom:8px"><div class="eyebrow">{"Answer Key · continued" if teacher else "Flight Log · continued"}</div><h2 style="font-size:15pt">Stops {chunk[0][0]}–{chunk[-1][0]}</h2></div>')
        foot = ('' if teacher else
                '<div class="app"><span class="badge">Web · Writing Lab</span> &nbsp;Type each call into <b>History Hack online → Writing Lab</b> and check it against the rubric for <b>instant feedback</b>.</div>')
        pages.append(f'<section class="page">{head}{body}{foot}</section>')
    entries_html = "".join(pages)

    # ---- ARC CAPTURE (points back to the textbook Arc section) ----
    if teacher:
        arc = f'''<section class="page">
<div class="sec"><div class="eyebrow">End of the flight · teacher note</div><h2>The Arc of the Union — reading the data</h2><div class="u"></div></div>
<p class="lead">Students plot each milestone (−3 … +3) in the reader’s <b>Arc of the Union</b> section, then bring the mean and verdict to their log. There is no single “correct” arc — the goal is a defensible reading.</p>
<div class="tnote"><b>What to look for.</b> A strong response (1) reports a mean and an overall trend, (2) names the <i>steepest</i> climb or drop and the turning point, and (3) defends a <b>toward / away</b> verdict with the shape of the graph — not just a vibe. Expect honest mixed arcs: this era’s gains (reform, the vote, victory) sit beside real costs (dispossession, Jim Crow, lost liberties, empire).</div>
<div class="tnote"><b>Cross-curricular check (math/science).</b> Confirm each call is plotted as an ordered pair (milestone, score), the points are connected in order, the mean is computed correctly, and the extrapolation to the next unit is drawn as a dotted prediction.</div>
<div class="fr-tie" style="margin-top:12px"><b>Debrief prompt.</b> Push for the trade-off sentence: in one line, what did this unit <i>cost</i>, and what did it <i>buy</i>? That is the historian’s move and the Ready-Graduate habit.</div></section>'''
    else:
        arc = f'''<section class="page">
<div class="sec"><div class="eyebrow">End of the flight</div><h2>The Arc of the Union — my call</h2><div class="u"></div></div>
<p class="lead">Turn to <b>The Arc of the Union</b> at the end of Unit {unit} in the textbook. Plot each milestone there, then bring your overall verdict home to this page.</p>
<div class="wlabel">My mean score (−3 … +3):</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:8px">Overall trend (circle): &nbsp; Climbing &nbsp; Falling &nbsp; Mixed</div>
<div class="wlabel" style="margin-top:10px">Make the call — did the country move <b>toward</b> a more perfect union in these years, or away? Defend it with your graph.</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="fr-tie" style="margin-top:12px"><b>Debrief for {DEBRIEFER}.</b> In one sentence: what did this unit cost, and what did it buy?</div>
<div class="write"><div class="ln"></div><div class="ln"></div></div></section>'''

    # Copyright + writing-attribution line (on-page) — appended to the intro page.
    import bookmeta
    colo = (f'<p class="small" style="margin-top:12px;color:#6b7280">{esc(bookmeta.SERIES)} · '
            f'Written by {esc(bookmeta.AUTHOR_LEGAL)} (“{esc(bookmeta.AUTHOR_VOICE)}”). '
            f'{esc(bookmeta.COPYRIGHT)}</p>')
    goals = goals.replace("</section>", colo + "</section>", 1)

    head_css = f'<link rel="stylesheet" href="style.css">' + (TEACHER_CSS if teacher else "")
    html = f'''<!doctype html><html><head><meta charset="utf-8">{head_css}</head><body>
{cover}{goals}{entries_html}{arc}</body></html>'''
    suffix = "_FlightLog_TeacherEdition" if teacher else "_FlightLog"
    out = BASE/"out"/f"ToFormAMorePerfectUnion_Unit{unit}{suffix}.pdf"
    HTML(string=html, base_url=str(BASE)).write_pdf(str(out))
    print("WROTE", out)
    ed = "Teacher Flight Log (Answer Key)" if teacher else "Student Flight Log"
    bookmeta.stamp_metadata(out, f"To Form a More Perfect Union — Unit {unit} {ed}: {U['title']}",
                            subject="Student write-in Flight Log companion")

if __name__ == "__main__":
    unit = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    teacher = len(sys.argv) > 2 and sys.argv[2].lower().startswith("t")
    build(unit, teacher)
