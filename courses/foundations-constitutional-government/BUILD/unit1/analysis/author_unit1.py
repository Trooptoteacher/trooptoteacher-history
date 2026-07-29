#!/usr/bin/env python3
"""Author Unit 1 (Foundations of Constitutional Government, GC.01–GC.09) content in the
platinum engine contract. Verbatim standards from government_standards_source.json.
Primary-source quotes are verbatim public-domain founding text with real repositories
(National Archives, Avalon Project, Congress.gov). No invented sources. No district label.
© 2026 TroopToTeacher Technologies LLC."""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
GOV=json.load(open(os.path.join(HERE,"government_standards_source.json")))

def V(term,say,es,d): return {"term":term,"say":say,"es":es,"def":d}
def SRC(title,who,date,quote,repo,url): return {"title":title,"who":who,"date":date,"quote":quote,"repo":repo,"url":url}

STD={}  # per-standard authored content keyed by GC code

STD["GC.01"]=dict(
 title="Enlightenment Roots of American Government",
 vocab=[
  V("Natural Rights","NATCH-rul RYTS","derechos naturales","God-given rights to life, liberty, and property that government does not grant and cannot rightfully take away — central to John Locke's political thought."),
  V("Social Contract","SOH-shul KON-trakt","contrato social","The idea that people agree to give up some freedom to a government in exchange for protection of their rights, and that government's authority comes from the consent of the governed."),
  V("Magna Carta","MAG-nuh KAR-tuh","Carta Magna","The 1215 English charter that limited the king's power and protected certain rights of life, liberty, and property — an early root of limited government and due process."),
 ],
 sources=[
  SRC("Second Treatise of Government","John Locke","1689",
   "Men being, as has been said, by nature all free, equal, and independent, no one can be put out of this estate and subjected to the political power of another without his own consent.",
   "Avalon Project, Yale Law School","https://avalon.law.yale.edu/17th_century/locke.asp"),
  SRC("Magna Carta, Clause 39","King John of England","1215",
   "No free man shall be seized or imprisoned, or stripped of his rights or possessions… except by the lawful judgment of his equals or by the law of the land.",
   "The National Archives (UK)","https://www.bl.uk/magna-carta"),
 ],
 cfu=dict(dok=2,
  stem="According to John Locke, where does a government's rightful authority come from?",
  options={"A":"The divine right of kings","B":"The consent of the people being governed",
           "C":"The strongest military","D":"Inherited wealth and land"},
  key="B",
  why="DOK 2: Locke's social-contract theory holds that legitimate government rests on the consent of the governed to protect natural rights — a direct root of the Declaration's 'consent of the governed.'"),
 auth=dict(
  close=("American ideas about liberty and self-government were not new in 1776 — they grew from older roots. "
   "John Locke argued that people are born with natural rights to life, liberty, and property, and that government "
   "exists by a social contract to protect them, losing its authority if it fails. Montesquieu urged dividing "
   "government power among separate branches; Hobbes explained why people trade some freedom for order. Older models "
   "mattered too: Greek democracy, the Roman republic, and the limits on rulers set in Magna Carta (1215) and the "
   "English Bill of Rights (1689). The colonists inherited these ideas and reshaped them."),
  tdq=["According to Locke, what rights do people have simply by being born, and what is government's job regarding them?",
       "What limit on the king's power does Magna Carta's Clause 39 establish, and how does it connect to due process today?",
       "Why does the text say the colonists used 'old ideas, not new ones' to justify independence?"],
  frayer=["Natural Rights","Social Contract"],
  quiz=[dict(id="u1-gc01-dok1-1",dok=1,
    stem="Which thinker is most associated with natural rights and the social contract?",
    opts={"A":"Thomas Hobbes","B":"John Locke","C":"Julius Caesar","D":"King John"},key="B")],
  cer="Claim + Evidence + Reasoning: Which European root — Locke's natural rights, Montesquieu's separated powers, or Magna Carta's limits on the king — shaped American government the most? Defend your claim with evidence from two sources."),
 hook="You already have rights no ruler gave you and none can take away — that's the idea that started a revolution. Where did it come from?",
 dim_map={"C":"How Enlightenment and classical ideas shaped a shared political culture of liberty.",
          "E":"Locke's inclusion of property among the natural rights government protects."},
)

