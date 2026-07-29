// Unit 1 — TEACHER Graphic Organizer Toolkit (reproducible). Platinum tokens.
// Part 1: course-wide blank reproducibles (each with a WHEN/WHY blurb).
// Part 2: Unit 1 pre-labeled organizers (best-fit per standard).
// Plus a "Which organizer when" master guide and Tennessee-connection highlighting.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,Header,Footer,PageNumber,ImageRun}=D;
const NAVY='1B2A4A',RED='B22234',GOLD='C89B3C',INK='1A1A1A',CREAM='F7F5EF',WHITE='FFFFFF',GREY='6B7280',BORD='D9D5C8';
const FONT='Calibri', CW=9648;
const bd=(c=BORD)=>({style:BorderStyle.SINGLE,size:4,color:c,space:0});
const CELLB=(c=BORD)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
function R(t,{s=22,b=false,i=false,c=INK,caps=false}={}){return new TextRun({text:t,size:s,bold:b,italics:i,color:c,font:FONT,allCaps:caps});}
function P(runs,{align,spacing,indent}={}){return new Paragraph({alignment:align,spacing:spacing||{after:100},indent,children:Array.isArray(runs)?runs:[runs]});}
function H(t,lvl,{brk=false}={}){const map={1:HeadingLevel.HEADING_1,2:HeadingLevel.HEADING_2,3:HeadingLevel.HEADING_3};
  return new Paragraph({heading:map[lvl],pageBreakBefore:brk,spacing:{before:lvl===1?200:150,after:90},keepNext:true,
    children:[R(t,{s:lvl===1?36:lvl===2?28:24,b:true,c:lvl===3?RED:NAVY})]});}
function cell(children,{w,fill,borders,valign}={}){return new TableCell({width:{size:w,type:WidthType.DXA},
  shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,margins:{top:70,bottom:70,left:110,right:110},
  verticalAlign:valign,borders:borders||CELLB(),children:Array.isArray(children)?children:[children]});}
function table(rows,widths){return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:widths,rows});}
function callout(label,lines=[]){const kids=[P(R(label,{s:21,b:true,c:NAVY}),{spacing:{after:lines.length?60:0}})];
  (Array.isArray(lines)?lines:[lines]).forEach(l=>kids.push(P(typeof l==='string'?R(l,{s:22}):l,{spacing:{after:40}})));
  return table([new TableRow({children:[cell(kids,{w:CW,fill:CREAM})]})],[CW]);}
function ruled(n=3){const out=[];for(let i=0;i<n;i++){
  out.push(new Paragraph({spacing:{before:0,after:0,line:255,lineRule:'auto'},border:{bottom:{style:BorderStyle.SINGLE,size:4,color:'C9C4B5',space:3}},children:[R(' ',{s:16})]}));
  if(i<n-1) out.push(new Paragraph({spacing:{before:0,after:0,line:70,lineRule:'exact'},children:[R(' ',{s:2})]}));}
  return out;}
// grid of writing cells; headers optional; each blank cell gets ruled lines.
// light:true -> header row is CREAM with navy text (writable — students fill in the labels; never dark).
function grid(headers,rows,widths,lines=3,{light=false}={}){const trs=[];
  if(headers)trs.push(new TableRow({tableHeader:true,children:headers.map((h,i)=>cell(P(R(h,{s:19,b:true,c:light?NAVY:WHITE}),{spacing:{after:0}}),{w:widths[i],fill:light?CREAM:NAVY}))}));
  rows.forEach(r=>trs.push(new TableRow({children:r.map((cx,i)=>cell(cx?[P(R(cx,{s:20,b:true}),{spacing:{after:0}})]:ruled(lines),{w:widths[i]}))})));
  return table(trs,widths);}
// embed a generated organizer graphic (PIL PNG), centered, sized to px width
function img(file,wpx){const [W,H]=require('child_process').execSync(`python3 -c "from PIL import Image;s=Image.open('${file}').size;print(s[0],s[1])"`).toString().trim().split(' ').map(Number);
  const h=Math.round(wpx*H/W);
  return new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:80},children:[new ImageRun({data:fs.readFileSync(file),transformation:{width:wpx,height:h}})]});}
