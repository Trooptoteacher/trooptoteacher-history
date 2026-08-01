// Unit 3 — Professional COVER WRAPS (front · spine · back + spec) for EVERY book.
// One sale-ready wrap per deliverable: Student Workbook, Teacher Edition, Assessment
// Book, Graphic Organizer Toolkit. Brand: navy + red + gold. © TroopToTeacher.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,AlignmentType,Table,TableRow,TableCell,WidthType,
  BorderStyle,ShadingType,HeightRule,ImageRun,TextDirection,VerticalAlign}=D;
const C=JSON.parse(fs.readFileSync('analysis/unit3_content.json','utf8'));
const NAVY='1B2A4A',RED='B22234',GOLD='C89B3C',INK='1A1A1A',CREAM='F7F5EF',WHITE='FFFFFF',GREY='6B7280',BORD='D9D5C8',FONT='Calibri';
const PW=12240,PH=15840,MAR=560, CW=PW-2*MAR;
const HERO='analysis/assets/hero.jpg'; const HERO_W=1200, HERO_H=967;
const HERO_CRED='Col. Theodore Roosevelt and the Rough Riders, San Juan Heights, 1898 · Library of Congress · Public domain';  // no verified public-domain hero image for this unit — typographic cover

function R(t,{s=22,b=false,i=false,c=INK,caps=false}={}){return new TextRun({text:t,size:s,bold:b,italics:i,color:c,font:FONT,allCaps:caps});}
function P(runs,{align=AlignmentType.LEFT,spacing,indent}={}){return new Paragraph({alignment:align,spacing:spacing||{after:80},indent,children:Array.isArray(runs)?runs:[runs]});}
const bd=(c,sz=8)=>({style:BorderStyle.SINGLE,size:sz,color:c,space:0});
const noB={top:{style:BorderStyle.NONE},bottom:{style:BorderStyle.NONE},left:{style:BorderStyle.NONE},right:{style:BorderStyle.NONE}};
function cell(children,{w,fill,valign,borders,margins}={}){return new TableCell({width:{size:w,type:WidthType.DXA},verticalAlign:valign,
  shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,margins:margins||{top:80,bottom:80,left:120,right:120},
  borders:borders||noB,children:Array.isArray(children)?children:[children]});}
function fullPanel(kids,{fill=NAVY,h=PH-2*MAR,valign=VerticalAlign.CENTER}={}){
  return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[CW],
    rows:[new TableRow({height:{value:h,rule:HeightRule.ATLEAST},children:[cell(kids,{w:CW,fill,valign,margins:{top:340,bottom:340,left:520,right:520}})]})]});}
function rule(w=CW,c=GOLD,h=26,align=AlignmentType.LEFT){return new Table({width:{size:w,type:WidthType.DXA},columnWidths:[w],alignment:align,
  rows:[new TableRow({height:{value:h,rule:HeightRule.EXACTLY},children:[new TableCell({width:{size:w,type:WidthType.DXA},shading:{type:ShadingType.CLEAR,fill:c,color:'auto'},borders:noB,children:[P(R(' ',{s:2}),{spacing:{after:0}})]})]})]});}
function bandBar(text,fill,tc,size){const w=CW-1200;return new Table({width:{size:w,type:WidthType.DXA},alignment:AlignmentType.CENTER,columnWidths:[w],
  rows:[new TableRow({children:[new TableCell({width:{size:w,type:WidthType.DXA},shading:{type:ShadingType.CLEAR,fill,color:'auto'},borders:noB,
    margins:{top:90,bottom:90,left:120,right:120},children:[P(R(text,{s:size||32,b:true,c:tc,caps:true}),{align:AlignmentType.CENTER,spacing:{after:0}})]})]})]});}
