#!/usr/bin/env python3
"""Build well-laid-out A4 study PDFs from source-grounded Markdown summaries."""
from __future__ import annotations

from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, KeepTogether, HRFlowable
)

ROOT=Path(__file__).resolve().parents[2]
CONTENT_ROOT=ROOT / "econometrie-s5-2026"
SRC=CONTENT_ROOT / "resumes-src"
OUT=CONTENT_ROOT / "resumes"
OUT.mkdir(parents=True,exist_ok=True)
SUBJECTS=[
    "microeconomie","tests-hypotheses","croissance-economique","anglais","ia-ro"
]
PAGE_W,PAGE_H=A4
LEFT=49
RIGHT=49
TOP=94
BOTTOM=57
TEXT_WIDTH=PAGE_W-LEFT-RIGHT

def register_fonts():
    fonts=[
        ("DVS","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ("DVS-Bold","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ]
    for name,path in fonts:
        if not Path(path).is_file():
            raise RuntimeError("Required Liberation/DejaVu font unavailable: "+path)
        pdfmetrics.registerFont(TTFont(name,path))
    pdfmetrics.registerFontFamily("DVS",normal="DVS",bold="DVS-Bold")

register_fonts()
NAVY=colors.HexColor("#102235")
DEEP=colors.HexColor("#172F44")
TEAL=colors.HexColor("#009E96")
MUTED=colors.HexColor("#596E7E")
RULE=colors.HexColor("#CEDDDE")
SOFT=colors.HexColor("#F2F7F8")
BLACK=colors.HexColor("#233648")

STYLES={
    "title":ParagraphStyle("Title",fontName="DVS-Bold",fontSize=20.5,leading=27.5,textColor=NAVY,spaceAfter=14),
    "intro":ParagraphStyle("Intro",fontName="DVS",fontSize=9.8,leading=16,textColor=MUTED,spaceAfter=12),
    "h2":ParagraphStyle("H2",fontName="DVS-Bold",fontSize=12.3,leading=17,textColor=TEAL,spaceBefore=16,spaceAfter=8,keepWithNext=True),
    "h3":ParagraphStyle("H3",fontName="DVS-Bold",fontSize=10.3,leading=14.3,textColor=DEEP,spaceBefore=10,spaceAfter=6,keepWithNext=True),
    "body":ParagraphStyle("Body",fontName="DVS",fontSize=8.75,leading=14.5,textColor=BLACK,spaceAfter=6),
    "bullet":ParagraphStyle("Bullet",fontName="DVS",fontSize=8.65,leading=14,textColor=BLACK,spaceAfter=4,leftIndent=14,firstLineIndent=-9),
    "small":ParagraphStyle("Small",fontName="DVS",fontSize=7.6,leading=11.5,textColor=MUTED,spaceAfter=3),
    "tablehead":ParagraphStyle("Th",fontName="DVS-Bold",fontSize=7.25,leading=10.3,textColor=NAVY),
    "tablecell":ParagraphStyle("Tc",fontName="DVS",fontSize=7.15,leading=10.5,textColor=BLACK),
}

def inline_markup(value:str)->str:
    """Escape user-controlled Markdown while supporting bold / italic emphasis."""
    pieces=re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|\\`[^\\`]+\\`)",value.strip())
    result=[]
    for fragment in pieces:
        if fragment.startswith("**") and fragment.endswith("**"):
            result.append("<b>"+html.escape(fragment[2:-2])+"</b>")
        elif fragment.startswith("*") and fragment.endswith("*"):
            result.append("<i>"+html.escape(fragment[1:-1])+"</i>")
        elif fragment.startswith("`") and fragment.endswith("`"):
            result.append("<font color='#075B65'>"+html.escape(fragment[1:-1])+"</font>")
        else:
            result.append(html.escape(fragment))
    return "".join(result)

def paragraph(text:str,style:str="body"):
    return Paragraph(inline_markup(text).replace("\n","<br/>"),STYLES[style])

def is_table_row(x:str)->bool:
    x=x.strip()
    return x.startswith("|") and x.endswith("|") and x.count("|")>=3

def table_block(rows:list[str]):
    matrix=[]
    for row in rows:
        items=[x.strip() for x in row.strip().strip("|").split("|")]
        if all(re.match(r"^:?-{3,}:?$",x) for x in items):continue
        matrix.append(items)
    if len(matrix)<2:return [paragraph(" ".join(rows))]
    cols=max(map(len,matrix))
    if cols>6:return [paragraph(" ".join(rows))]
    colw=TEXT_WIDTH/cols
    tbl=[]
    for i,row in enumerate(matrix):
        tbl.append([paragraph(row[j] if j<len(row) else "","tablehead" if i==0 else "tablecell") for j in range(cols)])
    t=Table(tbl,colWidths=[colw]*cols,repeatRows=1,hAlign="LEFT",splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E9F5F3")),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,SOFT]),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("TOPPADDING",(0,0),(-1,-1),7),
        ("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("LEFTPADDING",(0,0),(-1,-1),7),
        ("RIGHTPADDING",(0,0),(-1,-1),7),
        ("LINEBELOW",(0,0),(-1,0),0.8,TEAL),
        ("LINEBELOW",(0,1),(-1,-1),0.3,RULE),
    ]))
    return [Spacer(1,6),t,Spacer(1,9)]

def to_story(md:str):
    lines=md.replace("\r\n","\n").split("\n")
    story=[]
    first=True
    i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1
            continue
        if line.startswith("# "):
            if first:
                story.append(paragraph(line[2:],"title"))
                first=False
            else:story.append(paragraph(line[2:],"h2"))
            i+=1
            continue
        if line.startswith("## "):
            story.append(paragraph(line[3:],"h2"))
            i+=1
            continue
        if line.startswith("### "):
            story.append(paragraph(line[4:],"h3"))
            i+=1
            continue
        if is_table_row(line):
            rows=[]
            while i<len(lines) and is_table_row(lines[i]):
                rows.append(lines[i])
                i+=1
            story.extend(table_block(rows))
            continue
        if line.startswith("- ") or re.match(r"^\d+[.)] ",line):
            bullet=line[2:] if line.startswith("- ") else re.sub(r"^\d+[.)]\s*","",line)
            mark="&#8226; " if line.startswith("- ") else html.escape(re.match(r"^\d+[.)]",line).group(0))+" "
            story.append(Paragraph(mark+inline_markup(bullet),STYLES["bullet"]))
            i+=1
            continue
        if line.startswith("---"):
            story.append(HRFlowable(width="100%",color=RULE,thickness=0.5,spaceBefore=9,spaceAfter=9))
            i+=1
            continue
        paragraph_lines=[line]
        i+=1
        while i<len(lines):
            nxt=lines[i].strip()
            if not nxt or nxt.startswith("#") or nxt.startswith("- ") or is_table_row(nxt) or re.match(r"^\d+[.)] ",nxt):
                break
            paragraph_lines.append(nxt)
            i+=1
        txt=" ".join(paragraph_lines)
        style="intro" if txt.startswith("*Fiche") else "body"
        story.append(paragraph(txt,style))
    return story

def decorate(canvas,doc):
    canvas.saveState()
    w,h=A4
    canvas.setFillColor(NAVY)
    canvas.rect(0,h-55,w,55,stroke=0,fill=1)
    canvas.setFillColor(colors.HexColor("#7CE9DC"))
    canvas.rect(0,h-59,w,4,stroke=0,fill=1)
    canvas.setFont("DVS-Bold",13)
    canvas.setFillColor(colors.white)
    canvas.drawString(LEFT,h-34,"UNIVCOURS")
    canvas.setFont("DVS",8)
    canvas.setFillColor(colors.HexColor("#BFE8E5"))
    canvas.drawRightString(w-RIGHT,h-32,"ÉCONOMÉTRIE S5 · FICHE DE RÉVISION")
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(LEFT,43,w-RIGHT,43)
    canvas.setFont("DVS",7.0)
    canvas.setFillColor(MUTED)
    canvas.drawString(LEFT,29,"Synthèse pédagogique des documents déposés sur UnivCours")
    canvas.drawRightString(w-RIGHT,29,f"Page {doc.page}")
    canvas.restoreState()

def build_one(subject:str):
    source=SRC/(subject+".md")
    if not source.exists():raise FileNotFoundError(source)
    target=OUT/(subject+".pdf")
    doc=BaseDocTemplate(str(target),pagesize=A4,leftMargin=LEFT,rightMargin=RIGHT,topMargin=TOP,bottomMargin=BOTTOM,
                        title="UnivCours - Résumé "+subject,author="UnivCours - Fiches de révision",
                        subject="Licence Économétrie S5 : synthèse des PDF partagés")
    frame=Frame(LEFT,BOTTOM,TEXT_WIDTH,PAGE_H-TOP-BOTTOM,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="normal",frames=[frame],onPage=decorate)])
    story=to_story(source.read_text(encoding="utf-8"))
    if len(story)<10:raise ValueError("Source summary too short: "+subject)
    doc.build(story)
    magic=target.read_bytes()[:5]
    if magic!=b"%PDF-":raise ValueError("Not a PDF: "+subject)
    print("BUILT",subject,target.stat().st_size,"bytes",flush=True)
    return target

if __name__=="__main__":
    built=[build_one(s) for s in SUBJECTS]
    print("FINISHED",len(built),"STUDY PDF FILES",flush=True)