const w3=[3216,3216,3216], w2=[4824,4824];
function whenWhy(t){return callout('WHEN TO USE · WHY IT WORKS',[t]);}
const PB=()=>new Paragraph({children:[new PageBreak()]});
function TN(t){return callout('★ TENNESSEE CONNECTION',[t]);}
// research-based differentiation strip — fills the page AND reaches every learner (UDL/MTSS)
function everyStudent(scaffold,extend){return callout('MAKE IT WORK FOR EVERY STUDENT (UDL · MTSS)',[
  'Scaffold — '+(scaffold||'offer a sentence starter or a small word bank, or let students complete part of the organizer with a partner first.'),
  'Extend — '+(extend||'push higher-DOK: “Which side has the stronger case, and why?” or “What would change if one factor were different?”'),
  'Show it your way — students may write, say it aloud, draw/label, or build it (UDL response choice). Sentence frame: “______ because ______, which shows ______.”']);}

// ---------- ORGANIZER BODIES ----------
function venn2(a='Only ______ (A)',shared='Both / shared',b='Only ______ (B)',lines=14){return grid([a,shared,b],[['','',''],['','','']],w3,lines);}
function tchart(a='______',b='______',lines=15){return grid([a,b],[['',''],['','']],w2,lines);}
function matrix(cols,rows,lines=4){const widths=[2400].concat(new Array(cols.length-1).fill(Math.round(7248/(cols.length-1))));
  const body=rows.map(r=>[r].concat(new Array(cols.length-1).fill('')));return grid(cols,body,widths,lines);}
function causeEffect(){return grid(['Cause','→','Effect'],[['','→',''],['','→',''],['','→',''],['','→','']],[4000,648,5000],5);}
function timeline(){return grid(['Date / order','Event','Why it mattered'],[['','',''],['','',''],['','',''],['','',''],['','',''],['','','']],[2000,4000,3648],4);}
function web(center='Central idea'){return grid([center,'Connected idea','How it connects'],[['','',''],['','',''],['','',''],['','',''],['','',''],['','','']],[3000,3324,3324],4);}
function mainIdea(){return [grid(['MAIN IDEA'],[['']],[CW],3), grid(['Detail','Detail','Detail'],[['','',''],['','','']],w3,8)];}
function kwl(){return grid(['K — what I Know','W — what I Want to know','L — what I Learned'],[['','',''],['','','']],w3,12);}
function fiveW(){return grid(['Question','Answer'],[['Who?',''],['What?',''],['When?',''],['Where?',''],['Why?','']],[2400,7248],5);}
function problemSolution(){return grid(['Problem','Proposed solution','Result / evaluation'],[['','',''],['','','']],w3,10);}
function frayer(term='______'){return grid(['Definition (own words)','Characteristics'],[['',''],['Examples','Non-examples'],['','']],w2,7);}
function cer(){return grid(['Part','Write here'],[['Claim',''],['Evidence (two specifics)',''],['Reasoning','']],[2600,7048],7);}
function hippo(){return grid(['H-I-P-P-O','Prompt / notes'],[['H — Historical context',''],['I — Intended audience',''],['P — Purpose',''],['P — Point of view',''],['O — Outside connection','']],[3000,6648],4);}
function tnOrg(){return grid(['The national event / idea','Our Tennessee (or local) connection','Why the local story matters'],[['','',''],['','','']],w3,9);}

// each organizer = its own reproducible page (organizer fills the page; every-student strip removes dead space)
function organizer(title,when,body,diff){const out=[H(title,2,{brk:true}), whenWhy(when)];
  (Array.isArray(body)?body:[body]).forEach(b=>out.push(b));
  out.push(everyStudent((diff||{}).scaffold,(diff||{}).extend));
  return out;}

