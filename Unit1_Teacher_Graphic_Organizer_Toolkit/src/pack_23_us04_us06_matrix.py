# -*- coding: utf-8 -*-
"""Unit 1 labeled matrices.
US.04: compare three Gilded Age forces (Farmers | Wage earners | Industrial
       capitalists) across criteria.
US.06: Major industrial centers -- City x Industry (Boston, Chicago, New York
       City, Pittsburgh, San Francisco). Cities sourced from standards inventory.
"""

CSS = r"""
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0; }
  .mx .corner{ background:transparent; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10.5pt; text-align:center; padding:7px 6px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; }
  .mx .chead small{ font-weight:600; font-size:7.6pt; opacity:.92; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.6pt; padding:6px 9px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; }
  .mx .rhead small{ font-weight:600; font-size:7.6pt; opacity:.9; font-style:italic; }
  .mx .cell{ background:var(--paper); border:1.5px solid var(--rule); border-radius:6px;
             background-image:repeating-linear-gradient(to bottom, transparent 0 26px, var(--wl) 26px 27px);
             background-position:0 9px; }
  .mx .cell.tint{ background-color:var(--gold-tint); }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--navy-tint); border:1.5px solid var(--navy);
         border-radius:6px; padding:6px 11px; font-size:9pt; } .cbar b{ color:var(--navy); }
"""

# ---- US.04: 3 groups x 4 criteria (col1 = criteria labels) ----
US04_CRIT = [
    ("What they wanted", "goals &amp; interests"),
    ("Biggest challenge", "what squeezed them?"),
    ("How they built power", "unions? Grange/Populism? trusts?"),
    ("Where things stood by 1900", "what had changed for this group?"),
]
US04_GROUPS = [("Farmers", "the Grange &amp; Populists", "navy"),
               ("Wage earners", "factory &amp; rail labor", "red"),
               ("Industrial capitalists", "owners &amp; financiers", "gold")]

def _us04():
    cells = ['<div class="corner"></div>']
    for nm, sub, col in US04_GROUPS:
        cells.append(f'<div class="chead" style="background:var(--{col})'
                     + ('; color:var(--navy)' if col == 'gold' else '') + f'">{nm}<small>{sub}</small></div>')
    for nm, sub in US04_CRIT:
        cells.append(f'<div class="rhead">{nm}<small>{sub}</small></div>')
        for _ in US04_GROUPS:
            cells.append('<div class="cell"></div>')
    grid = ('<div class="mx" style="grid-template-columns:1.15fr 1fr 1fr 1fr; '
            'grid-template-rows:auto 1fr 1fr 1fr 1fr;">' + "".join(cells) + '</div>')
    return f"""
    <div class="prompt">Compare the three great forces of the Gilded Age across each row. Look for the <b>conflict</b> between them.</div>
    {grid}
    <div class="cbar"><b>Pattern:</b> Whose interests most often collided &mdash; and who held the most power by 1900? ____________________________________</div>
"""

# ---- US.06: 5 cities x 3 attributes ----
US06_ATTR = [("Signature industry", "what was it known for?"),
             ("Why it grew here", "geography, rivers, rails, port"),
             ("Who powered it", "immigrants &amp; migrants who came to work")]
US06_CITIES = ["Boston", "Chicago", "New York City", "Pittsburgh", "San Francisco"]

def _us06():
    cells = ['<div class="corner"></div>']
    for nm, sub in US06_ATTR:
        cells.append(f'<div class="chead" style="background:var(--navy)">{nm}<small>{sub}</small></div>')
    for city in US06_CITIES:
        cells.append(f'<div class="rhead">{city}</div>')
        for _ in US06_ATTR:
            cells.append('<div class="cell"></div>')
    grid = ('<div class="mx" style="grid-template-columns:0.85fr 1fr 1fr 1fr; '
            'grid-template-rows:auto 1fr 1fr 1fr 1fr 1fr;">' + "".join(cells) + '</div>')
    return f"""
    <div class="prompt">Map each city to its industry and the people who built it. What made these five <b>engines</b> of urban America?</div>
    {grid}
    <div class="cbar"><b>Pattern:</b> What did fast-growing industrial cities have in common &mdash; in geography <em>and</em> in who did the work? ____________________</div>
"""

ORGANIZERS = [
    dict(
        slug="23_us04_matrix",
        title="Three Forces of the Gilded Age",
        kicker="Unit 1 &middot; US.04 &middot; Best-Fit Organizer",
        chips=[("Matrix &middot; Compare on Criteria", "navy"), ("DOK 3 &middot; Analysis", "skill")],
        why=("A matrix lets students compare farmers, wage earners, and industrial capitalists across the same criteria at once &mdash; "
             "exposing the competing interests that drove Gilded Age politics. "
             "<span class='cite'>Structured comparison across criteria is Marzano&rsquo;s highest-yield strategy.</span>"),
        body=_us04(), extra_css=CSS,
        udl=dict(
            scaffold="Fill one full row together as a model; give a word bank (Grange, Populists, unions, trusts, deflation) for the rest.",
            extend="Add a fourth column of your choice (e.g., immigrants, reformers) and defend why it belongs in the comparison.",
            show="Students may <b>write</b> in cells, <b>say</b> a row aloud, <b>draw</b> a symbol per group, or <b>build</b> it as a sort."),
        role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.04 (labeled)",
    ),
    dict(
        slug="25_us06_matrix",
        title="Engines of Urban America",
        kicker="Unit 1 &middot; US.06 &middot; Best-Fit Organizer",
        chips=[("Matrix &middot; City &times; Industry", "navy"), ("DOK 2&ndash;3 &middot; Analysis", "skill")],
        why=("Charting five industrial cities against the same three questions reveals why urbanization clustered where it did "
             "and who did the work. <span class='cite'>Comparing cases on shared criteria builds analytical reasoning (Marzano).</span>"),
        body=_us06(), extra_css=CSS,
        udl=dict(
            scaffold="Complete Chicago together as the model row; provide a labeled U.S. map so students can reason from geography.",
            extend="Rank the five cities by how fast they likely grew and justify the order with your matrix evidence.",
            show="Students may <b>write</b>, <b>say</b> a city&rsquo;s story, <b>draw</b> it on a map, or <b>build</b> a matching card set."),
        role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.06 (labeled)",
    ),
]
