# -*- coding: utf-8 -*-
"""Author Unit 4 — Executive Branch (GC.16-GC.18) content source.
Schema parity with Units 1-3. Verbatim cited sources (Constitution Art. II;
Federalist 68). CFU keys distributed. UDL 3.0 + MTSS framework embedded inline.
Literal '&' in content (deck escapes once). Brand: Government Hack.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "unit4_content.json")

unit = {
  "code": "Unit 4",
  "title": "The Executive Branch",
  "course_name": "Foundations of Constitutional Government",
  "standards_range": "GC.16–GC.18",
  "quarter": 2,
  "suggested_days": "8–10",
  "essential_question": "How much power should one person hold — and how is the presidency kept in check?",
  "publisher": "TroopToTeacher Technologies LLC",
  "footer": "Foundations of Constitutional Government · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards (GC) · Supplemental under TCA § 49-6-2202(a)(3)",
  "perspectives_title": "How Strong Should the President Be? Perspectives on Executive Power",
  "perspectives_intro": "This section weighs a central tension of the office: energy in the executive versus the danger of one person holding too much power. It is Government Hack–authored instructional synthesis grounded in this unit's sourced record — not a primary source.",
  "perspectives": [
    ["Energy in the Executive",
     "Hamilton argued a single, energetic executive is essential to act decisively in war and crisis (Federalist 68/70; connects to GC.16)."],
    ["Fear of a King",
     "Anti-Federalists worried the presidency could become an elected monarchy — a fear that shaped term limits and impeachment (GC.16, connects to Unit 1 GC.04)."],
    ["The Bureaucracy",
     "Millions of federal employees in departments and agencies carry out the law day to day, raising questions about who really controls policy (GC.17)."],
    ["The Electoral College",
     "The winner of the most national votes has sometimes lost the presidency, sparking a lasting debate over how we choose a President (GC.18)."]
  ],
  "tn_connection_label": "TENNESSEE CONNECTION",
  "tn_connection": "Tennessee has sent three of its own to the presidency: Andrew Jackson, James K. Polk, and Andrew Johnson all built their careers in Tennessee before reaching the White House. Andrew Johnson's presidency ended in the first impeachment trial of a President — a direct test of the checks on executive power studied in this unit (GC.16).",
  "tn_connection_task": "Three Presidents called Tennessee home. Choose one — Jackson, Polk, or Johnson — and investigate one power of the presidency they used or tested, and record what you find with a source.",
  "course_short": "Government & Civics",
  "cover_era": "1787 · 1788 · 1868",
  "cover_title_lines": ["THE EXECUTIVE", "BRANCH"],
  "cover_image": "GC.16_washington-portrait.jpg",
  "brand": "Government Hack",
  "frameworks": {
    "udl_designed_in": {
      "engagement": ["7.1 choice", "7.2 relevance (TN presidents)", "7.3 play (Cabinet Match)", "7.4 neutral framing", "8.1 I-can goals", "8.2 scaffold+extend", "8.4 belonging (multiple perspectives)", "8.5 rationale feedback", "9.1 belief-check", "9.3 reflection", "9.4 discussion norms"],
      "representation": ["1.1 print+digital", "1.2 read-aloud+image", "1.3 multiple perspectives", "2.1 Frayer", "2.2 pronunciation", "2.3 EN/ES", "2.4 neutral language", "2.5 multimedia", "3.1 K-W-L/hooks", "3.2 concept web/EQ", "3.4 spiral to Units 1-3"],
      "action_expression": ["4.1 write/say/draw/build", "4.2 alt text/AT", "5.1 multiple media", "5.2 organizer toolkit", "5.3 graduated support", "5.4 access-format items", "6.1 goals", "6.3 organizers", "6.4 CFU+analytics", "6.5 access not tracking"]
    },
    "mtss": {"tier1": "UDL core for all", "tier2": "scaffold column + support-form items", "tier3": "teacher reteach + most-supported modes", "progress": "per-standard CFU + mastery analytics"}
  },
  "belief_check": "Predict first: Should the candidate with the most votes nationwide always become President? Write your gut answer now — you'll test it against the Electoral College and Hamilton's Federalist 68.",
  "play": {
    "name": "Cabinet Match",
    "how": "2-minute game (GC.17). Read a real problem — a disease outbreak, a border dispute, a counterfeit bill, a civil-rights complaint — and race to name the department that handles it (State, Treasury, Defense, Justice, Education). Students feel how the executive branch divides the work of running the country."
  },
  "spiral": [
    {"from": "GC.16", "to": "Unit 3 (GC.15, Senate confirmation)", "link": "The Senate that confirms the President's appointments is the same power you studied in the Legislative unit — checks & balances in action."},
    {"from": "GC.16", "to": "Unit 1 (GC.06, checks & balances)", "link": "The veto, impeachment, and appointment checks all come from the separation of powers you learned in Foundations."},
    {"from": "GC.18", "to": "Unit 1 (GC.04, the Great Compromise)", "link": "The Electoral College's mix of population and state equality echoes the same large-vs-small-state bargain from the Convention."}
  ],
  "discussion_norms": {
    "name": "Executive Debate",
    "norms": ["Cite the clause — point to Article II before you argue.", "Separate the power from the person who used it.", "Disagree with the argument, not the classmate.", "One voice at a time; make room for the quiet voice."]
  }
}

def std(title, tn, ican, vocab, sources, cfu, auth, target, learning_targets,
        criteria, cues, lenses, dim_map, hook, civic_label, ssp_focus, ref):
    return dict(title=title, tn=tn, ican=ican, vocab=vocab, sources=sources, cfu=cfu,
                auth=auth, std_source="TN Academic Standards — United States Government & Civics (GC), verbatim",
                target=target, learning_targets=learning_targets, criteria=criteria, cues=cues,
                lenses=lenses, dim_map=dim_map, hook=hook, civic_label=civic_label,
                ssp_focus=ssp_focus, ref=ref)

CRIT = [
  "state the key idea of the standard in your own words with an accurate example;",
  "use at least one primary or secondary source to support your explanation;",
  "connect the idea to how executive power is used or checked today.",
]
CUES = ["Key idea of this standard?", "One source that supports it?",
        "One check on executive power?", "Key terms →"]
REF = {"vocab": 3, "dt": "4–6", "source": 7, "persp": 7, "progress": 8, "range": "2–8"}
S = {}

S["GC.16"] = std(
  title="Article II & the Presidency",
  tn="Analyze Article II of the U.S. Constitution as it relates to the executive branch, including: appointments; Commander-in-chief of the military; eligibility for office; executive orders; length of term (22nd Amendment); oath of office; powers of the president; succession (25th Amendment); treaties. (H)",
  ican="I can analyze Article II — the qualifications, powers, roles, term, and succession of the President.",
  vocab=[
    {"term": "Commander-in-Chief", "say": "kuh-MAN-der in cheef", "es": "comandante en jefe",
     "def": "The President's role as civilian head of the U.S. armed forces, ensuring the military answers to elected leadership."},
    {"term": "Executive Order", "say": "eg-ZEK-yuh-tiv OR-der", "es": "orden ejecutiva",
     "def": "A directive from the President that manages the operations of the federal government and has the force of law, though it cannot override the Constitution or statute."},
    {"term": "Succession", "say": "suk-SESH-un", "es": "sucesión presidencial",
     "def": "The order set by the Constitution (25th Amendment) for who becomes President if the office is vacated — starting with the Vice President."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article II, Section 1 (Oath)", "who": "Constitutional Convention", "date": "1787",
     "quote": "I do solemnly swear (or affirm) that I will faithfully execute the Office of President of the United States, and will to the best of my Ability, preserve, protect and defend the Constitution of the United States.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "U.S. Constitution, Article II, Section 2", "who": "Constitutional Convention", "date": "1787",
     "quote": "The President shall be Commander in Chief of the Army and Navy of the United States… he shall have Power, by and with the Advice and Consent of the Senate, to make Treaties.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
  ],
  cfu={"dok": 2, "stem": "Which check on the President is built into the treaty and appointment powers of Article II?",
       "options": {"A": "The President may act only during wartime",
                   "B": "The Supreme Court must approve every treaty",
                   "C": "The Senate must give its 'Advice and Consent'",
                   "D": "The House must sign every appointment"},
       "key": "C",
       "why": "DOK 2: Article II gives the President power to make treaties and appointments only 'by and with the Advice and Consent of the Senate' — a legislative check on executive power."},
  auth={
    "close": "Article II creates a single President — the head of the executive branch — and lists both the powers and the limits of the office. To serve, a President must be a natural-born citizen, at least 35, and a U.S. resident for 14 years, and must swear the oath to 'preserve, protect and defend the Constitution.' The powers are real: the President is Commander-in-Chief of the military (a civilian in charge of the armed forces), makes treaties and appointments — but only with the Senate's 'Advice and Consent' — and can issue executive orders to direct the government. Yet every power is checked. Terms are limited to two by the 22nd Amendment; the 25th Amendment sets the order of succession if the office is vacated; and Congress can impeach and remove a President. The office is powerful by design, and limited by design.",
    "tdq": [
      "What does the President's oath promise, and why put that promise in the Constitution?",
      "How do the Senate's 'Advice and Consent' powers check the President?",
      "How do the 22nd and 25th Amendments limit or stabilize the presidency?"],
    "frayer": ["Commander-in-Chief", "Executive Order"],
    "quiz": [{"id": "u4-gc16-dok1-1", "dok": 1,
              "stem": "The 22nd Amendment limits a President to how many elected terms?",
              "opts": {"A": "One", "B": "Two", "C": "Three", "D": "No limit"}, "key": "B"}],
    "cer": "Claim + Evidence + Reasoning: Is the President's power well balanced by the checks in Article II, or does one branch hold too much? Defend your claim with evidence."},
  target="I can analyze Article II — the qualifications, powers, roles, term, and succession of the President.",
  learning_targets="List the formal qualifications to serve as President. Explain the significance of a civilian leader of the military and the impact of the War Powers Act of 1973. Describe the primary duties and powers of the Executive Branch as outlined in Article II. Identify the eight official and unofficial roles of the President including: Commander-in-Chief, Chief of State, Chief Executive, Chief Diplomat, Chief Administrator, Chief Legislator, Chief Citizen, and Chief of Party. Explain presidential succession and disability based on the 25th amendment.",
  criteria=CRIT, cues=CUES, lenses="History (H)",
  dim_map={"H": "How the presidency's powers and limits have been tested across U.S. history."},
  hook="One person commands the world's most powerful military — yet cannot make a treaty or hire a cabinet officer alone. Who holds the leash?",
  civic_label="EXECUTIVE POWER", ssp_focus="SSP.02", ref=REF)

S["GC.17"] = std(
  title="Departments of the Executive Branch",
  tn="Identify major departments of the executive branch, including: Defense; Education; Justice; State; Treasury. (—)",
  ican="I can identify the major executive departments and describe what each one does to carry out the law.",
  vocab=[
    {"term": "Bureaucracy", "say": "byoo-ROK-ruh-see", "es": "burocracia",
     "def": "The departments, agencies, and employees of the executive branch that carry out and administer federal laws and programs day to day."},
    {"term": "Cabinet", "say": "KAB-ih-net", "es": "gabinete",
     "def": "The group of the heads (secretaries) of the executive departments who advise the President."},
    {"term": "Iron Triangle", "say": "EYE-urn TRY-ang-gul", "es": "triángulo de hierro",
     "def": "The close relationship among a federal agency, a congressional committee, and interest groups that shapes policy in a specific area."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article II, Section 2", "who": "Constitutional Convention", "date": "1787",
     "quote": "…he may require the Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject relating to the Duties of their respective Offices.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "U.S. Constitution, Article II, Section 3 (Take Care Clause)", "who": "Constitutional Convention", "date": "1787",
     "quote": "…he shall take Care that the Laws be faithfully executed.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
  ],
  cfu={"dok": 2, "stem": "Which executive department is chiefly responsible for foreign policy and relations with other countries?",
       "options": {"A": "The Department of the Treasury",
                   "B": "The Department of State",
                   "C": "The Department of Defense",
                   "D": "The Department of Education"},
       "key": "B",
       "why": "DOK 2: The Department of State manages diplomacy and foreign relations; Treasury handles money, Defense the military, Justice the law, and Education federal school policy."},
  auth={
    "close": "The Constitution makes the President responsible to 'take Care that the Laws be faithfully executed' — but no one person can run a country of over 330 million people. So the executive branch is organized into departments, each led by a secretary who sits in the President's Cabinet. Five of the major departments show the range of the job: State manages foreign policy and diplomacy; Treasury handles money, taxes, and the debt; Defense runs the armed forces; Justice enforces federal law and runs the courts and FBI; and Education sets federal school policy and funding. Together these departments and their agencies form the bureaucracy — the millions of federal workers who carry out the law day to day. Because agencies, congressional committees, and interest groups often work closely together on the same issues, analysts call that relationship an 'iron triangle.'",
    "tdq": [
      "What does the Take Care Clause require of the President, and why does that create a need for departments?",
      "Match each of the five major departments to the kind of problem it handles.",
      "What is an 'iron triangle,' and how might it shape policy?"],
    "frayer": ["Bureaucracy", "Cabinet"],
    "quiz": [{"id": "u4-gc17-dok1-1", "dok": 1,
              "stem": "The heads of the executive departments who advise the President make up the:",
              "opts": {"A": "Cabinet", "B": "Senate", "C": "Electoral College", "D": "Supreme Court"}, "key": "A"}],
    "cer": "Claim + Evidence + Reasoning: Which executive department has the greatest effect on your daily life? Defend your claim with evidence about what it does."},
  target="I can identify the major executive departments and describe what each one does to carry out the law.",
  learning_targets="List and describe the duties of the agencies used by the president in the executive branch. Identify historical policy changes in the major departments of the executive branch. Explain the relationship between the bureaucracy, standing committees, and interest groups and why people use the term 'iron triangle' when referring to them.",
  criteria=CRIT, cues=CUES, lenses="Civic Structure",
  dim_map={"P": "How the executive branch is organized to carry out the law at scale."},
  hook="An outbreak, a counterfeit bill, a border dispute, a school-funding fight — four problems, four different departments. Do you know which handles which?",
  civic_label="THE BUREAUCRACY", ssp_focus="SSP.01", ref=REF)

S["GC.18"] = std(
  title="The Electoral College",
  tn="Explain the Electoral College system and compare and contrast arguments for and against it. (G, H)",
  ican="I can explain how the Electoral College works and weigh the arguments for and against it.",
  vocab=[
    {"term": "Electoral College", "say": "ee-LEK-tor-ul KOL-ij", "es": "Colegio Electoral",
     "def": "The body of electors — one per senator and representative — that formally elects the President; a candidate needs a majority (270 of 538)."},
    {"term": "Elector", "say": "ee-LEK-ter", "es": "elector",
     "def": "A person chosen by each state to cast that state's official vote for President based on the state's popular vote."},
    {"term": "Winner-Take-All", "say": "WIN-er take all", "es": "el ganador se lleva todo",
     "def": "The practice, used by most states, of awarding all of a state's electoral votes to whichever candidate wins that state's popular vote."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article II, Section 1", "who": "Constitutional Convention", "date": "1787",
     "quote": "Each State shall appoint, in such Manner as the Legislature thereof may direct, a Number of Electors, equal to the whole Number of Senators and Representatives to which the State may be entitled in the Congress.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "Federalist No. 68", "who": "Alexander Hamilton (Publius)", "date": "1788",
     "quote": "It was desirable, that the sense of the people should operate in the choice of the person to whom so important a trust was to be confided.",
     "repo": "The Avalon Project, Yale Law School", "url": "https://avalon.law.yale.edu/18th_century/fed68.asp"},
  ],
  cfu={"dok": 3, "stem": "Why can a candidate win the national popular vote yet still lose the presidency?",
       "options": {"A": "Because the Supreme Court chooses the President",
                   "B": "Because Congress ignores the popular vote entirely",
                   "C": "Because the President is chosen by the Cabinet",
                   "D": "Because most states award all their electoral votes winner-take-all, so the Electoral College total can differ from the national vote"},
       "key": "D",
       "why": "DOK 3: The winner is decided by electoral votes, not the national popular vote; because most states use winner-take-all, a candidate can gather more electoral votes while another wins more total votes nationwide."},
  auth={
    "close": "Americans do not elect the President directly. Instead, each state appoints electors — equal to its number of senators plus representatives — and those electors formally choose the President, with 270 of 538 needed to win. Alexander Hamilton defended the design in Federalist 68, arguing it let 'the sense of the people' operate while filtering the choice through informed electors. Because most states award all their electors winner-take-all, a candidate can win the national popular vote and still lose the Electoral College — which has happened and fuels an ongoing debate. Supporters say the system protects smaller states and forces national campaigns; critics say it can override the popular will and focuses attention on a few 'swing' states. If no candidate wins a majority, the House chooses the President. Whatever one concludes, the Electoral College shows the Framers' habit of balancing popular voice against structure.",
    "tdq": [
      "How does a state decide its number of electors, according to Article II?",
      "What argument does Hamilton make for the Electoral College in Federalist 68?",
      "State one argument for and one against the Electoral College, and say which you find stronger."],
    "frayer": ["Electoral College", "Winner-Take-All"],
    "quiz": [{"id": "u4-gc18-dok1-1", "dok": 1,
              "stem": "How many electoral votes are needed to win the presidency?",
              "opts": {"A": "218", "B": "270", "C": "435", "D": "538"}, "key": "B"}],
    "cer": "Claim + Evidence + Reasoning: Should the United States keep, reform, or replace the Electoral College? Defend your claim with an argument on each side."},
  target="I can explain how the Electoral College works and weigh the arguments for and against it.",
  learning_targets="Explain how each state's number of Electoral College electors is determined and explain the reasoning behind the establishment of the Electoral College including: maintaining federalism; encourage national campaigns; prevent system fraud; prevent majority-rule tyranny. Explain how population shifts affect presidential elections and electoral votes. Explain how the President is selected when there is no candidate with a majority of electoral votes.",
  criteria=CRIT, cues=CUES, lenses="Geography (G) · History (H)",
  dim_map={"G": "How electoral votes map onto states and 'swing states' shape campaigns.",
           "H": "How the Electoral College has produced popular-vote/electoral-vote splits over time."},
  hook="You never actually vote for President — you vote for someone who does. Meet the electors, and decide if the system still makes sense.",
  civic_label="ELECTIONS", ssp_focus="SSP.04", ref=REF)

order = ["GC.16", "GC.17", "GC.18"]
doc = {"unit": unit, "order": order, "standards": S}
blob = json.dumps(doc, ensure_ascii=False)
assert "W" + "CS" not in blob and "History Hack" not in blob, "leak"
json.dump(doc, open(OUT, "w"), ensure_ascii=False, indent=1)
print("wrote", OUT, "| CFU keys:", {c: S[c]["cfu"]["key"] for c in order})
