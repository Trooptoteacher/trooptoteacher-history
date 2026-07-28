# -*- coding: utf-8 -*-
"""Blank reproducible: K-W-L chart -- topic line + three colored-band columns over light wells."""

CSS = r"""
  .kwl{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; gap:10px; }
  /* topic line */
  .kwl-topic{ flex:0 0 auto; display:flex; align-items:center; gap:10px;
    border:1.6px solid var(--rule); border-radius:6px; padding:8px 12px; background:var(--cream); }
  .kwl-topic .k{ font-size:9.5pt; font-weight:800; color:var(--navy); text-transform:uppercase; letter-spacing:.04em; white-space:nowrap; }
  .kwl-topic .line{ flex:1 1 auto; border-bottom:2px solid var(--navy); height:18px; }
  /* three columns */
  .kwl-cols{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .kwl-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .kwl-col .well{ flex:1 1 auto; }
  .kwl-sub{ font-size:8pt; font-style:italic; color:#fff; opacity:.92; font-weight:600; text-transform:none; letter-spacing:0; }
  .band .kwl-sub{ display:block; margin-top:1px; }
  .band.gold .kwl-sub{ color:var(--navy); opacity:.8; }
"""

BODY = r"""
    <div class="prompt">Before you start, fill <b>K</b> and <b>W</b>. After learning, complete <b>L</b> &mdash; then compare it to what you wanted to know.</div>
    <div class="canvas">
      <div class="kwl">
        <div class="kwl-topic">
          <span class="k">Topic</span>
          <span class="line"></span>
        </div>
        <div class="kwl-cols">
          <div class="kwl-col">
            <div class="band navy" style="border-radius:6px 6px 0 0;">K &mdash; What I KNOW<span class="kwl-sub">(before &mdash; prior knowledge)</span></div>
            <div class="well lines" style="border-radius:0 0 6px 6px;"></div>
          </div>
          <div class="kwl-col">
            <div class="band red" style="border-radius:6px 6px 0 0;">W &mdash; What I WANT to know<span class="kwl-sub">(my questions)</span></div>
            <div class="well lines" style="border-radius:0 0 6px 6px;"></div>
          </div>
          <div class="kwl-col">
            <div class="band gold" style="border-radius:6px 6px 0 0;">L &mdash; What I LEARNED<span class="kwl-sub">(after &mdash; new learning)</span></div>
            <div class="well lines" style="border-radius:0 0 6px 6px;"></div>
          </div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="10_kwl_blank",
    title="K&#8209;W&#8209;L Chart",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Activate + track", "navy"), ("DOK 1&ndash;2 &middot; Metacognition", "skill")],
    why=("Use to <b>activate prior knowledge</b>, set a purpose for learning, and <b>track</b> new "
         "understanding across a lesson or unit. "
         "<span class='cite'>Self&#8209;regulation and monitoring one&rsquo;s own learning is a UDL principle "
         "(engagement).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill <b>K</b> as a whole class on chart paper first. Give question stems for <b>W</b>: &ldquo;I wonder ___&rdquo; / &ldquo;How does ___?&rdquo;",
        extend="In <b>L</b>, mark which of your <b>W</b> questions got answered &mdash; and write one new question you still have.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> what they know and learned in each column."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
