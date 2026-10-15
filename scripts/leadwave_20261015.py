from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import random
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def f(s,b=True):return ImageFont.truetype(BOLD if b else REG,s)
def T(d,x,y,s,size,col='#ffffff',b=True):d.text((x,y),s,font=f(size,b),fill=col)
def box(d,coords,r,c,outline=None):d.rounded_rectangle(coords,radius=r,fill=c,outline=outline,width=2)
def bg(w,h):
 im=Image.new('RGB',(w,h));d=ImageDraw.Draw(im)
 for y in range(h):
  p=y/h
  d.line((0,y,w,y),fill=(int(12+12*p),int(16+7*p),int(46+35*p)))
 d.ellipse((-230,140,520,950),fill='#24265b')
 d.ellipse((660,450,1400,1300),fill='#322063')
 return im
def scene(d,y,h):
 box(d,(70,y,1010,y+h),35,'#172143','#6773a8')
 box(d,(124,y+36,492,y+h-36),38,'#f4f7ff','#9aa7d4')
 box(d,(139,y+49,477,y+128),23,'#e7ecff')
 box(d,(162,y+68,199,y+106),19,'#6b55ed')
 T(d,215,y+66,'LEADWAVE',21,'#192749')
 T(d,215,y+95,'Enquiry inbox',15,'#52668e',False)
 box(d,(158,y+152,453,y+222),18,'#ffffff')
 T(d,177,y+164,'New enquiry',16,'#566b92')
 T(d,177,y+189,'Can I get details?',18,'#192749',False)
 box(d,(189,y+241,455,y+308),18,'#d8f5eb')
 T(d,204,y+253,'Sure! Let me help.',16,'#22584e')
 T(d,204,y+278,'Next step: follow-up',15,'#286a5b',False)
 box(d,(158,y+328,454,y+382),15,'#f0eaff')
 T(d,177,y+346,'Follow-up planned',17,'#5335a1')
 box(d,(525,y+80,961,y+h-68),25,'#ffffff')
 T(d,548,y+102,'FOLLOW-UP FLOW',24,'#1a2850')
 for i,(a,b) in enumerate([('Capture enquiry','Keep context clear'),('Set next action','Know what to do'),('Reply on time','Stay consistent')]):
  cy=y+155+i*78
  box(d,(546,cy,938,cy+65),15,'#eff3fb')
  d.ellipse((561,cy+16,594,cy+49),fill=['#7058ea','#4a8fdb','#20bda5'][i])
  T(d,572,cy+21,str(i+1),16)
  T(d,608,cy+9,a,18,'#1c294d')
  T(d,608,cy+36,b,15,'#657696',False)
def info(d,y,problem):
 color='#602a49' if problem else '#1b5355'
 accent='#ffadba' if problem else '#80f5d8'
 box(d,(70,y,1010,y+94),23,color,accent)
 box(d,(90,y+18,100,y+76),5,accent)
 T(d,120,y+12,'THE PROBLEM' if problem else 'USEFUL INSIGHT',18,accent)
 T(d,120,y+47,'New enquiries get buried in chats.' if problem else 'Give every lead a clear next action.',24)
def make(story):
 w,h=1080,(1920 if story else 1350);im=bg(w,h);d=ImageDraw.Draw(im)
 oy=210 if story else 60
 box(d,(70,oy,121,oy+52),14,'#7457f7')
 T(d,84,oy+10,'D',29)
 T(d,141,oy+7,'DIGITAL',30)
 T(d,283,oy+7,'NAGARI',30,'#7cf0dc')
 T(d,806,oy+16,'@digital_nagari',19,'#b5c6e9',False)
 d.line((70,oy+77,1010,oy+77),fill='#707cb5',width=2)
 if story:
  box(d,(70,319,445,371),23,'#303c78')
  T(d,97,333,'BETTER LEAD FOLLOW-UPS',19,'#d4dbff')
  T(d,70,410,'WHATSAPP',94)
  T(d,70,521,'AI CRM',102,'#7af0d9')
  T(d,73,642,'Stop losing warm leads.',32,'#d4e2ff')
  scene(d,705,500)
  info(d,1227,True);info(d,1340,False)
  labels=[('WHATSAPP AI CRM',70,345),('LEAD MANAGEMENT',365,651),('CUSTOMER FOLLOW-UP',671,1010)]
  for s,x1,x2 in labels:
   box(d,(x1,1470,x2,1528),18,'#293865')
   T(d,x1+18,1488,s,17,'#e3ebff')
  box(d,(70,1564,1010,1682),28,'#7459f7')
  T(d,330,1594,'DM LEADWAVE',46)
  T(d,540,1730,'One product. One clear next step.',20,'#b2c0e5',False)
 else:
  box(d,(70,164,389,212),20,'#303c78')
  T(d,87,178,'CLEARER FOLLOW-UPS',19,'#d4dbff')
  T(d,70,235,'WHATSAPP AI CRM',72)
  T(d,72,326,'Stop losing warm leads.',40,'#7af0d9')
  T(d,72,395,'LeadWave - a smarter enquiry workflow',24,'#c4d1ef',False)
  scene(d,458,457)
  labels=[('LEAD MANAGEMENT',70,360),('CUSTOMER FOLLOW-UP',377,703),('SALES PIPELINE',721,1010)]
  for s,x1,x2 in labels:
   box(d,(x1,932,x2,982),17,'#293865')
   T(d,x1+19,947,s,17,'#e3ebff')
  info(d,1000,True);info(d,1109,False)
  box(d,(70,1222,1010,1305),26,'#7459f7')
  T(d,334,1239,'DM LEADWAVE',38)
  T(d,364,1317,'Digital Nagari - All-in-One Digital Tools',17,'#b2c0e5',False)
 p=Path('assets/2026-10-15');p.mkdir(parents=True,exist_ok=True)
 path=p/('leadwave-story.jpg' if story else 'leadwave-feed.jpg')
 im.save(path,'JPEG',quality=90,optimize=True)
 print(path,im.size)
make(False)
make(True)
