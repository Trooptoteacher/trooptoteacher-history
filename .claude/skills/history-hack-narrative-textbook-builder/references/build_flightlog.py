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

import base64 as _b64
def _svg_fig(svg, alt):
    """Render an inline SVG as an <img> with a real alt so WeasyPrint tags it a Figure
    with /Alt (PDF/UA). Visually identical for a static print graphic; the alt gives AT a
    full description while the numbered legend/scale remain as adjacent live text."""
    b = _b64.b64encode(svg.encode("utf-8")).decode("ascii")
    return (f'<img src="data:image/svg+xml;base64,{b}" alt="{_html.escape(alt, quote=True)}" '
            f'style="width:100%;display:block">')

# Faint blank U.S. outline behind a plot/mark sketch box, so students plot on an actual map
# (not a blank rectangle). Base64 <img> with alt so WeasyPrint tags it /Figure + /Alt (PDF/UA).
_US_OUTLINE_PATH = ("M43,40 L325,40 L400,50 L430,88 L470,70 L520,92 L581,66 "
                    "L552,142 L524,168 L510,219 L458,277 L467,347 L448,334 L429,283 "
                    "L382,290 L325,296 L306,334 L268,296 L216,260 L137,251 L116,251 "
                    "L83,232 L64,184 L46,155 L49,78 Z")
def _us_sketch_bg():
    svg = ('<svg viewBox="0 0 640 380" xmlns="http://www.w3.org/2000/svg">'
           f'<path d="{_US_OUTLINE_PATH}" fill="#f4f7fb" stroke="#9aa6b6" stroke-width="2" '
           'stroke-linejoin="round"/></svg>')
    b = _b64.b64encode(svg.encode("utf-8")).decode("ascii")
    return (f'<img src="data:image/svg+xml;base64,{b}" '
            'alt="Blank outline map of the contiguous United States, for marking your answer." '
            'style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);height:1.18in;'
            'opacity:0.85">')

# Unit 1 is rendered by render_proof.py (its own stop metadata); keep a local
# index here so the Flight Log matches the reader exactly. Units in BU.UNITS are
# derived from that source of truth instead (see resolve()).
STOPS_U1 = {"title":"The Nation Turns West — and the Cities Rise","years":"1877–1900",
    "stops":[(1,["US.01"],"Free Land — and Whose Land?"),(2,["US.02"],"Made to Vanish"),
             (3,["US.03"],"The Refs Walk Off"),(4,["US.04"],"The Group Chat You’re Not In"),
             (5,["US.05"],"Gospel — and Its Price"),(6,["US.06"],"The City That Can’t House Its Workers"),
             (7,["US.07"],"‘Expat’ or ‘Immigrant’?")]}

# ── TDOE conceptual-category dimensions (canonical per-standard map) ──
# Same source of truth the reader uses, so Geography (and the rest) are visible on the
# Flight Log too, not only in the item bank / crosswalk. Geography set bold (non-color).
_DIM_BY_CODE = {}
try:
    _dimdoc = _json.load(open(ROOT/"public"/"data"/"us-history"/"standard-dimensions"/"unit-1.json"))
    _DIM_BY_CODE = {s["code"]: s for s in _dimdoc.get("standards", [])}
except Exception:
    _DIM_BY_CODE = {}

def _dim_chips_fl(codes):
    """Union of dimensions across a stop's standard codes, rendered as small chips."""
    seen, order = set(), []
    for c in codes:
        for d in (_DIM_BY_CODE.get(c) or {}).get("dimensions", []):
            if d not in seen:
                seen.add(d); order.append(d)
    if not order: return ""
    chips = " ".join((f'<span class="dchip geo">{esc(d)}</span>' if d == "Geography"
                      else f'<span class="dchip">{esc(d)}</span>') for d in order)
    return f'<p class="dims"><span class="dims-lab">TDOE dimensions</span> {chips}</p>'

