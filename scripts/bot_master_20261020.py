from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

OUT = Path("assets/2026-10-20")
OUT.mkdir(parents=True, exist_ok=True)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)

NAVY=(9,16,52); NAVY2=(18,25,83); BLUE=(39,102,255)
PURPLE=(124,58,237); CYAN=(62,211,255); WHITE=(248,250,255)
MUTED=(198,209,240); PINK=(255,83,130); MINT=(103,232,179)

def bg(w,h):
    im=Image.new("RGB",(w,h)); px=im.load()
    for y in range(h):
        t=y/max(1,h-1)
        for x in range(w):
            u=x/max(1,w-1)
            base=[int(NAVY[i]*(1-t)+NAVY2[i]*t) for i in range(3)]
            glow=max(0,1-math.sqrt(((u-.88)/.68)**2+((t-.18)/.45)**2))
            glow2=max(0,1-math.sqrt(((u-.05)/.7)**2+((t-.85)/.55)**2))
            for i in range(3):
                base[i]=min(255,int(base[i]+glow*(63,35,170)[i]*.45+glow2*BLUE[i]*.22))
            px[x,y]=tuple(base)
    return im

def box(d, xy, r, fill, outline=None, width=2):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def wrap(d,text,x,y,maxw,fnt,fill,gap=8,max_lines=None):
    words=text.split(); lines=[]; cur=""
    for word in words:
        trial=word if not cur else cur+" "+word
        if d.textbbox((0,0),trial,font=fnt)[2] <= maxw: cur=trial
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    if max_lines: lines=lines[:max_lines]
    lineh=fnt.getbbox("Ag")[3]-fnt.getbbox("Ag")[1]+gap
    for line in lines:
        d.text((x,y),line,font=fnt,fill=fill); y+=lineh
    return y

def brand(d,x,y,scale=1.0):
    s=int(56*scale)
    box(d,(x,y,x+s,y+s),int(14*scale),(38,91,242))
    d.text((x+8*scale,y+12*scale),"DN",font=F(int(26*scale)),fill=WHITE)
    d.text((x+s+16*scale,y+5*scale),"Digital Nagari",font=F(int(28*scale)),fill=WHITE)
    d.text((x+s+17*scale,y+34*scale),"SMART TOOLS FOR BUSINESS",font=F(int(11*scale)),fill=MUTED)

