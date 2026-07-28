# -*- coding: utf-8 -*-
"""Unit 4 labeled matrix -- US.35 Civil Liberties: challenges & advancements.
A context band names the era's CHALLENGES (First Red Scare, immigration quotas,
KKK resurgence, Tulsa). The matrix then compares three ADVANCEMENTS -- three ways
people pushed back (Ida B. Wells-Barnett | Marcus Garvey/UNIA | the NAACP) across
the same three criteria (goal | strategy | signature work). Faded italic hints in
LIGHT cells. TN tie: KKK founded in Pulaski, TN. Neutral framing. Approved US.35.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ctxband{ flex:0 0 auto; background:var(--red-tint); border:1.5px solid #e2b3b8;
            border-left:6px solid var(--red); border-radius:0 6px 6px 0; padding:6px 11px;
            font-size:8.3pt; color:#5a2a30; line-height:1.34; margin-bottom:7px; }
  .ctxband b{ color:var(--red); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.72fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1fr 1fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 4px;
       font-size:7.2pt; font-weight:800; letter-spacing:.03em; color:var(--muted);
       text-transform:uppercase; line-height:1.25; }
  .mx .chead{ color:#fff; font-weight:800; font-size:9.6pt; text-align:center;
       padding:7px 6px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.05; }
  .mx .chead small{ font-weight:600; font-size:7.1pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9pt;
       padding:6px 9px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 28px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:6px; left:9px; right:9px; font-size:7.5pt;
       font-style:italic; color:#9aa6bd; line-height:1.22; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

COLS = [
    ("Ida B. Wells&#8209;Barnett", "journalist &amp; activist"),
    ("Marcus Garvey", "the UNIA"),
    ("The NAACP", "founded 1909"),
]

ROWS = [
    ("Main goal", [
        "end lynching; expose its myths",
        "Black pride, self&#8209;reliance &amp; unity",
        "full legal &amp; civil rights and equality",
    ]),
    ("Strategy / method", [
        "investigative journalism &amp; public speaking",
        "a mass movement &amp; Black&#8209;owned business",
        "lawsuits, lobbying &amp; anti&#8209;lynching campaigns",
    ]),
    ("Signature work", [
        "&ldquo;Southern Horrors&rdquo; (1892); lynching statistics",
        "the UNIA, <i>Negro World</i> &amp; the Black Star Line",
        "<i>The Crisis</i> magazine; legal challenges",
    ]),
]


def _grid():
    cells = ['<div class="corner">Who&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">First read the <b>challenges</b> of the era in the red band. Then compare three <b>responses</b> &mdash; how each fought for civil rights &mdash; across the same three questions. Write over the faint starters.</div>
    <div class="ctxband"><b>The challenges (1919&ndash;1929):</b> the <b>First Red Scare</b> &amp; Palmer Raids (6,000+ arrested);
    the <b>Emergency Quota Act</b> (1921) &amp; <b>National Origins Act</b> (1924) sharply limiting immigration; a
    <b>KKK resurgence</b> (4&ndash;5 million members) reaching beyond the South; and the <b>Tulsa Race Massacre</b> (1921).</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> The Ku Klux Klan was originally founded in <b>Pulaski, Tennessee,</b>
      in 1865. Its 1920s resurgence reached <b>Nashville, Knoxville, and Memphis,</b> and the NAACP organized
      counter&#8209;efforts &mdash; making Tennessee a battleground for civil liberties.</span>
    </div>
"""

_UDL = dict(
    scaffold="Read the challenge band aloud together, then fill the <b>Main goal</b> row as the model before students finish by column.",
    extend="Whose approach do you think fit the era best &mdash; and why? Use the matrix as evidence; note how the three could work together.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>chart</b> the three responses side by side.")

ORGANIZERS = [
    dict(
        slug="27_us35_matrix",
        title="Three Ways of Fighting for Civil Rights",
        kicker="Unit 4 &middot; US.35 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("The 1920s tested civil liberties &mdash; and people pushed back in different ways. A matrix holds the three "
             "approaches against one yardstick so their goals, methods, and work compare clearly. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.35 (labeled)",
    ),
]
