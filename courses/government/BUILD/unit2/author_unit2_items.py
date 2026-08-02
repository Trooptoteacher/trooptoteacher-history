#!/usr/bin/env python3
"""Unit 2 (Citizen Participation, GC.31–34) scaled MCQ bank — tn-assessment-specialist
schema + rigor (option-length parity, tagged distractors PK/MC/PE/NE + rationales, dok/blooms rationales,
C3, reporting category, de-biased keys). ~5 items/standard across DOK 1–3. No district label."""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
GOV=json.load(open(os.path.join(HERE,"analysis","government_standards_source.json")))
OUT=os.path.abspath(os.path.join(HERE,"..","..","WEB_EDITION","public","data","government","questions","unit-2"))
os.makedirs(OUT,exist_ok=True)
RC="RC-GOV2: Citizen Participation"

# (std,dok,blooms,c3,ssp,stem,{A..D},correct,{tags},{rats},dokR,blR)
I=[
# ---------------- GC.31 Responsibilities of citizens ----------------
("GC.31",1,"Remember","D2","SSP.04","Which action is a legal duty of U.S. citizens rather than a voluntary act?",
 {"A":"Serving on a jury if summoned","B":"Volunteering weekly at a food bank","C":"Joining a political party campaign","D":"Attending a city council meeting"},"A",
 {"A":None,"B":"PE","C":"NE","D":"PE"},
 {"A":"Correct — jury duty is a legal obligation when summoned.","B":"Voluntary service, not a legal duty.","C":"Voluntary participation, not required.","D":"Voluntary civic engagement, not a duty."},
 "Recalls which listed act is a legal duty.","Student recognizes a fact from the standard."),
("GC.31",2,"Understand","D2","SSP.04","Why is paying taxes considered essential to the well-being of the nation?",
 {"A":"It funds public services and national defense","B":"It replaces the need for any voting","C":"It guarantees a citizen a public office","D":"It removes the duty to obey the laws"},"A",
 {"A":None,"B":"MC","C":"PE","D":"MC"},
 {"A":"Correct — taxes fund shared services and defense.","B":"Misconception — taxes do not replace voting.","C":"Plausible error — taxes do not buy office.","D":"Misconception — taxes do not remove legal duties."},
 "Explains why a duty matters, not just recall.","Student explains a civic relationship."),
("GC.31",1,"Remember","D2","SSP.04","Which requirement must a person meet to register to vote in Tennessee?",
 {"A":"Be eighteen years of age","B":"Own property in the county","C":"Belong to a political party","D":"Pass a national civics exam"},"A",
 {"A":None,"B":"MC","C":"MC","D":"MC"},
 {"A":"Correct — 18, U.S. citizenship, and residency are required.","B":"Misconception — no property requirement exists.","C":"Misconception — party membership is not required.","D":"Misconception — civics/literacy tests are prohibited."},
 "Recalls a voting requirement.","Student identifies a factual requirement."),
("GC.31",2,"Understand","D2","SSP.05","What is one likely impact when many eligible citizens choose not to vote?",
 {"A":"Results represent fewer people's real views","B":"The winning candidate must resign at once","C":"Taxes are automatically canceled that year","D":"Jury duty is no longer legally required"},"A",
 {"A":None,"B":"MC","C":"MC","D":"NE"},
 {"A":"Correct — low turnout narrows whose views count.","B":"Misconception — no resignation results.","C":"Misconception — taxes are unaffected.","D":"Near miss — an unrelated duty."},
 "Explains a consequence of non-voting.","Student explains cause and effect."),
("GC.31",2,"Understand","D2","SSP.04","Serving in the military or performing alternative service is best described as:",
 {"A":"a way to serve the nation","B":"a punishment for breaking the law","C":"a requirement to hold any job","D":"a substitute for paying all taxes"},"A",
 {"A":None,"B":"MC","C":"PE","D":"PE"},
 {"A":"Correct — service is a civic contribution.","B":"Misconception — it is not a punishment.","C":"Plausible error — not a job requirement.","D":"Plausible error — it does not replace taxes."},
 "Explains the civic meaning of service.","Student classifies a responsibility."),
# ---------------- GC.32 Political parties & nominations ----------------
("GC.32",1,"Remember","D2","SSP.04","The United States is best described as having what kind of party system?",
 {"A":"A two-party system","B":"A one-party system","C":"A no-party system","D":"A four-party system"},"A",
 {"A":None,"B":"NE","C":"MC","D":"PE"},
 {"A":"Correct — two major parties dominate U.S. politics.","B":"Near miss — describes authoritarian states.","C":"Misconception — parties do exist.","D":"Plausible error — not four dominant parties."},
 "Recalls the U.S. party structure.","Student recognizes a fact."),
("GC.32",2,"Understand","D2","SSP.04","What is the main difference between an open and a closed primary?",
 {"A":"Who may vote in the primary election","B":"When the votes are finally counted up","C":"How many candidates may enter it","D":"Where the polling places are set up"},"A",
 {"A":None,"B":"PE","C":"NE","D":"PE"},
 {"A":"Correct — open lets any voter; closed limits to party members.","B":"Plausible error — timing is not the difference.","C":"Near miss — candidate count is unrelated.","D":"Plausible error — location is not the difference."},
 "Explains a distinction between two processes.","Student contrasts two concepts."),
("GC.32",1,"Remember","D2","SSP.04","In the presidential nomination process, a caucus is a:",
 {"A":"meeting where members pick a candidate","B":"national holiday set for all voters","C":"court that settles election disputes","D":"tax paid by each new candidate here"},"A",
 {"A":None,"B":"MC","C":"NE","D":"MC"},
 {"A":"Correct — a local meeting to select a candidate.","B":"Misconception — not a holiday.","C":"Near miss — courts are unrelated.","D":"Misconception — not a tax."},
 "Recalls the definition of a caucus.","Student defines a term."),
("GC.32",3,"Analyze","D2","SSP.04","Why do winner-take-all elections help keep the two-party system in place?",
 {"A":"Small parties rarely win any seats outright","B":"A law bans the forming of new parties","C":"A firm rule requires two parties","D":"A tax is charged to every third party"},"A",
 {"A":None,"B":"MC","C":"MC","D":"MC"},
 {"A":"Correct — winner-take-all shuts out small parties, favoring two.","B":"Misconception — no ban on parties.","C":"Misconception — no two-party rule exists.","D":"Misconception — no such tax."},
 "Analyzes a cause of the two-party structure.","Student examines a causal relationship."),
("GC.32",2,"Understand","D2","SSP.04","How does a general election differ from a primary election?",
 {"A":"It chooses officials between parties' nominees","B":"It selects each party's own single nominee","C":"It counts only the early caucus results","D":"It is open only to elected officials now"},"A",
 {"A":None,"B":"NE","C":"PE","D":"MC"},
 {"A":"Correct — the general election decides among nominees.","B":"Near miss — that describes a primary.","C":"Plausible error — caucuses are separate.","D":"Misconception — general elections are open to voters."},
 "Explains a distinction between election types.","Student contrasts two processes."),
# ---------------- GC.33 Media & public opinion ----------------
("GC.33",1,"Remember","D3","SSP.02","A public opinion poll is used mainly to:",
 {"A":"measure what people think about issues","B":"elect the president of the country now","C":"write the new laws for the states","D":"count the votes on election day here"},"A",
 {"A":None,"B":"MC","C":"MC","D":"NE"},
 {"A":"Correct — polls sample public opinion.","B":"Misconception — polls do not elect anyone.","C":"Misconception — polls do not make law.","D":"Near miss — vote counting is separate."},
 "Recalls the purpose of a poll.","Student identifies a function."),
("GC.33",2,"Understand","D3","SSP.02","How can the wording of a poll question affect its results?",
 {"A":"Biased wording can push certain answers","B":"Wording has no effect on the responses","C":"Longer questions get more correct answers","D":"Only the poll's date changes the results"},"A",
 {"A":None,"B":"MC","C":"PE","D":"PE"},
 {"A":"Correct — loaded wording skews responses.","B":"Misconception — wording clearly matters.","C":"Plausible error — length is not the issue.","D":"Plausible error — date is not the driver."},
 "Explains how a design choice affects data.","Student explains cause and effect."),
("GC.33",2,"Understand","D2","SSP.02","What does the term 'media bias' describe?",
 {"A":"Slanted coverage that favors one side","B":"The total number of news channels now","C":"A tax placed on all of the newspapers","D":"The rule that reporters must go vote"},"A",
 {"A":None,"B":"NE","C":"MC","D":"MC"},
 {"A":"Correct — bias is one-sided coverage.","B":"Near miss — channel count is unrelated.","C":"Misconception — not a tax.","D":"Misconception — no such rule."},
 "Explains the meaning of a key term.","Student defines a concept."),
("GC.33",2,"Understand","D2","SSP.04","One important role of the media in a democracy is to:",
 {"A":"inform the public about government actions","B":"choose the winners of every election","C":"collect the taxes from all news readers","D":"write the laws that are passed by Congress"},"A",
 {"A":None,"B":"MC","C":"MC","D":"MC"},
 {"A":"Correct — the media informs citizens (a watchdog role).","B":"Misconception — media does not elect officials.","C":"Misconception — media does not tax.","D":"Misconception — media does not legislate."},
 "Explains a civic function of the media.","Student identifies a role."),
("GC.33",3,"Analyze","D3","SSP.02","A poll asks, 'Do you support wasteful government spending?' Why might its results mislead?",
 {"A":"The loaded word 'wasteful' invites a No","B":"Polls cannot measure any real opinion","C":"The sample was clearly far too large","D":"People answer every poll the same way"},"A",
 {"A":None,"B":"MC","C":"PE","D":"MC"},
 {"A":"Correct — the loaded word biases the answer.","B":"Misconception — polls can measure opinion.","C":"Plausible error — sample size is not the flaw.","D":"Misconception — responses vary."},
 "Analyzes how wording biases a result.","Student evaluates a source flaw."),
# ---------------- GC.34 Means of participation ----------------
("GC.34",1,"Remember","D4","SSP.04","Which of these is a way citizens participate in the political process?",
 {"A":"Signing a petition for a cause","B":"Watching television purely for fun","C":"Paying a monthly cell phone bill","D":"Buying groceries at the local store"},"A",
 {"A":None,"B":"NE","C":"MC","D":"MC"},
 {"A":"Correct — petitioning is political participation.","B":"Near miss — entertainment is not participation.","C":"Misconception — a private expense.","D":"Misconception — a private activity."},
 "Recalls a form of participation.","Student recognizes an example."),
("GC.34",1,"Remember","D2","SSP.04","Lobbying is best defined as:",
 {"A":"trying to influence officials' decisions","B":"voting once in a national election","C":"serving a full sentence in a prison","D":"paying yearly taxes to the government"},"A",
 {"A":None,"B":"NE","C":"MC","D":"PE"},
 {"A":"Correct — lobbying seeks to influence officials.","B":"Near miss — voting is separate.","C":"Misconception — unrelated to lobbying.","D":"Plausible error — a duty, not lobbying."},
 "Recalls the definition of lobbying.","Student defines a term."),
("GC.34",2,"Understand","D4","SSP.04","What is the shared purpose of an initiative, a referendum, and a recall?",
 {"A":"To let citizens shape laws more directly","B":"To choose the U.S. Supreme Court justices","C":"To collect extra taxes from the states","D":"To declare a war on other foreign nations"},"A",
 {"A":None,"B":"MC","C":"NE","D":"MC"},
 {"A":"Correct — these tools give voters direct influence.","B":"Misconception — courts are unrelated.","C":"Near miss — taxation is separate.","D":"Misconception — unrelated to war powers."},
 "Explains the purpose of direct-democracy tools.","Student explains a shared function."),
("GC.34",2,"Understand","D2","SSP.04","How does a recall election increase citizen participation?",
 {"A":"It lets voters remove an official early","B":"It doubles the yearly salary of officials","C":"It bans all of the future elections","D":"It appoints new judges without a vote"},"A",
 {"A":None,"B":"MC","C":"MC","D":"NE"},
 {"A":"Correct — voters can remove an official before term's end.","B":"Misconception — unrelated to pay.","C":"Misconception — it does not ban elections.","D":"Near miss — appointments are separate."},
 "Explains how a tool broadens participation.","Student explains a civic mechanism."),
("GC.34",2,"Understand","D4","SSP.04","Demonstrating and petitioning are protected as forms of:",
 {"A":"citizens expressing their political views","B":"paying the required yearly federal taxes","C":"serving on a local county trial jury","D":"running a small private family business"},"A",
 {"A":None,"B":"NE","C":"NE","D":"MC"},
 {"A":"Correct — protest and petition are political expression.","B":"Near miss — a duty, not expression.","C":"Near miss — a duty, not expression.","D":"Misconception — unrelated economic activity."},
 "Explains the category of two participation forms.","Student classifies civic actions."),
]

