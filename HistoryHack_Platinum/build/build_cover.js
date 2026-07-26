// Unit 1 — Professional COVER WRAP (front · spine · back) + print/listing spec.
// Sale-ready book cover for online sales + professional printing. Platinum branding.
// Copy reflects the platinum system: UDL 3.0, MTSS, CER, Cornell, HIPPO, DOK, standards-aligned.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,AlignmentType,Table,TableRow,TableCell,WidthType,
  BorderStyle,ShadingType,HeightRule,ImageRun,TextDirection,VerticalAlign}=D;
const C=JSON.parse(fs.readFileSync('analysis/unit1_content.json','utf8'));
const NAVY='1B2A4A',RED='B22234',GOLD='C89B3C',INK='1A1A1A',CREAM='F7F5EF',WHITE='FFFFFF',GREY='6B7280',BORD='D9D5C8',FONT='Calibri';
// letter trim, thin margins for a full-bleed look
const PW=12240,PH=15840,MAR=560, CW=PW-2*MAR;
const HERO='assets/primary_sources/transcontinental-railroad-ceremony.jpg';

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
function rule(w=CW,c=GOLD){return new Table({width:{size:w,type:WidthType.DXA},columnWidths:[w],alignment:AlignmentType.CENTER,
  rows:[new TableRow({height:{value:26,rule:HeightRule.EXACTLY},children:[new TableCell({width:{size:w,type:WidthType.DXA},shading:{type:ShadingType.CLEAR,fill:GOLD,color:'auto'},borders:noB,children:[P(R(' ',{s:2}),{spacing:{after:0}})]})]})]});}
function badge(text){return new TableCell({width:{size:Math.floor((CW-1000)/6),type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,
  shading:{type:ShadingType.CLEAR,fill:NAVY,color:'auto'},borders:{top:bd(GOLD,6),bottom:bd(GOLD,6),left:bd(GOLD,6),right:bd(GOLD,6)},
  margins:{top:70,bottom:70,left:40,right:40},children:[P(R(text,{s:17,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:0}})]});}
function badgeRow(items){const w=Math.floor((CW-1000)/6);
  return new Table({width:{size:CW,type:WidthType.DXA},alignment:AlignmentType.CENTER,columnWidths:items.map(()=>w),
    rows:[new TableRow({children:items.map(badge)})]});}

// ---------- FRONT COVER ----------
const heroImg=new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:120},children:[
  new ImageRun({data:fs.readFileSync(HERO),transformation:{width:560,height:400},
    altText:{title:'Cover image',description:'Golden Spike Ceremony at Promontory Summit, 1869',name:'cover'}})]});