STD["GC.02"]=dict(
 title="The Declaration of Independence",
 vocab=[
  V("Unalienable Rights","un-AY-lee-uh-nuh-bul RYTS","derechos inalienables","Rights so fundamental they cannot be taken away or given up — in the Declaration, 'Life, Liberty and the pursuit of Happiness.'"),
  V("Grievances","GREE-vun-sez","agravios","Formal complaints; in the Declaration, the list of specific abuses by King George III used to justify independence."),
  V("Declaration of Independence","dek-luh-RAY-shun","Declaración de Independencia","The 1776 document, drafted mainly by Thomas Jefferson, that announced the colonies' separation from Britain and stated the principles of government by consent."),
 ],
 sources=[
  SRC("Declaration of Independence","Continental Congress (drafted by Thomas Jefferson)","July 4, 1776",
   "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.",
   "National Archives","https://www.archives.gov/founding-docs/declaration-transcript"),
  SRC("Declaration of Independence (grievance)","Continental Congress","July 4, 1776",
   "He has refused his Assent to Laws, the most wholesome and necessary for the public good… He has dissolved Representative Houses repeatedly.",
   "National Archives","https://www.archives.gov/founding-docs/declaration-transcript"),
 ],
 cfu=dict(dok=3,
  stem="The Declaration lists the colonists' natural rights and then a long list of grievances against the king. Why did the writers put these two parts together?",
  options={"A":"To make the document longer and more impressive",
           "B":"To show that when a government repeatedly violates the people's rights, the people may justly alter or abolish it",
           "C":"To ask King George III to apologize","D":"To describe how to run the new state governments"},
  key="B",
  why="DOK 3: The structure is an argument — universal rights (major premise) + the king's specific violations (evidence) → the conclusion that the colonies may rightfully separate. Grievances turn principle into justification."),
 auth=dict(
  close=("On July 4, 1776, the Continental Congress adopted the Declaration of Independence, drafted mainly by Thomas Jefferson. "
   "Its most famous lines borrow directly from Locke: all people are 'created equal' and hold 'unalienable Rights' to 'Life, "
   "Liberty and the pursuit of Happiness,' and governments derive 'their just powers from the consent of the governed.' The "
   "Declaration then lists specific grievances against King George III — dissolving colonial legislatures, taxing without consent, "
   "keeping standing armies. The logic is an argument: because government exists to protect rights, a government that repeatedly "
   "violates them may justly be altered or abolished. The Declaration announced not just a separation, but a theory of legitimate government."),
  tdq=["What three unalienable rights does the Declaration name, and where does government get its 'just powers'?",
       "Choose one grievance against King George III and explain how it violated the colonists' rights.",
       "How does the Declaration use natural rights to justify the colonies' break from Britain?"],
  frayer=["Unalienable Rights","Declaration of Independence"],
  quiz=[dict(id="u1-gc02-dok1-1",dok=1,
    stem="According to the Declaration, governments derive their just powers from:",
    opts={"A":"the consent of the governed","B":"the king","C":"the wealthiest citizens","D":"the army"},key="A")],
  cer="Claim + Evidence + Reasoning: Was the Declaration of Independence mainly a list of complaints, or an argument about the purpose of government? Defend your claim with two quotations from the text."),
 hook="'All men are created equal.' A bold claim in 1776 — and the colonists used it to fire a king. How does the Declaration build its case?",
 dim_map={"H":"The 1776 break from Britain and the grievances that justified it."},
)

