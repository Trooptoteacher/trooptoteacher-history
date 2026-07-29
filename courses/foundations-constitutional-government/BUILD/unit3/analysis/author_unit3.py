# -*- coding: utf-8 -*-
"""Author Unit 3 — Legislative Branch (GC.35, GC.10-GC.15) content source.
Full schema parity with Units 1-2 (same builders consume it). Every primary-
source quotation is verbatim from a cited repository (Constitution / U.S.
Reports, verified). CFU keys distributed. UDL 3.0 + MTSS framework embedded
inline (frameworks / belief_check / play / spiral / discussion_norms), per the
design contract. Brand: Government Hack. No source-district references.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "unit3_content.json")

unit = {
  "code": "Unit 3",
  "title": "The Legislative Branch",
  "course_name": "Foundations of Constitutional Government",
  "standards_range": "GC.35 · GC.10–GC.15",
  "quarter": 1,
  "suggested_days": "15–17",
  "essential_question": "How does Congress represent the people — and where do its powers begin and end?",
  "publisher": "TroopToTeacher Technologies LLC",
  "footer": "Foundations of Constitutional Government · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards (GC) · Supplemental under TCA § 49-6-2202(a)(3)",
  "perspectives_title": "Who Gets Represented? Perspectives on Congress",
  "perspectives_intro": "This section examines how representation is built and contested: which places and people a legislature counts, and who draws the lines. It is Government Hack–authored instructional synthesis grounded in this unit's sourced record — not a primary source.",
  "perspectives": [
    ["Large vs. Small States",
     "The Great Compromise gave every state two senators but seats the House by population — a bargain carried straight from the Constitutional Convention (connects to GC.10, GC.04)."],
    ["Urban vs. Rural Voters",
     "For decades Tennessee's unequal districts made a rural vote worth many times an urban one, until Baker v. Carr forced 'one person, one vote' (GC.11)."],
    ["Majority vs. Minority Power",
     "Senate rules like the filibuster let a minority slow or block the majority; House rules move faster — the same bill can face very different odds (GC.13)."],
    ["Who Draws the Lines",
     "Whoever controls redistricting can shape outcomes through gerrymandering, changing who wins without changing a single vote (GC.11)."]
  ],
  "tn_connection_label": "TENNESSEE CONNECTION",
  "tn_connection": "One person, one vote started in Tennessee. Charles Baker, a voter from Shelby County (Memphis), sued because the state had not redrawn its legislative districts since 1901 — leaving a Memphis vote worth about one-eighth of a rural vote. In Baker v. Carr (1962) the Supreme Court ruled that federal courts could hear redistricting cases, opening the door to the 'one person, one vote' standard (GC.11).",
  "tn_connection_task": "Tennessee's own unequal districts sparked a national rule. Investigate your current Tennessee state legislative district or U.S. House district — who represents it, and roughly how many people live there — and record what you find.",
  "course_short": "Government & Civics",
  "cover_era": "1787 · 1819 · 1962",
  "cover_title_lines": ["THE LEGISLATIVE", "BRANCH"],
  "cover_image": "GC.12_us-capitol.jpg",
  "brand": "Government Hack",
  "frameworks": {
    "udl_designed_in": {
      "engagement": ["7.1 choice", "7.2 relevance (Baker v. Carr, TN)", "7.3 play (Redistrict It!)", "7.4 neutral framing", "8.1 I-can goals", "8.2 scaffold+extend", "8.4 belonging (who gets represented)", "8.5 rationale feedback", "9.1 belief-check", "9.3 reflection", "9.4 discussion norms"],
      "representation": ["1.1 print+digital", "1.2 read-aloud+image", "1.3 multiple perspectives", "2.1 Frayer", "2.2 pronunciation", "2.3 EN/ES", "2.4 neutral language", "2.5 multimedia", "3.1 K-W-L/hooks", "3.2 concept web/EQ", "3.4 spiral to Units 1-2"],
      "action_expression": ["4.1 write/say/draw/build", "4.2 alt text/AT", "5.1 multiple media", "5.2 organizer toolkit", "5.3 graduated support", "5.4 access-format items", "6.1 goals", "6.3 organizers", "6.4 CFU+analytics", "6.5 access not tracking"]
    },
    "mtss": {"tier1": "UDL core for all", "tier2": "scaffold column + support-form items", "tier3": "teacher reteach + most-supported modes", "progress": "per-standard CFU + mastery analytics"}
  },
  "belief_check": "Predict first: Should a vote in the city count the same as a vote in the countryside? Write your gut answer now — you'll test it against Tennessee's own Baker v. Carr and the idea of 'one person, one vote.'",
  "play": {
    "name": "Redistrict It!",
    "how": "4-minute map game (GC.11). Give teams a small grid 'state' of colored voters and ask them to draw the district lines so their side wins. Reveal how the same voters produce different winners depending only on where the lines go — gerrymandering, felt in four minutes."
  },
  "spiral": [
    {"from": "GC.10", "to": "Unit 1 (GC.04, the Great Compromise)", "link": "Two senators per state + a House by population is the Great Compromise you studied in Foundations, now in action."},
    {"from": "GC.13", "to": "Unit 1 (GC.06, checks & balances)", "link": "The presidential veto and the override are checks & balances — retrieve the principle, then watch a bill run the gauntlet."},
    {"from": "GC.14", "to": "Unit 2 (GC.34, participation)", "link": "Contacting or petitioning your representative is the participation you practiced in Unit 2 — now you know who to contact."}
  ],
  "discussion_norms": {
    "name": "Legislative Debate",
    "norms": ["Cite the clause — point to Article I before you argue.", "Represent a position fairly before you rebut it.", "Disagree with the rule, not the person.", "One voice at a time; make room for the quiet voice."]
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
  "connect the idea to how Congress represents people or uses its powers today.",
]
CUES = ["Key idea of this standard?", "One source that supports it?",
        "One effect on representation or lawmaking?", "Key terms →"]
REF = {"vocab": 3, "dt": "4–6", "source": 7, "persp": 7, "progress": 8, "range": "2–8"}
S = {}

S["GC.35"] = std(
  title="Citizenship & Naturalization",
  tn="Explain the requirements to be considered a natural-born U.S. citizen, and describe the process of naturalization, including the knowledge required by the Naturalization Test. (T)",
  ican="I can explain who is a natural-born U.S. citizen and describe how a foreign-born person becomes a naturalized citizen.",
  vocab=[
    {"term": "Natural-Born Citizen", "say": "NATCH-rul born SIT-ih-zen", "es": "ciudadano por nacimiento",
     "def": "A person who is a U.S. citizen at birth — by being born in the U.S. or, in most cases, to U.S.-citizen parents; a requirement to be President."},
    {"term": "Naturalization", "say": "natch-er-uh-lih-ZAY-shun", "es": "naturalización",
     "def": "The legal process by which a foreign-born person becomes a U.S. citizen, including residency, an application, an interview, the Naturalization Test, and an Oath of Allegiance."},
    {"term": "Naturalization Test", "say": "test", "es": "examen de naturalización",
     "def": "A civics and English test applicants must pass to naturalize, drawn from 100 questions about U.S. history and government."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article I, Section 8", "who": "Constitutional Convention", "date": "1787",
     "quote": "The Congress shall have Power… To establish an uniform Rule of Naturalization.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "U.S. Constitution, Amendment XIV, Section 1", "who": "39th U.S. Congress", "date": "1868",
     "quote": "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/amendments-11-27"},
  ],
  cfu={"dok": 2, "stem": "Which power does the Constitution give to Congress regarding citizenship?",
       "options": {"A": "To choose which states may grant citizenship",
                   "B": "To deny citizenship to anyone born in the U.S.",
                   "C": "To establish a uniform rule of naturalization",
                   "D": "To require every citizen to pass the Naturalization Test"},
       "key": "C",
       "why": "DOK 2: Article I, Section 8 gives Congress the power 'to establish an uniform Rule of Naturalization,' so the rules for becoming a citizen are the same nationwide."},
  auth={
    "close": "There are two paths to U.S. citizenship. A natural-born citizen is a citizen at birth — generally by being born in the United States (as the 14th Amendment guarantees) or, in most cases, to U.S.-citizen parents. Only a natural-born citizen may become President. A foreign-born person becomes a citizen through naturalization, a process Congress controls under its Article I power to set 'an uniform Rule of Naturalization.' Applicants must meet residency requirements, apply, be interviewed, pass the Naturalization Test on U.S. civics and English, and take an Oath of Allegiance. The 100-question test asks exactly the kind of civics this course teaches — proof that citizenship is not only a status but a body of shared knowledge.",
    "tdq": [
      "What power does Article I, Section 8 give Congress over citizenship, and why does it say 'uniform'?",
      "According to the 14th Amendment, who is a citizen at birth?",
      "What must a foreign-born person do to naturalize, and why include a civics test?"],
    "frayer": ["Natural-Born Citizen", "Naturalization"],
    "quiz": [{"id": "u3-gc35-dok1-1", "dok": 1,
              "stem": "Becoming a U.S. citizen through a legal process rather than by birth is called:",
              "opts": {"A": "Naturalization", "B": "Apportionment", "C": "Cloture", "D": "Ratification"}, "key": "A"}],
    "cer": "Claim + Evidence + Reasoning: Should the President be required to be a natural-born citizen? Defend your claim with evidence from the Constitution."},
  target="I can explain who is a natural-born U.S. citizen and describe the process of naturalization.",
  learning_targets="Identify the right of Congress to create rules on naturalization and explain the process of becoming a naturalized citizen. Honors: answer the 100 question Naturalization Test as group work or individually and discuss your opinion of its validity.",
  criteria=CRIT, cues=CUES, lenses="Tennessee (T)",
  dim_map={"T": "How Tennesseans establish state citizenship and residency for civic purposes."},
  hook="You could be asked the same civics question a new citizen must answer to be sworn in. Could you pass the test to join the country you already live in?",
  civic_label="CITIZENSHIP", ssp_focus="SSP.01", ref=REF)

S["GC.10"] = std(
  title="Article I & the 17th Amendment",
  tn="Analyze Article I and the 17th Amendment of the Constitution as they relate to the legislative branch, including eligibility for office, roles, length of terms, and election to office for representatives and senators, respectively. (H)",
  ican="I can analyze Article I and the 17th Amendment — the qualifications, terms, and election of members of the House and Senate.",
  vocab=[
    {"term": "Bicameral", "say": "by-KAM-er-ul", "es": "bicameral",
     "def": "A legislature made of two houses — in Congress, the House of Representatives and the Senate."},
    {"term": "Apportionment", "say": "uh-POR-shun-ment", "es": "prorrateo / distribución",
     "def": "The division of the 435 House seats among the states based on population, recalculated after each census."},
    {"term": "17th Amendment", "say": "sev-en-TEENTH", "es": "Decimoséptima Enmienda",
     "def": "The 1913 amendment that changed the election of U.S. senators from state legislatures to a direct vote of the people."},
  ],
  sources=[
    {"title": "U.S. Constitution, Amendment XVII", "who": "62nd U.S. Congress", "date": "1913",
     "quote": "The Senate of the United States shall be composed of two Senators from each State, elected by the people thereof, for six years.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/amendments-11-27"},
    {"title": "U.S. Constitution, Article I, Section 2", "who": "Constitutional Convention", "date": "1787",
     "quote": "The House of Representatives shall be composed of Members chosen every second Year by the People of the several States.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
  ],
  cfu={"dok": 2, "stem": "What key change did the 17th Amendment make to the Senate?",
       "options": {"A": "Senators are now elected directly by the people instead of by state legislatures",
                   "B": "Senators now serve two-year terms instead of six",
                   "C": "The number of senators per state increased to three",
                   "D": "The Senate lost its power to confirm appointments"},
       "key": "A",
       "why": "DOK 2: Before 1913, state legislatures chose U.S. senators; the 17th Amendment gave that choice directly to the voters of each state."},
  auth={
    "close": "Congress is bicameral — two houses with different rules. Article I sets the House of Representatives as the chamber 'chosen every second Year by the People': members serve two-year terms, must be at least 25, a citizen for seven years, and live in their state. House seats are apportioned by population after each census, so a state's delegation grows or shrinks as its population does. The Senate is the smaller, slower chamber: two senators per state, six-year terms, at least 30 years old and a citizen for nine years. Originally state legislatures chose senators; the 17th Amendment (1913) moved that choice to a direct vote of the people, making the Senate answerable to voters rather than to state politicians. The Vice President presides over the Senate but votes only to break a tie.",
    "tdq": [
      "How does the 17th Amendment change who chooses U.S. senators, and why might that matter?",
      "Contrast the House and Senate on term length and how members are elected.",
      "Why are House seats reapportioned after each census?"],
    "frayer": ["Bicameral", "Apportionment"],
    "quiz": [{"id": "u3-gc10-dok1-1", "dok": 1,
              "stem": "How long is one term for a U.S. Senator?",
              "opts": {"A": "Two years", "B": "Four years", "C": "Six years", "D": "Life"}, "key": "C"}],
    "cer": "Claim + Evidence + Reasoning: Was the 17th Amendment a good change — should the people or state legislatures choose senators? Defend your claim with evidence."},
  target="I can analyze Article I and the 17th Amendment — the qualifications, terms, and election of members of the House and Senate.",
  learning_targets="List the constitutional qualifications to serve in the House of Representatives and Senate and terms in office and the role of the Vice-President. List informal qualifications for members of Congress. Explain the significance of the 17th amendment. Identify the length of a House of Representatives and Senators term, and a session and term of Congress.",
  criteria=CRIT, cues=CUES, lenses="History (H)",
  dim_map={"H": "How the design of the two chambers reflects the Framers' compromises over representation."},
  hook="One chamber turns over every two years; the other moves at a six-year pace and once answered to state politicians, not voters. Why build Congress out of two such different halves?",
  civic_label="REPRESENTATION", ssp_focus="SSP.03", ref=REF)

S["GC.11"] = std(
  title="Census, Redistricting & Baker v. Carr",
  tn="Describe the census and its role in redistricting and reapportionment, including the role of Baker v. Carr. (T)",
  ican="I can describe the census and its role in reapportionment and redistricting, including the significance of Baker v. Carr.",
  vocab=[
    {"term": "Census", "say": "SEN-sus", "es": "censo",
     "def": "The count of the U.S. population taken every ten years, used to apportion House seats and federal funds."},
    {"term": "Redistricting", "say": "ree-DIS-trik-ting", "es": "redistribución de distritos",
     "def": "The redrawing of the boundaries of legislative districts, usually after each census, to reflect population changes."},
    {"term": "Gerrymandering", "say": "JAIR-ee-man-der-ing", "es": "manipulación de distritos",
     "def": "Drawing district lines to give one party or group an unfair advantage — changing who wins without changing any votes."},
  ],
  sources=[
    {"title": "Baker v. Carr, 369 U.S. 186", "who": "U.S. Supreme Court", "date": "1962",
     "quote": "We conclude that the complaint's allegations of a denial of equal protection present a justiciable constitutional cause of action… the right asserted is within the reach of judicial protection under the Fourteenth Amendment.",
     "repo": "U.S. Reports (Justia)", "url": "https://supreme.justia.com/cases/federal/us/369/186/"},
    {"title": "U.S. Constitution, Article I, Section 2", "who": "Constitutional Convention", "date": "1787",
     "quote": "The actual Enumeration shall be made… within every subsequent Term of ten Years, in such Manner as they shall by Law direct.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
  ],
  cfu={"dok": 3, "stem": "Why was Baker v. Carr (1962) so important for representation?",
       "options": {"A": "It abolished the census",
                   "B": "It made gerrymandering a federal crime",
                   "C": "It ended the Senate's six-year terms",
                   "D": "It ruled that federal courts could hear redistricting cases, opening the door to 'one person, one vote'"},
       "key": "D",
       "why": "DOK 3: Baker v. Carr held that unequal districts could be challenged in federal court under the 14th Amendment — making reapportionment a justiciable issue and leading to the 'one person, one vote' standard."},
  auth={
    "close": "Every ten years the Constitution requires a census — a full count of the population. That count drives apportionment (how the 435 House seats are split among the states) and redistricting (redrawing district lines within each state). Because district lines decide which voters are grouped together, whoever draws them holds real power; drawing them to favor one side is called gerrymandering. For decades some states, including Tennessee, simply refused to redraw districts as people moved to cities — so a rural vote could be worth many times an urban one. In Baker v. Carr (1962), the Supreme Court ruled that federal courts could hear such cases under the 14th Amendment. That decision opened the door to 'one person, one vote,' the principle that districts must hold roughly equal populations.",
    "tdq": [
      "How does the census connect to apportionment and redistricting?",
      "What did the Court decide in Baker v. Carr, and which amendment did it rely on?",
      "How can gerrymandering change an election's outcome without changing any votes?"],
    "frayer": ["Redistricting", "Gerrymandering"],
    "quiz": [{"id": "u3-gc11-dok1-1", "dok": 1,
              "stem": "How often is the U.S. census taken?",
              "opts": {"A": "Every year", "B": "Every four years", "C": "Every ten years", "D": "Only once"}, "key": "C"}],
    "cer": "Claim + Evidence + Reasoning: Should courts or legislatures control how district lines are drawn? Defend your claim with evidence, including Baker v. Carr."},
  target="I can describe the census and its role in reapportionment and redistricting, including the significance of Baker v. Carr.",
  learning_targets="Explain the Supreme Court decision of Baker v. Carr and its role in the redistricting process. Explain the constitutional reason the government takes a census every ten years and how that census leads to reapportionment, redistricting, and gerrymandering. Evaluate how population shifts affect congressional representation.",
  criteria=CRIT, cues=CUES, lenses="Tennessee (T)",
  dim_map={"T": "Baker v. Carr began with a Tennessee voter and Tennessee's own unequal districts."},
  hook="A vote in Memphis once counted for one-eighth of a vote in the countryside — legally. A Tennessean sued, and changed the country. How?",
  civic_label="REDISTRICTING", ssp_focus="SSP.05", ref=REF)

S["GC.12"] = std(
  title="Leadership of Congress",
  tn="Identify leadership positions of the legislative branch, including: Majority and Minority leaders; President pro tempore; role of the vice president; Speaker of the House. (—)",
  ican="I can identify the leadership positions in both houses of Congress and explain how each is chosen.",
  vocab=[
    {"term": "Speaker of the House", "say": "SPEE-ker", "es": "presidente de la Cámara",
     "def": "The leader of the House of Representatives, chosen by the majority party; sets the House agenda and is second in line to the presidency."},
    {"term": "President pro tempore", "say": "PREZ-ih-dent proh TEM-por-ay", "es": "presidente pro tempore",
     "def": "The senator who presides over the Senate in the Vice President's absence, traditionally the longest-serving member of the majority party."},
    {"term": "Majority & Minority Leaders", "say": "muh-JOR-ih-tee", "es": "líderes de mayoría y minoría",
     "def": "The elected floor leaders of each party in each chamber, who guide their party's strategy and schedule."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article I, Section 2", "who": "Constitutional Convention", "date": "1787",
     "quote": "The House of Representatives shall chuse their Speaker and other Officers.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "U.S. Constitution, Article I, Section 3", "who": "Constitutional Convention", "date": "1787",
     "quote": "The Vice President of the United States shall be President of the Senate, but shall have no Vote, unless they be equally divided.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
  ],
  cfu={"dok": 2, "stem": "Who leads the House of Representatives and sets its agenda?",
       "options": {"A": "The President pro tempore",
                   "B": "The Speaker of the House",
                   "C": "The Vice President",
                   "D": "The Chief Justice"},
       "key": "B",
       "why": "DOK 2: The Constitution says the House shall 'chuse their Speaker'; the Speaker, chosen by the majority party, leads the House and controls its agenda."},
  auth={
    "close": "Each chamber of Congress runs on party leadership. In the House, the majority party chooses the Speaker of the House — named in the Constitution, the Speaker leads the chamber, controls the agenda, and stands second in line to the presidency. In the Senate, the Constitution makes the Vice President the President of the Senate, who presides but votes only to break a tie; when the VP is absent, the President pro tempore (usually the longest-serving majority senator) presides. In both chambers, each party elects a Majority Leader and a Minority Leader to guide strategy and scheduling, assisted by 'whips' who count votes. Leadership decides which bills move and which stall, so knowing who holds these posts explains a great deal about what Congress does.",
    "tdq": [
      "Which leadership post does the Constitution name for the House, and who chooses it?",
      "What is the Vice President's role in the Senate, and when does it matter most?",
      "How do majority and minority leaders shape what Congress accomplishes?"],
    "frayer": ["Speaker of the House", "President pro tempore"],
    "quiz": [{"id": "u3-gc12-dok1-1", "dok": 1,
              "stem": "The Vice President's main power in the Senate is to:",
              "opts": {"A": "Write all bills", "B": "Break a tie vote", "C": "Appoint senators", "D": "Veto laws"}, "key": "B"}],
    "cer": "Claim + Evidence + Reasoning: Which congressional leadership position has the most influence over what becomes law? Defend your claim with evidence."},
  target="I can identify the leadership positions in both houses of Congress and explain how each is chosen.",
  learning_targets="Create a chart of Congressional leadership in both houses and explain the selection process for their respective positions.",
  criteria=CRIT, cues=CUES, lenses="Civic Structure",
  dim_map={"P": "How party leadership structures the work of a representative body."},
  hook="One person decides which bills the House will even vote on. Who holds that gatekeeper's gavel — and how did they get it?",
  civic_label="CONGRESSIONAL STRUCTURE", ssp_focus="SSP.01", ref=REF)

S["GC.13"] = std(
  title="How a Bill Becomes a Law",
  tn="Describe the process of how a bill becomes a law. (—)",
  ican="I can describe how a bill becomes a law, including the differences between the House and Senate processes.",
  vocab=[
    {"term": "Filibuster", "say": "FIL-ih-bus-ter", "es": "obstruccionismo",
     "def": "A Senate tactic of extended debate used to delay or block a vote on a bill."},
    {"term": "Cloture", "say": "KLOH-cher", "es": "clausura del debate",
     "def": "A Senate vote (usually 60 senators) to end a filibuster and force a final vote on a bill."},
    {"term": "Veto", "say": "VEE-toh", "es": "veto",
     "def": "The President's power to reject a bill passed by Congress; Congress can override a veto with a two-thirds vote of both houses."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article I, Section 7", "who": "Constitutional Convention", "date": "1787",
     "quote": "Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become a Law, be presented to the President of the United States.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "U.S. Constitution, Article I, Section 7 (override)", "who": "Constitutional Convention", "date": "1787",
     "quote": "If after such Reconsideration two thirds of that House shall agree to pass the Bill… it shall become a Law.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
  ],
  cfu={"dok": 2, "stem": "A Senate tactic of unlimited debate used to block a bill is a:",
       "options": {"A": "Cloture",
                   "B": "Veto",
                   "C": "Filibuster",
                   "D": "Quorum"},
       "key": "C",
       "why": "DOK 2: A filibuster uses extended debate to delay or block a Senate vote; it takes a cloture vote (usually 60 senators) to end one."},
  auth={
    "close": "A bill's path to becoming law is a gauntlet by design. A member introduces the bill; it goes to committee, where most bills die; if it survives, it reaches the floor. Here the chambers differ: the House Rules Committee sets strict limits on debate, so the House moves quickly, while the Senate allows extended debate — the filibuster — which a minority can use to stall a bill unless 60 senators vote for cloture to end it. Both chambers must pass identical text, often after a conference committee reconciles differences. Then, as Article I, Section 7 requires, the bill is 'presented to the President,' who may sign it into law or veto it. Congress can override a veto with a two-thirds vote of both houses. Each of these steps is a check — a chance to stop, slow, or improve a law before it binds the whole country.",
    "tdq": [
      "According to Article I, Section 7, what must happen to a bill after both houses pass it?",
      "How do the House and Senate differ in how they debate a bill?",
      "What is a filibuster, and how can the Senate end one?"],
    "frayer": ["Filibuster", "Cloture"],
    "quiz": [{"id": "u3-gc13-dok1-1", "dok": 1,
              "stem": "Congress can override a presidential veto with a vote of:",
              "opts": {"A": "A simple majority of the House only", "B": "Two-thirds of both houses",
                       "C": "The Supreme Court", "D": "Three-fourths of the states"}, "key": "B"}],
    "cer": "Claim + Evidence + Reasoning: Is it too hard for a bill to become a law, or is the difficulty a feature? Defend your claim with evidence from the process."},
  target="I can describe how a bill becomes a law, including the differences between the House and Senate processes.",
  learning_targets="Create a flow chart of how a bill becomes a law, including the steps a bill takes through both houses of Congress and the differences between the process in the House and the Senate including House Rules Committee, filibuster, and cloture.",
  criteria=CRIT, cues=CUES, lenses="Civic Structure",
  dim_map={"P": "How the lawmaking process builds in checks at every step."},
  hook="Thousands of bills are introduced each year; only a few hundred become law. What kills the rest — and why did the Framers make it so hard?",
  civic_label="LAWMAKING", ssp_focus="SSP.05", ref=REF)

S["GC.14"] = std(
  title="Tennessee's Delegation to Congress",
  tn="Identify the Tennessee representatives and senators to the U.S. Congress. (T)",
  ican="I can identify who represents Tennessee in the U.S. Congress and locate my own congressional district.",
  vocab=[
    {"term": "Congressional District", "say": "kun-GRESH-un-ul", "es": "distrito congresional",
     "def": "A geographic area whose voters elect one member of the U.S. House of Representatives; Tennessee is divided into several."},
    {"term": "Delegation", "say": "del-ih-GAY-shun", "es": "delegación",
     "def": "The full group of a state's members of Congress — its U.S. representatives plus its two U.S. senators."},
    {"term": "Constituent", "say": "kun-STITCH-oo-ent", "es": "elector / representado",
     "def": "A person who lives in the district or state a legislator represents, and whom the legislator is elected to serve."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article I, Section 2", "who": "Constitutional Convention", "date": "1787",
     "quote": "Representatives… shall be apportioned among the several States… according to their respective Numbers.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "U.S. Constitution, Amendment XVII", "who": "62nd U.S. Congress", "date": "1913",
     "quote": "…two Senators from each State, elected by the people thereof.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/amendments-11-27"},
  ],
  cfu={"dok": 2, "stem": "How many U.S. Senators does Tennessee — like every state — send to Congress?",
       "options": {"A": "Two",
                   "B": "One per congressional district",
                   "C": "Based on its population",
                   "D": "Ten"},
       "key": "A",
       "why": "DOK 2: The Constitution gives every state exactly two U.S. Senators, regardless of population; a state's number of U.S. Representatives, by contrast, depends on population."},
  auth={
    "close": "Every state's voice in Congress has two parts. Tennessee, like every state, elects two U.S. Senators who represent the whole state. It also elects several U.S. Representatives — the exact number set by population through apportionment — each speaking for one congressional district. Together these members are Tennessee's delegation. The people who live in a member's district or state are that member's constituents, and a core job of any legislator is to answer to them: holding town halls, casting votes, and helping with federal problems. Knowing who your representatives are — and which district you live in — is the first step to being heard, because a legislator's office exists to serve the people back home.",
    "tdq": [
      "How does the Constitution decide how many senators and representatives Tennessee has?",
      "What is the difference between a senator's constituents and a representative's constituents?",
      "Why is knowing your own district the first step to contacting your representative?"],
    "frayer": ["Delegation", "Constituent"],
    "quiz": [{"id": "u3-gc14-dok1-1", "dok": 1,
              "stem": "A person a legislator is elected to represent is called a:",
              "opts": {"A": "Constituent", "B": "Delegate", "C": "Lobbyist", "D": "Justice"}, "key": "A"}],
    "cer": "Claim + Evidence + Reasoning: Does a senator who represents an entire state, or a representative who represents one district, better serve your interests? Defend your claim."},
  target="I can identify who represents Tennessee in the U.S. Congress and locate my own congressional district.",
  learning_targets="Name my current Representative for my district and the current U.S. Senators.",
  criteria=CRIT, cues=CUES, lenses="Tennessee (T)",
  dim_map={"T": "Identifying Tennessee's own senators, representatives, and districts — the geography of representation."},
  hook="Two people in Washington are paid to answer to you personally — plus one more for your neighborhood. Do you know their names?",
  civic_label="TENNESSEE & CONGRESS", ssp_focus="SSP.06", ref=REF)

S["GC.15"] = std(
  title="The Powers of Congress",
  tn="Describe the powers of U.S. Congress, including: appropriations; commerce; confirmations; declaration of war; implied powers; Necessary and proper clause. (H)",
  ican="I can describe the enumerated and implied powers of Congress, including the Necessary and Proper Clause and McCulloch v. Maryland.",
  vocab=[
    {"term": "Enumerated Powers", "say": "ee-NOO-mer-ay-ted", "es": "poderes enumerados",
     "def": "The powers specifically listed for Congress in the Constitution, such as taxing, borrowing, regulating commerce, and declaring war."},
    {"term": "Implied Powers", "say": "im-PLYD", "es": "poderes implícitos",
     "def": "Powers not listed but reasonably needed to carry out the enumerated powers, justified by the Necessary and Proper Clause."},
    {"term": "Necessary & Proper Clause", "say": "NESS-uh-sair-ee", "es": "cláusula necesaria y apropiada",
     "def": "The 'Elastic Clause' (Art. I, §8) letting Congress make all laws needed to carry out its powers — the basis of implied powers."},
  ],
  sources=[
    {"title": "U.S. Constitution, Article I, Section 8", "who": "Constitutional Convention", "date": "1787",
     "quote": "The Congress shall have Power… To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers.",
     "repo": "U.S. National Archives", "url": "https://www.archives.gov/founding-docs/constitution-transcript"},
    {"title": "McCulloch v. Maryland, 17 U.S. 316", "who": "Chief Justice John Marshall", "date": "1819",
     "quote": "Let the end be legitimate, let it be within the scope of the constitution, and all means which are appropriate, which are plainly adapted to that end… are constitutional.",
     "repo": "U.S. Reports (Justia)", "url": "https://supreme.justia.com/cases/federal/us/17/316/"},
  ],
  cfu={"dok": 3, "stem": "How did McCulloch v. Maryland (1819) affect the powers of Congress?",
       "options": {"A": "It abolished the Necessary and Proper Clause",
                   "B": "It limited Congress to only the powers explicitly listed",
                   "C": "It gave the states power to tax the federal government",
                   "D": "It upheld broad implied powers under the Necessary and Proper Clause"},
       "key": "D",
       "why": "DOK 3: Marshall's opinion read the Necessary and Proper Clause broadly — Congress may use any appropriate means to carry out its enumerated powers — establishing implied powers and upholding the national bank."},
  auth={
    "close": "Congress's powers come in two kinds. Its enumerated powers are the ones the Constitution lists in Article I, Section 8 — to tax and spend (appropriations), to borrow, to regulate commerce, to declare war, to coin money, and to issue patents and copyrights, among others. The Senate also confirms many presidential appointments. But the Framers could not list every power Congress might need, so they added the Necessary and Proper Clause — the 'Elastic Clause' — allowing Congress to make all laws needed to carry out its listed powers. These are its implied powers. In McCulloch v. Maryland (1819), Chief Justice John Marshall upheld this broad reading: 'let the end be legitimate… and all means which are appropriate… are constitutional.' Marshall also warned that 'the power to tax involves the power to destroy,' ruling that a state could not tax the national bank. The case cemented both implied powers and national supremacy.",
    "tdq": [
      "What is the difference between an enumerated and an implied power of Congress?",
      "How does the Necessary and Proper Clause create implied powers?",
      "How did Marshall's opinion in McCulloch v. Maryland expand what Congress can do?"],
    "frayer": ["Enumerated Powers", "Implied Powers"],
    "quiz": [{"id": "u3-gc15-dok1-1", "dok": 1,
              "stem": "The 'Elastic Clause' that stretches Congress's powers is also called the:",
              "opts": {"A": "Supremacy Clause", "B": "Commerce Clause",
                       "C": "Necessary and Proper Clause", "D": "Due Process Clause"}, "key": "C"}],
    "cer": "Claim + Evidence + Reasoning: Do the implied powers make Congress too strong, or are they necessary for it to govern? Defend your claim using the Constitution and McCulloch v. Maryland."},
  target="I can describe the enumerated and implied powers of Congress, including the Necessary and Proper Clause and McCulloch v. Maryland.",
  learning_targets="List and give historic examples of the enumerated powers of Congress, including the power to: impeach, tax, borrow, issue copyrights and patents. Explain Congress' role in the budget making process. Explain the Commerce Clause and list historical examples of expansion and retraction over time. Define implied powers and explain its significance with the Necessary and Proper clause. Explain the outcome of McCulloch v. Maryland as it relates to the Supremacy Clause.",
  criteria=CRIT, cues=CUES, lenses="History (H)",
  dim_map={"H": "How the Necessary and Proper Clause and McCulloch v. Maryland expanded federal power over time."},
  hook="The Constitution never says Congress can create an air force, a national bank, or the interstate highways — yet it did all three. Where does that power come from?",
  civic_label="POWERS OF CONGRESS", ssp_focus="SSP.02", ref=REF)

order = ["GC.35", "GC.10", "GC.11", "GC.12", "GC.13", "GC.14", "GC.15"]
doc = {"unit": unit, "order": order, "standards": S}
blob = json.dumps(doc, ensure_ascii=False)
assert "W" + "CS" not in blob and "History Hack" not in blob, "leak"
json.dump(doc, open(OUT, "w"), ensure_ascii=False, indent=1)
print("wrote", OUT)
print("CFU keys:", {c: S[c]["cfu"]["key"] for c in order})
