# -*- coding: utf-8 -*-
"""Unit 10 labeled matrix -- US.93 The Increasing Role of Women & Minorities.
Compare three barrier-breaking leaders (Sandra Day O'Connor | Colin Powell |
Hillary Clinton) across the same two questions (barrier broken | role & impact).
Faded italic hints in LIGHT cells. HAS a Tennessee Connection.
Content approved for US.93.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.42fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1.25fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 3px;
       font-size:7pt; font-weight:800; letter-spacing:.02em; color:var(--muted);
       text-transform:uppercase; line-height:1.22; }
  .mx .chead{ color:#fff; font-weight:800; font-size:9.4pt; text-align:center;
       padding:7px 5px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.05; }
  .mx .chead small{ font-weight:600; font-size:6.9pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:8.6pt;
       padding:5px 7px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 32px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:6px; left:8px; right:8px; font-size:7.5pt;
       font-style:italic; color:#9aa6bd; line-height:1.26; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

COLS = [
    ("Sandra Day O&rsquo;Connor", "Supreme Court"),
    ("Colin Powell", "military &amp; diplomacy"),
    ("Hillary Clinton", "politics"),
]

ROWS = [
    ("Barrier broken", [
        "first woman on the U.S. Supreme Court (1981, appointed by Reagan)",
        "first Black Chairman of the Joint Chiefs; first Black Secretary of State",
        "First Lady &rarr; U.S. Senator &rarr; Secretary of State &rarr; first woman nominated for president by a major party",
    ]),
    ("Role &amp; impact", [
        "a moderate voice who often cast the deciding swing vote",
        "led Gulf War planning; kept broad respect across party lines",
        "advocated for healthcare, women&rsquo;s &amp; children&rsquo;s issues at the highest levels",
    ]),
]


def _grid():
    cells = ['<div class="corner">Leader&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the three leaders across the same two questions. The faint notes are starters &mdash; <b>write over them</b>, then notice the &ldquo;firsts&rdquo; each achieved and the doors they opened.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee&rsquo;s leadership grew more diverse too: <b>Harold Ford Jr.</b>
      represented Memphis as one of the nation&rsquo;s youngest African American congressmen, and <b>Marsha Blackburn</b>
      became Tennessee&rsquo;s <b>first female U.S. Senator</b> in 2019.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>&ldquo;barrier broken&rdquo;</b> row together first, then let students complete each leader&rsquo;s impact.",
    extend="Which &ldquo;first&rdquo; do you think opened the most doors for others? Defend your answer.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>match</b> each leader to the barrier they broke.")

ORGANIZERS = [
    dict(
        slug="30_us93_matrix",
        title="Breaking Barriers in American Leadership",
        kicker="Unit 10 &middot; US.93 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds three trailblazers against the same two questions, so students see both the barrier each "
             "broke and the impact each had. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.93 (labeled)",
    ),
]