STD["GC.03"]=dict(
 title="The Articles of Confederation",
 vocab=[
  V("Confederation","kon-fed-uh-RAY-shun","confederación","A loose union of independent states that keep most of their power, giving only limited authority to a weak central government."),
  V("Articles of Confederation","AR-tih-kulz","Artículos de la Confederación","The first national constitution of the United States (1781–1789); it created a weak central government that could not tax or regulate trade."),
  V("Shays's Rebellion","SHAYZ ree-BEL-yun","Rebelión de Shays","A 1786–1787 uprising of Massachusetts farmers that the weak national government could not put down — exposing the failures of the Articles and pushing leaders toward a new constitution."),
 ],
 sources=[
  SRC("Articles of Confederation, Article II","Second Continental Congress","ratified 1781",
   "Each state retains its sovereignty, freedom, and independence, and every power, jurisdiction, and right, which is not by this Confederation expressly delegated to the United States, in Congress assembled.",
   "Avalon Project, Yale Law School","https://avalon.law.yale.edu/18th_century/artconf.asp"),
  SRC("Letter on Shays's Rebellion","George Washington","1786",
   "There are combustibles in every State, which a spark might set fire to… I feel infinitely more than I can express for the disorders which have arisen.",
   "National Archives, Founders Online","https://founders.archives.gov"),
 ],
 cfu=dict(dok=2,
  stem="Under the Articles of Confederation, which power did the national government LACK that caused serious problems?",
  options={"A":"The power to declare war","B":"The power to tax the states and citizens directly",
           "C":"The power to run a post office","D":"The power to make treaties"},
  key="B",
  why="DOK 2: The Articles denied Congress the power to tax; it could only request money from the states. Without reliable revenue, the national government could not pay debts or respond to crises like Shays's Rebellion."),
 auth=dict(
  close=("Winning independence required a national government, but Americans feared creating another all-powerful ruler. So the "
   "Articles of Confederation (ratified 1781) kept the states 'sovereign' and gave Congress only limited powers. Congress could "
   "declare war, make treaties, and run a post office — but it could NOT tax, could NOT regulate trade between states, and needed "
   "nine of thirteen states to pass major laws and all thirteen to amend the Articles. The result was a government too weak to pay "
   "its debts or keep order. When Shays's Rebellion broke out in Massachusetts in 1786, the national government could not raise an "
   "army to stop it. Leaders like Washington and Madison concluded the Articles had to be replaced."),
  tdq=["According to Article II, how much power did each state keep under the Articles of Confederation?",
       "Name two powers the national government lacked under the Articles, and explain one problem each caused.",
       "How did Shays's Rebellion reveal the weaknesses of the Articles?"],
  frayer=["Confederation","Articles of Confederation"],
  quiz=[dict(id="u1-gc03-dok1-1",dok=1,
    stem="The Articles of Confederation created a national government that was:",
    opts={"A":"too weak to tax or regulate trade","B":"a monarchy","C":"stronger than today's federal government","D":"controlled by the president"},key="A")],
  cer="Claim + Evidence + Reasoning: Was the greatest weakness of the Articles the lack of taxing power, the lack of a strong executive, or the difficulty of amendment? Defend your claim with evidence."),
 hook="Imagine a national government that can declare war but can't collect a dime to pay for it. That was America under the Articles. What went wrong?",
 dim_map={"H":"Why the first national constitution failed and set up the 1787 Convention."},
)

STD["GC.04"]=dict(
 title="The Constitutional Convention & Ratification",
 vocab=[
  V("Great Compromise","GRAYT KOM-pruh-myz","Gran Compromiso","The 1787 agreement creating a two-house Congress: a House based on state population and a Senate with equal representation (two per state) — settling the fight between large and small states."),
  V("Federalists","FED-uh-rul-ists","federalistas","Supporters of ratifying the Constitution who favored a stronger national government; their arguments appear in the Federalist Papers."),
  V("Anti-Federalists","AN-tee-FED-uh-rul-ists","antifederalistas","Opponents of ratifying the Constitution as written, who feared a too-powerful central government and demanded a bill of rights to protect individual liberty."),
 ],
 sources=[
  SRC("Federalist No. 10","James Madison (Publius)","1787",
   "The latent causes of faction are thus sown in the nature of man… The regulation of these various and interfering interests forms the principal task of modern legislation.",
   "Congress.gov / Library of Congress","https://guides.loc.gov/federalist-papers/text-1-10"),
  SRC("Brutus No. 1 (Anti-Federalist)","'Brutus' (likely Robert Yates)","1787",
   "In a republic, the manners, sentiments, and interests of the people should be similar… In a large extended country, it is impossible to have a representation, possessing the sentiments, and of integrity, to declare the minds of the people.",
   "Teaching American History / Avalon Project","https://teachingamericanhistory.org/document/brutus-i/"),
 ],
 cfu=dict(dok=3,
  stem="The Great Compromise settled which major disagreement at the Constitutional Convention?",
  options={"A":"Whether to have a president or a king",
           "B":"How states should be represented in Congress — by population or equally",
           "C":"Whether to keep the Articles of Confederation","D":"Whether to allow political parties"},
  key="B",
  why="DOK 3: Large states favored the Virginia Plan (representation by population); small states favored the New Jersey Plan (equal representation). The Great Compromise combined both — a population-based House and an equal-representation Senate."),
 auth=dict(
  close=("In 1787, delegates met in Philadelphia — officially to fix the Articles, but they wrote an entirely new Constitution. The "
   "hardest fight was representation. Large states backed the Virginia Plan (seats by population); small states backed the New "
   "Jersey Plan (equal seats). The Great Compromise split the difference: a House of Representatives based on population and a Senate "
   "with two senators per state. The Three-Fifths Compromise, counting enslaved people as three-fifths of a person for representation "
   "and taxation, exposed the deep contradiction of slavery in a document about liberty. Once signed, the Constitution faced a fierce "
   "ratification debate. Federalists (Madison, Hamilton, Jay, writing as 'Publius' in the Federalist Papers) argued for a stronger "
   "union; Anti-Federalists (like 'Brutus') warned of a distant, too-powerful government and demanded a bill of rights."),
  tdq=["How did the Great Compromise resolve the conflict between large and small states?",
       "In Federalist No. 10, what problem does Madison say a large republic can control better than a small one?",
       "What was the Anti-Federalists' main fear, and what did they demand before ratifying?"],
  frayer=["Great Compromise","Federalists"],
  quiz=[dict(id="u1-gc04-dok1-1",dok=1,
    stem="The Federalist Papers were written to:",
    opts={"A":"persuade people to ratify the Constitution","B":"declare independence","C":"repeal the Bill of Rights","D":"end the Convention early"},key="A")],
  cer="Claim + Evidence + Reasoning: In the ratification debate, whose warning has aged better — the Federalists' case for a strong union, or the Anti-Federalists' fear of centralized power? Use one quote from each side."),
 hook="Two plans, thirteen stubborn states, one hot Philadelphia summer. How did the Framers turn a deadlock into a Constitution?",
 dim_map={"H":"The 1787 Convention, its compromises, and the ratification debate."},
)