const front=fullPanel([
  P(R('U.S. HISTORY HACK™',{s:30,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:40}}),
  P(R('COURSE STANDARD  ·  PLATINUM EDITION',{s:19,b:true,c:WHITE,caps:true}),{align:AlignmentType.CENTER,spacing:{after:220}}),
  P(R('THE RISE OF',{s:60,b:true,c:WHITE,caps:true}),{align:AlignmentType.CENTER,spacing:{after:0}}),
  P(R('INDUSTRIALIZATION',{s:60,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:20}}),
  P(R('1877 – 1900',{s:30,b:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:60}}),
  new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:40},border:{top:{style:BorderStyle.SINGLE,size:12,color:GOLD,space:6},bottom:{style:BorderStyle.SINGLE,size:12,color:GOLD,space:6}},children:[R('  Unit 1  ·  High-School U.S. History  ·  Standards-Aligned  ',{s:20,b:true,c:WHITE})]}),
  heroImg,
  P(R('STUDENT WORKBOOK',{s:34,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{before:60,after:60}}),
  badgeRow(['UDL 3.0','MTSS','CER','Cornell','HIPPO','DOK']),
  P(R('Universal Design for Learning  ·  Multi-Tiered Supports  ·  Evidence-Based Writing',{s:16,i:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{before:120,after:0}}),
  P(R('TroopToTeacher Technologies LLC',{s:20,b:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{before:200,after:0}}),
],{fill:NAVY});

// ---------- SPINE ----------
const spineTxt=new TableCell({width:{size:900,type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,
  textDirection:TextDirection.BOTTOM_TO_TOP_LEFT_TO_RIGHT,shading:{type:ShadingType.CLEAR,fill:NAVY,color:'auto'},borders:noB,
  margins:{top:200,bottom:200,left:60,right:60},
  children:[new Paragraph({alignment:AlignmentType.CENTER,children:[
    R('U.S. HISTORY HACK™   ',{s:26,b:true,c:GOLD,caps:true}),
    R('Unit 1 — The Rise of Industrialization (1877–1900)      ',{s:22,b:true,c:WHITE}),
    R('Student Workbook   ·   TroopToTeacher Technologies LLC',{s:18,b:true,c:GOLD})]})]});
const spine=new Table({width:{size:900,type:WidthType.DXA},alignment:AlignmentType.CENTER,columnWidths:[900],
  rows:[new TableRow({height:{value:PH-2*MAR,rule:HeightRule.ATLEAST},children:[spineTxt]})]});
const spineNote=[
  P(R('SPINE  (shown at width for a perfect-bound book)',{s:20,b:true,c:NAVY}),{spacing:{before:160,after:60}}),
  P(R('Spine width scales with page count and paper. For this 90-page interior on 60-lb (90 gsm) white offset, the spine is ≈ 0.20 in (5.1 mm). Recompute if the page count or paper changes: white 60-lb ≈ 0.002252 in/page; cream 60-lb ≈ 0.0025 in/page. At ≈ 0.20 in the book is perfect-bindable; below ~0.10 in (≈ 46 pp) use saddle-stitch and drop the spine text.',{s:19,c:INK})),
];

// ---------- BACK COVER ----------
const sellBullets=[
  ['Built on UDL 3.0 (CAST).','Every activity offers multiple means of engagement, representation, and action — word banks, sentence frames, visuals, and choice built in, so the rigor stays the same for every learner.'],
  ['MTSS tiers on every page.','Core instruction with layered Guided and Light Support, plus a formative Exit Ticket for each standard and a “What’s Next” reteach path in the Teacher Edition.'],
  ['Writes like a historian — CER.','A 6-point Claim–Evidence–Reasoning rubric runs through the whole course, with scaffolded organizers and lined response space.'],
  ['Real primary sources, cited.','Photographs, political cartoons, and maps from the Library of Congress and National Archives — analyzed with the HIPPO routine — every source documented to Chicago style.'],
  ['Cornell notes paired to the slide deck.','Structured note pages capture the direct-teaching slides, with retrieval checks and doodle zones for visual learners.'],
  ['Standards-aligned & TCAP-ready.','DOK-balanced checks and a companion Assessment Book with two parallel forms, keyed to the standards and reporting categories.'],
];
const back=fullPanel([
  P(R('U.S. HISTORY HACK™',{s:22,b:true,c:GOLD,caps:true}),{align:AlignmentType.CENTER,spacing:{after:20}}),
  P(R('The workbook that teaches every learner — without lowering the bar.',{s:26,b:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:40}}),
  P(R('Unit 1 — The Rise of Industrialization (1877–1900)',{s:19,i:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:20}}),
],{fill:NAVY,h:2000,valign:VerticalAlign.CENTER});
// back body (cream)
const stdList=C.order.map(c=>P([R(`${c}  `,{s:19,b:true,c:RED}),R(C.standards[c].title,{s:19,c:INK})],{spacing:{after:34}}));
const barcodeBox=new Table({width:{size:3200,type:WidthType.DXA},alignment:AlignmentType.RIGHT,columnWidths:[3200],
  rows:[new TableRow({height:{value:1500,rule:HeightRule.ATLEAST},children:[new TableCell({width:{size:3200,type:WidthType.DXA},
    verticalAlign:VerticalAlign.CENTER,borders:{top:bd(INK,6),bottom:bd(INK,6),left:bd(INK,6),right:bd(INK,6)},
    children:[P(R('ISBN barcode',{s:18,b:true,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:10}}),
      P(R('ISBN 978-X-XXXXX-XXX-X',{s:16,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:0}}),
      P(R('placeholder — replace at print',{s:14,i:true,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:0}})]})]})]});
const backBody=[
  P(R('WHAT MAKES THIS WORKBOOK DIFFERENT',{s:22,b:true,c:NAVY,caps:true}),{spacing:{before:200,after:100}}),
  ...sellBullets.flatMap(([h,b])=>[P([R('◆  ',{s:20,b:true,c:GOLD}),R(h+'  ',{s:20,b:true,c:NAVY}),R(b,{s:19,c:INK})],{spacing:{after:90}})]),
  P(R('INSIDE THIS UNIT — the seven standards',{s:21,b:true,c:NAVY,caps:true}),{spacing:{before:120,after:80}}),
  ...stdList,
  P(R('Part of the U.S. History Hack™ Course Standard series — a complete, standards-aligned system: Student Workbook · Teacher Edition · Student & Teacher Slide Decks · Graphic Organizer Toolkit · Unit Assessment Book.',{s:19,i:true,c:INK}),{spacing:{before:120,after:120}}),
];
const backFooter=new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[CW-3400,3400],
  rows:[new TableRow({children:[
    cell([
      P(R('TroopToTeacher Technologies LLC',{s:20,b:true,c:NAVY}),{spacing:{after:24}}),
      P(R('U.S. History Hack™  ·  Course Standard (Platinum) Edition',{s:18,c:INK}),{spacing:{after:24}}),
      P(R('© 2026 TroopToTeacher Technologies LLC. All rights reserved. U.S. History Hack™ is a trademark of TroopToTeacher Technologies LLC. No part of this book may be reproduced without written permission, except as licensed for classroom use.',{s:15,c:GREY}),{spacing:{after:20}}),
      P([R('www.trooptoteacher.com',{s:17,b:true,c:NAVY}),R('   ·   Printed in the U.S.A.   ·   First Edition',{s:16,c:GREY})],{spacing:{after:0}}),
    ],{w:CW-3400,valign:VerticalAlign.BOTTOM}),
    cell([barcodeBox],{w:3400,valign:VerticalAlign.BOTTOM}),
  ]})]});

