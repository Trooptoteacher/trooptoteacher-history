# -*- coding: utf-8 -*-
"""Unit 2 labeled best-fit organizer -- T-chart with a shared criteria spine.
US.16-US.17: Two Progressive presidents compared on the same four criteria down
       the middle -- Theodore Roosevelt (the Square Deal) vs. Woodrow Wilson
       (the New Freedom). Signature acts seeded as faint hints in each cell.
TN tie: TR's conservation (Great Smoky Mountains) + Wilson's Columbia, TN boyhood.
Neutral framing: neither presidency is ranked; the verdict is the student's.
"""

CSS = r"""
  .pg{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .pgrid{ flex:1 1 auto; display:grid; grid-template-columns:1fr 0.62fr 1fr;
          grid-template-rows:auto 1fr 1fr 1fr 1fr; gap:5px 8px; min-height:0; }
  .pgrid .band{ border-radius:6px; display:flex; flex-direction:column; justify-content:center; }
  .pgrid .band small{ display:block; font-weight:600; font-size:8pt; opacity:.92; letter-spacing:0; text-transform:none; }
  .spinehd{ background:transparent; display:flex; align-items:center; justify-content:center;
            font-size:7.6pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase; color:var(--muted); }
  .crit{ background:var(--navy); color:#fff; border-radius:6px; display:flex; flex-direction:column; justify-content:center;
         text-align:center; padding:4px 6px; font-size:8.6pt; font-weight:800; line-height:1.15; }
  .pcell{ background:var(--paper); border:1.5px solid var(--rule); border-radius:6px; position:relative; overflow:hidden;
          background-image:repeating-linear-gradient(to bottom, transparent 0 24px, var(--wl) 24px 25px);
          background-position:0 20px; }
  .pcell.red{ border-color:#e2b7bd; }
  .pcell .sh{ position:absolute; top:3px; left:7px; right:7px; font-size:7.3pt; font-style:italic; color:#9aa4b4; line-height:1.15; }
  .tnbox{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.9pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
  .synth{ flex:0 0 auto; background:var(--cream); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:8px 12px; font-size:9.3pt; color:var(--navy); text-align:center; }
  .synth b{ color:var(--navy); }
"""

# (criterion label, TR faint hint, Wilson faint hint)
ROWS = [
    ("Signature program", "the Square Deal", "the New Freedom"),
    ("Taking on trusts", "Northern Securities (1902)", "FTC + Clayton Antitrust Act (1914)"),
    ("Consumer &amp; economic reform", "Pure Food &amp; Drug Act + Meat Inspection Act (1906)", "Federal Reserve Act (1913) &middot; Underwood Tariff"),
    ("Conservation / lasting mark", "conservation of public lands", "National Park Service (1916)"),
]

def _grid():
    cells = []
    cells.append('<div class="band navy" style="padding:6px 8px; text-align:center;">THEODORE ROOSEVELT<small>the Square Deal</small></div>')
    cells.append('<div class="spinehd">Criteria</div>')
    cells.append('<div class="band red" style="padding:6px 8px; text-align:center;">WOODROW WILSON<small>the New Freedom</small></div>')
    for crit, tr, wil in ROWS:
        cells.append(f'<div class="pcell"><span class="sh">TR: {tr}</span></div>')
        cells.append(f'<div class="crit">{crit}</div>')
        cells.append(f'<div class="pcell red"><span class="sh">Wilson: {wil}</span></div>')
    return '<div class="pgrid">' + "".join(cells) + '</div>'

BODY = f"""
    <div class="prompt">Compare the two Progressive presidents on the <b>same four criteria</b>. Add evidence on each side &mdash; then judge.</div>
    <div class="pg">
      {_grid()}
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> Roosevelt&rsquo;s conservation helped protect the
        <b>Great Smoky Mountains</b> region, and Woodrow Wilson spent part of his childhood in <b>Columbia, Tennessee</b>.</span>
      </div>
      <div class="synth"><b>Evaluate:</b> Whose progressivism did more to reshape America?
      ____________ <b>because</b> ________________________________________</div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the &ldquo;Taking on trusts&rdquo; row together using the faint hints as anchors, then students complete the rest.",
    extend="Write a one-paragraph verdict that cites at least one criterion from <b>each</b> president and names the trade-off.",
    show="Students may <b>write</b> in cells, <b>say</b> a verdict aloud, <b>draw</b> a symbol for each presidency, or <b>build</b> it as evidence cards.")

ORGANIZERS = [
    dict(
        slug="28_us1617_tchart",
        title="Two Progressive Presidents: Roosevelt <span style='font-family:Georgia;font-style:italic'>or</span> Wilson?",
        kicker="Unit 2 &middot; US.16 &middot; US.17 &middot; Best-Fit Organizer",
        chips=[("T&#8209;Chart &middot; Two Presidents", "navy"), ("DOK 3 &middot; Evaluate", "skill")],
        why=("Comparing the two Progressive presidents on the same criteria clarifies what Progressivism actually achieved &mdash; "
             "and lets students weigh two records evenly instead of memorizing one. "
             "<span class='cite'>Comparing similarities and differences is Marzano&rsquo;s highest-yield move.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL, tn=True,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.16&ndash;US.17 (labeled)",
    ),
]