def bot(d,cx,cy,scale=1):
    w,h=int(154*scale),int(124*scale)
    box(d,(cx-w//2,cy-h//2,cx+w//2,cy+h//2),int(28*scale),(25,45,118),(88,140,255),max(2,int(3*scale)))
    d.line((cx,cy-h//2,cx,cy-h//2-int(24*scale)),fill=CYAN,width=max(3,int(5*scale)))
    d.ellipse((cx-int(9*scale),cy-h//2-int(39*scale),cx+int(9*scale),cy-h//2-int(21*scale)),fill=CYAN)
    r=int(10*scale)
    for ex in (cx-int(39*scale),cx+int(39*scale)):
        d.ellipse((ex-r,cy-int(5*scale)-r,ex+r,cy-int(5*scale)+r),fill=WHITE)
    d.arc((cx-int(32*scale),cy+int(7*scale),cx+int(32*scale),cy+int(39*scale)),15,165,fill=MINT,width=max(3,int(4*scale)))

def feed():
    w,h=1080,1350; im=bg(w,h); d=ImageDraw.Draw(im)
    brand(d,58,52)
    d.ellipse((840,65,1035,260),outline=(67,95,202),width=3)
    d.ellipse((900,100,1030,230),outline=(89,67,204),width=3)
    d.text((58,160),"BOT MASTER",font=F(76),fill=WHITE)
    d.text((62,252),"Make FAQs easier to handle",font=F(34),fill=(178,198,255))
    d.text((62,306),"A clearer chatbot workflow starts with better answers.",font=F(22,False),fill=MUTED)
    box(d,(58,365,1022,610),34,(17,29,81),(68,104,224),3)
    bot(d,172,484,.88)
    d.text((292,394),"BOT WORKFLOW",font=F(18),fill=CYAN)
    d.text((292,427),"Question received",font=F(30),fill=WHITE)
    d.text((292,470),"↓",font=F(30),fill=MUTED)
    d.text((332,477),"Match a clear FAQ answer",font=F(24,False),fill=WHITE)
    d.text((292,526),"↳ Human handoff for complex queries",font=F(21,False),fill=MINT)
    box(d,(58,646,514,880),28,(111,34,81),(255,91,139),2)
    d.ellipse((82,672,132,722),fill=PINK); d.text((96,678),"!",font=F(31),fill=WHITE)
    d.text((151,681),"THE PROBLEM",font=F(22),fill=WHITE)
    wrap(d,"Repeated customer questions can slow replies and distract your team.",84,744,398,F(26),WHITE,10,4)
    box(d,(536,646,1022,880),28,(17,82,82),(103,232,179),2)
    d.ellipse((560,672,610,722),fill=MINT); d.text((573,679),"✓",font=F(27),fill=(7,52,57))
    d.text((629,681),"QUICK INSIGHT",font=F(22),fill=WHITE)
    wrap(d,"Map common questions to clear answers—and give complex queries a human handoff.",562,744,432,F(25),WHITE,10,4)
    d.text((60,917),"CHATBOT AUTOMATION",font=F(20),fill=CYAN)
    d.text((60,950),"FAQ Automation  •  Customer Support Automation",font=F(22,False),fill=WHITE)
    box(d,(58,1030,1022,1148),32,(105,48,245),(172,153,255),3)
    d.text((103,1063),"DM:",font=F(31),fill=WHITE); d.text((205,1053),"BOT",font=F(48),fill=WHITE)
    d.text((770,1073),"GET DETAILS  →",font=F(20),fill=WHITE)
    d.line((58,1190,1022,1190),fill=(68,89,165),width=2)
    d.text((60,1214),"Digital Nagari  •  Smart tools for business",font=F(20),fill=MUTED)
    d.text((60,1265),"#ChatbotAutomation   #FAQAutomation   #DigitalNagari",font=F(17),fill=(167,181,237))
    im.save(OUT/"bot-master-feed.jpg","JPEG",quality=95,optimize=True)

def story():
    w,h=1080,1920; im=bg(w,h); d=ImageDraw.Draw(im)
    brand(d,58,60,1.12)
    d.ellipse((790,80,1050,340),outline=(68,94,205),width=4)
    d.ellipse((850,130,1010,290),outline=(100,60,220),width=3)
    d.text((58,205),"BOT MASTER",font=F(80),fill=WHITE)
    wrap(d,"Make FAQs easier to handle",62,307,880,F(39),(177,198,255),8,2)
    box(d,(58,455,1022,800),38,(17,29,81),(68,104,224),3)
    bot(d,230,620,1.15)
    d.text((400,500),"A SIMPLE FLOW",font=F(21),fill=CYAN)
    d.text((400,555),"Question",font=F(30),fill=WHITE)
    d.text((400,603),"↓",font=F(30),fill=MUTED)
    d.text((440,610),"FAQ answer",font=F(27),fill=WHITE)
    d.text((400,658),"↓",font=F(30),fill=MUTED)
    d.text((440,665),"Human handoff",font=F(25),fill=MINT)
    box(d,(58,850,1022,1085),30,(111,34,81),(255,91,139),2)
    d.text((96,884),"THE PROBLEM",font=F(24),fill=WHITE)
    wrap(d,"Repeated customer questions can delay replies.",96,937,860,F(34),WHITE,10,3)
    box(d,(58,1120,1022,1390),30,(17,82,82),(103,232,179),2)
    d.text((96,1155),"USEFUL INSIGHT",font=F(24),fill=WHITE)
    wrap(d,"Prepare clear answers for common questions and route complex requests to a person.",96,1210,860,F(32),WHITE,12,4)
    d.text((60,1445),"WHATSAPP CHATBOT",font=F(26),fill=CYAN)
    d.text((60,1495),"FAQ AUTOMATION",font=F(26),fill=WHITE)
    d.text((60,1545),"CUSTOMER SUPPORT AUTOMATION",font=F(24),fill=WHITE)
    box(d,(58,1630,1022,1765),34,(105,48,245),(172,153,255),3)
    d.text((108,1666),"DM:",font=F(32),fill=WHITE); d.text((218,1652),"BOT",font=F(55),fill=WHITE)
    d.text((735,1683),"TAP TO MESSAGE →",font=F(19),fill=WHITE)
    d.line((58,1810,1022,1810),fill=(68,89,165),width=2)
    d.text((60,1840),"Digital Nagari  •  Smarter customer conversations",font=F(19),fill=MUTED)
    im.save(OUT/"bot-master-story.jpg","JPEG",quality=95,optimize=True)

feed(); story()
print("Rendered feed and story in assets/2026-10-20/")