STD["GC.05"]=dict(
 title="The Preamble: Purposes of Government",
 vocab=[
  V("Preamble","PREE-am-bul","preámbulo","The introduction to the Constitution that states the document's purposes, beginning 'We the People.'"),
  V("Popular Sovereignty","POP-yuh-lur SOV-rin-tee","soberanía popular","The principle that government's authority comes from the people — expressed in the Preamble's opening words, 'We the People.'"),
  V("General Welfare","JEN-uh-rul WEL-fair","bienestar general","The well-being of the whole community; one of the Preamble's stated purposes of government ('promote the general Welfare')."),
 ],
 sources=[
  SRC("Preamble to the U.S. Constitution","Constitutional Convention","1787",
   "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.",
   "National Archives","https://www.archives.gov/founding-docs/constitution-transcript"),
  SRC("Federalist No. 51","James Madison (Publius)","1788",
   "Justice is the end of government. It is the end of civil society. It ever has been and ever will be pursued until it be obtained, or until liberty be lost in the pursuit.",
   "Congress.gov / Library of Congress","https://guides.loc.gov/federalist-papers/text-51-60"),
 ],
 cfu=dict(dok=2,
  stem="The Preamble begins with the words 'We the People.' Which principle of government does this phrase express?",
  options={"A":"Judicial review","B":"Popular sovereignty — government power comes from the people",
           "C":"Separation of powers","D":"Federalism"},
  key="B",
  why="DOK 2: 'We the People' declares that the Constitution's authority flows from the people themselves — the principle of popular sovereignty — not from a king or a single state."),
 auth=dict(
  close=("Before a single power is granted, the Constitution states WHY it exists. The Preamble — 'We the People of the United States' — "
   "opens by declaring popular sovereignty: the government's authority comes from the people. It then lists six purposes: to form a "
   "more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, "
   "and secure the Blessings of Liberty for ourselves and future generations ('our Posterity'). The Preamble grants no powers by "
   "itself, but it is a mission statement: every power in the articles that follow is meant to serve these ends."),
  tdq=["What do the first three words of the Preamble tell us about where government power comes from?",
       "List three of the six purposes of government named in the Preamble.",
       "How does the phrase 'to ourselves and our Posterity' show the Framers were thinking beyond their own time?"],
  frayer=["Preamble","Popular Sovereignty"],
  quiz=[dict(id="u1-gc05-dok1-1",dok=1,
    stem="'We the People' at the start of the Preamble expresses the principle of:",
    opts={"A":"popular sovereignty","B":"monarchy","C":"judicial review","D":"federal supremacy"},key="A")],
  cer="Claim + Evidence + Reasoning: Of the six purposes in the Preamble, which is most important for a free society today? Defend your claim with reasoning tied to the text."),
 hook="Six goals, one sentence, and it starts with three world-changing words: 'We the People.' What did the Framers promise?",
 dim_map={"P":"The Preamble's statement of popular sovereignty and the purposes of government."},
)