# ── GEOGRAPHY WAYPOINTS (consumable home for the reader's Geography-section map tasks) ──
# The maps live in the textbook's Geography section; students do the marking + writing here.
# One waypoint per geography-coded standard (US.01/US.02/US.06/US.07). Unit-1 only.
GEO_TASKS = {
 1: {"t":"US.01 · Settlement of the West",
     "task":"Mark the transcontinental route and one Homestead region it opened. Then answer: how did the railroad shape <i>where</i> the West filled in?",
     "ex":"The rails set the routes of settlement — towns, farms, and Homestead claims followed the track west, so the railroad (not just free land) decided which land people could reach and work. It also carried settlement onto treaty land promised to Plains nations.",
     "look":["Dense rail grid east of the Mississippi; only a few long trunk lines cross the West.",
             "Towns and Homestead claims hug the tracks — settlement follows the route.",
             "Every western line crosses land promised by treaty to Plains nations."],
     "tn":"TN tie — the Exodusters Pap Singleton led west, and Tennessee-born Buffalo Soldiers on the frontier, traveled this same network.",
     "mis":"Misconception to catch — “free land” settled the West. The rail line, not the offer of land, decided which land was reachable and worth claiming."},
 2: {"t":"US.02 · Federal policy & land cessions",
     "task":"Sketch the sequence of land cessions — one early eastern cession and one late western one. Then answer: what does the <i>order</i> of cessions reveal about federal policy toward American Indians?",
     "ex":"Cessions move east-to-west and early-to-late: a homeland taken piece by piece by treaty and act, then broken further by the Dawes Act (1887). The order shows a consistent federal policy of removal, confinement to reservations, and finally allotment.",
     "look":["Eastern cessions are small and early; western cessions are large and late.",
             "Each numbered zone ties to a specific treaty or act of Congress.",
             "After the Dawes Act (1887), reservation land itself is fractured into allotments."],
     "tn":"TN tie — Red Clay was the last seat of the Cherokee national government before the 1838 Removal — the same logic these cessions carry.",
     "mis":"Misconception to catch — cessions were voluntary land sales. They were compelled by treaty, war, and federal statute."},
 3: {"t":"US.03 · Exoduster migration (1879)",
     "task":"On the blank U.S. map, draw arrows from Mississippi, Louisiana, Texas, and Tennessee to Kansas. Then answer: what pushed the Exodusters out of the South, and what pulled them to Kansas?",
     "ex":"After the Compromise of 1877 ended federal protection, Jim Crow, disenfranchisement, and violence pushed Black Southerners out; Kansas — free-state land with Homestead opportunity — pulled them in. In 1879 roughly six thousand Exodusters, many recruited by Tennessee's Pap Singleton, moved up the Mississippi and west to Kansas.",
     "look":["The flow runs north from the Deep South to Kansas in 1879.",
             "Migrants followed the Mississippi to St. Louis, then pushed west.",
             "Push = Jim Crow and violence; pull = free-state land and Homestead opportunity."],
     "tn":"TN tie — Nashville's Benjamin 'Pap' Singleton organized and led Exoduster colonies to Kansas.",
     "mis":"Misconception to catch — the Exodus was one forced event. It was a sustained response to the withdrawal of federal protection and the rise of Jim Crow."},
 4: {"t":"US.04 · Gilded Age economics & the Populist revolt",
     "task":"On the blank U.S. map, shade the Plains/Mountain-West farm belt where Populism ran strongest and mark the cotton South's Alliance country. Then answer: why did the revolt rise in the farm country and not the industrial Northeast?",
     "ex":"Squeezed by railroad rates, debt, and falling crop prices, farmers organized as the Grange, the Farmers' Alliance, and the People's Party. In 1892 the Populists carried Kansas, Colorado, Idaho, and Nevada — the wheat-and-silver West — with strong Alliance support in the cotton South. The industrial Northeast, holding the banks and factories, stayed with the major parties: the revolt was geographic.",
     "look":["Populist strength clustered in the Plains and Mountain-West wheat belt.",
             "The cotton South grew a strong Farmers' Alliance too.",
             "The industrial Northeast stayed with the major parties — geography of grievance."],
     "tn":"TN tie — the Farmers' Alliance ran strong through Tennessee's cotton and tobacco country; the agrarian revolt was a home-state story.",
     "mis":"Misconception to catch — Populism was a fringe movement everywhere. In the farm belt it was a majority movement that carried whole states in 1892."},
 6: {"t":"US.06 · Locate the industrial centers",
     "task":"Mark the five centers — Boston, New York City, Pittsburgh, Chicago, San Francisco. Then answer: why did industry cluster where it did?",
     "ex":"Four centers sit in the Northeast/Great Lakes belt where coal, water, rail, and labor met; San Francisco anchors the Pacific. Industry clustered at those junctions, and people moved from farms and abroad to them — the rural-to-urban shift.",
     "look":["Four of the five centers sit in the Northeast/Great Lakes manufacturing belt.",
             "San Francisco anchors the West — the Pacific port and rail terminus.",
             "Industry gathered where coal, water, rail, and labor met."],
     "tn":"TN tie — Memphis (river and cotton) and Nashville (rail) grew on the same industrial logic at a regional scale.",
     "mis":"Misconception to catch — the big cities grew at random. Each sits at a coal/water/rail/labor junction — geography chose them."},
 7: {"t":"US.07 · Immigrant settlement",
     "task":"List the three states with the most foreign-born residents (top of the ranked chart). Then answer: why did immigrants settle where they did instead of spreading evenly?",
     "ex":"The chart ranks states by foreign-born population: New York, Pennsylvania, and Illinois lead — the industrial Northeast and Great Lakes — while Southern states trail. Immigrants followed the ports (Ellis Island) and the factory jobs, so the ranking mirrors the industrial map, not an even spread.",
     "look":["New York, Pennsylvania, and Illinois top the ranking (industrial NE/Great Lakes).",
             "Southern and interior-Western states rank near the bottom.",
             "The ranking, not an even spread, shows immigrants followed ports and jobs."],
     "tn":"TN tie — smaller than the northern industrial states, Tennessee’s cities still drew new arrivals to rail, mills, and river trade.",
     "mis":"Misconception to catch — immigrants spread evenly across the country. The ranking shows they concentrated where the ports and the factory jobs were."},
}
GEO_LINK = {
 1: "The geography <i>is</i> the standard — the rail map shows how the Homestead West became reachable and settled.",
 2: "The map is federal policy made visible: removal and the reservation system, cession by cession.",
 3: "Migration as the consequence of the Compromise of 1877 — the route out of the South is the standard.",
 4: "The Populist belt maps the farmer-vs-industrialist economic divide at the heart of US.04.",
 6: "The standard’s verb is ‘locate’ — the map is the assessment.",
 7: "<i>Where</i> immigrants settled, not simply that they came, is the geographic core of US.07.",
}
def _geo_waypoints(teacher):
    order = [1, 2, 3, 4, 6, 7]
    intro_s = ('<div class="sec"><div class="eyebrow">Flight Log · Geography Waypoints</div>'
               '<h2>Read the land — then make the meaning</h2><div class="u"></div></div>'
               '<p class="lead">The maps live in your textbook’s <b>Geography of Unit 1</b> section. '
               'Here is where you <b>mark them and write</b>. Geography is evidence: where things happened '
               'explains why. Do each map task, then defend the pattern you see.</p>')
    # Teacher section opens with a full overview page (header + geographic-reasoning method +
    # a quick-reference table), then the six waypoints flow two per page. No separate close.
    _qr_rows = [
        ("US.01", "Rail network & western settlement", "read the 1890 railroad map"),
        ("US.02", "Land cessions & the reservation system", "read the Royce cession map"),
        ("US.03", "Exoduster migration (1879)", "plot the South→Kansas routes"),
        ("US.04", "Populist farm belt vs. the industrial core", "shade the agrarian-revolt regions"),
        ("US.06", "Locate the industrial centers", "mark the five cities"),
        ("US.07", "Immigrant distribution by state", "read the ranked foreign-born chart"),
    ]
    _qr = "".join(f'<tr><th scope="row">{c}</th><td>{f}</td><td>{d}</td></tr>' for c, f, d in _qr_rows)
    intro_t = (
        '<div class="sec"><div class="eyebrow">Answer Key · Geography Waypoints</div>'
        '<h2>Geography as evidence — teacher overview</h2><div class="u"></div></div>'
        '<p class="lead">Students mark the maps, charts, and routes in the reader’s <b>Geography of Unit 1</b> '
        'section and write here. Six of the seven Unit-1 standards are geography-coded (all but US.05); each '
        'waypoint below carries one <b>defensible</b> exemplar read — model the reasoning, then have students '
        'argue the pattern from the source.</p>'
        '<div class="apx" style="border-left-color:#1F3A5F">'
        '<p><span class="lab" style="color:#1F3A5F">Geographic reasoning (SSP)</span> — read a map, chart, or route '
        'as a primary source: <b>gather</b> (title, legend, units, date) → <b>interpret</b> (the pattern) → '
        '<b>corroborate</b> (lay it beside another source) → <b>connect</b> (to the standard and the unit question). '
        'It ties to ELA evidence-based writing and to math/data reading on distribution and scale.</p>'
        '<p style="margin-top:3px"><span class="lab" style="color:#1F3A5F">Assessment</span> — score each like any '
        'CER in the unit: a claim about the pattern, evidence read from the source, and the connection to the '
        'standard. A strong answer corroborates two sources; a weak one describes one source without a claim.</p></div>'
        '<table class="rubric" style="margin-top:8px"><thead><tr><th scope="col">Standard</th>'
        '<th scope="col">Geography focus</th><th scope="col">What students do in the Flight Log</th></tr></thead>'
        f'<tbody>{_qr}</tbody></table>'
        '<div class="apx" style="border-left-color:#1F3A5F;margin-top:8px">'
        '<p><span class="lab" style="color:#1F3A5F">Tennessee thread</span> — every waypoint has a home-state tie '
        '(Singleton’s Exodusters, the Cherokee and Chickasaw cessions, the growth of Memphis and Nashville, '
        'Tennessee’s own arrivals). Ask students to find Tennessee on each source.</p>'
        '<p style="margin-top:3px"><span class="lab" style="color:#1F3A5F">Differentiate</span> — <b>Below:</b> give '
        'the top states or the route to trace. <b>On:</b> full reasoning from the source. <b>Above:</b> corroborate '
        'one geography source against another (railroad ↔ immigrant ranking ↔ Populist belt) and explain the overlap.</p>'
        '<p style="margin-top:3px"><span class="lab" style="color:#1F3A5F">Run it in class</span> — put the source '
        'up, have students mark it in the reader’s Geography section and defend the pattern <i>before</i> you reveal '
        'the exemplar; the argument about <i>why</i> is the lesson. <span class="lab" style="color:#1F3A5F">Pacing</span> — '
        '~10 min per waypoint; the full set is one ~50-minute lesson or a recurring warm-up, always inside the '
        'workbook flow. <i>Exemplars are one defensible read each — credit any claim a student defends from the source.</i></p></div>'
        '<div class="apx" style="border-left-color:#1F3A5F;margin-top:8px">'
        '<p><span class="lab" style="color:#1F3A5F">Prep &amp; materials</span> — no prep beyond the reader and the '
        'Flight Log. The plot waypoints (US.01/02/03/04/06) print a faint blank U.S. outline in the student Flight '
        'Log for students to mark directly; US.07 lists states from the ranked chart. Colored pencils help but are '
        'optional — every task reads correctly in black and white.</p>'
        '<p style="margin-top:3px"><span class="lab" style="color:#1F3A5F">Prior knowledge</span> — students should '
        'have worked the matching Stop in the reader first; each waypoint recalls a source they have already met, so '
        'the geography lesson reinforces the standard rather than introducing it cold.</p></div>')
    close_t = ""
    close_s = ('<div class="geo-wp"><h3 class="geo-h">Geography wrap-up</h3>'
               '<p class="small">Look back across the five maps, charts, and routes you just worked. '
               '<b>Which one changed how you see the unit’s question</b> — is the Union bending toward its '
               'founding promise, or away? Name the source, name the pattern, then make your call.</p>'
               '<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div>'
               '<div class="ln"></div></div></div>')
    def wp_student(n):
        g = GEO_TASKS[n]
        # Map-marking waypoints get a faint blank U.S. outline to plot on; US.07 lists states (no plot).
        if n == 7:
            sketch = '<div class="geo-sketch"><span class="geo-sketch-lab">Note the states here</span></div>'
        else:
            sketch = (f'<div class="geo-sketch">{_us_sketch_bg()}'
                      '<span class="geo-sketch-lab">Mark the map here</span></div>')
        return (f'<div class="geo-wp"><h3 class="geo-h">{esc(g["t"])}</h3>{_dim_chips_fl([f"US.0{n}"])}'
                f'<p class="small"><b>✈ Map task.</b> {g["task"]}</p>'
                f'{sketch}'
                f'<div class="write"><div class="ln"></div><div class="ln"></div></div></div>')
    def wp_teacher(n):
        g = GEO_TASKS[n]
        looks = "".join(f"<li>{esc(x)}</li>" for x in g["look"])
        on = "chart" if n == 7 else "map"
        return (f'<div class="geo-wp geo-wp-t"><h3 class="geo-h">{esc(g["t"])}</h3>{_dim_chips_fl([f"US.0{n}"])}'
                f'<p class="small"><b>Map task.</b> {g["task"]}</p>'
                f'<p class="small"><b>Exemplar read.</b> {esc(g["ex"])}</p>'
                f'<div class="geo-notice"><b>Look for on the {on}</b><ul>{looks}</ul></div>'
                f'<p class="small"><b>Standard link.</b> {GEO_LINK.get(n,"")} <span class="geo-tn">{esc(g["tn"])}</span></p>'
                f'<p class="small"><b>Facilitate.</b> Geography is evidence — have students defend the pattern '
                f'from the {on} (<b>Below:</b> give the route/regions; <b>On:</b> full reasoning from the source; '
                f'<b>Above:</b> corroborate it against a second geography source and explain the overlap).</p></div>')
    wp = wp_teacher if teacher else wp_student
    intro = intro_t if teacher else intro_s
    close = close_t if teacher else close_s
    # Flow the waypoints in one section; each .geo-wp is break-inside:avoid, so WeasyPrint packs
    # them ~2 per page and never splits one — filling each page naturally (no fragile hard pairing).
    body = intro + "".join(wp(n) for n in order) + close
    return f'<section class="page">{body}</section>'

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

# Student Flight-Log styles, inlined so the shared style.css is never touched. The
# student log is the ENGAGEMENT surface: the crew re-engages the student here (they
# met the crew in the textbook, were sent here) and the page CAPTURES DATA. Every card
# is a full page, UDL-embedded (sentence frame + choice of expression + graphic
# organizer + word wall), with ≤10% white space — write-in room framed by structure,
# never a blank bottom.
STUDENT_CSS = """<style>
.crewcall{border:1.4pt solid #1F3A5F;border-left:6pt solid #1F3A5F;background:#eef2f8;border-radius:0 7px 7px 0;
  padding:8px 12px;margin:8px 0 10px;font-size:9.6pt;line-height:1.42}
.crewtag{display:inline-block;background:#1F3A5F;color:#fff;font-weight:700;font-size:9pt;letter-spacing:.1em;
  text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-right:6px}
.codepin{display:inline-block;border:1.3px solid #1F3A5F;color:#1F3A5F;font-weight:700;font-size:9pt;
  border-radius:5px;padding:1px 7px;float:right}
.cap{border:1px solid #c9cfd8;border-radius:8px;padding:8px 11px 9px;margin:9px 0}
.caphd{font:700 9pt "DejaVu Sans";color:#1F3A5F;margin-bottom:5px}
.capn{display:inline-block;width:17px;height:17px;line-height:17px;text-align:center;background:#1F3A5F;color:#fff;
  border-radius:50%;font-size:9pt;margin-right:6px;vertical-align:1px}
.udl{float:right;font:700 9pt "DejaVu Sans";letter-spacing:.04em;color:#846009;background:#fbf4e2;
  border:1px solid #e4cf92;border-radius:10px;padding:1px 8px;text-transform:uppercase}
.frame2{background:#f5f2ec;border-left:3px solid #C9A227;border-radius:0 5px 5px 0;padding:5px 9px;margin:2px 0 6px;
  font-size:9pt;color:#41506a}
.twocol{display:flex;gap:10px}
.twocol .col{flex:1}
.colh{font:700 9pt "DejaVu Sans";text-transform:uppercase;letter-spacing:.03em;color:#B22234;margin-bottom:3px}
.colh.buy{color:#1b5e20}
.fillline{display:inline-block;min-width:1.7in;border-bottom:1px solid #9aa4b4;margin:0 4px}
.tensionrow{background:#eef2f8;font-size:10pt;line-height:2.1}
.caprow{display:flex;gap:10px;align-items:stretch;margin:9px 0}
.wordwall{flex:1.35;border:1px solid #c9cfd8;border-radius:8px;padding:8px 11px}
.chips{display:flex;gap:8px;margin-top:6px}
.chips span{flex:1;height:26px;border:1px dashed #9aa4b4;border-radius:5px}
.scorebox{flex:1;border:1px solid #1F3A5F;border-radius:8px;padding:8px 10px;background:#eef2f8}
.sbh{font:700 9pt "DejaVu Sans";color:#1F3A5F;text-transform:uppercase;letter-spacing:.05em}
.sbscale{font-size:9pt;color:#41506a;margin:3px 0 6px;line-height:1.35}
.sbbox{font:700 9pt "DejaVu Sans";color:#1F3A5F}
.arc-wrap{border:1px solid #c9cfd8;border-radius:8px;padding:8px 10px;margin:8px 0;background:#fff}
</style>"""