// ---------- PRINT & LISTING SPEC (handoff) ----------
const kw='U.S. history workbook, high school history, UDL curriculum, MTSS, CER writing, primary source analysis, Cornell notes, standards-aligned, Gilded Age, industrialization, TCAP review';
const spec=[
  P(R('PRINT & ONLINE-LISTING SPEC',{s:30,b:true,c:NAVY,caps:true}),{spacing:{before:100,after:40}}),
  rule(CW),
  P(R('An internal handoff sheet for your printer and your storefront listing — not part of the printed book.',{s:19,i:true,c:GREY}),{spacing:{before:100,after:120}}),
  ...[
    ['Title (listing)','U.S. History Hack™ — Unit 1: The Rise of Industrialization (1877–1900) · Student Workbook'],
    ['Series','U.S. History Hack™ Course Standard (Platinum) Edition'],
    ['Publisher / Author','TroopToTeacher Technologies LLC'],
    ['Trim size','8.5 × 11 in (US Letter) — consumable workbook'],
    ['Interior','90 pages, black-and-white, 60-lb (90 gsm) white offset'],
    ['Spine width','≈ 0.20 in (5.1 mm) at 90 pp — perfect-bound; recompute if page count changes'],
    ['Cover stock','10-pt or 12-pt C1S gloss/matte laminate; full color'],
    ['Bleed','Add 0.125 in bleed on all outside edges before sending to print (this concept is at trim).'],
    ['Copyright','© 2026 TroopToTeacher Technologies LLC. All rights reserved.'],
    ['ISBN','Assign one ISBN per format (paperback / PDF); place barcode in the back-cover box.'],
    ['Age / grade','Grades 9–12 · U.S. History'],
    ['Categories','Education › Teaching Methods & Materials › Social Science; Study Aids › History'],
    ['Keywords',kw],
  ].map(([k,v])=>new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[2600,CW-2600],
    rows:[new TableRow({children:[
      cell(P(R(k,{s:19,b:true,c:NAVY}),{spacing:{after:0}}),{w:2600,fill:CREAM,borders:{top:bd(BORD,4),bottom:bd(BORD,4),left:bd(BORD,4),right:bd(BORD,4)}}),
      cell(P(R(v,{s:19,c:INK}),{spacing:{after:0}}),{w:CW-2600,borders:{top:bd(BORD,4),bottom:bd(BORD,4),left:bd(BORD,4),right:bd(BORD,4)}})]})]})),
  P(R('BACK-COVER BLURB (for your storefront)',{s:21,b:true,c:NAVY,caps:true}),{spacing:{before:180,after:70}}),
  P(R('U.S. History Hack™ turns a full unit of high-school U.S. History into one student-ready workbook that reaches every learner without lowering the bar. Built on Universal Design for Learning (UDL 3.0) and Multi-Tiered Systems of Support (MTSS), each of the seven standards moves from a core lesson to Cornell notes paired with the slide deck, real Library-of-Congress primary sources analyzed with HIPPO, evidence-based writing on a 6-point CER rubric, and a formative Exit Ticket with a built-in reteach path. Standards-aligned, DOK-balanced, and TCAP-ready — with a companion Assessment Book of two parallel forms. Unit 1 covers the Rise of Industrialization, 1877–1900.',{s:19,c:INK}),{spacing:{after:0}}),
];

const doc=new Document({styles:{default:{document:{run:{font:FONT,size:22,color:INK}}}},
  sections:[
    {properties:{page:{size:{width:PW,height:PH},margin:{top:MAR,bottom:MAR,left:MAR,right:MAR}}},children:[front]},
    {properties:{page:{size:{width:PW,height:PH},margin:{top:MAR,bottom:MAR,left:MAR,right:MAR}}},children:[spine,...spineNote]},
    {properties:{page:{size:{width:PW,height:PH},margin:{top:MAR,bottom:MAR,left:MAR,right:MAR}}},children:[back,...backBody,backFooter]},
    {properties:{page:{size:{width:PW,height:PH},margin:{top:1000,bottom:1000,left:1200,right:1200}}},children:spec},
  ]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('deliverables/Unit1_Cover_Wrap.docx',b);console.log('WROTE cover wrap',b.length,'bytes');});