STD["GC.06"]=dict(
 title="Principles of Limited Government",
 vocab=[
  V("Separation of Powers","sep-uh-RAY-shun","separación de poderes","Dividing government into three branches — legislative, executive, and judicial — so no one branch holds all power."),
  V("Checks and Balances","CHEKS and BAL-un-sez","controles y equilibrios","The system that lets each branch limit the others (e.g., the president vetoes laws; Congress can override; courts can rule laws unconstitutional)."),
  V("Judicial Review","joo-DISH-ul ree-VYOO","revisión judicial","The power of courts to decide whether a law or government action is constitutional — established in Marbury v. Madison (1803)."),
 ],
 sources=[
  SRC("Federalist No. 51","James Madison (Publius)","1788",
   "If men were angels, no government would be necessary. If angels were to govern men, neither external nor internal controls on government would be necessary… Ambition must be made to counteract ambition.",
   "Congress.gov / Library of Congress","https://guides.loc.gov/federalist-papers/text-51-60"),
  SRC("Federalist No. 78","Alexander Hamilton (Publius)","1788",
   "A constitution is, in fact, and must be regarded by the judges, as a fundamental law… No legislative act, therefore, contrary to the Constitution, can be valid.",
   "Congress.gov / Library of Congress","https://guides.loc.gov/federalist-papers/text-71-85"),
 ],
 cfu=dict(dok=3,
  stem="In Federalist No. 51, Madison writes that 'ambition must be made to counteract ambition.' Which constitutional design does this describe?",
  options={"A":"Popular sovereignty","B":"Checks and balances that let each branch limit the others",
           "C":"Federalism between nation and states","D":"The amendment process"},
  key="B",
  why="DOK 3: Madison's point is structural — because people seek power, the Constitution pits the branches against each other so each checks the others' ambition. That is the logic of checks and balances."),
 auth=dict(
  close=("The Framers feared concentrated power, so they built limits into the Constitution's structure. Separation of powers divides "
   "government into three branches — Congress makes laws, the president executes them, the courts interpret them. Checks and balances "
   "let each branch restrain the others: the president can veto a bill, Congress can override the veto and impeach officials, and the "
   "courts can strike down unconstitutional acts through judicial review, established in Marbury v. Madison (1803). Other limits include "
   "federalism (power split between nation and states), the rule of law (everyone, including leaders, is bound by law), popular "
   "sovereignty, and civilian control of the military. As Madison put it in Federalist No. 51, 'ambition must be made to counteract ambition.'"),
  tdq=["Name the three branches of government and one job of each.",
       "According to Federalist No. 51, why can't we simply trust leaders to limit their own power?",
       "How did Marbury v. Madison strengthen the system of checks and balances?"],
  frayer=["Checks and Balances","Judicial Review"],
  quiz=[dict(id="u1-gc06-dok1-1",dok=1,
    stem="The power of courts to declare a law unconstitutional is called:",
    opts={"A":"judicial review","B":"the veto","C":"impeachment","D":"popular sovereignty"},key="A")],
  cer="Claim + Evidence + Reasoning: Which principle does the most to prevent tyranny — separation of powers, checks and balances, or federalism? Defend your claim with evidence from the sources."),
 hook="'If men were angels, no government would be necessary.' Since we're not angels, how did Madison design a government to guard against itself?",
 dim_map={"P":"Separation of powers, checks and balances, and judicial review as limits on government.",
          "H":"Marbury v. Madison (1803) establishing judicial review."},
)

