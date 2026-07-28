# -*- coding: utf-8 -*-
"""Unit 7 labeled matrix -- US.59 U.S.-Soviet Competition.
Compare the two superpowers (United States | Soviet Union) across the same four
criteria (arms race | economy | ideology | alliances). Faded italic hints in LIGHT
cells. Neutral, descriptive framing. HAS a Tennessee Connection (Oak Ridge).
Content approved for US.59.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.66fr 1fr 1fr;
       grid-template-rows:auto 1fr 1fr 1fr 1fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 4px;
       font-size:7.3pt; font-weight:800; letter-spacing:.03em; color:var(--muted);
       text-transform:uppercase; line-height:1.25; }
  .mx .chead{ color:#fff; font-weight:800; font-size:11pt; text-align:center;
       padding:8px 6px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.05; }
  .mx .chead.us{ background:var(--navy); } .mx .chead.su{ background:var(--red); }
  .mx .chead small{ font-weight:600; font-size:7.4pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.6pt;
       padding:6px 9px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 26px, var(--wl) 26px 27px);
       background-position:0 32px; background-clip:content-box; }
  .mx .cell.su{ background-image:repeating-linear-gradient(to bottom, transparent 0 26px, #e6c4c8 26px 27px); }
  .mx .fh{ position:absolute; top:6px; left:10px; right:10px; font-size:7.9pt;
       font-style:italic; color:#9aa6bd; line-height:1.24; }
  .mx .cell.su .fh{ color:#c69aa0; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

ROWS = [
    ("Arms race", [
        "atomic bomb by 1945; H&#8209;bombs &amp; ICBMs; a &ldquo;balance of terror&rdquo;",
        "caught up by 1949; matched the arsenal &mdash; both could destroy the world",
    ]),
    ("Economy", [
        "capitalism &amp; free markets; the Marshall Plan won allies",
        "a communist planned economy; state&#8209;controlled production",
    ]),
    ("Ideology", [
        "democracy, individual freedoms, free markets, religious liberty",
        "communist authoritarianism, collective ownership, atheism",
    ]),
    ("Alliances", [
        "NATO (1949) &amp; SEATO",
        "the Warsaw Pact",
    ]),
]


def _grid():
    cells = ['<div class="corner">Power&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>',
             '<div class="chead us">United States<small>capitalism &middot; democracy</small></div>',
             '<div class="chead su">Soviet Union<small>communism &middot; one&#8209;party state</small></div>']
    for crit, (us, su) in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        cells.append(f'<div class="cell"><span class="fh">{us}</span></div>')
        cells.append(f'<div class="cell su"><span class="fh">{su}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the two superpowers across the same four questions. The faint notes are starters &mdash; <b>write over them</b>, then see how the rivalry played out without the two ever fighting directly.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee sat at the center of the arms race. <b>Oak Ridge&rsquo;s Y&#8209;12
      plant</b> kept producing nuclear materials throughout the Cold War, and <b>Oak Ridge National Laboratory</b> led
      critical nuclear research &mdash; making Tennessee a key state in the U.S.&ndash;Soviet competition.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>Arms race</b> row together first as the model, then let students complete each power by column.",
    extend="On which front &mdash; arms, economy, or ideology &mdash; was the competition most dangerous? Defend your answer.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>chart</b> the two powers side by side.")

ORGANIZERS = [
    dict(
        slug="20_us59_matrix",
        title="Two Superpowers, One Cold War",
        kicker="Unit 7 &middot; US.59 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds the U.S. and the USSR against one yardstick, so students see the rivalry across arms, "
             "economy, and ideology &mdash; a global contest fought without direct war. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.59 (labeled)",
    ),
]
