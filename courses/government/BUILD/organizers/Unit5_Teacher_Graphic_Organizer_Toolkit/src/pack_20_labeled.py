# -*- coding: utf-8 -*-
"""Unit 5 labeled best-fit organizers (GC.19-GC.22).
Best-fit: GC.19 Main Idea & Details (Article III), GC.20 Sequence (nomination ->
confirmation), GC.21 Cause & Effect (Marbury -> judicial review), GC.22 T-chart
(judicial activism vs. restraint). Verbatim topics; writable areas light.
"""
from common import main_idea, cause_effect_chain, tchart

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role); d.update(kw); return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; {std} (labeled)"
def KICK(std): return f"Unit 5 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.19 — Article III -> Main Idea & Details
  _o("20_gc19_mainidea", "Article III &mdash; The Judicial Power",
     KICK("GC.19"),
     [("Main Idea &amp; Details", "navy"), ("DOK 2 &middot; Summarize", "skill")],
     "Article III sketches the judicial branch in a few lines. Pulling out its key features shows students how the "
     "Framers protected judges&rsquo; independence. "
     "<span class='cite'>Separating central idea from supporting detail builds disciplinary literacy (SSP.02).</span>",
     main_idea(
       "Main idea: what Article III establishes. Fill each column with the detail from the text.",
       "ARTICLE III &mdash; the judicial power of the United States",
       [("One Supreme Court", "what does Congress get to create?"),
        ("&lsquo;Good Behaviour&rsquo; tenure", "how does life tenure protect independence?"),
        ("Jurisdiction", "original vs. appellate &mdash; how do cases arrive?")],
       "<b>In one sentence:</b> How does Article III keep judges independent of politics? ______________________________________________"),
     dict(scaffold="Give the three details as cards; students match each to the right column first.",
          extend="Explain how a federal judge is removed, and why it is so rare.", show=_SHOW),
     ROLE("GC.19")),

  # GC.20 — Selection & confirmation -> Sequence
  _o("21_gc20_sequence", "Seating a Supreme Court Justice",
     KICK("GC.20"),
     [("Sequence &middot; Process Flow", "red"), ("SSP.05 &middot; DOK 2", "skill")],
     "A justice reaches the bench through a shared process no one branch controls. Mapping the steps shows students "
     "exactly where the President&rsquo;s power ends and the Senate&rsquo;s begins. "
     "<span class='cite'>Sequencing a process builds chronological reasoning (SSP.05).</span>",
     cause_effect_chain(
       "Work down the process. Note who controls each step.",
       [("A seat opens", "&mdash; what creates a Supreme Court vacancy?"),
        ("The President NOMINATES", "&mdash; how does the President choose a nominee?"),
        ("Senate Judiciary Committee HEARINGS", "&mdash; what does the committee ask the nominee?"),
        ("The full Senate CONFIRMS (majority vote)", "&mdash; the &lsquo;Advice and Consent&rsquo; check &mdash; then the justice is seated for life")],
       tail=('<div class="midbar" style="margin-top:8px"><b>Why so high-stakes?</b> A justice can serve for decades &mdash; '
             'how does that raise the stakes of one confirmation? ____________________________________</div>')),
     dict(scaffold="Provide the four steps on cards; students order them, then label who controls each.",
          extend="Explain why a single appointment can shape the law long after a President leaves office.", show=_SHOW),
     ROLE("GC.20")),

  # GC.21 — Marbury -> Cause & Effect
  _o("22_gc21_causeeffect", "How Marbury Created Judicial Review",
     KICK("GC.21"),
     [("Cause &amp; Effect &middot; Chain", "red"), ("SSP.02 &middot; DOK 3", "skill")],
     "The Court claimed its greatest power in a single 1803 case. Tracing the chain of Marshall&rsquo;s reasoning shows "
     "students where judicial review actually comes from. "
     "<span class='cite'>Examining a source&rsquo;s reasoning builds TN Practice SSP.02.</span>",
     cause_effect_chain(
       "Work down Marshall&rsquo;s reasoning in Marbury v. Madison (1803).",
       [("The dispute (1803)", "&mdash; a law and the Constitution seemed to conflict &mdash; which one wins?"),
        ("Marshall&rsquo;s reasoning", "&mdash; &lsquo;it is&hellip; the province and duty of the judicial department to say what the law is&rsquo; &mdash; what does he claim?"),
        ("The rule", "&mdash; &lsquo;a law repugnant to the constitution is void&rsquo; &mdash; what happens to a conflicting law?"),
        ("The effect: JUDICIAL REVIEW", "&mdash; how did this make the courts a check on the other branches?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>So what?</b> The Constitution never lists this power &mdash; '
             'was Marshall right to claim it? ____________________________________</div>')),
     dict(scaffold="Give the four steps on cards; students order Marshall&rsquo;s logic before writing effects.",
          extend="Explain how judicial review connects to the checks &amp; balances you studied in Unit 1.", show=_SHOW),
     ROLE("GC.21")),

  # GC.22 — Activism vs restraint -> T-chart
  _o("23_gc22_tchart", "Judicial Activism <span style='font-family:Georgia;font-style:italic;font-size:15pt'>vs.</span> Restraint",
     KICK("GC.22"),
     [("T&#8209;Chart &middot; Two Approaches", "navy"), ("SSP.04 &middot; DOK 3", "skill")],
     "How boldly should judges use their power? The standard asks students to weigh two philosophies. A T&#8209;chart "
     "collects evidence for each before a reasoned judgment. "
     "<span class='cite'>Constructing arguments from evidence builds TN Practice SSP.04.</span>",
     tchart("Sort each idea or case, then decide which approach the courts should favor.",
            "JUDICIAL ACTIVISM", "living Constitution; willing to act", "JUDICIAL RESTRAINT", "original intent; defer to elected branches",
            [("View of the Constitution", "a &lsquo;living document&rsquo; that adapts?"),
             ("Willingness to strike laws", "more willing to overturn a law?"),
             ("An example ruling", "a case that fits this approach?")],
            [("View of the Constitution", "read by its &lsquo;original intent&rsquo;?"),
             ("Deference", "defer to Congress &amp; precedent?"),
             ("An example ruling", "a case that fits this approach?")],
            "<b>Your verdict:</b> Which approach should the Court favor &mdash; <b>because</b> ____________________________________________"),
     dict(scaffold="Sort a set of statement cards into Activism vs. Restraint before writing.",
          extend="Honors: place the Warren, Burger, Rehnquist, or Roberts Court on the activism&ndash;restraint spectrum with evidence.",
          show=_SHOW),
     ROLE("GC.22")),
]
