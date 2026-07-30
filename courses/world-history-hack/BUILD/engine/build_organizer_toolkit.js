// Unit 1 — TEACHER Graphic Organizer Toolkit (reproducible). Platinum tokens.
// Part 1: course-wide blank reproducibles (each with a WHEN/WHY blurb).
// Part 2: Unit 1 pre-labeled organizers (best-fit per standard).
// Plus a "Which organizer when" master guide and Tennessee-connection highlighting.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,Header,Footer,PageNumber,ImageRun}=D;
const NAVY='1B2A4A',RED='B22234',GOLD='C89B3C',INK='1A1A1A',CREAM='F7F5EF',WHITE='FFFFFF',GREY='6B7280',BORD='D9D5C8';
const FONT='Calibri', CW=9648;
const C=JSON.parse(fs.readFileSync('analysis/unit1_content.json','utf8'));
const U=C.unit; const BRAND=U.brand||'Course'; const BRANDTM=BRAND+'™'; const BRANDUP=BRANDTM.toUpperCase();
const UNITLABEL=(U.code||'Unit 1')+' — '+(U.title||'');
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
 organizer('★ Tennessee Connection — Local ↔ Global','Whenever a standard has a Tennessee tie: link the world event or idea to our state/community and say why the local story matters. This local-to-global move is a World History Hack signature — use it whenever a genuine tie exists.',tnOrg()),
];

// ---------- PART 2: Unit 1 pre-labeled (best-fit per standard) ----------
const PART2=[
 organizer('W.01 — Absolutism: Louis XIV vs. Peter the Great (Matrix)','The standard compares two absolute monarchs. A compare-and-contrast matrix lines them up on the same criteria so the similarities (total power) and differences (tradition vs. westernization) are explicit.',matrix(['Ruler','How power was used','Signature project','One strength','One weakness'],['Louis XIV (France)','Peter the Great (Russia)'],2)),
 organizer('W.02 — Magna Carta vs. English Bill of Rights (Venn)','The standard compares two documents that limited the monarch. A Venn captures what each did alone and what both shared (the rule of law and a limited crown).',venn2('Only Magna Carta (1215)','Both limit the monarch','Only English Bill of Rights (1689)')),
 organizer('W.03 — Enlightenment Thinkers (Matrix)','The standard compares four philosophers. A matrix pairs each thinker with their key work, main idea, and view of government — the highest-yield way to compare 3+ items on set criteria.',matrix(['Thinker','Key work','Main idea','View of government'],['Hobbes','Locke','Montesquieu','Rousseau'],2)),
 organizer('W.04 — The English Civil War → Constitutional Monarchy (Timeline)','The standard traces causes and consequences across time. A timeline makes the sequence visible: clashes between king and Parliament → civil war (1640s) → execution of Charles I (1649) → Commonwealth → Restoration → Glorious Revolution (1688) → constitutional monarchy.',timeline()),
 organizer('W.04 — Causes → Consequences of the English Civil War (Cause & Effect)','A cause → effect flow shows how each grievance (taxes, religion, king vs. Parliament) drove the conflict and its outcomes.',causeEffect()),
 organizer('W.08a — Enlightenment Idea → Declaration Wording (T-Chart)','The standard asks students to trace ideas into a document. A T-chart maps each Enlightenment idea (Locke’s natural rights, consent of the governed) to where it appears in the Declaration of Independence.',tchart('Enlightenment idea (Locke, Rousseau…)','Where it appears in the Declaration of Independence')),
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
const header=new Header({children:[P(R(`${BRANDTM} · ${U.code||'Unit 1'} · Teacher Graphic Organizer Toolkit`,{s:16,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0},children:[R(`${BRANDTM} · ${U.code||'Unit 1'} (Course Standard) © 2026 TroopToTeacher Technologies LLC   |   Page `,{s:16,c:GREY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GREY,font:FONT})]})]});

const cover=[
 new Paragraph({spacing:{before:1400,after:0},children:[R(BRANDUP,{s:30,b:true,c:GOLD})]}),
 new Paragraph({spacing:{after:0},children:[R('Teacher Graphic Organizer Toolkit',{s:52,b:true,c:NAVY})]}),
 new Paragraph({spacing:{after:200},children:[R(`${UNITLABEL}  ·  Reproducible`,{s:26,c:INK})]}),
 callout('WHY THIS TOOLKIT',['Knowing WHICH organizer to use, and WHEN, is half the battle. This toolkit tells you — with a brief why for each — then gives you reproducible blanks (Part 1) and '+(U.code||'Unit 1')+' ready-to-print, pre-labeled organizers (Part 2). Tennessee connections are highlighted where a genuine tie exists; the local-to-global move is a World History Hack signature and a point of difference for our classrooms.']),
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