function badge(text){return new TableCell({width:{size:Math.floor((CW-1000)/6),type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,
  shading:{type:ShadingType.CLEAR,fill:NAVY,color:'auto'},borders:{top:bd(GOLD,6),bottom:bd(GOLD,6),left:bd(GOLD,6),right:bd(GOLD,6)},
  margins:{top:70,bottom:70,left:40,right:40},children:[P(R(text,{s:17,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:0}})]});}
function badgeRow(items){const w=Math.floor((CW-1000)/6);
  return new Table({width:{size:CW,type:WidthType.DXA},alignment:AlignmentType.CENTER,columnWidths:items.map(()=>w),
    rows:[new TableRow({children:items.map(badge)})]});}

const BADGES=['UDL 3.0','MTSS','CER','Cornell','HIPPO','DOK'];
const stdList=()=>C.order.map(c=>P([R(`${c}  `,{s:19,b:true,c:RED}),R(C.standards[c].title,{s:19,c:INK})],{spacing:{after:34}}));
function barcodeBox(){return new Table({width:{size:3200,type:WidthType.DXA},alignment:AlignmentType.RIGHT,columnWidths:[3200],
  rows:[new TableRow({height:{value:1500,rule:HeightRule.ATLEAST},children:[new TableCell({width:{size:3200,type:WidthType.DXA},
    verticalAlign:VerticalAlign.CENTER,borders:{top:bd(INK,6),bottom:bd(INK,6),left:bd(INK,6),right:bd(INK,6)},
    children:[P(R('ISBN barcode',{s:18,b:true,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:10}}),
      P(R('ISBN 978-X-XXXXX-XXX-X',{s:16,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:0}}),
      P(R('placeholder — replace at print',{s:14,i:true,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:0}})]})]})]});}

// spine width math: white 60-lb offset ≈ 0.002252 in/page; perfect-bind at ≥ ~48 pp
function spineInfo(pages){const win=+(pages*0.002252).toFixed(3); const mm=+(win*25.4).toFixed(1);
  const perfect=pages>=48; return {win,mm,perfect};}

function buildCover(spec){
  const S=spineInfo(spec.pages);
  let _hw=600, _hh=Math.round(HERO_H*(_hw/HERO_W)); if(_hh>470){_hh=470;_hw=Math.round(HERO_W*(_hh/HERO_H));}
  const heroImg=(HERO && fs.existsSync(HERO))
    ? [new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:30},
        border:{top:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:8},bottom:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:8}},
        children:[new ImageRun({data:fs.readFileSync(HERO),transformation:{width:_hw,height:_hh},altText:{title:'Cover image',description:HERO_CRED,name:'cover-hero'}})]}),
       P(R(HERO_CRED,{s:14,i:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:120}})]
    : [new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:120},border:{top:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:10},bottom:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:10}},children:[R('SEMIQUINCENTENNIAL  ·  1776–2026',{s:22,b:true,c:GOLD,caps:true})]})];
  // FRONT
  const front=fullPanel([
    P(R('U.S. HISTORY HACK™',{s:30,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:26}}),
    bandBar('COURSE STANDARD  ·  PLATINUM EDITION',RED,WHITE,17),
    P(R('',{s:10}),{spacing:{after:170}}),
    P(R('IMPERIALISM &',{s:52,b:true,c:WHITE,caps:true}),{align:AlignmentType.CENTER,spacing:{after:0}}),
    P(R('WORLD WAR I',{s:52,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:20}}),
    P(R('1890–1920',{s:30,b:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:60}}),
    new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:40},border:{top:{style:BorderStyle.SINGLE,size:14,color:RED,space:6},bottom:{style:BorderStyle.SINGLE,size:14,color:RED,space:6}},children:[R('  Unit 3  ·  High-School U.S. History  ·  Standards-Aligned  ',{s:20,b:true,c:WHITE})]}),
    ...heroImg,
    bandBar(spec.designation,RED,WHITE,spec.designation.length>18?26:34),
    P(R('',{s:10}),{spacing:{after:70}}),
    badgeRow(BADGES),
    P(R('Universal Design for Learning  ·  Multi-Tiered Supports  ·  Evidence-Based Writing',{s:16,i:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{before:120,after:spec.audience.toUpperCase()===spec.designation.toUpperCase()?0:20}}),
    ...(spec.audience.toUpperCase()===spec.designation.toUpperCase()?[]:[P(R(spec.audience,{s:18,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:0}})]),
    P(R('TroopToTeacher Technologies LLC',{s:20,b:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{before:140,after:0}}),
  ],{fill:NAVY});
  // SPINE
  const spineTxt=new TableCell({width:{size:900,type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,
    textDirection:TextDirection.BOTTOM_TO_TOP_LEFT_TO_RIGHT,shading:{type:ShadingType.CLEAR,fill:NAVY,color:'auto'},borders:noB,
    margins:{top:200,bottom:200,left:60,right:60},
    children:[new Paragraph({alignment:AlignmentType.CENTER,children:[
      R('U.S. HISTORY HACK™   ',{s:26,b:true,c:GOLD,caps:true}),
      R('Unit 3 — Imperialism and World War I (1890–1920)      ',{s:22,b:true,c:WHITE}),
      R(`${spec.designation}   ·   TroopToTeacher Technologies LLC`,{s:18,b:true,c:GOLD})]})]});
  const spine=new Table({width:{size:900,type:WidthType.DXA},alignment:AlignmentType.CENTER,columnWidths:[900],
    rows:[new TableRow({height:{value:PH-2*MAR,rule:HeightRule.ATLEAST},children:[spineTxt]})]});
  const spineNote=[
    P(R('SPINE',{s:20,b:true,c:NAVY}),{spacing:{before:160,after:60}}),
    S.perfect
      ? P(R(`Perfect-bound. At ${spec.pages} pages on 60-lb (90 gsm) white offset the spine is ≈ ${S.win} in (${S.mm} mm) — wide enough to print the spine text above. Recompute if the page count or paper changes (white 60-lb ≈ 0.002252 in/page).`,{s:19,c:INK}))
      : P([R(`Saddle-stitch. `,{s:19,b:true,c:RED}),R(`At ${spec.pages} pages the folded spine is only ≈ ${S.win} in (${S.mm} mm) — too thin to print spine text; bind saddle-stitch (no printed spine). To get a printable spine, perfect-bind at ≥ ~48 pages, or combine thin teacher books into one volume. The spine panel above is provided for when this title is perfect-bound.`,{s:19,c:INK})]),
  ];
  // BACK
  const backTop=fullPanel([
    P(R('U.S. HISTORY HACK™',{s:22,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:20}}),
    P(R(spec.backHeadline,{s:26,b:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:40}}),
    P(R(`Unit 3 — Imperialism and World War I (1890–1920)  ·  ${spec.audience}`,{s:19,i:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:20}}),
  ],{fill:NAVY,h:2000,valign:VerticalAlign.CENTER});
  const backBody=[
    P(R(spec.backSectionTitle,{s:22,b:true,c:NAVY,caps:true}),{spacing:{before:200,after:30}}),
    rule(2400,RED,28),
    P(R('',{s:8}),{spacing:{after:60}}),
    ...spec.sellBullets.flatMap(([h,b])=>[P([R('◆  ',{s:20,b:true,c:RED}),R(h+'  ',{s:20,b:true,c:NAVY}),R(b,{s:19,c:INK})],{spacing:{after:90}})]),
    P(R('INSIDE THIS UNIT — the nine standards',{s:21,b:true,c:NAVY,caps:true}),{spacing:{before:120,after:30}}),
    rule(2400,RED,28),
    P(R('',{s:8}),{spacing:{after:50}}),
    ...stdList(),
    P(R('Part of the U.S. History Hack™ Course Standard series — a complete, standards-aligned system: Student Workbook · Teacher Edition · Student & Teacher Slide Decks · Graphic Organizer Toolkit · Unit Assessment Book.',{s:19,i:true,c:INK}),{spacing:{before:120,after:120}}),
  ];
  const backFooter=new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[CW-3400,3400],
    rows:[new TableRow({children:[
      cell([
        P(R('TroopToTeacher Technologies LLC',{s:20,b:true,c:NAVY}),{spacing:{after:24}}),
        P(R(`U.S. History Hack™  ·  Course Standard (Platinum) Edition  ·  ${spec.audience}`,{s:18,c:INK}),{spacing:{after:24}}),
        P(R('© 2026 TroopToTeacher Technologies LLC. All rights reserved. U.S. History Hack™ is a trademark of TroopToTeacher Technologies LLC. No part of this book may be reproduced without written permission, except as licensed for classroom use.',{s:15,c:GREY}),{spacing:{after:20}}),
        P([R('www.trooptoteacher.com',{s:17,b:true,c:NAVY}),R('   ·   Printed in the U.S.A.   ·   First Edition',{s:16,c:GREY})],{spacing:{after:0}}),
      ],{w:CW-3400,valign:VerticalAlign.BOTTOM}),
      cell([barcodeBox()],{w:3400,valign:VerticalAlign.BOTTOM}),
    ]})]});
  // SPEC
  const spec4=[
    P(R('PRINT & ONLINE-LISTING SPEC',{s:30,b:true,c:NAVY,caps:true}),{spacing:{before:100,after:40}}),
    rule(CW,GOLD,20),
    P(R('An internal handoff sheet for your printer and your storefront listing — not part of the printed book.',{s:19,i:true,c:GREY}),{spacing:{before:100,after:120}}),
    ...[
      ['Title (listing)',spec.listingTitle],
      ['Series','U.S. History Hack™ Course Standard (Platinum) Edition'],
      ['Publisher / Author','TroopToTeacher Technologies LLC'],
      ['Trim size','8.5 × 11 in (US Letter)'],
      ['Interior',`${spec.pages} pages, black-and-white, 60-lb (90 gsm) white offset`],
      ['Binding & spine', S.perfect
        ? `Perfect-bound; spine ≈ ${S.win} in (${S.mm} mm). Print spine text.`
        : `Saddle-stitch (no printed spine) at ${spec.pages} pp; spine ≈ ${S.win} in only. Perfect-bind at ≥ ~48 pp for a printable spine.`],
      ['Cover stock','10-pt or 12-pt C1S gloss/matte laminate; full color'],
      ['Bleed','Add 0.125 in bleed on all outside edges before print (this concept is at trim).'],
      ['Copyright','© 2026 TroopToTeacher Technologies LLC. All rights reserved.'],
      ['ISBN','Assign one ISBN per format (paperback / PDF); place barcode in the back-cover box.'],
      ['Age / grade','Grades 9–12 · U.S. History'],
      ['Categories','Education › Teaching Methods & Materials › Social Science; Study Aids › History'],
      ['Keywords',spec.keywords],
    ].map(([k,v])=>new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[2600,CW-2600],
      rows:[new TableRow({children:[
        cell(P(R(k,{s:19,b:true,c:NAVY}),{spacing:{after:0}}),{w:2600,fill:CREAM,borders:{top:bd(BORD,4),bottom:bd(BORD,4),left:bd(BORD,4),right:bd(BORD,4)}}),
        cell(P(R(v,{s:19,c:INK}),{spacing:{after:0}}),{w:CW-2600,borders:{top:bd(BORD,4),bottom:bd(BORD,4),left:bd(BORD,4),right:bd(BORD,4)}})]})]})),
    P(R('BACK-COVER BLURB (for your storefront)',{s:21,b:true,c:NAVY,caps:true}),{spacing:{before:180,after:70}}),
    P(R(spec.blurb,{s:19,c:INK}),{spacing:{after:0}}),
  ];

  const doc=new Document({styles:{default:{document:{run:{font:FONT,size:22,color:INK}}}},
    sections:[
      {properties:{page:{size:{width:PW,height:PH},margin:{top:MAR,bottom:MAR,left:MAR,right:MAR}}},children:[front]},
      {properties:{page:{size:{width:PW,height:PH},margin:{top:MAR,bottom:MAR,left:MAR,right:MAR}}},children:[spine,...spineNote]},
      {properties:{page:{size:{width:PW,height:PH},margin:{top:MAR,bottom:MAR,left:MAR,right:MAR}}},children:[backTop,...backBody,backFooter]},
      {properties:{page:{size:{width:PW,height:PH},margin:{top:1000,bottom:1000,left:1200,right:1200}}},children:spec4},
    ]});
  return Packer.toBuffer(doc).then(b=>{fs.writeFileSync(`deliverables/${spec.out}`,b);console.log('WROTE',spec.out,b.length,'bytes  ·',spec.pages,'pp ·',S.perfect?`perfect-bound spine ${S.win}in`:`saddle-stitch (${S.win}in)`);});
}