# Teacher-only styles, inlined so the shared style.css (which the passing units
# depend on) is never touched.
TEACHER_CSS = """<style>
.ted-band{background:#B22234}
.tkey{border:1.4pt solid #1F3A5F;border-left:6pt solid #1F3A5F;background:#f4f7fb;
  border-radius:5px;padding:7px 12px;margin-top:6px;font-size:9.4pt;line-height:1.33}
.tkey .kl{color:#B22234;font-weight:700;letter-spacing:.02em}
.tkey p{margin:2px 0}
.tkey .anchor{margin-top:5px;font-size:9pt;color:#41506a;border-top:1px dashed #b9c4d6;padding-top:4px}
.tnote{background:#fff8e6;border:1pt solid #d8b24a;border-radius:5px;padding:8px 11px;
  margin:8px 0;font-size:9pt}
.ted-tag{display:inline-block;background:#B22234;color:#fff;font-weight:700;font-size:9pt;
  letter-spacing:.12em;padding:2px 7px;border-radius:3px;vertical-align:middle}
.arc-wrap{border:1px solid #c9cfd8;border-radius:8px;padding:8px 10px;margin:8px 0;background:#fff}
.readbox{border-left:4px solid #1F3A5F;background:#f4f7fb;border-radius:5px;padding:9px 12px;margin:8px 0;font-size:9.6pt;line-height:1.45}
.readbox h3, .readbox h4{margin:0 0 4px;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:#B22234}
.disc{border:1pt dashed #B22234;background:#faf0ef;border-radius:5px;padding:7px 11px;margin:8px 0;font-size:9pt;line-height:1.4}
.disc b{color:#B22234}
.apx{border:1px solid #c9cfd8;border-left:4px solid #C9A227;border-radius:6px;padding:6px 11px;margin-top:6px;font-size:9pt;line-height:1.33}
.apx .at{font-weight:700;color:#1F3A5F;font-size:9.6pt;margin-bottom:3px}
.apx .lab{font-weight:700;color:#B22234;font-size:9pt;letter-spacing:.03em;text-transform:uppercase}
.apx p{margin:2px 0}
.frame{border:1pt dashed #1F3A5F;background:#f4f7fb;border-radius:6px;padding:6px 11px;margin-top:6px;font-size:9pt;line-height:1.33}
.frame .lab{font-weight:700;color:#1F3A5F;font-size:9pt;letter-spacing:.03em;text-transform:uppercase}
</style>"""

# ── Teacher Arc-of-the-Union exemplar ────────────────────────────────────────
# ONE defensible "historian's read": a −3…+3 score per milestone (same order as the
# narrative arcPoints). NOT an answer key — see the disclaimer. Scores are the
# builder's synthesis of a broadly-defensible reading; flag for tn-content-specialist.
ARC_SCORES = {
 1:[ 1,-3,-2,-3,-2, 1, 2,-3, 1, 1, 2],
 2:[-2,-1, 2,-1, 2, 2, 3],
 3:[-2,-3,-1, 0, 2,-1],
}
HISTORIAN_READ = {
 1:"Score the Gilded Age honestly and the line dips below the baseline. The retreat from Reconstruction (1877), the Chinese Exclusion Act (1882), and <i>Plessy</i> (1896) pull hard toward <b>away</b>; the railroad's opportunity, Ida B. Wells's witness, and the first real antitrust enforcement lift it back. The mean sits just below zero — a nation that grew its power and wealth faster than it grew its promise, with the reformers already gathering who will bend the next decades back toward it.",
 2:"The Progressive-Era line climbs. Labor's defeat at Homestead and the compromises on race weigh it down, but consumer protection, the direct election of senators, the check on the trusts, and — decisively — the Nineteenth Amendment carry the arc above the baseline. The mean is clearly positive: the era when organized ordinary people force the promise wider. Tennessee casting the deciding vote for suffrage is the whole era in miniature.",
 3:"Here the line falls again. A nation born rejecting empire takes one — the Philippine War is the low point — and enters a European war whose peace it then refuses to keep. The Fourteen Points are the one clear climb, a vision of self-determination the country articulates and then walks away from at Versailles. The mean sits below zero: power projected outward, the promise deferred at home and abandoned abroad.",
}
ARC_DISCLAIMER = ("<b>This is one defensible arc — not an answer key.</b> It is the kind of reading a historian could argue "
 "and support with evidence; it is not the reading. A student who scores a milestone differently is <b>not wrong</b> if they "
 "defend it with evidence — the standard is the argument, not the number. Use this to model reasoning and to press: "
 "“Where would <i>you</i> move a point, and why?”")

# ── Teacher supports (teacher-side) — {unit:{stop#:(misconception, reteach, extension)}} ──
APPENDIX = {
 1:{
  1:("The West was “empty” and the land was “free.”",
     "Put the 100th-meridian rainfall line on a map beside the 160-acre claim — show why the “gift” often failed on the dry plains — and name whose land the Act redistributed (Native nations, by treaty and force).",
     "Structured debate: “Homestead Act — opportunity or dispossession?” Require each side to concede one true point to the other before closing."),
  2:("Boarding schools were charity that “helped” Native children.",
     "HIPP the Carlisle before/after portrait as advertising: who made it, for whom, and what it hides. The policy's goal, in its founder's words, was to erase a culture.",
     "Pair the staged photo with a boarding-school survivor's testimony; students list what the photo leaves out."),
  3:("Reconstruction “failed” because freedpeople weren't ready for rights.",
     "Timeline it: 13th/14th/15th Amendments → Compromise of 1877 → <i>Plessy</i> (1896). Reconstruction was ended by a political deal and organized violence, not by any incapacity.",
     "Close-read Justice Harlan's lone dissent in <i>Plessy</i> against the majority — “our Constitution is color-blind.”"),
  4:("Political machines were purely, simply evil.",
     "Analyze “The Bosses of the Senate” (who is drawn giant, who tiny, where the “People's Entrance” is) — then add the other column: machines also delivered jobs, coal, and citizenship help to the poor.",
     "Cost–benefit chart of machine politics; students decide whether the services were worth the corruption."),
  5:("“Robber Baron” vs. “Captain of Industry” is an either/or choice.",
     "Same men, both true: T-chart Carnegie's “Gospel of Wealth” beside the Standard Oil octopus cartoon. Judgment depends on which evidence you weight.",
     "Diagram vertical vs. horizontal integration with a real company; connect to monopoly power today."),
  6:("Immigrants “chose” to live in slums.",
     "Wages and discrimination set the choices — analyze a Riis tenement photo and the push/pull factors that funneled newcomers into crowded blocks.",
     "Map an immigrant neighborhood by decade; connect density and housing law to a city today."),
  7:("“Expat” and “immigrant” are neutral, interchangeable words.",
     "Word-choice analysis: have students privately list who they'd call an “expat” and who an “immigrant,” then surface the class/race pattern in the room. Connect it to Gilded-Age nativism and the Chinese Exclusion Act.",
     "Scan today's headlines for the same word-choice split; students rewrite one to remove the bias."),
 },
 2:{
  1:("Washington and Du Bois were enemies with nothing in common.",
     "Both wanted Black advancement — they split on <i>means and timing</i>. T-chart Washington's vocational self-help/accommodation against Du Bois's demand for immediate civil rights and the “Talented Tenth.”",
     "Read short excerpts of the Atlanta Compromise beside Du Bois's critique in <i>The Souls of Black Folk</i>; students mark where they actually agree."),
  2:("Farmers and industrial workers were one and the same movement.",
     "Different grievances, overlapping enemies: farmers organized as the Grange/Alliance/Populists against railroads and the money supply; workers organized as unions against mills — both met force.",
     "Map Populist strongholds and stage a two-minute “free silver vs. gold” exchange."),
  3:("Trust-busting destroyed big business.",
     "It <i>regulated</i>, it didn't abolish — Sherman, then Clayton and the FTC set rules of the game. Contrast TR's Square Deal (referee) with Wilson's New Freedom (competition).",
     "Compare a Square Deal action to a New Freedom law; which better checks concentrated power?"),
  4:("The Triangle fire was a freak accident.",
     "It was predictable: doors locked from the outside, no sprinklers, no code — a business decision that turned a spark into 146 deaths and drove landmark safety law.",
     "Trace one modern workplace-safety rule (OSHA) back to a Progressive-Era reform."),
  5:("Muckrakers made things up for attention.",
     "Their power was <i>evidence</i>: Tarbell documented Standard Oil, Sinclair researched the stockyards, Riis photographed the tenements — and the exposés produced real laws (Pure Food & Drug, Meat Inspection).",
     "Find a modern investigative report that changed a law; students map exposé → outcome."),
  6:("Progressive reform was only about the economy.",
     "It reshaped <i>democracy</i> too — initiative, referendum, recall, the direct primary, and the 16th (income tax) and 17th (direct election of senators) Amendments.",
     "Does your state have the initiative or referendum? Investigate and report how it's used."),
  7:("The 19th Amendment gave <i>all</i> women the vote.",
     "In law, yes (1920) — in practice, Jim Crow, poll taxes, and other barriers still blocked many Black, Native, and immigrant women for decades.",
     "Research when different groups of women actually secured reliable voting access; build a timeline."),
 },
 3:{
  1:("The United States had always been an empire.",
     "1898 was the <i>turning point</i>: frame the real debate between expansionists (Mahan's sea power, markets, “civilizing mission”) and the Anti-Imperialist League.",
     "Give students one pro- and one anti-imperialism source and stage the 1898 debate."),
  2:("The Spanish-American War was purely about freeing Cuba.",
     "Yellow journalism, markets, naval strategy, and a “civilizing mission” all drove it — and TR's Big Stick, Taft's Dollar, and Wilson's Moral diplomacy followed.",
     "Analyze a yellow-journalism front page on the <i>Maine</i>; separate verified fact from provocation."),
  3:("The U.S. entered WWI only because of the <i>Lusitania</i>.",
     "The <i>Lusitania</i> sank in 1915; the U.S. declared war in 1917 after <b>unrestricted submarine warfare resumed</b> and the <b>Zimmermann Telegram</b> — on top of the MAIN long-causes.",
     "Sequence the road to war, 1914–1917, and mark the true tipping point."),
  4:("New weapons made the war quick.",
     "Machine guns, gas, and trenches produced <i>stalemate</i> and mass casualties; it was the fresh AEF in 1918 that finally tipped the balance.",
     "Research one WWI technology and its human cost; present the trade-off in one slide."),
  5:("Free speech is absolute, even in wartime.",
     "The Espionage and Sedition Acts criminalized dissent, and <i>Schenck</i>'s “clear and present danger” upheld wartime limits — a line courts have argued ever since.",
     "Compare <i>Schenck</i> (1919) with a later free-speech case (e.g., <i>Brandenburg</i>, 1969); how did the line move?"),
  6:("The United States joined the League of Nations.",
     "Wilson <i>designed</i> it — but the Senate, led by Lodge, rejected the Treaty of Versailles, and the U.S. <b>never joined</b>.",
     "Debate: should the U.S. have joined the League? Weigh isolationism against internationalism."),
 },
}
# A reusable EL / MTSS sentence frame for the CER (teacher-side scaffold).
EL_FRAME = ('<div class="frame"><span class="lab">EL · MTSS sentence frame</span> — say it, then write it: '
            '“______ moved the nation <b>toward / away from</b> the promise, because ______. '
            'It <b>cost</b> ______ and it <b>bought</b> ______.”</div>')

