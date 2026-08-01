# -*- coding: utf-8 -*-
"""Blank reproducibles (content-agnostic; reusable in any unit/subject).
Same house style as the labeled organizers; students supply all content.
"""
from common import (venn2, venn3, tchart, matrix, cause_effect_split, timeline,
                    concept_web, main_idea, kwl, five_ws, problem_solution,
                    frayer, cer, hippo, tn_connection)

RE_KICK = "Reusable Organizer"
RE_ROLE = "Teacher Graphic Organizer Toolkit &middot; Reusable Reproducible"

def _o(slug, title, chips, why, bc, udl, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=RE_KICK, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=RE_ROLE)
    d.update(kw)
    return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."

ORGANIZERS = [
  _o("02_venn2_blank", "Venn Diagram &mdash; Compare Two",
     [("Venn &middot; Compare Two", "navy"), ("Marzano #1", "skill")],
     "Reach for a Venn when students compare <b>two</b> things: the overlap makes shared traits visible and "
     "sharpens the differences. <span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s highest-yield strategy.</span>",
     venn2("Write what makes each unique in its own circle &mdash; and what they <b>share</b> in the middle.",
           "Topic A: ____________", "write in the left circle", "Topic B: ____________", "write in the right circle",
           ["unique to A?", "only here?"], ["unique to B?", "only here?"], ["shared?", "true of both?"],
           cap_a="ONLY A", cap_b="ONLY B"),
     dict(scaffold="Give a word bank of traits to sort into the three regions before writing.",
          extend="Use the overlap to write one sentence explaining what the two share at a deeper level.",
          show=_SHOW)),

  _o("03_venn3_blank", "Venn Diagram &mdash; Compare Three",
     [("Venn &middot; Compare Three", "navy"), ("Synthesis", "skill")],
     "Use a three-circle Venn to compare <b>three</b> things at once and find what any two &mdash; or all three &mdash; share. "
     "<span class='cite'>Synthesizing across sources builds TN Practice SSP.03.</span>",
     venn3("Place each example in the right region. What belongs to one, to a pair, or to <b>all three</b>?",
           "Topic 1", "Topic 2", "Topic 3"),
     dict(scaffold="Start by placing three sure examples &mdash; one clearly in each &lsquo;only&rsquo; region &mdash; then work toward the overlaps.",
          extend="Explain why the center region (all three) is the hardest to fill &mdash; what must be true there?",
          show=_SHOW)),

  _o("04_tchart_blank", "T-Chart &mdash; Two Sides",
     [("T&#8209;Chart &middot; Two Sides", "navy"), ("DOK 2&ndash;3", "skill")],
     "A T&#8209;chart forces students to hold <b>two</b> sides at once &mdash; strengths/weaknesses, for/against, before/after. "
     "<span class='cite'>Weighing evidence on both sides supports argument (SSP.04).</span>",
     tchart("Gather evidence on each side &mdash; then use the bottom line to decide.",
            "SIDE A", "label this column", "SIDE B", "label this column",
            [("Point 1", "what belongs on this side?"), ("Point 2", "add your evidence")],
            [("Point 1", "what belongs on this side?"), ("Point 2", "add your evidence")],
            "<b>Weigh it:</b> Based on both columns, what do you conclude? ______________________________________________"),
     dict(scaffold="Fill one strong point on each side together, then students add two more per side.",
          extend="Write a one-paragraph judgment that uses evidence from <b>both</b> columns.",
          show=_SHOW)),

  _o("05_matrix_blank", "Comparison Matrix",
     [("Matrix &middot; Compare 3+", "navy"), ("Patterns", "skill")],
     "When students compare <b>three or more</b> cases against the same criteria, a matrix holds them to one yardstick "
     "so patterns pop. <span class='cite'>Structured comparison is Marzano&rsquo;s highest-yield move.</span>",
     matrix("Fill each cell, then read <b>down</b> each column and <b>across</b> each row for patterns.",
            [("Case 1", "name it", "navy"), ("Case 2", "name it", "red"), ("Case 3", "name it", "gold")],
            [("Criterion A", ["", "", ""]), ("Criterion B", ["", "", ""]), ("Criterion C", ["", "", ""])],
            "What pattern do you see across the cases? ______________________________________________"),
     dict(scaffold="Fill one full row together so students see how to compare across the same criterion.",
          extend="Add a fourth case or a fourth criterion and predict where it would fall.",
          show=_SHOW)),

  _o("06_causeeffect_blank", "Cause &amp; Effect",
     [("Cause &amp; Effect", "red"), ("SSP.05", "skill")],
     "Trace the chain of <b>why</b> something happened and what followed. <span class='cite'>Cause-and-effect reasoning "
     "builds TN Practice SSP.05.</span>",
     cause_effect_split("List what led up to the event on the left; list what it set in motion on the right.",
                        "THE EVENT", "name it", "What conditions made it happen?", "What did it lead to?",
                        "<b>So what?</b> Which single cause mattered most, and why? ______________________________________________"),
     dict(scaffold="Provide two causes and two effects on cards; students place and then add one of each.",
          extend="Draw an arrow from one effect to a new cause: how did one result trigger the next?",
          show=_SHOW)),

  _o("07_timeline_blank", "Timeline &mdash; Change Over Time",
     [("Timeline", "red"), ("SSP.05 Chronology", "skill")],
     "Put events <b>in order</b> to expose how one step made the next possible. <span class='cite'>Chronological "
     "reasoning is TN Practice SSP.05.</span>",
     timeline("Write each <b>date</b> on the left, then explain why the event mattered.",
              [("", "Event 1", "&mdash; what happened?", False),
               ("", "Event 2", "&mdash; what happened?", False),
               ("", "Event 3", "&mdash; what happened?", False),
               ("", "Event 4", "&mdash; why did it matter?", True)], blank_dates=True),
     dict(scaffold="Give the events on cards; students order them on the spine first, then add significance.",
          extend="Add arrows between nodes to show cause &amp; effect across the sequence.",
          show=_SHOW)),

  _o("08_conceptweb_blank", "Concept Web",
     [("Concept Web", "gold"), ("Schema", "skill")],
     "<b>Brainstorm</b> and connect ideas around one central concept &mdash; it surfaces prior knowledge and shows how "
     "ideas link to a hub. <span class='cite'>Building schema is a UDL comprehension support.</span>",
     concept_web("Write the central idea in the hub, then fill each bubble with a connected idea &mdash; and name the link.",
                 "CENTRAL IDEA", ["idea", "idea", "idea", "idea", "idea", "idea"]),
     dict(scaffold="Fill two bubbles together and model naming the link on the connecting line.",
          extend="Draw a line between two outer bubbles that connect to each other, not just to the hub.",
          show=_SHOW)),

  _o("09_mainidea_blank", "Main Idea &amp; Details",
     [("Main Idea &amp; Details", "navy"), ("Summarize", "skill")],
     "<b>Summarize</b> by separating the big idea from the details that support it. <span class='cite'>Distinguishing "
     "central idea from detail is core disciplinary literacy (SSP.02).</span>",
     main_idea("Write the main idea on top; add supporting details below; then sum it up in one line.",
               "MAIN IDEA", [("Detail", "evidence"), ("Detail", "evidence"), ("Detail", "evidence")],
               "<b>In one sentence:</b> the main idea matters because ______________________________________________"),
     dict(scaffold="Give the main idea and have students hunt only for the supporting details.",
          extend="Rank the details from strongest to weakest support and justify the top one.",
          show=_SHOW)),

  _o("10_kwl_blank", "K-W-L Chart",
     [("K&#8209;W&#8209;L", "gold"), ("Metacognition", "skill")],
     "<b>Activate</b> prior knowledge and <b>track</b> learning: what you Know, Want to know, and Learned. "
     "<span class='cite'>Setting a purpose and self-monitoring is a UDL self-regulation support.</span>",
     kwl("Fill <b>K</b> and <b>W</b> before you start; return to <b>L</b> after the lesson."),
     dict(scaffold="Offer sentence starters: &lsquo;I already know&hellip;&rsquo;, &lsquo;I want to know&hellip;&rsquo;, &lsquo;I learned&hellip;&rsquo;.",
          extend="In the L column, note one thing you still wonder &mdash; a question for further inquiry.",
          show=_SHOW)),

  _o("11_5ws_blank", "5 Ws",
     [("5 Ws", "gold"), ("SSP.01", "skill")],
     "Capture the <b>basics of an event</b> fast &mdash; who, what, when, where, why (and how). <span class='cite'>Collecting "
     "information from sources is TN Practice SSP.01.</span>",
     five_ws("Name the event or issue in the center, then answer each question around it."),
     dict(scaffold="Assign each question to a partner pair, then combine into one shared chart.",
          extend="Turn the &lsquo;Why&rsquo; and &lsquo;How&rsquo; answers into a single cause-and-effect sentence.",
          show=_SHOW)),

  _o("12_problemsolution_blank", "Problem &amp; Solution",
     [("Problem&ndash;Solution", "red"), ("Decision", "skill")],
     "<b>Weigh options</b> against a defined problem and decide with evidence, naming each trade-off. "
     "<span class='cite'>Devising and defending solutions builds SSP.04.</span>",
     problem_solution("State the problem, sketch two possible solutions with their trade-offs, then decide.",
                      "what is the problem, exactly?", ["______________", "______________"],
                      "<b>Best solution:</b> ____________ &mdash; <b>because</b> ____________________________________________"),
     dict(scaffold="Provide one worked solution with its trade-off; students generate the second.",
          extend="Add a third option and rank all three by which trade-off is easiest to accept.",
          show=_SHOW)),

  _o("13_frayer_blank", "Frayer Model &mdash; Key Term",
     [("Frayer", "navy"), ("Vocabulary", "skill")],
     "<b>Learn a key term</b> deeply: definition, characteristics, examples, and non-examples &mdash; not a definition "
     "forgotten by Friday. <span class='cite'>Robust vocabulary work is Marzano&rsquo;s six-step method.</span>",
     frayer("Write the term in the center, then complete all four corners.", term_line="write the term"),
     dict(scaffold="Give the definition; students generate the examples and non-examples.",
          extend="Write one sentence that uses the term correctly in a new context.",
          show=_SHOW)),

  _o("14_cer_blank", "Claim &ndash; Evidence &ndash; Reasoning",
     [("C&#8209;E&#8209;R", "navy"), ("SSP.04 Argument", "skill")],
     "Turn an opinion into a <b>defensible argument</b>: a claim, the evidence for it, and the reasoning that ties them. "
     "<span class='cite'>Constructing evidence-based arguments is TN Practice SSP.04.</span>",
     cer("Answer the question with a claim, back it with evidence, then explain your reasoning.",
         "one clear sentence", "quote / fact 1 &hellip; quote / fact 2", "how does the evidence prove the claim?"),
     dict(scaffold="Provide a claim stem and one piece of evidence; students supply the reasoning.",
          extend="Add a counter-claim and one sentence explaining why your evidence still wins.",
          show=_SHOW)),

  _o("15_hippo_blank", "HIPPO &mdash; Source Analysis",
     [("HIPPO", "red"), ("SSP.02", "skill")],
     "Give students a historian&rsquo;s routine for <b>interrogating a source</b>: context, audience, point of view, "
     "purpose, outside information. <span class='cite'>Critically examining sources is TN Practice SSP.02.</span>",
     hippo("Record the source, then work through each element to analyze it."),
     dict(scaffold="Model H and I together on a shared source before students do P, P, O.",
          extend="Use the O row to connect this source to another document you have studied.",
          show=_SHOW)),

  _o("16_tn_connection", "Tennessee Connection",
     [("&#9733; TN Connection", "tn"), ("Signature Move", "skill")],
     "Connect the <b>nation</b> to <b>Tennessee</b> &mdash; local ties make national civics stick. This is our signature move. "
     "<span class='cite'>Relevance and connection to students&rsquo; lives is a UDL engagement principle.</span>",
     tn_connection("Note the national idea on the left and its Tennessee counterpart on the right, then link them.",
                   "NATIONAL", "TENNESSEE"),
     tn=True,
     udl=dict(scaffold="Give the national example; students find the Tennessee counterpart with a provided source.",
              extend="Explain how the Tennessee case is similar to <em>and</em> different from the national one.",
              show=_SHOW)),
]