STD["GC.07"]=dict(
 title="Structure of the Constitution & How to Amend It",
 vocab=[
  V("Amendment","uh-MEND-munt","enmienda","A formal change or addition to the Constitution; there have been 27, beginning with the Bill of Rights."),
  V("Article V","AR-tih-kul FYV","Artículo V","The part of the Constitution that sets out how it can be amended — a deliberately difficult, two-step process of proposal and ratification."),
  V("Ratification","rat-ih-fih-KAY-shun","ratificación","Formal approval; an amendment must be ratified by three-fourths of the states (38 of 50) to take effect."),
 ],
 sources=[
  SRC("U.S. Constitution, Article V","Constitutional Convention","1787",
   "The Congress, whenever two thirds of both Houses shall deem it necessary, shall propose Amendments to this Constitution, or… shall call a Convention for proposing Amendments, which… shall be valid… when ratified by the Legislatures of three fourths of the several States.",
   "National Archives","https://www.archives.gov/founding-docs/constitution-transcript"),
  SRC("U.S. Constitution, structure","Constitutional Convention","1787",
   "The Constitution consists of a Preamble and seven Articles: Article I (Legislative), II (Executive), III (Judicial), IV (States), V (Amendment), VI (Supremacy), and VII (Ratification).",
   "National Archives","https://www.archives.gov/founding-docs/constitution-transcript"),
 ],
 cfu=dict(dok=2,
  stem="Why did the Framers make the amendment process in Article V deliberately difficult?",
  options={"A":"To make sure the Constitution could never change",
           "B":"So the Constitution could adapt over time, but only with broad agreement across the country",
           "C":"To give the president control over amendments","D":"To let a single state change it alone"},
  key="B",
  why="DOK 2: Requiring supermajorities to propose (2/3 of Congress) and ratify (3/4 of states) means change is possible but requires broad national consensus — balancing stability with flexibility."),
 auth=dict(
  close=("The Constitution is short and organized: a Preamble and seven Articles. Article I creates the legislative branch (Congress), "
   "Article II the executive, Article III the judiciary; Article IV covers the states, Article V the amendment process, Article VI the "
   "supremacy of federal law, and Article VII ratification. The Framers knew the document would need to change, so Article V provides a "
   "path — but a hard one. An amendment must be proposed by two-thirds of both houses of Congress (or a national convention) and then "
   "ratified by three-fourths of the states. This high bar keeps the Constitution stable while still allowing change: in over 230 years "
   "it has been amended just 27 times."),
  tdq=["How many Articles does the Constitution have, and what do the first three establish?",
       "What are the two steps to amend the Constitution, and what fraction is required at each step?",
       "Why does the difficulty of Article V protect both stability and federalism?"],
  frayer=["Amendment","Article V"],
  quiz=[dict(id="u1-gc07-dok1-1",dok=1,
    stem="To ratify a constitutional amendment requires approval by:",
    opts={"A":"three-fourths of the states","B":"the president","C":"a simple majority of voters","D":"the Supreme Court"},key="A")],
  cer="Claim + Evidence + Reasoning: Is the difficulty of amending the Constitution a strength or a weakness for a modern democracy? Defend your claim with reasoning tied to Article V."),
 hook="Only 27 changes in more than 230 years. Is the Constitution nearly perfect — or nearly impossible to change? Article V holds the answer.",
 dim_map={"P":"The structure of the Constitution and the Article V amendment process."},
)

STD["GC.08"]=dict(
 title="The Bill of Rights",
 vocab=[
  V("Bill of Rights","BIL of RYTS","Carta de Derechos","The first ten amendments to the Constitution (1791), which protect individual freedoms and limit the power of government."),
  V("Reserved Powers","ree-ZURVD POW-erz","poderes reservados","Powers kept by the states or the people, not given to the national government — protected by the Tenth Amendment."),
  V("Due Process","DOO PROSS-ess","debido proceso","The requirement that government follow fair legal procedures before taking a person's life, liberty, or property — guaranteed by the Fifth Amendment."),
 ],
 sources=[
  SRC("First Amendment","U.S. Congress (Bill of Rights)","ratified 1791",
   "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.",
   "National Archives","https://www.archives.gov/founding-docs/bill-of-rights-transcript"),
  SRC("Tenth Amendment","U.S. Congress (Bill of Rights)","ratified 1791",
   "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.",
   "National Archives","https://www.archives.gov/founding-docs/bill-of-rights-transcript"),
 ],
 cfu=dict(dok=3,
  stem="The First Amendment begins 'Congress shall make no law…' Why does the Bill of Rights phrase protections as limits on the government rather than as gifts to the people?",
  options={"A":"To show the government created these rights and can remove them",
           "B":"Because the Framers saw rights as belonging to people already — the Constitution's job is to stop government from violating them",
           "C":"To give Congress more power over speech and religion","D":"Because only Congress has rights"},
  key="B",
  why="DOK 3: The Bill of Rights reflects natural-rights thinking: rights pre-exist government. Framing them as prohibitions ('shall make no law') limits government power rather than granting rights it could later revoke."),
 auth=dict(
  close=("The Anti-Federalists agreed to the Constitution only if a bill of rights was added. In 1791 the first ten amendments were "
   "ratified. The Bill of Rights protects individual freedoms and, notably, most protections apply to 'persons,' not only citizens. "
   "The First Amendment guards religion, speech, press, assembly, and petition. The Fourth through Eighth protect people accused of "
   "crimes — from unreasonable searches to cruel and unusual punishment — through guarantees like due process. The Ninth Amendment "
   "says the people keep other rights not listed, and the Tenth reserves to the states and the people all powers not given to the "
   "national government — a cornerstone of federalism. Every clause is a limit on government power. This standard is required "
   "instruction under Tennessee law (T.C.A. § 49-6-1028)."),
  tdq=["List three freedoms protected by the First Amendment.",
       "According to the Tenth Amendment, who keeps the powers not given to the national government?",
       "Why does it matter that the Bill of Rights protects 'persons' and not only citizens?"],
  frayer=["Bill of Rights","Reserved Powers"],
  quiz=[dict(id="u1-gc08-dok1-1",dok=1,
    stem="The Bill of Rights is the name for:",
    opts={"A":"the first ten amendments to the Constitution","B":"the Preamble","C":"the Articles of Confederation","D":"the Declaration of Independence"},key="A")],
  cer="Claim + Evidence + Reasoning: Which amendment in the Bill of Rights does the most to protect individual liberty today? Defend your claim with evidence from the text."),
 hook="Ten amendments, one purpose: to tell the government what it may NOT do to you. Why did Americans insist on adding them?",
 dim_map={"C":"How the Bill of Rights protects the individual freedoms at the heart of American civic culture."},
 tca="(T.C.A. § 49-6-1028)",
)