const SPECS=[
 {out:'Unit3_Cover_Student_Workbook.docx', designation:'STUDENT WORKBOOK', audience:'Student Edition', pages:99,
  backHeadline:'The workbook that teaches every learner — without lowering the bar.',
  backSectionTitle:'WHAT MAKES THIS WORKBOOK DIFFERENT',
  sellBullets:[
    ['Built on UDL 3.0 (CAST).','Every activity offers multiple means of engagement, representation, and action — word banks, sentence frames, visuals, and choice built in, so the rigor stays the same for every learner.'],
    ['MTSS tiers on every page.','Core instruction with layered Guided and Light Support, plus a formative Exit Ticket for each standard and a “What’s Next” reteach path in the Teacher Edition.'],
    ['Writes like a historian — CER.','A 6-point Claim–Evidence–Reasoning rubric runs through the whole course, with scaffolded organizers and lined response space.'],
    ['Real primary sources, cited.','Photographs, political cartoons, and maps from the Library of Congress and National Archives — analyzed with the HIPPO routine — every source documented to Chicago style.'],
    ['Cornell notes paired to the slide deck.','Structured note pages capture the direct-teaching slides, with retrieval checks and doodle zones for visual learners.'],
    ['Standards-aligned & TCAP-ready.','DOK-balanced checks and a companion Assessment Book with two parallel forms, keyed to the standards and reporting categories.'],
  ],
  listingTitle:'U.S. History Hack™ — Unit 3: Imperialism and World War I (1890–1920) · Student Workbook',
  keywords:'U.S. history workbook, high school history, UDL curriculum, MTSS, CER writing, primary source analysis, Cornell notes, standards-aligned, American imperialism, Spanish-American War, World War I, Wilson, Fourteen Points, Rough Riders, standards-aligned, TCAP review',
  blurb:'U.S. History Hack™ turns a full unit of high-school U.S. History into one student-ready workbook that reaches every learner without lowering the bar. Built on Universal Design for Learning (UDL 3.0) and Multi-Tiered Systems of Support (MTSS), each of the nine standards moves from a core lesson to Cornell notes paired with the slide deck, real Library-of-Congress primary sources analyzed with HIPPO, evidence-based writing on a 6-point CER rubric, and a formative Exit Ticket with a built-in reteach path. Standards-aligned, DOK-balanced, and TCAP-ready — with a companion Assessment Book of two parallel forms. Unit 3 covers Imperialism and World War I, 1890–1920.'},

 {out:'Unit3_Cover_Teacher_Edition.docx', designation:'TEACHER EDITION', audience:'Teacher Edition', pages:14,
  backHeadline:'Everything you need to teach the unit — with the supports already built in.',
  backSectionTitle:'WHAT’S IN THE TEACHER EDITION',
  sellBullets:[
    ['One standard, one period.','A pacing map with honest per-activity time estimates and a menu — you choose what fills the 45 minutes; the rest become bell-ringers, stations, or homework.'],
    ['The MTSS decision cycle.','Progress-monitor → identify barrier → select support → reteach → recheck → extend, with scaffold-fading guidance that never displaces IEP/504 accommodations.'],
    ['Crosswalks that pass review.','Standards & SSP crosswalk and a dimension-coverage crosswalk (C·E·G·H·P·T), plus a district review evidence snapshot.'],
    ['The 6-point CER rubric.','The same evidence-based-writing rubric used across the course, ready to score.'],
    ['Answer keys — teacher-side only.','Practice-quiz keys with rationales and exit-ticket keys with “What’s Next” reteach routing, kept separate from student copies.'],
    ['Deck + Cornell workflow.','How the Lean Student and Full Teacher decks pair with the workbook’s Cornell notes and primary-source analysis.'],
  ],
  listingTitle:'U.S. History Hack™ — Unit 3: Imperialism and World War I · Teacher How-to-Use & MTSS Guide',
  keywords:'teacher edition, lesson plans, MTSS, UDL, CER rubric, social studies practices, standards crosswalk, pacing guide, U.S. history, answer key',
  blurb:'The Teacher Edition for U.S. History Hack™ Unit 3 gives you the full teaching system: a one-standard-one-period pacing map with honest activity time estimates, the MTSS decision cycle, standards/SSP and dimension crosswalks, the 6-point CER rubric, teacher-side answer keys with reteach routing, and the deck-plus-Cornell workflow. Designed on UDL 3.0 so the rigor stays the same for every learner.'},

 {out:'Unit3_Cover_Assessment_Book.docx', designation:'ASSESSMENT BOOK', audience:'Teacher Edition', pages:21,
  backHeadline:'Formative + summative, parallel forms, keyed and ready to reteach.',
  backSectionTitle:'WHAT’S IN THE ASSESSMENT BOOK',
  sellBullets:[
    ['A checkpoint per standard.','Short, DOK-balanced formative checks for progress monitoring across US.01–US.07.'],
    ['Two parallel summative forms.','Form A and Form B for pre/post or retakes, built for minimal overlap.'],
    ['Keyed with item analysis.','Correct answer, DOK, reporting category, and distractor-based routing — teacher-side only.'],
    ['Reteach built in.','Each item maps to a “What’s Next” move tied to the workbook’s Cornell notes and Guided Support.'],
    ['From a real item bank.','Every item is pulled from the History Hack question bank; positions de-biased and synced across surfaces.'],
    ['Honest calibration status.','Items are classroom-formative and pre-field-test — the first cycle of use is what calibrates them.'],
  ],
  listingTitle:'U.S. History Hack™ — Unit 3: Imperialism and World War I · Assessment Book (Teacher)',
  keywords:'assessment, formative, summative, parallel forms, item analysis, reteach, DOK, reporting category, U.S. history, TCAP',
  blurb:'The Unit 3 Assessment Book gives you a formative checkpoint for each standard, two parallel summative forms (A and B) for pre/post or retakes, and a full teacher answer key with item analysis and reteach routing. Every item is drawn from the History Hack question bank, de-biased, and labeled classroom-formative · pre-field-test. Reproduce the student sections; keep the key section for yourself.'},

 {out:'Unit3_Cover_Organizer_Toolkit.docx', designation:'GRAPHIC ORGANIZER TOOLKIT', audience:'Teacher Edition', pages:39,
  backHeadline:'Reproducible thinking tools — blank and labeled, ready to print.',
  backSectionTitle:'WHAT’S IN THE TOOLKIT',
  sellBullets:[
    ['The organizers the course runs on.','Frayer, CER, HIPPO, Cornell, cause–effect, timeline, T-chart, Venn, and more — on brand and classroom-ready.'],
    ['Blank and labeled versions.','A blank for open use and a guided/labeled version for scaffolding — pick by learner need.'],
    ['UDL response choice.','Students write, diagram, or map their thinking — multiple means of action and expression by design.'],
    ['A quick-use guide.','When and how to reach for each organizer, tied to the workbook activities.'],
    ['Reproducible for your class.','Print as needed for licensed classroom use.'],
    ['Consistent across the course.','The same tools students meet in every unit, so routines transfer.'],
  ],
  listingTitle:'U.S. History Hack™ — Unit 3 · Teacher Graphic Organizer Toolkit',
  keywords:'graphic organizers, Frayer, CER, HIPPO, Cornell notes, cause and effect, timeline, UDL, reproducible, social studies',
  blurb:'The Graphic Organizer Toolkit collects the reproducible thinking tools the course runs on — Frayer, CER, HIPPO, Cornell, cause–effect, timeline, T-chart, Venn, and more — each in a blank and a labeled version, with a quick-use guide. Built on UDL so students can write, diagram, or map their thinking. Print as needed for your classroom.'},
];

(async()=>{ for(const s of SPECS) await buildCover(s); console.log('all covers built'); })();