// ---------- PART 1: blank reproducibles ----------
const PART1=[
 organizer('Venn Diagram (2) — Compare & Contrast','Task says “compare,” “contrast,” “how are they alike/different?” for TWO things. Marzano’s #1 strategy (identifying similarities & differences). The shared column forces students to name what overlaps, not just list traits.',venn2()),
 organizer('Venn (3) / Triple T-Chart — Compare THREE','Comparing three people, groups, or ideas. Use the columns for each item and note shared traits in your notes.',matrix(['Item A','Item B','Item C'],['Trait / criterion 1','Trait / criterion 2','Trait / criterion 3','Trait / criterion 4'],2)),
 organizer('T-Chart — Two Sides / Pros & Cons / Before–After','Two categories to sort or weigh: benefits vs costs, pros vs cons, before vs after, cause vs effect. Fast, low-floor entry point for comparison.',tchart()),
 organizer('Compare & Contrast Matrix — Items × Criteria','Comparing several items across the SAME set of criteria. Reduces cognitive load by making the comparison systematic.',matrix(['Criterion','Item 1','Item 2','Item 3'],['','','',''],2)),
 organizer('Cause & Effect — Causal Chains','Task asks “what caused…?”, “what were the effects/consequences of…?” Makes causal reasoning visible (builds SSP.05).',causeEffect()),
 organizer('Timeline / Sequence — Chronology','Ordering events or tracing change over time. Builds chronological reasoning (SSP.05).',timeline()),
 organizer('Concept Web — Connect & Brainstorm','Activating prior knowledge or showing how ideas relate to a central concept. Great as a pre-reading or review move.',web()),
 organizer('Main Idea & Details — Summarize','Pulling the central idea and its support from a text or source. Separates the big idea from the evidence.',mainIdea()),
 organizer('KWL — Activate & Track Learning','Start of a standard: what students Know / Want to know; end: what they Learned. Builds metacognition and frames inquiry.',kwl()),
 organizer('5 Ws — Cover the Basics of an Event','Making sure students capture who/what/when/where/why of an event before analysis.',fiveW()),
 organizer('Problem & Solution — Evaluate Responses','Analyzing a problem and the responses to it (e.g., a policy or reform). Structures evaluation.',problemSolution()),
 organizer('Frayer Model — Deep Vocabulary','Learning a key term deeply (definition, characteristics, examples, non-examples).',frayer()),
 organizer('CER — Build an Argument','Any “make a claim / defend / argue” task. Claim + two pieces of evidence + reasoning (builds SSP.04).',cer()),
 organizer('HIPPO — Analyze a Primary Source','Analyzing a photo, cartoon, map, or document (builds SSP.01–SSP.02). Pair with OPTIC for visuals.',hippo()),
 organizer('★ Tennessee Connection — Local ↔ National','Whenever a standard has a Tennessee tie: link the national event to our state/community and say why the local story matters. This local-to-national move is a HistoryHack signature — use it often.',tnOrg()),
];

// ---------- PART 2: Unit 1 pre-labeled (best-fit per standard) ----------
const PART2=[
 [...organizer('GC.04 — Federalists vs. Anti-Federalists (T-Chart)','This standard weighs the ratification debate. A T-chart makes the two positions explicit: Federalists favored a stronger union; Anti-Federalists feared central power and demanded a Bill of Rights.',tchart('Federalists (for ratification)','Anti-Federalists (against, as written)')), TN('Tennessee entered the Union in 1796; its state constitution echoes the same separation of powers and Bill of Rights framed in this unit.')],
 organizer('GC.03 — Weaknesses of the Articles of Confederation (Cause & Effect)','The Articles created a weak national government. A cause -> effect flow shows how each weakness led to a problem: no taxing power -> unpaid debts; no army -> Shays’s Rebellion went unchecked.',causeEffect()),
 organizer('GC.02–GC.08 — Founding Documents Timeline','The founding is a sequence of documents. A timeline makes the chronology clear: Declaration of Independence (1776) -> Articles of Confederation (1781) -> Constitutional Convention (1787) -> Constitution ratified (1788) -> Bill of Rights (1791).',timeline()),
 organizer('GC.06 — Principles of Limited Government (Matrix)','The standard names the principles that limit government. A matrix compares each across the same criteria.',matrix(['Principle','What it does','Example'],['Separation of powers','Checks and balances','Federalism','Judicial review','Popular sovereignty','Rule of law'],2)),
 organizer('GC.09 — Republic vs. Direct Democracy (T-Chart)','The standard asks students to distinguish two systems. A T-chart makes the contrast explicit.',tchart('Republic (representative)','Direct democracy')),
 organizer('GC.08 — The Bill of Rights (Matrix)','The standard analyzes how the first amendments limit government. A matrix pairs each amendment with what it protects and an example.',matrix(['Amendment','What it protects','Example / limit on government'],['1st','2nd','4th','5th','10th'],2)),
 organizer('GC.03–GC.04 — Articles vs. U.S. Constitution (Venn)','The standard compares the two frameworks. A Venn captures what changed, what stayed, and what both shared.',venn2('Only the Articles','Both frameworks','Only the U.S. Constitution')),
];