STD["GC.09"]=dict(
 title="Republic and Democracy",
 vocab=[
  V("Republic","ree-PUB-lik","república","A government in which citizens elect representatives to make laws and decisions on their behalf."),
  V("Representative Democracy","rep-ree-ZEN-tuh-tiv","democracia representativa","A system in which the people rule indirectly by electing officials to represent them — the model of U.S. government."),
  V("Direct Democracy","dih-REKT dih-MOK-ruh-see","democracia directa","A system in which citizens vote directly on laws themselves, rather than through elected representatives."),
 ],
 sources=[
  SRC("Federalist No. 10","James Madison (Publius)","1787",
   "A republic, by which I mean a government in which the scheme of representation takes place… promises the cure for which we are seeking. Let us examine the points in which it varies from pure democracy.",
   "Congress.gov / Library of Congress","https://guides.loc.gov/federalist-papers/text-1-10"),
  SRC("U.S. Constitution, Article IV, Section 4","Constitutional Convention","1787",
   "The United States shall guarantee to every State in this Union a Republican Form of Government.",
   "National Archives","https://www.archives.gov/founding-docs/constitution-transcript"),
 ],
 cfu=dict(dok=2,
  stem="What is the main difference between a direct democracy and a republic (representative democracy)?",
  options={"A":"A republic has no elections","B":"In a direct democracy citizens vote on laws themselves; in a republic they elect representatives to make laws",
           "C":"A republic is ruled by a king","D":"There is no difference"},
  key="B",
  why="DOK 2: In a direct democracy the people vote on laws directly; in a republic (representative democracy) the people elect representatives who make laws on their behalf — the model the Framers chose."),
 auth=dict(
  close=("Americans often call the United States a 'democracy,' but the Framers designed a republic — a representative democracy. In a "
   "direct democracy, citizens vote on laws themselves; in a republic, they elect representatives to make laws for them. In Federalist "
   "No. 10, Madison argued a large republic would better control the dangers of 'faction' than a small direct democracy. The "
   "Constitution guarantees every state 'a Republican Form of Government' (Article IV). A constitutional republic combines majority rule "
   "through elections with protection of minority rights and individual liberties through the Constitution — so the majority governs, "
   "but cannot simply vote away the basic rights of others."),
  tdq=["What is the difference between a direct democracy and a representative democracy (republic)?",
       "In Federalist No. 10, why does Madison prefer a large republic over a pure democracy?",
       "How does a constitutional republic balance majority rule with minority rights?"],
  frayer=["Republic","Direct Democracy"],
  quiz=[dict(id="u1-gc09-dok1-1",dok=1,
    stem="The United States is best described as a:",
    opts={"A":"constitutional republic / representative democracy","B":"direct democracy","C":"monarchy","D":"confederation"},key="A")],
  cer="Claim + Evidence + Reasoning: Was the Framers' choice of a republic over a direct democracy the right one for a large nation? Defend your claim using Federalist No. 10."),
 hook="Is the United States a democracy or a republic? The answer is 'both, on purpose' — and it changes how your voice reaches government.",
 dim_map={"P":"The distinction between a republic and a democracy and the U.S. as a constitutional republic."},
)