def _arc_svg(arc, scores, plot=True):
    """Milestones on X, −3…+3 on Y. plot=True draws the exemplar line + points + mean
    (teacher key). plot=False draws a BLANK, labelled coordinate grid for students to
    plot their own Arc on — the actual interactive graph, not a picture of one."""
    nt = len(arc)
    # Teacher exemplar plot gets a tall graph (fills its own page); the student plotting
    # grid is shorter so the grid + capture fields fit on ONE page.
    GH = (250 if nt < 9 else 232) if not plot else (380 if nt < 7 else (360 if nt < 9 else 340))
    def X(i): return 74 + (i-0.5)/nt*(662-74-12)
    def Y(v): return 20 + (3-v)/6*(GH-20-44)
    s = [f'<svg viewBox="-28 0 690 {GH}" width="100%" role="img" aria-label="The Arc of the Union — a coordinate grid: eleven Unit-1 milestones (with years) along the bottom, a scale from −3 (away from the promise) to +3 (toward it) up the side, with the 0 line and gold on-track band. Plot each milestone, then connect the points to draw the arc." xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans"><title>The Arc of the Union — plot each milestone from −3 (away from the promise) to +3 (toward it)</title>']
    yl = {3:"+3 Toward",2:"+2",1:"+1",0:"0",-1:"−1",-2:"−2",-3:"−3 Away"}
    for v in range(-3,4):
        y=Y(v); b=v==0
        s.append(f'<line x1="74" y1="{y:.1f}" x2="650" y2="{y:.1f}" stroke="{"#1F3A5F" if b else "#dfe4ec"}" stroke-width="{1.4 if b else .7}"/>')
        s.append(f'<text x="68" y="{y+3:.1f}" text-anchor="end" font-size="16.2" fill="#41506a">{yl[v]}</text>')
    for i,(yr,lab) in enumerate(arc,1):
        x=X(i); s.append(f'<line x1="{x:.1f}" y1="20" x2="{x:.1f}" y2="{GH-44:.0f}" stroke="{"#eef1f6" if plot else "#e4e9f1"}" stroke-width=".8"/>')
        s.append(f'<text x="{x:.1f}" y="{GH-30:.0f}" text-anchor="middle" font-size="15.4" font-weight="bold" fill="#1F3A5F">{i}</text>')
        s.append(f'<text x="{x:.1f}" y="{GH-17:.0f}" text-anchor="middle" font-size="13.8" fill="#5f6b7d">{yr}</text>')
        # On the student grid, drop a faint plotting dot at the baseline so students
        # can see exactly which column each milestone sits in.
        if not plot:
            s.append(f'<circle cx="{X(i):.1f}" cy="{Y(0):.1f}" r="2" fill="#c9cfd8"/>')
    if plot:
        pts = " ".join(f'{X(i):.1f},{Y(sc):.1f}' for i,sc in enumerate(scores,1))
        s.append(f'<polyline points="{pts}" fill="none" stroke="#B22234" stroke-width="2"/>')
        for i,sc in enumerate(scores,1):
            s.append(f'<circle cx="{X(i):.1f}" cy="{Y(sc):.1f}" r="3.4" fill="#B22234"/>')
        mean = sum(scores)/len(scores); ym=Y(mean)
        s.append(f'<line x1="74" y1="{ym:.1f}" x2="650" y2="{ym:.1f}" stroke="#C9A227" stroke-width="1" stroke-dasharray="4 3"/>')
        s.append(f'<text x="150" y="{ym-4:.1f}" font-size="14.4" fill="#846009">mean {mean:+.1f} (dashed)</text></svg>')
        return "".join(s), mean
    s.append('</svg>')
    return "".join(s), 0

# ── CORNELL NOTES (Flight Log) — aligned 1:1 to the slide-deck DIRECT INSTRUCTION ──────────────
# Each cue mirrors a deck DIRECT INSTRUCTION slide for that standard (Unit1 Teacher Deck), so students
# take Cornell notes DURING the lecture and the cue column matches exactly what is taught. The teacher
# edition shows a concise "key points to elicit" per cue (drawn from the deck DI + the historian-checked
# reader — no fabrication); the student edition leaves the note column blank. Format = classic Cornell:
# cue/question column · notes column · summary. (FLIGHT_LOG_STANDARD: Cornell notes live in the Flight Log,
# aligned to the decks.)  {n: (deck_slide_ref, [(cue_question, teacher_keypoint), ...])}
CORNELL = {
 1: ("US.01 Direct Instruction (Teacher Deck slides 9–11)", [
   ("How did the Homestead Act and the Transcontinental Railroad open the West — and in what order did settlement follow?",
    "1862 Homestead Act: 160 acres for a small fee + 5 years’ work; the Pacific Railway Act laid the rails to reach it. Settlement followed the tracks."),
   ("Who moved west, and what did the promise of “free land” actually deliver?",
    "Immigrants, freed families, and land-poor farmers filed claims. Real gains — but uneven: drought, debt, and railroad land prices."),
   ("What did western expansion cost the Native nations already living there?",
    "The acres the law called “unclaimed” were tribal homelands; expansion drove dispossession and destroyed the buffalo economy.")]),
 2: ("US.02 Direct Instruction (Teacher Deck slides 23–25)", [
   ("How and why were most Native nations confined to reservations?",
    "After decades of war and removal, federal policy confined nations to reservations, often far from ancestral land."),
   ("What was the goal of assimilation and the boarding schools — and how did they pursue it?",
    "To erase Native cultures. Carlisle (1879) cut hair and banned languages; Pratt’s doctrine: “kill the Indian, save the man.”"),
   ("How did the Dawes Act (1887) break up tribal land — and who ended up with it?",
    "It split communal land into individual allotments; most “surplus” passed to speculators and railroads (138M→48M acres by 1934).")]),
 3: ("US.03 Direct Instruction (Teacher Deck slides 37–40)", [
   ("How did the Compromise of 1877 end Reconstruction?",
    "It settled the 1876 election and withdrew the last federal troops from the South, ending federal protection of Black rights."),
   ("How did new state laws and violence strip away Black rights?",
    "Poll taxes, literacy tests, and grandfather clauses disenfranchised; lynching enforced the color line with impunity."),
   ("How did African Americans respond by moving west?",
    "Benjamin “Pap” Singleton and the Exodusters led thousands to Kansas seeking land and safety."),
   ("How did Plessy v. Ferguson make “separate but equal” the law?",
    "The 1896 Court upheld segregation as constitutional; Harlan’s lone dissent called the Constitution “color-blind.”")]),
 4: ("US.04 Direct Instruction (Teacher Deck slides 53–56)", [
   ("How did political machines like Tammany Hall control cities?",
    "Patronage and graft traded jobs and services for votes; Boss Tweed ran NYC until Nast’s cartoons helped expose him."),
   ("How did the spoils system breed corruption?",
    "Government jobs rewarded loyalty, not merit; scandals like Crédit Mobilier reached into Congress."),
   ("How did Garfield’s assassination lead to reform?",
    "A disappointed office-seeker shot Garfield (1881); the Pendleton Act (1883) created a merit-based civil service."),
   ("Why did wealth concentrate while farmers and workers fell behind?",
    "Capitalists amassed fortunes; farmers sank into debt and wage earners worked 12-hour days; the ICC (1887) tried to rein in railroads.")]),
 5: ("US.05 Direct Instruction (Teacher Deck slides 68–70)", [
   ("How did new inventions remake daily life?",
    "Edison’s electric light, Bell’s telephone, and Tesla’s alternating current brought power and connection to homes and factories."),
   ("How did Carnegie and Rockefeller build — and dominate — steel and oil?",
    "Carnegie: Bessemer steel + vertical integration. Rockefeller: Standard Oil + horizontal integration and trusts."),
   ("How did African American entrepreneurs innovate despite discrimination?",
    "George Washington Carver transformed Southern agriculture; Madam C.J. Walker built a beauty empire (first self-made female millionaire).")]),
 6: ("US.06 Direct Instruction (Teacher Deck slides 83–85)", [
   ("Which cities became manufacturing centers, and why there?",
    "Boston, New York, Chicago, Pittsburgh, San Francisco — access to resources, railroads, and immigrant labor."),
   ("Why did people leave farms for the factory floor?",
    "Factory wages beat farm income; rural Americans and new immigrants crowded into tenements and 12-hour shifts."),
   ("What geographic factors decided where industry located?",
    "Coal, iron, water and rail access, and ports concentrated industry near its inputs and its shipping.")]),
 7: ("US.07 Direct Instruction (Teacher Deck slides 98–101)", [
   ("How did the “new” immigrants differ from earlier waves?",
    "Post-1880 arrivals came from southern/eastern Europe and Asia — new languages, religions, and customs."),
   ("What happened at Ellis Island and Angel Island?",
    "Ellis Island processed European arrivals; Angel Island detained and screened Asian arrivals under exclusion laws."),
   ("What pushed people to leave home — and pulled them to America?",
    "Push: poverty, persecution, famine. Pull: jobs, land, freedom, and family already here."),
   ("How did nativism lead to restriction?",
    "Nativism produced the Chinese Exclusion Act (1882) and the Gentlemen’s Agreement (1907).")]),
}

