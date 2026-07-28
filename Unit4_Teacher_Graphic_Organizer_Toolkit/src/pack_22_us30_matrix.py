# -*- coding: utf-8 -*-
"""Unit 4 labeled matrix -- US.30 Country, Blues & the Grand Ole Opry.
Compare three cases (Country music | Blues music | the Grand Ole Opry) across the
same four criteria (roots | sound & instruments | key figures | how radio grew it).
Pre-loaded content is a FADED italic watermark inside each LIGHT cell so students
write over it. TN tie: Nashville (Opry) & Memphis (Beale Street). Neutral framing.
Content approved for US.30.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.78fr 1fr 1fr 1fr;
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
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
         font-size:9pt; color:var(--navy); } .cbar b{ color:var(--navy); }
"""

COLS = [
    ("Country Music", "rural Southern roots"),
    ("Blues Music", "African American roots"),
    ("Grand Ole Opry", "WSM Radio, Nashville"),
]

ROWS = [
    ("Roots &middot; where it began", [
        "Scots&#8209;Irish ballads, folk &amp; gospel of the rural South",
        "work songs, field hollers &amp; spirituals; the Mississippi Delta",
        "&ldquo;WSM Barn Dance,&rdquo; Nashville, Nov.&nbsp;28, 1925",
    ]),
    ("Sound &amp; instruments", [
        "fiddle, banjo, guitar, harmonica; themes of home &amp; hardship",
        "12&#8209;bar blues; Delta guitar; themes of love, loss &amp; resilience",
        "live Saturday&#8209;night string bands &amp; performers",
    ]),
    ("Key figures", [
        "1920s recording artists carried it to national audiences",
        "W.C.&nbsp;Handy (&ldquo;Memphis Blues,&rdquo; 1912); Bessie Smith",
        "George D. Hay, the &ldquo;Solemn Old Judge&rdquo;",
    ]),
    ("How radio grew it", [
        "records &amp; radio brought rural music to the whole country",
        "urban blues spread as people migrated to cities",
        "WSM broadcasts reached millions &mdash; Nashville became country&rsquo;s center",
    ]),
]


def _grid():
    cells = ['<div class="corner">Case&nbsp;&rarr;<br>Criteria&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the three across the same four questions. The faint notes are starters &mdash; <b>write over them</b> in your own words, then look for what they <b>share</b>: the radio.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> <b>Nashville</b> became the epicenter of country music with the
      <b>Grand Ole Opry</b> (WSM Radio, 1925) and later Music Row, while <b>Memphis&rsquo;s Beale Street</b> was a
      cradle of the blues &mdash; making Tennessee a birthplace of two American sounds.</span>
    </div>
    <div class="cbar"><b>Your call:</b> How did the <b>radio</b> change music in the 1920s? ______________________________________________</div>
"""

_UDL = dict(
    scaffold="Fill the <b>Roots</b> row together first as the model, then let students complete the rest by column.",
    extend="What did country and blues <b>share</b>, and how did each spread? Use the &ldquo;how radio grew it&rdquo; row as evidence.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>play/describe</b> a sample of each style.")

ORGANIZERS = [
    dict(
        slug="22_us30_matrix",
        title="Two American Sounds &amp; the Radio That Grew Them",
        kicker="Unit 4 &middot; US.30 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds several cases against one yardstick, so patterns across country, blues, and the Opry &mdash; "
             "and the radio&rsquo;s role in all three &mdash; pop into view. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.30 (labeled)",
    ),
]