// ---------- MASTER "WHICH ORGANIZER WHEN" GUIDE ----------
const GUIDE=grid(['When the task asks students to…','Reach for…','Why it works'],[
 ['compare / contrast TWO things','Venn (2) or T-Chart','Marzano’s highest-yield strategy; the overlap names shared traits'],
 ['compare 3+ things on set criteria','Compare & Contrast Matrix','systematic; lowers cognitive load'],
 ['explain causes / effects','Cause & Effect','makes causal chains visible (SSP.05)'],
 ['put events in order / show change','Timeline / Sequence','builds chronological reasoning (SSP.05)'],
 ['brainstorm or connect ideas','Concept Web','activates prior knowledge; shows relationships'],
 ['summarize a text or source','Main Idea & Details','separates the central idea from support'],
 ['activate prior knowledge & track learning','KWL','metacognition; frames inquiry'],
 ['learn a key term deeply','Frayer','deep vocabulary processing'],
 ['analyze a primary source','HIPPO / OPTIC','disciplinary sourcing (SSP.01–02)'],
 ['make and defend a claim','CER','claim + evidence + reasoning (SSP.04)'],
 ['weigh two sides / a decision','T-Chart or Problem–Solution','structures evaluation'],
 ['capture the basics of an event','5 Ws','ensures full coverage'],
 ['connect a national event to Tennessee','★ Tennessee Connection','our signature local-to-national move'],
],[3400,2600,3648],2);

// ---------- ASSEMBLE ----------
const header=new Header({children:[P(R('Government Hack™ · Unit 1 · Teacher Graphic Organizer Toolkit',{s:16,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0},children:[R('Government Hack™ · Unit 1 (Course Standard) © 2026 TroopToTeacher Technologies LLC   |   Page ',{s:16,c:GREY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GREY,font:FONT})]})]});

const cover=[
 new Paragraph({spacing:{before:1400,after:0},children:[R('GOVERNMENT HACK™',{s:30,b:true,c:GOLD})]}),
 new Paragraph({spacing:{after:0},children:[R('Teacher Graphic Organizer Toolkit',{s:52,b:true,c:NAVY})]}),
 new Paragraph({spacing:{after:200},children:[R('Unit 1 — Foundations of Constitutional Government  ·  Reproducible',{s:26,c:INK})]}),
 callout('WHY THIS TOOLKIT',['Knowing WHICH organizer to use, and WHEN, is half the battle. This toolkit tells you — with a brief why for each — then gives you reproducible blanks (Part 1) and Unit 1 ready-to-print, pre-labeled organizers (Part 2). Tennessee connections are highlighted throughout; the local-to-national move is a HistoryHack signature and a point of difference for our classrooms.']),
 PB(),
 H('Which Organizer, When — Quick Guide',1),
 P(R('Scan the left column for what the activity asks students to do; reach for the organizer on the right. Every organizer in Part 1 also carries its own “when to use · why it works” note.',{s:22})),
 GUIDE,
 P(R('Reproducible — you may copy these pages for classroom use.',{s:18,i:true,c:GREY}),{spacing:{before:120}}),
 H('Part 1 — Reusable Blank Organizers (all subjects, all units)',1,{brk:true}),
 P(R('Content-agnostic blanks. Print as many as you need; use across any standard or subject.',{s:22})),
];
const part1=PART1.flat();
const part2Head=[H('Part 2 — Unit 1 Ready-to-Use Organizers (pre-labeled, best-fit)',1,{brk:true}),
 P(R('Each is matched to the standard whose task it best fits, with a short note on why. Tennessee connections are flagged.',{s:22}))];
const part2=PART2.flat();

const doc=new Document({styles:{default:{document:{run:{font:FONT,size:22,color:INK}}}},
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1152,bottom:1152,left:1296,right:1296,header:720,footer:720}}},
  headers:{default:header},footers:{default:footer},
  children:[...cover,...part1,...part2Head,...part2]}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('deliverables/Unit1_Teacher_Graphic_Organizer_Toolkit.docx',b);console.log('WROTE toolkit',b.length,'bytes');});