def cornell_page(n, cs, title, teacher=False):
    """Cornell notes for Stop n, aligned to the deck's DIRECT INSTRUCTION slides. Student = blank note
    lines to fill during the lecture; Teacher = concise 'key points to elicit' per cue. Classic Cornell:
    cue/question column · notes column · summary. Fills the page by design (dense note-taking grid)."""
    codestr = ", ".join(cs)
    ref, cues = CORNELL.get(n, ("", []))
    # Generous, page-filling note space (Cornell needs room to write): ~18 student lines total, spread
    # evenly across the cues; the teacher edition shows key points + a few annotation lines per cue.
    nlines = max(4, 18 // max(1, len(cues)))
    rows = []
    for q, kp in cues:
        if teacher:
            # key points already add height; keep annotation lines light so 4-cue stops don't spill.
            tlines = 3 if len(cues) <= 3 else 2
            lines = "".join('<div class="ln"></div>' for _ in range(tlines))
            notes = f'<div class="cn-key"><b>Key points to elicit:</b> {esc(kp)}</div><div class="write">{lines}</div>'
        else:
            lines = "".join('<div class="ln"></div>' for _ in range(nlines))
            notes = f'<div class="write">{lines}</div>'
        rows.append(f'<div class="cn-row"><div class="cn-cue">{esc(q)}</div><div class="cn-notes">{notes}</div></div>')
    if teacher:
        summ = ('<div class="cn-sumbody"><b>Model summary:</b> guide students to one 2–3 sentence synthesis that '
                'names both the gain and the cost of this standard — the tension they will argue at Wheels Down.</div>')
    else:
        summ = '<div class="write"><div class="ln"></div><div class="ln"></div></div>'
    return f'''<section class="page cornell">
<div class="sec"><div class="eyebrow">Flight Log · Cornell Notes · Stop {n}</div><h2>{esc(title)}</h2><div class="u"></div></div>
<div class="crewcall"><span class="crewtag">Take these during the lesson</span> Fill the notes column while the crew teaches the <b>{esc(ref)}</b>. After the lesson, cover the notes and use the <b>cue questions</b> on the left to quiz yourself — then write the summary.</div>
<div class="cn-grid"><div class="cn-head"><div class="cn-cue cn-h">Cue — ask yourself</div><div class="cn-notes cn-h">Notes — capture as you learn</div></div>{"".join(rows)}</div>
<div class="cn-summary"><div class="cn-sumhd">Summary — the big idea in 2–3 sentences (name the gain <b>and</b> the cost)</div>{summ}</div>
</section>'''

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
<div class="apx" style="border-left-color:#1F3A5F;margin-top:10px"><div class="lab" style="color:#1F3A5F">What's on each stop page</div>
<p style="margin:4px 0 0">A grounded <b>exemplar CER</b> (claim · two evidence · {DEBRIEFER}'s debrief) · a <b>4–3–2–1 rubric</b> · the <b>common misconception</b> · <b>reteach / ways to explain</b> · an <b>extension</b> · a <b>facilitate / watch-for / differentiate / time</b> block · and an <b>EL·MTSS sentence frame</b>. Pull what fits — nothing here is required.</p></div>
<div class="tnote"><b>Grade fast.</b> Score against the rubric on the page, not against the exact wording of the exemplar. Look for the <i>tension</i> (cost vs. benefit): naming it is the difference between a 3 and a 4. A one-sided answer caps at a 2.</div>
<table class="rubric" style="margin-top:10px"><thead><tr><th scope="col">4 — Cleared</th><th scope="col">3 — Airworthy</th><th scope="col">2 — Pre-flight</th><th scope="col">1 — Grounded</th></tr></thead>
<tbody><tr><td>Clear claim + evidence from <b>both</b> sides; <b>names the tension</b> (cost vs. benefit).</td><td>Claim + evidence from both sides; tension only implied.</td><td>Claim with evidence from <b>one</b> side only.</td><td>An opinion, no evidence yet.</td></tr></tbody></table>
<p class="small" style="margin:4px 2px 0;color:#6b7280">One master rubric — every stop is scored the same way, so students internalize the move, not a stop-by-stop checklist.</p>
<div class="apx" style="border-left-color:#1F3A5F;margin-top:10px"><div class="lab" style="color:#1F3A5F">Three moves that raise any score</div>
<p style="margin:4px 0 0"><b>1. Name the trade-off.</b> “X bought ______, and it cost ______.” That single sentence is the 3→4 jump. &nbsp; <b>2. Cite both sides.</b> A 4 needs evidence <i>for</i> and <i>against</i> — one-sided caps at 2. &nbsp; <b>3. Use the source, not a memory.</b> Quote or paraphrase the stop’s document; “I think” with no evidence is a 1.</p></div>
<div class="fr-tie" style="margin-top:10px"><b>Cross-check.</b> Each entry ties to one <b>Stop</b> in the textbook; students write from {DEBRIEFER}’s debrief on the matching Stop page. The numbers are generated from the same stop list as the reader, so Entry N always equals Stop N. <b>Pacing:</b> ≈ one stop per class; the Arc closes the unit.</div></section>'''
    else:
        goals = f'''<section class="page">
<div class="sec"><div class="eyebrow">Before the flight</div><h2>Your Flight Log — how it works</h2><div class="u"></div></div>
<p class="lead">This log is your co-pilot’s seat. In the textbook the crew flies each Stop <i>with</i> you and hands you a source. When {DEBRIEFER} says <i>“capture it in your Flight Log,”</i> you come <b>here</b> — to the matching Entry — and log your call.</p>
<div class="crewcall"><span class="crewtag">The loop</span> <b>Textbook Stop N</b> — the crew hands you a source &amp; you make the call &nbsp;→&nbsp; <b>Flight Log Entry N</b> — frames, the Word Wall, and the rubric help you write it, then you <b>grade your own work</b> &nbsp;→&nbsp; <b>Writing Lab</b> — fly it to the app for <b>instant feedback</b>, then <b>compare the app’s grade to yours</b>. Entry N always equals Stop N.</div>
<div class="cap"><div class="caphd"><span class="udl">UDL · your choice</span><span class="capn">✓</span>Ways to make your call — pick what fits you</div>
<div class="twocol">
  <div class="col"><div class="colh buy">Capture it</div><div style="font-size:9pt;color:#41506a;line-height:1.4">Write it on the lines · sketch the source · or say it out loud and type it into the app’s Writing Lab.</div></div>
  <div class="col"><div class="colh buy">Reach a 4</div><div style="font-size:9pt;color:#41506a;line-height:1.4">Name the <b>tension</b>: what the moment <b>cost</b> and what it <b>bought</b>. Use evidence from <b>both</b> sides — not just your opinion.</div></div>
</div></div>
<div class="cap"><div class="caphd"><span class="capn">✈</span>My SMART goals for this unit</div>
<div class="wlabel">Short-term goal (this unit)</div><div class="write"><div class="ln"></div><div class="ln"></div></div>
<div class="wlabel" style="margin-top:6px">Mid-term goal (this quarter)</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:6px">Long-term goal (Ready Graduate — ACT ≥ 21 or an EPSO/credential)</div><div class="write"><div class="ln"></div></div></div>
<div class="cap"><div class="caphd"><span class="capn">★</span>How I’ll fly — one habit I’ll hold all unit</div>
<div class="frame2">Reflect: how does today’s work ladder toward that long-term goal? Name the habit, then commit to it.</div>
<div class="write"><div class="ln"></div><div class="ln"></div></div></div>
<div class="fr-tie" style="margin-top:8px"><b>Cross-check.</b> Entry <b>N</b> in this log always matches <b>Stop N</b> in the textbook — same number, same crew, same source. Pacing: about one Stop per class; the Arc closes the unit.</div></section>'''

    # ---- LOG ENTRIES (cross-referenced) ----
    def entry_student(n, cs, title):
        codestr = ", ".join(cs)
        # Full-page data-capture CARD. The crew re-engages the student here (they met
        # the crew in the textbook and were sent to this entry); the card captures the
        # student's source read, claim, both-sides evidence, the tension, vocabulary,
        # and self-grade — then hands off to the app. UDL is embedded throughout.
        return f'''<section class="page scard">
<div class="sec"><div class="eyebrow">Flight Log · Data Capture · Entry {n}</div><h2>{esc(title)}</h2><div class="u"></div></div>
<div class="crewcall"><span class="codepin">{codestr}</span><span class="crewtag">{DEBRIEFER} · radio in</span>You met this back in the textbook at <b>Stop {n}</b> and made your call with the crew. Now <b>capture it here</b> — then fly it to the app for your feedback.</div>
<div class="cap"><div class="caphd"><span class="udl">UDL · write · sketch · say it in the app</span><span class="capn">1</span>The source — what did it show you?</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="cap"><div class="caphd"><span class="capn">2</span>Your call — one-sentence claim</div>
<div class="frame2">Frame: “______ moved the nation <b>toward / away</b> from the promise, because ______.”</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="cap"><div class="caphd"><span class="capn">3</span>Your evidence — capture <b>both</b> sides (that is the tension)</div>
<div class="twocol">
  <div class="col"><div class="colh buy">What it BOUGHT — the gain</div><div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
  <div class="col"><div class="colh">What it COST — the price</div><div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
</div></div>
<div class="cap tensionrow"><div class="caphd"><span class="capn">4</span>Name the tension — the historian’s move</div>
It <b>cost</b> <span class="fillline"></span> but it <b>bought</b> <span class="fillline"></span>.</div>
<div class="caprow">
  <div class="wordwall"><div class="caphd"><span class="capn">5</span>Word Wall — jot 3 terms {DEBRIEFER} used</div><div class="chips"><span></span><span></span><span></span></div></div>
  <div class="scorebox"><div class="sbh">Self-grade → fly it</div><div class="sbscale"><b>4</b> both sides + names the tension · <b>3</b> both, implied · <b>2</b> one side · <b>1</b> opinion</div><div class="sbbox">MY SCORE <span class="fl-box"></span></div></div>
</div>
<div class="app"><span class="badge">Web · Writing Lab</span> &nbsp;Fly it to the app: type your call into <b>History Hack online → Writing Lab</b> for <b>instant feedback</b>, then revise your score above.</div>
</section>'''
    def entry_teacher(n, cs, title):
        codestr = ", ".join(cs)
        # Full-page teacher guide per stop: exemplar CER + supports + EL frame.
        e = ex.get(n, {})
        sup = APPENDIX.get(unit, {}).get(n)
        supblock = ""
        bulk = sum(len(e.get(k, "")) for k in ("claim", "ev1", "ev2", "debrief"))
        if sup:
            mis, reteach, ext = sup
            supblock = (f'<div class="apx"><p><span class="lab">Common misconception</span> — {mis}</p>'
                        f'<p><span class="lab">Reteach / ways to explain</span> — {reteach}</p>'
                        f'<p><span class="lab">Extension</span> — {ext}</p></div>')
            bulk += sum(len(x) for x in sup)
        # An extra Exit-ticket line fills the shorter stop pages to the ≥90% guardrail;
        # the longest exemplars (U1) already fill the page, so adding it there would
        # overflow — gate it on the page's text bulk (verified by verify_fill below).
        exitticket = ("" if bulk >= 920 else
                      '<p><span class="lab" style="color:#1F3A5F">Exit ticket</span> — one line out the door: '
                      '<i>“This stop moved the nation toward / away from the promise, because ____.”</i></p>')
        return f'''<section class="page">
<div class="sec"><div class="eyebrow">Answer Key &amp; Teacher Guide · Stop {n}</div><h2>{esc(title)}</h2><div class="u"></div></div>
<div class="fl-eh" style="margin-bottom:4px"><span class="fl-num">{n}</span><span class="fl-ec">{codestr}</span> <span class="ted-tag">KEY</span> <span style="font-size:9pt;color:#41506a">Students write from {DEBRIEFER}’s debrief on the <b>Stop {n}</b> page.</span></div>
<div class="tkey">
  <p><span class="kl">Exemplar claim.</span> {esc(e.get("claim"))}</p>
  <p><span class="kl">Evidence 1.</span> {esc(e.get("ev1"))}</p>
  <p><span class="kl">Evidence 2.</span> {esc(e.get("ev2"))}</p>
  <p><span class="kl">{DEBRIEFER}’s debrief (model).</span> {esc(e.get("debrief"))}</p>
  <div class="anchor"><b>Self-grade anchor →</b> a <b>4</b> states the claim <i>and</i> names the tension between the two sides (cost vs. benefit); a <b>3</b> gives both evidence points but leaves the tension implied; a <b>2</b> has one side; a <b>1</b> is opinion only.</div>
</div>
<table class="rubric" style="margin-top:8px"><thead><tr><th scope="col">4 — Cleared</th><th scope="col">3 — Airworthy</th><th scope="col">2 — Pre-flight</th><th scope="col">1 — Grounded</th></tr></thead>
<tbody><tr><td>Clear claim + evidence from <b>both</b> sides; names the tension.</td><td>Claim + evidence from both; tension implied.</td><td>Claim with evidence from one side only.</td><td>An opinion, no evidence yet.</td></tr></tbody></table>
{supblock}
<div class="apx" style="border-left-color:#1F3A5F"><p><span class="lab" style="color:#1F3A5F">Facilitate</span> — Open: <i>What is the strongest evidence on each side?</i> Push: <i>What single fact would move your score — and which way?</i></p>
<p><span class="lab" style="color:#1F3A5F">Watch for</span> — students who pick a side without naming the trade-off; send them back to the tension. A one-sided answer caps at a <b>2</b>.</p>
<p><span class="lab" style="color:#1F3A5F">Differentiate</span> — <b>Below:</b> give the sentence frame + two of the four rubric rows. <b>On:</b> full CER. <b>Above:</b> add and rebut a counter-argument.</p>
<p><span class="lab" style="color:#1F3A5F">Time</span> — ≈10 min write · 5 min pair-share · 3 min self-grade on the rubric, then revise in the Writing Lab.</p>{exitticket}</div>
{EL_FRAME}
<div class="app"><span class="badge">Web · Writing Lab</span> &nbsp;Students type each call into <b>History Hack online → Writing Lab</b> and check it against the rubric for <b>instant feedback</b>.</div>
</section>'''
    ent = U["stops"]
    entry_fn = entry_teacher if teacher else entry_student
    # Cornell notes section — one page per stop, cue column aligned to the deck's Direct Instruction.
    cornell_intro = f'''<section class="page">
<div class="sec"><div class="eyebrow">Flight Log · During the lesson</div><h2>Cornell Notes — aligned to the slide decks</h2><div class="u"></div></div>
<p class="lead">These pages ride along with the <b>slide decks</b>. As the crew teaches each standard’s <b>Direct Instruction</b>, capture the key ideas in the <b>notes</b> column. Afterward, cover the notes, use the <b>cue questions</b> on the left to quiz yourself, and write a 2–3 sentence <b>summary</b>. That loop — <b>take notes → self-quiz → summarize</b> — is retrieval practice plus summarizing, two of the highest-leverage study moves there are.</p>
<div class="crewcall"><span class="crewtag">Cornell in three moves</span> <b>1 · Notes</b> — capture as you learn (right column). &nbsp; <b>2 · Cues</b> — cover the notes; answer the questions on the left. &nbsp; <b>3 · Summary</b> — the big idea in your own words, gain <b>and</b> cost.</div>
<div class="cn-map"><b>Deck ⇄ Cornell map.</b> Cornell Stop N pairs with Standard US.0N’s Direct-Instruction slides — the same number as your reader Stop. <b>Each Stop now travels together:</b> take your Cornell notes as the crew teaches, then turn the page to make your evidence-based call at Wheels Down in <b>Entry N</b> — right behind its notes.</div>
<div class="cn-grid" style="margin-top:12px"><div class="cn-head"><div class="cn-cue cn-h">Worked example — how a row looks filled</div><div class="cn-notes cn-h">(sample: US.01)</div></div>
<div class="cn-row"><div class="cn-cue">What did western expansion cost the Native nations already living there?</div><div class="cn-notes"><div class="cn-key">The Homestead Act called the land “unclaimed,” but it was tribal homeland. Expansion → dispossession; the railroads and settlers destroyed the buffalo herds the Plains nations depended on. <i>Gain for settlers = loss for Native nations, on the same ground.</i></div></div></div></div>
<div class="cn-summary"><div class="cn-sumhd">Sample summary — the big idea in 2–3 sentences</div><div class="cn-sumbody">The railroad and the Homestead Act opened the West and built a continental economy — a real gain for millions. But the same policies dispossessed Native nations and destroyed the buffalo economy. Progress and cost landed on the same ground, in the same years.</div></div>
<div class="cn-map" style="margin-top:12px"><b>Why this works.</b> Splitting the page into <b>notes</b> (as you learn) and <b>cues</b> (to test yourself) turns passive listening into active recall — and writing the <b>summary</b> forces you to decide what actually mattered. Do the cue-and-summary step the <i>same day</i>, then again before the quiz: two quick self-tests beat one long re-read. Keep every stop’s page — together they are your unit study guide for the EOC.</div></section>'''
    # Per-stop flow (merged): each Stop travels together — Cornell notes (during the
    # lesson) immediately followed by the write Entry (Wheels Down), so the log runs
    # stop-by-stop with the slide deck and the mission book instead of all-notes-then-
    # all-entries. cornell_intro (the method + Deck⇄Cornell map) stays once, up front.
    stops_html = "".join(cornell_page(n, cs, t, teacher) + entry_fn(n, cs, t) for n, cs, t in ent)

    # ---- ARC CAPTURE (points back to the textbook Arc section) ----
    if teacher:
        arcpts = [(a.get("year"), a.get("label") or a.get("milestone")) for a in
                  _json.load(open(ROOT/f"content-build/us-history/narrative/unit-0{unit}.json")).get("arcPoints", [])]
        scores = ARC_SCORES.get(unit, [])
        svg, mean = _arc_svg(arcpts, scores) if scores and len(scores) == len(arcpts) else ("", 0)
        def _sc(v): return "0" if v == 0 else f"{v:+d}"
        rows = "".join(f'<tr><td class="c">{i}</td><td class="c">{yr}</td><td>{esc(lab)}</td><td class="c"><b>{_sc(sc)}</b></td></tr>'
                       for i, ((yr, lab), sc) in enumerate(zip(arcpts, scores), 1))
        # Scale row height inversely with milestone count so a 6-row unit fills the
        # scoring table's page as fully as an 11-row unit (no short-page white space).
        rowpad = max(5, round((13 - len(scores)) * 2.4))
        arc = f'''<section class="page">
<div class="sec"><div class="eyebrow">End of the flight · teacher exemplar</div><h2>The Arc of the Union — a historian’s read</h2><div class="u"></div></div>
<p class="lead">Students plot each milestone (−3 … +3) in the reader’s <b>Arc of the Union</b>. Here is <b>one defensible plot</b> — put it on the board to model the reasoning, then invite students to argue with it.</p>
<div class="arc-wrap">{_svg_fig(svg, "The Arc of the Union — teacher exemplar: the eleven Unit-1 milestones scored from −3 (away from the promise) to +3 (toward it) and connected into one line with the mean marked. One defensible reading, not an answer key.")}</div>
<div class="disc">{ARC_DISCLAIMER}</div>
<div class="readbox"><h3>A historian’s read (one defensible arc)</h3>{HISTORIAN_READ.get(unit,"")} <b>Mean ≈ {mean:+.1f}.</b></div>
<div class="apx" style="border-left-color:#1F3A5F"><p><span class="lab" style="color:#1F3A5F">Run it in class</span> — reveal this plot only <i>after</i> students commit their own. Then argue one point: pick a milestone and ask, “Where would you move it, and what evidence backs the move?” The disagreement is the lesson.</p>
<p style="margin-top:3px"><span class="lab" style="color:#1F3A5F">The move to model</span> — a historian scores the <i>whole</i> arc honestly: gains and costs on the same line. Praise the student who plots a real dip beside a real climb over the one who forces a tidy story — that mixed shape is the accurate read of this era, and defending it is the standard.</p></div></section>
<section class="page">
<div class="sec" style="margin-bottom:8px"><div class="eyebrow">Arc exemplar · continued</div><h2 style="font-size:15pt">The scoring behind the plot</h2></div>
<style>.arcscore td{{padding-top:{rowpad}px;padding-bottom:{rowpad}px}}</style>
<table class="rubric arcscore" style="font-size:9pt"><thead><tr><th class="c" scope="col">#</th><th class="c" scope="col">Year</th><th scope="col">Milestone</th><th class="c" scope="col">Read</th></tr></thead><tbody>{rows}</tbody></table>
<div class="tnote"><b>What to look for in student work.</b> A strong response (1) reports a mean and overall trend, (2) names the steepest climb or drop and the turning point, and (3) defends a <b>toward/away</b> verdict with the <i>shape</i> of the graph — not a vibe. Expect honest mixed arcs: this era’s gains sit beside real costs.</div>
<div class="apx" style="border-left-color:#1F3A5F"><p><span class="lab" style="color:#1F3A5F">Cross-curricular (math / science)</span> — each call is an ordered pair (milestone, score); connected points make a line graph. Confirm the mean is computed correctly and the trend read from the <i>slope</i>. Have students name the steepest change (greatest rate) and the turning point (where the sign flips).</p>
<p><span class="lab" style="color:#1F3A5F">Extrapolate → next unit</span> — extend the line past the last milestone with a dotted prediction; students test it against the next unit's arc.</p>
<p><span class="lab" style="color:#1F3A5F">Differentiate</span> — <b>Below:</b> pre-plot two anchor points and co-score the rest. <b>Above:</b> defend the verdict against a partner who scored the mean on the other side of zero.</p></div>
<div class="frame"><span class="lab">Verdict sentence stems</span> — “Across {esc(U["years"])} the arc <b>climbed / fell / stayed mixed</b>, mean about ____, because ____.” · “The steepest <b>climb / drop</b> was ____ (year ____), where ____.” · “The turning point was ____, when the line crossed zero.” · “On balance the nation moved <b>toward / away from</b> a more perfect union, because the graph ____.”</div>
<div class="tnote" style="margin-top:8px"><b>Score band at a glance.</b> &nbsp;<b>4</b> — mean + trend, names the steepest move <i>and</i> the turning point, defends toward/away by the graph’s <b>shape</b>. &nbsp;<b>3</b> — mean + trend + a defended verdict, evidence mostly from the graph. &nbsp;<b>2</b> — plots and gives a verdict, but argues by vibe, not shape. &nbsp;<b>1</b> — points plotted, no defended verdict yet.</div>
<div class="fr-tie" style="margin-top:10px"><b>Debrief prompt.</b> Push for the trade-off sentence: in one line, what did this unit <i>cost</i>, and what did it <i>buy</i>? That is the historian’s move and the Ready-Graduate habit.</div></section>'''
    else:
        # Student edition: a BLANK, labelled plotting grid — the actual interactive
        # graph. Students plot one point per milestone (−3…+3) and connect them, then
        # capture the mean, trend, and verdict. This is data capture, not a picture.
        arcpts = [(a.get("year"), a.get("label") or a.get("milestone")) for a in
                  _json.load(open(ROOT/f"content-build/us-history/narrative/unit-0{unit}.json")).get("arcPoints", [])]
        grid, _ = _arc_svg(arcpts, [], plot=False)
        legend = " &nbsp;·&nbsp; ".join(f'<b>{i}</b> {esc(lab)} <span style="color:#5f6b7d">({yr})</span>'
                                       for i, (yr, lab) in enumerate(arcpts, 1))
        arc = f'''<section class="page">
<div class="sec"><div class="eyebrow">End of the flight · plot your Arc</div><h2>The Arc of the Union — my call</h2><div class="u"></div></div>
<p class="lead">You flew every Stop with the crew. Now plot the whole unit: for each milestone below, put a dot at how far it moved the nation <b>toward (+)</b> or <b>away (−)</b> from “a more perfect union,” then connect your dots into your Arc.</p>
<div class="arc-wrap">{_svg_fig(grid, "A blank coordinate grid for plotting the Arc of the Union: the seven Unit-1 milestones (with years) run along the bottom, and a scale from −3 (away from the promise) to +3 (toward it) runs up the side, with a 0 line and a gold on-track band. Plot a dot for each milestone, then connect them; the milestone list and scale are also given as text below.")}</div>
<div class="cap"><div class="caphd"><span class="capn">1</span>The milestones — plot one dot per column above</div>
<div style="font-size:9pt;color:#41506a;line-height:1.5">{legend}</div></div>
<div class="caprow">
  <div class="wordwall"><div class="caphd"><span class="capn">2</span>Read your graph</div>
    <div style="font-size:9pt;color:#41506a;line-height:1.7">My <b>mean</b> score (add them, divide by the count): <span class="fillline" style="min-width:.7in"></span><br>Overall <b>trend</b> (circle): &nbsp;<b>Climbing</b> &nbsp; <b>Falling</b> &nbsp; <b>Mixed</b><br>My <b>steepest</b> move (biggest jump/drop) is at milestone # <span class="fillline" style="min-width:.5in"></span></div></div>
  <div class="scorebox"><div class="sbh">Scoring scale</div><div class="sbscale" style="font-size:9pt;line-height:1.6"><b>+3</b> big move toward · <b>+1</b> small toward · <b>0</b> no change · <b>−1</b> small away · <b>−3</b> big move away</div></div>
</div>
<div class="cap"><div class="caphd"><span class="capn">3</span>Make the call — toward or away? Defend it with the <b>shape</b> of your graph</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="fr-tie" style="margin-top:8px"><b>Debrief for {DEBRIEFER}.</b> In one sentence: what did this unit <b>cost</b>, and what did it <b>buy</b>? &nbsp;Then fly your verdict to the <b>Writing Lab</b> for feedback.</div></section>'''

    # ---- WHERE YOU STAND · Unit Master Plot (the running mastery graph) ----
    # After each Stop's exit ticket the student brings that landing (1–4) up here and plots it
    # over that standard; connect the dots across the unit = the mastery arc. Teacher edition
    # frames it as the class "Where They Stand" heat-map. Same 1–4 landing scale as the exit ticket.
    def _wherestand_svg(stops):
        n = len(stops); GH = 320; top = 32; bot = 274
        def X(i): return 82 + (i - 0.5) / n * (650 - 82)
        def Y(v): return bot - (v - 1) / 3 * (bot - top)
        s = [f'<svg viewBox="-14 0 676 {GH}" width="100%" role="img" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans"><title>Where You Stand — plot your landing (1–4) for each standard</title>']
        # on-track band 3–4 — gold fill PLUS a dashed border and an in-band label so the
        # zone survives grayscale printing (not a color-only cue; a11y PR-22).
        s.append(f'<rect x="82" y="{Y(4):.1f}" width="568" height="{Y(3)-Y(4):.1f}" fill="#f6edcf" stroke="#846009" stroke-width="1" stroke-dasharray="5 3"/>')
        s.append(f'<text x="646" y="{Y(4)+13:.1f}" text-anchor="end" font-size="16.2" font-weight="bold" fill="#7a5c12">ON-TRACK ZONE (3–4)</text>')
        ylab = {4: "4 Smooth", 3: "3 Wheels down", 2: "2 Bumpy", 1: "1 In the air"}
        for v in range(1, 5):
            y = Y(v)
            s.append(f'<line x1="82" y1="{y:.1f}" x2="650" y2="{y:.1f}" stroke="#dfe4ec" stroke-width="1"/>')
            s.append(f'<text x="74" y="{y+4:.1f}" text-anchor="end" font-size="15" font-weight="bold" fill="#1F3A5F">{v}</text>')
            s.append(f'<text x="74" y="{y+15:.1f}" text-anchor="end" font-size="14.4" fill="#5f6b7d">{ylab[v][2:]}</text>')
        for i, (num, cs, title) in enumerate(stops, 1):
            x = X(i)
            s.append(f'<line x1="{x:.1f}" y1="34" x2="{x:.1f}" y2="{bot:.0f}" stroke="#e4e9f1" stroke-width="1"/>')
            s.append(f'<text x="{x:.1f}" y="{bot+20:.0f}" text-anchor="middle" font-size="15.8" font-weight="bold" fill="#1F3A5F">{esc(cs[0])}</text>')
            s.append(f'<circle cx="{x:.1f}" cy="{Y(1):.1f}" r="5" fill="none" stroke="#b9c4d6" stroke-width="1.6"/>')  # plot me
        s.append('</svg>')
        return "".join(s)
    ws_svg = _wherestand_svg(U["stops"])
    ws_leg = " &nbsp;·&nbsp; ".join(f'<b>{esc(cs[0])}</b> {esc(t)}' for (n_, cs, t) in U["stops"])
    if teacher:
        wherestand = f'''<section class="page">
<div class="sec"><div class="eyebrow">Teacher · Where They Stand</div><h2>The class mastery heat-map</h2><div class="u"></div></div>
<p class="lead">Each student keeps the <b>Where You Stand</b> plot below — after every Stop's exit ticket they plot that landing (1–4). Collected across the class, the seven columns become your unit heat-map.</p>
<div class="arc-wrap">{_svg_fig(ws_svg, "Where They Stand class heat-map grid: the seven Unit-1 standards (US.01–US.07) along the bottom and a 1–4 landing scale up the side with a gold on-track band at 3–4, for plotting each student's exit-ticket landing.")}</div>
<div style="font-size:9pt;color:#41506a;line-height:1.5;margin-top:6px">{ws_leg}</div>
<div class="tnote" style="margin-top:10px"><b>Read it in 30 seconds.</b> Any standard sitting at <b>1–2</b> for a cluster of students is a reteach group before the EOC. A whole-class dip on one column flags the standard, not the kids. This is the paper mirror of the app's real-time standard-mastery view — the same data whether or not your school runs the platform.</div>
<div class="apx" style="border-left-color:#1F3A5F;margin-top:10px"><div class="lab" style="color:#1F3A5F">From heat-map to action — the MTSS read</div>
<p style="margin:4px 0 0"><b>Tier 1 (whole class at 3–4).</b> The standard landed — move on, and spiral it into the next Stop's warm-up so it stays retrieved. <b>Tier 2 (a cluster at 1–2).</b> Pull a small group back to that Stop's primary source; re-run the CER move on it, then re-plot. <b>Tier 3 (a student flat/falling across two or more columns).</b> That is a leading indicator — conference this week, set one concrete next step, and log it in Mission Control so you both watch the same trend.</p></div>
<div class="apx" style="margin-top:8px"><div class="lab">Before the EOC</div>
<p style="margin:4px 0 0">Rank the columns lowest-first — that is your reteach order. One <b>lap</b> = re-read the source, re-argue the call, re-plot the landing. A column that climbs from 2 to 3 after a lap is the evidence the reteach worked; a column that does not move is the one to escalate.</p></div>
<div class="fr-tie" style="margin-top:8px"><b>On-trajectory = 3 (gold band).</b> Flat or falling across two standards → check in early; that is the leading indicator, read while there is still time to steer.</div></section>'''
    else:
        wherestand = f'''<section class="page">
<div class="sec"><div class="eyebrow">Your unit flight map</div><h2>Where You Stand — Unit {unit}</h2><div class="u"></div></div>
<p class="lead" style="margin-bottom:13px">After every Stop's <b>exit ticket</b>, bring your landing score up here and plot it over that standard. <b>Connect the dots</b> as you go — that line is your climb through the whole unit. Aim to land in the <b>gold band</b> (3–4).</p>
<div class="arc-wrap" style="margin:15px 0 16px">{_svg_fig(ws_svg, "Where You Stand · Unit 1 grid: the seven standards (US.01–US.07) along the bottom and a 1–4 landing scale up the side with a gold on-track band at 3–4. Plot your exit-ticket landing after each Stop and connect the dots into your mastery arc.")}</div>
<div class="cap" style="margin-top:15px"><div class="caphd"><span class="capn">1</span>The standards — plot one landing per column above</div>
<div style="font-size:9pt;color:#41506a;line-height:1.65">{ws_leg}</div></div>
<div class="cap" style="margin-top:15px"><div class="caphd"><span class="capn">2</span>Read your line</div>
<div class="frame2">Where did you climb the most — and which standard needs another lap before the test?</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="fr-tie" style="margin-top:15px"><b>3 is on-trajectory.</b> If a landing sits at 1–2, that standard is your next lap — loop back to the source before the EOC.</div></section>'''

    # ---- FLIGHT READINESS · the Future-Ready check-in ("ACT prep" rename) ----
    # Canon: FRAMEWORKS_CANON.md §5 "The Flight Plan to a Ready Graduate". The grade-check loop +
    # durable-skill trend on the shared 1–4 scale; the commander sends students to Mission Control (app).
    def _fr_plot():
        # The readiness TREND graph — one dot per check-in across the year. y = 1–4 (gold on-track
        # band 3–4); x = Check 1…6. This is where the student plots each Commander's Check.
        s = ['<svg viewBox="0 0 312 152" width="100%" role="img" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans"><title>Readiness trend — plot your overall readiness (1–4) each check-in</title>']
        def Y(v): return 118 - (v - 1) / 3 * 100
        def X(i): return 44 + (i - 1) / 5 * (288 - 44)
        s.append(f'<rect x="44" y="{Y(4):.1f}" width="244" height="{Y(3)-Y(4):.1f}" fill="#f6edcf" stroke="#846009" stroke-width="0.8" stroke-dasharray="4 2"/>')
        s.append(f'<text x="286" y="{Y(4)+11:.1f}" text-anchor="end" font-size="13.4" font-weight="bold" fill="#7a5c12">ON-TRACK</text>')
        ylab = {4: "4", 3: "3", 2: "2", 1: "1"}   # numbers only (words in the caption) so ≥9pt labels fit the mini-plot
        for v in range(1, 5):
            y = Y(v)
            s.append(f'<line x1="44" y1="{y:.1f}" x2="288" y2="{y:.1f}" stroke="#dfe4ec" stroke-width=".9"/>')
            s.append(f'<text x="38" y="{y+3:.1f}" text-anchor="end" font-size="13" font-weight="bold" fill="#1F3A5F">{ylab[v]}</text>')
        for i in range(1, 7):
            x = X(i)
            s.append(f'<line x1="{x:.1f}" y1="18" x2="{x:.1f}" y2="118" stroke="#eef1f6" stroke-width=".8"/>')
            s.append(f'<text x="{x:.1f}" y="134" text-anchor="middle" font-size="13.7" font-weight="bold" fill="#1F3A5F">Ck {i}</text>')
            s.append(f'<circle cx="{x:.1f}" cy="{Y(1):.1f}" r="4" fill="none" stroke="#b9c4d6" stroke-width="1.5"/>')
        s.append('</svg>')
        return "".join(s)
    if teacher:
        readiness = ""
    else:
        readiness = f'''<section class="page frpage"><style>@page fr{{size:Letter;margin:0.42in 0.5in 0.5in 0.55in;@bottom-left{{content:"© 2026 TroopToTeacher Technologies LLC";font:9pt 'DejaVu Sans';color:#5f6b7d;white-space:nowrap}}}}.frpage{{page:fr}}</style>
<div style="background:#1F3A5F;color:#fff;border-radius:10px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center">
  <div><div style="font:700 9pt DejaVu Sans;letter-spacing:.14em;text-transform:uppercase;color:#e8c25a">&#9992; Flight Readiness · the flight plan to a ready graduate</div>
    <div style="font:700 17pt 'DejaVu Serif';margin-top:1px">Are you cleared for takeoff?</div></div>
  <div style="text-align:right;font:700 9pt DejaVu Sans;letter-spacing:.06em;text-transform:uppercase;color:#c9d4e6">Commander&#8217;s Check<br>every 3&ndash;4 missions</div></div>
<div style="margin-top:10px;background:#f6edcf;border-left:4px solid #C9A227;border-radius:0 8px 8px 0;padding:9px 13px;font:400 9pt 'DejaVu Serif';color:#3a4a66;line-height:1.45">
  <b style="color:#1F3A5F">Your 30,000-ft goal:</b> graduate <b style="color:#1F3A5F">Ready</b> &mdash; an ACT composite of <b style="color:#1F3A5F">21+</b> (or a credential/EPSO equal). Measured too late to fix &mdash; so these check-ins are the <b style="color:#1F3A5F">instruments you read now</b>, while there&#8217;s still time to steer.</div>
<div style="display:table;width:100%;margin-top:20px;border-collapse:separate;border-spacing:18px 0">
  <div style="display:table-cell;width:54%;vertical-align:top">
    <div style="font:700 9pt DejaVu Sans;letter-spacing:.06em;text-transform:uppercase;color:#1F3A5F;border-bottom:2px solid #C9A227;padding-bottom:3px">Close the loop &mdash; your grade check</div>
    <div style="display:flex;gap:9px;margin-top:6px"><div style="flex:0 0 20px;height:20px;background:#1F3A5F;color:#fff;border-radius:50%;font:700 9pt DejaVu Sans;text-align:center;line-height:20px">1</div><div style="flex:1;font:400 9pt 'DejaVu Serif';line-height:1.4"><b style="color:#1F3A5F">Check your grades.</b> Log into the gradebook. Write each class&#8217;s current average.<div style="border-bottom:1px solid #9aa8bf;height:16px;margin-top:4px"></div></div></div>
    <div style="display:flex;gap:9px;margin-top:6px"><div style="flex:0 0 20px;height:20px;background:#1F3A5F;color:#fff;border-radius:50%;font:700 9pt DejaVu Sans;text-align:center;line-height:20px">2</div><div style="flex:1;font:400 9pt 'DejaVu Serif';line-height:1.4"><b style="color:#1F3A5F">Find your missing work.</b> Every missing assignment is points still on the table. List them.<div style="border-bottom:1px solid #9aa8bf;height:16px;margin-top:4px"></div></div></div>
    <div style="display:flex;gap:9px;margin-top:6px"><div style="flex:0 0 20px;height:20px;background:#1F3A5F;color:#fff;border-radius:50%;font:700 9pt DejaVu Sans;text-align:center;line-height:20px">3</div><div style="flex:1;font:400 9pt 'DejaVu Serif';line-height:1.4"><b style="color:#1F3A5F">Make the plan &mdash; ask for help.</b> Email the teacher. Asking well is itself a Ready-Graduate skill:<div style="border:1px dashed #b9c4d6;border-radius:6px;padding:6px 8px;margin-top:4px;font:italic 9pt 'DejaVu Serif';color:#3a4a66;line-height:1.4">&ldquo;Dear ______, I&#8217;m missing ______. Could I come in on ______ to make it up? Thank you, ______&rdquo;</div></div></div>
    <div style="display:flex;gap:9px;margin-top:6px"><div style="flex:0 0 20px;height:20px;background:#1F3A5F;color:#fff;border-radius:50%;font:700 9pt DejaVu Sans;text-align:center;line-height:20px">4</div><div style="flex:1;font:400 9pt 'DejaVu Serif';line-height:1.4"><b style="color:#1F3A5F">Set your follow-up.</b> Pick the day you&#8217;ll confirm it&#8217;s done &mdash; that&#8217;s how you close the loop. <b style="color:#1F3A5F">Follow-up date:</b> __________</div></div>
  </div>
  <div style="display:table-cell;width:46%;vertical-align:top">
    <div style="font:700 9pt DejaVu Sans;letter-spacing:.06em;text-transform:uppercase;color:#1F3A5F;border-bottom:2px solid #C9A227;padding-bottom:3px">Your readiness trend &mdash; plot each check-in</div>
    <div style="margin-top:7px">{_svg_fig(_fr_plot(), "Readiness trend graph: six check-ins (Ck 1 to Ck 6) along the bottom and a 1–4 scale up the side with a gold on-track band at 3–4, for plotting your overall readiness at each Commander's Check.")}</div>
    <div style="margin-top:5px;font:400 9pt 'DejaVu Serif';color:#3a4a66;line-height:1.4">Scale: <b style="color:#1F3A5F">4 Advanced · 3 Proficient · 2 Developing · 1 Emerging</b>. Rate <b style="color:#1F3A5F">Timeliness · Work ethic · Integrity · Follow-through</b>, then plot your <b style="color:#1F3A5F">overall readiness</b> as one dot &amp; connect it. <i style="color:#7a5c12">Flat or falling twice &rarr; see your commander;</i> 3 = on-trajectory.</div>
  </div>
</div>
<div style="margin-top:11px;background:#1F3A5F;color:#fff;border-radius:8px;padding:9px 13px;display:flex;align-items:center;gap:10px">
  <div style="font:700 9pt DejaVu Sans;color:#e8c25a;letter-spacing:.04em;white-space:nowrap">&#9992; Commander&#8217;s orders</div>
  <div style="font:400 9pt 'DejaVu Serif';color:#eef2f8;line-height:1.3"><b style="color:#fff">Log all of this in Mission Control</b> (the app) &mdash; your averages, missing work, plan, and readiness scores live there, so you and your teacher watch the same trend. <i style="color:#c9d4e6">These are conversation-starters, not labels &mdash; we measure to help you steer, never to judge.</i></div></div>
<div style="margin-top:8px;border-radius:10px;overflow:hidden;position:relative;line-height:0;height:3.4in">
  <img src="assets/readiness_franklin.png" alt="The U.S. History Hack C-130 transport plane banking over Franklin High School at sunrise — the Flight Readiness hero image." style="width:100%;height:100%;object-fit:cover;object-position:center 40%;display:block">
  <div style="position:absolute;left:0;right:0;bottom:0;padding:11px 16px 10px;line-height:1.3;background:linear-gradient(to top,rgba(8,15,28,0.96) 0%,rgba(8,15,28,0.92) 45%,rgba(8,15,28,0.55) 80%,rgba(8,15,28,0) 100%)">
    <span style="font:700 12.5pt 'DejaVu Serif';color:#fff">Cleared for takeoff.</span>
    <span style="font:400 9.5pt 'DejaVu Serif';color:#ffd97a"> &nbsp;Your climb doesn&#8217;t end at the bell &mdash; it ends at Ready.</span></div></div>
</section>'''

    # Copyright + writing-attribution line (on-page) — appended to the intro page.
    import bookmeta
    colo = (f'<p class="small" style="margin-top:12px;color:#6b7280">{esc(bookmeta.SERIES)} · '
            f'Written by {esc(bookmeta.AUTHOR_LEGAL)} (“{esc(bookmeta.AUTHOR_VOICE)}”). '
            f'{esc(bookmeta.COPYRIGHT)}</p>' + bookmeta.build_stamp_html())
    goals = goals.replace("</section>", colo + "</section>", 1)

    head_css = f'<link rel="stylesheet" href="style.css">' + (TEACHER_CSS if teacher else STUDENT_CSS)
    geo_wp = _geo_waypoints(teacher) if unit == 1 else ""
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">{head_css}</head><body>
{cover}{goals}{wherestand}{readiness}{cornell_intro}{stops_html}{geo_wp}{arc}</body></html>'''
    suffix = "_FlightLog_TeacherEdition" if teacher else "_FlightLog"
    out = BASE/"out"/f"ToFormAMorePerfectUnion_Unit{unit}{suffix}.pdf"
    HTML(string=html, base_url=str(BASE)).write_pdf(str(out), pdf_variant='pdf/ua-1', pdf_tags=True)
    print("WROTE", out)
    # Folios come from the @page CSS @bottom-center margin box (tagged as a page artifact,
    # and suppressed on the .fl-cover via @page cover). Do NOT also run bookmeta.paginate()
    # here — that stamps a second, UNTAGGED insert_text folio over every page, which both
    # double-prints the number and injects untagged content into the PDF/UA render.
    ed = "Teacher Flight Log (Answer Key)" if teacher else "Student Flight Log"
    bookmeta.stamp_metadata(out, f"To Form a More Perfect Union — Unit {unit} {ed}: {U['title']}",
                            subject="Student write-in Flight Log companion")
    bookmeta.add_th_scope(out)   # PDF/UA: /Scope on every table-header cell (WeasyPrint omits it)
    verify_fill(out)


def verify_fill(pdf_path, target=90.0, enforce=True):
    """White-space guardrail: every content page must be ≥ target% filled (≤10% white
    space). Cover page (index 0) is a full-bleed image and is exempt. Prints a PASS/WARN
    line per build so a regression surfaces immediately.

    The gate is ENFORCED on dense pages (teacher answer-key/guide). The student edition
    is a write-in workbook whose blank ruled lines are the intended content — they render
    as light-gray rules the dark-pixel measure does not count — so it is reported for
    information only, never WARNed (its 'white space' is functional writing room)."""
    import fitz
    d = fitz.open(str(pdf_path))
    npages = d.page_count
    DPI = 100; FOOT = int(0.55 * DPI); under = []
    for i in range(npages):
        pix = d[i].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
        w, h, s = pix.width, pix.height, pix.samples; lim = h - FOOT; end = 0
        for y in range(lim):
            if any(b < 205 for b in s[y * w:(y + 1) * w]): end = y + 1
        f = 100 * end / lim
        if i > 0 and f < target: under.append((i + 1, round(f, 1)))
    d.close()
    if not enforce:
        print(f"  fill INFO (write-in, blank lines intentional): {pdf_path.name} — {npages}pp")
        return
    tag = "PASS" if not under else "WARN"
    print(f"  fill {tag}: {pdf_path.name} — {npages}pp, under-{target:.0f}%: {under or 'none'}")

if __name__ == "__main__":
    unit = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    teacher = len(sys.argv) > 2 and sys.argv[2].lower().startswith("t")
    build(unit, teacher)