def dims_of(std):
    d=GOV[std]["dimensions"]; return [x.strip() for x in d.strip("()").split(",")] if d else []
items=[]
per={}
for (std,dok,bl,c3,ssp,stem,opts,key,tags,rats,dokR,blR) in I:
    per[std]=per.get(std,0)+1
    items.append({"id":f"{std}-U2Q{per[std]:02d}","standard":std,"secondaryStandard":None,"unit":2,
      "reportingCategory":RC,"dok":dok,"blooms":bl,"dokRationale":dokR,"bloomsRationale":blR,
      "question":stem,"stimulus":None,"stimulusAttribution":None,"options":opts,"correctAnswer":key,
      "distractorTags":tags,"distractorRationales":rats,"tcapFormat":False,"itemWritingCompliant":True,
      "instructionalPurpose":"formative","itemCategory":"classroom-instructional","c3Dimension":c3,
      "sspAlignment":ssp,"tennesseeSpecific":False,"tcaRequired":bool(GOV[std]["tca"]),
      "contentTags":dims_of(std),"rubricId":None,"rubricName":None,"sensitivityFlag":None,
      "type":"multiple-choice","pointValue":1,"calibration":"pre-field-test","pre_field_test":True,
      "remediation":{"standard":std,"reteach_narrative":f"03_TEXTBOOK_UNITS/unit-2/unit-2.html#{std}",
        "reteach_teacher":f"03_TEXTBOOK_UNITS/unit-2/unit-2-teacher-guide.html#{std}"}})
# de-bias keys within each standard's items (rotate A/B/C/D)
L=["A","B","C","D"]
for i,q in enumerate(items):
    tgt=L[i%4]; cur=q["correctAnswer"]
    if cur!=tgt:
        for f in ("options","distractorTags","distractorRationales"):
            d=q[f]; d[cur],d[tgt]=d[tgt],d[cur]
        q["correctAnswer"]=tgt
    q["distractorTags"][q["correctAnswer"]]=None
from collections import Counter
payload={"_schema":"tn-assessment-specialist / tcap-item-writer-v2 schema (Government adaptation). Scaled Unit 2 "
  "MCQ bank across DOK 1–3. Classroom-formative · pre-field-test.","subject":"government","unit":2,
  "count":len(items),"items":items}
s=json.dumps(payload,indent=2,ensure_ascii=False); assert "W"+"CS" not in s
open(os.path.join(OUT,"mcq-bank.json"),"w").write(s)
print("Unit 2 mcq-bank.json:",len(items),"MCQ | per-standard:",dict(Counter(q['standard'] for q in items)))
print("key dist:",dict(Counter(q['correctAnswer'] for q in items)),"| dok dist:",dict(Counter(q['dok'] for q in items)))