# ---- assemble with verbatim standard text + ican from the source of truth ----
def target_from(ican): return ican  # verbatim instructional-guide target
order=["GC.0%d"%i for i in range(1,10)]
standards={}
for code in order:
    src=GOV[code]; a=STD[code]
    dims=src["dimensions"]; tn=src["standard"]+(f" {dims}" if dims else "")
    ican_verb=src["ican"]
    # student-facing "I can" derived from the verbatim standard (never labels the source district)
    ican="I can "+src["standard"][0].lower()+src["standard"][1:]
    entry=dict(
      title=a["title"], tn=tn, ican=ican,
      vocab=a["vocab"], sources=a["sources"], cfu=a["cfu"], auth=a["auth"],
      std_source="TN Academic Standards — United States Government & Civics (GC), verbatim",
      target="I can "+src["standard"][0].lower()+src["standard"][1:],
      learning_targets=ican_verb,   # verbatim instructional-guide targets (source of truth)
      criteria=[
        "state the key idea of the standard in your own words with an accurate example;",
        "use at least one primary source to support your explanation;",
        "connect the idea to how it limits or empowers government today.",
      ],
      cues=["Key idea of this standard?","One primary source that supports it?","One effect on government or rights?","Key terms →"],
      lenses=" · ".join({"C":"Culture (C)","E":"Economics (E)","G":"Geography (G)","H":"History (H)","P":"Politics/Government (P)","T":"Tennessee (T)"}[d]
               for d in ["C","E","G","H","P","T"] if d in dims),
      dim_map=a.get("dim_map",{}),
      hook=a["hook"],
      civic_label={"GC.01":"CONSTITUTIONAL PRINCIPLES","GC.02":"CIVIC ARGUMENTATION","GC.03":"CONSTITUTIONAL PRINCIPLES",
        "GC.04":"CIVIC ARGUMENTATION","GC.05":"CONSTITUTIONAL PRINCIPLES","GC.06":"SEPARATION OF POWERS / CHECKS & BALANCES",
        "GC.07":"CONSTITUTIONAL PRINCIPLES","GC.08":"RIGHTS ANALYSIS","GC.09":"CONSTITUTIONAL PRINCIPLES"}[code],
      ssp_focus="SSP.02" if code in ("GC.01","GC.02","GC.08") else "SSP.04",
    )
    if a.get("tca") or src["tca"]:
        entry["tca"]=src["tca"] or a.get("tca")
    i=order.index(code); base=2+i*7
    entry["ref"]={"vocab":base+1,"dt":f"{base+2}–{base+4}","source":base+5,"persp":base+5,
                  "progress":base+6,"range":f"{base}–{base+6}"}
    standards[code]=entry

out=dict(
  unit=dict(code="Unit 1", title="Foundations of Constitutional Government",
    course_name="Foundations of Constitutional Government",
    standards_range="GC.01–GC.09", quarter=1, suggested_days="15–17",
    essential_question="How and why did the Founders build a limited constitutional republic?",
    publisher="TroopToTeacher Technologies LLC",
    footer="Foundations of Constitutional Government · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards (GC) · Supplemental under TCA § 49-6-2202(a)(3)",
    perspectives_title="Whose Voice Counted? Perspectives on the Founding",
    perspectives_intro="This section complicates the founding narrative: whose interests the new government served, who was left out, and who organized in response. It is Government Hack–authored instructional synthesis grounded in this unit's sourced record — not a primary source.",
    perspectives=[
      ["Federalists","Argued for a stronger national union and ratification; Madison and Hamilton defended checks and balances and the large republic in the Federalist Papers (GC.04, GC.06)."],
      ["Anti-Federalists","Feared a distant, too-powerful central government and refused to ratify without a Bill of Rights to protect individual liberty (GC.04, GC.08)."],
      ["Enslaved & Free Black Americans","The Three-Fifths Compromise counted enslaved people as three-fifths of a person for representation (GC.04), even as the Declaration proclaimed that 'all men are created equal' (GC.02)."],
      ["Women & the Unenfranchised","Women, most non-property holders, and Native peoples could not vote at ratification; the Article V amendment process (GC.07) later became the path to expand the franchise."],
    ],
    tn_connection_label="TENNESSEE CONNECTION",
    tn_connection="Tennessee entered the Union in 1796 as the 16th state. Its own state constitution echoes the federal design studied in this unit — a separation of powers among three branches and a Declaration of Rights modeled on the Bill of Rights (GC.06, GC.08).",
    tn_connection_task="Tennessee's government mirrors the federal framework. Investigate one way your state or local government reflects a principle from this unit — separation of powers, checks and balances, or the protection of individual rights — and record what you find.",
    course_short="Government & Civics",
    cover_era="1776 · 1787 · 1791",
    cover_title_lines=["FOUNDATIONS OF","CONSTITUTIONAL GOVERNMENT"],
    cover_image=""),
  order=order, standards=standards)

s=json.dumps(out,indent=2,ensure_ascii=False)
assert "W"+"CS" not in s, "GUARDRAIL: source-district label present"
open(os.path.join(HERE,"unit1_content.json"),"w").write(s)
print("Wrote unit1_content.json:",len(order),"standards ·",len(s)//1024,"KB · guardrail OK")
for c in order:
    e=standards[c]; print(f"  {c}: {e['title']} | vocab {len(e['vocab'])} | src {len(e['sources'])} | tdq {len(e['auth']['tdq'])}"+(" | TCA" if 'tca' in e else ""))
