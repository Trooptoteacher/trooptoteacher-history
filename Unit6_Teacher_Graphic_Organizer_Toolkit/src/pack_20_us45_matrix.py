# -*- coding: utf-8 -*-
"""Unit 6 labeled matrix -- US.45 Fascism, Communism & Totalitarianism.
Compare three systems (Fascism | Communism | Totalitarianism) across the same four
criteria (core idea | economy | who holds power | where seen). Faded italic hints
in LIGHT cells. Neutral, descriptive framing -- systems described by their own
tenets, no side called good/bad; students draw the comparison. No TN tie in source.
Content approved for US.45.
"""

CSS = r"""
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.86fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1fr 1fr 1fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 4px;
       font-size:7.3pt; font-weight:800; letter-spacing:.03em; color:var(--muted);
       text-transform:uppercase; line-height:1.25; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10pt; text-align:center;
       padding:7px 6px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.05; }
  .mx .chead small{ font-weight:600; font-size:7.2pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.2pt;
       padding:6px 9px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 30px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:6px; left:9px; right:9px; font-size:7.5pt;
       font-style:italic; color:#9aa6bd; line-height:1.22; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
         font-size:9pt; color:var(--navy); } .cbar b{ color:var(--navy); }
"""

COLS = [
    ("Fascism", "Italy &amp; Germany"),
    ("Communism", "Soviet Union"),
    ("Totalitarianism", "the shared system"),
]

ROWS = [
    ("Core idea", [
        "ultranationalism &mdash; the nation above the individual; militarism",
        "class struggle; workers overthrow capitalism &rarr; a classless society",
        "the state controls <b>all</b> of public &amp; private life",
    ]),
    ("The economy", [
        "corporate state &mdash; private owners, but the government directs it",
        "collective &amp; state ownership; central planning",
        "government direction of the economy",
    ]),
    ("Who holds power", [
        "one leader (F&uuml;hrer/Duce); cult of personality",
        "a vanguard Communist Party rules for the workers",
        "a dictator + secret police, propaganda, no dissent",
    ]),
    ("Where seen", [
        "Mussolini&rsquo;s Italy; Hitler&rsquo;s Germany",
        "Stalin&rsquo;s Soviet Union",
        "Nazi Germany, the USSR &amp; Fascist Italy alike",
    ]),
]


def _grid():
    cells = ['<div class="corner">System&nbsp;&rarr;<br>Criteria&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the three systems across the same four questions. The faint notes are starters &mdash; <b>write over them</b>, then find where fascism and communism <b>differ</b> but both turn <b>totalitarian</b>.</div>
    {_grid()}
    <div class="cbar"><b>Your call:</b> Fascism and communism were bitter enemies &mdash; so how did both become <b>totalitarian</b>? __________________________________________</div>
"""

_UDL = dict(
    scaffold="Fill the <b>Core idea</b> row together first as the model, then let students complete the rest by column.",
    extend="Fascism and communism opposed each other &mdash; yet both produced dictatorships. Explain that paradox using the &ldquo;who holds power&rdquo; row.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>chart</b> the three systems side by side.")

ORGANIZERS = [
    dict(
        slug="20_us45_matrix",
        title="Three Systems That Shaped the 20th Century",
        kicker="Unit 6 &middot; US.45 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds fascism, communism, and totalitarianism against one yardstick, so their ideas, economics, "
             "and power structures compare clearly &mdash; and the overlap becomes visible. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.45 (labeled)",
    ),
]
