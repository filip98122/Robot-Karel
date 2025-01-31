import pygame
import time
import math

import pygame.tests
pygame.init()
def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False


def pokupi():
    global vedrict
    for i in range(len(l_l)):
        if karel.x==l_l[i].x and karel.y==l_l[i].y:
            if l_l[i].state==1:
                l_l[i].state=2
                break
        else:
            dugme.wait=59
            dugme.line=len(dugme.lines)-1
            vedrict="Nema loptice"


vedrict=""
font=pygame.sysfont.SysFont("B",45)
txt= font.render(f"{vedrict}", True, (15, 15, 15))
w=txt.get_width()
h=txt.get_height()



def napred():
    dole=False
    gore=False
    levo=False
    desno=False
    for i in range(len(l_z)):
        if karel.x==0:
            levo=True
        if karel.y == (HEIGHT/10)*2:
            gore=True
        if karel.x==(WIDTH/10)*9:
            desno=True
        if karel.y == (HEIGHT/10)*9:
            dole=True

        if l_z[i].x==karel.x and l_z[i].y==karel.y:
            if l_z[i].x1==karel.x+WIDTH/10:
                gore=True
            if l_z[i].y1==karel.y+HEIGHT/10:
                levo=True
        if l_z[i].y==karel.y+HEIGHT/10 and l_z[i].x==karel.x:
            if l_z[i].y1==karel.y+HEIGHT/10 and l_z[i].x==karel.x+WIDTH/10:
                dole=True
        if l_z[i].y==karel.y and l_z[i].x==karel.x+WIDTH/10:
            if l_z[i].y1==karel.y+HEIGHT/10 and l_z[i].x==karel.x+WIDTH/10:
                desno=True
    if karel.strana==0:
        if dole==False:
            karel.y+=HEIGHT/10
        else:
            dugme.wait=59
            dugme.line=len(dugme.lines)-1
            vedrict="Karl ne moze da prodje"
    if karel.strana==2:
        if gore==False:
            karel.y-=HEIGHT/10
        else:
            dugme.wait=59
            dugme.line=len(dugme.lines)-1
            vedrict="Karl ne moze da prodje"
    if karel.strana==1:
        if desno==False:
            karel.x+=WIDTH/10
        else:
            dugme.wait=59
            dugme.line=len(dugme.lines)-1
            vedrict="Karl ne moze da prodje"
    if karel.strana==3:
        if levo==False:
            karel.x-=WIDTH/10
        else:
            dugme.wait=59
            dugme.line=len(dugme.lines)-1
            vedrict="Karl ne moze da prodje"
def desno():
    karel.strana-=1
    if karel.strana<0:
        karel.strana+=4
def kraj():
    global karel
    karel=Karel(0,HEIGHT/10*2,0,0)
def levo():
    karel.strana+=1
    if karel.strana>3:
        karel.strana-=4
        
        
        
        
        
        
        
        
        
        
clock = pygame.time.Clock()
WIDTH,HEIGHT = 765,765
window = pygame.display.set_mode((WIDTH,HEIGHT))















def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False
class Karel:
    def __init__(self,x,y,strana,loptice):
        self.x=x
        self.y=y
        self.strana=strana
        self.loptice=loptice
    def draw(self,window):
        img=pygame.image.load(f"karel{self.strana}.png")
        w=WIDTH/11.76923076923077
        h=HEIGHT/11.76923076923077
        scldimg=pygame.transform.scale(img, (w, h))
        window.blit(scldimg,(self.x+WIDTH/109.2857142857143,self.y+HEIGHT/100))


class Zid():
    def __init__(s,x,y,x1,y1):
        s.x=x
        s.y=y
        s.x1=x1
        s.y1=y1
    def draw(s,window):
        pygame.draw.line(window,(0,0,0),(s.x,s.y),(s.x1,s.y1),WIDTH//153)
class Loptica:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.state=1
        self.w=WIDTH/30.6
        self.h=HEIGHT/30.6
        self.scldimg=pygame.transform.scale(pygame.image.load("loptica.png"),(self.w,self.h))
    def draw(s,window):
        if s.state==1:
            window.blit(s.scldimg,(s.x+s.w,s.y+s.h))
class Polje:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img=pygame.image.load("polje.png")
        h=HEIGHT
        w=WIDTH
        self.img1=pygame.transform.scale(self.img,(w,h))
    def draw(self,window):
        window.blit(self.img1,(self.x,self.y))
#/


l_z=[
    Zid((WIDTH/10),(HEIGHT/10)*4,(WIDTH/10),(HEIGHT/10)*5)
    
    
    
    
    
    
    
    
]
l_l=[
    Loptica((WIDTH/10),(HEIGHT/10)*4)
    
    
    
    
]



bckg=Polje(0,0)
karel=Karel(0,HEIGHT/10*2,0,0)


class Dugme:
    def __init__(s):
        s.line=0
        s.holding=False
        img=pygame.image.load("dugme.png")
        s.w=img.get_width()*WIDTH/510
        s.h=img.get_height()*HEIGHT/510
        s.scaled_img=pygame.transform.scale(img,(s.w,s.h))
        s.wait=1
        s.t=0
        s.c=False
    def draw_and_check(s,window):
        global karel
        global vedrict
        window.blit(s.scaled_img,(WIDTH//2-s.w//2,HEIGHT/100))
        if button_colision(s.w,s.h,WIDTH//2-s.w//2,HEIGHT/100,mousePos,mouseState):
            if s.holding==False:
                if s.wait==1:
                    with open("kodovde.py") as file:
                        s.lines = file.readlines()
                    vedrict=""
                    s.wait=len(s.lines)*60
                    s.wait+=59
                    s.c=True
                    s.holding=True
                    s.line=0
                    s.t=1
        else:
            s.holding=False
        if s.wait>1:
            s.wait-=1
dugme=Dugme()
while True:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
    window.fill("white")
    #Kod ovde
    bckg.draw(window)
    for i in range(11):
        if i ==10:
            w1=WIDTH//51
            pygame.draw.line(window,(0,0,0),(i*(WIDTH/10),HEIGHT/5),(i*(WIDTH/10),HEIGHT),w1)
            pygame.draw.line(window,(0,0,0),(0,HEIGHT/5),(0,HEIGHT),w1)
        else:
            w1=WIDTH//153
            pygame.draw.line(window,(120,120,120),(i*(WIDTH/10),HEIGHT/5),(i*(WIDTH/10),HEIGHT),w1)
    for i in range(9):
        if i ==8:
            w1=HEIGHT//51
            pygame.draw.line(window,(0,0,0),(0,HEIGHT/5),(WIDTH,HEIGHT/5),w1//2)
            pygame.draw.line(window,(0,0,0),(0,HEIGHT/5+i*HEIGHT/10),(WIDTH,HEIGHT/5+i*HEIGHT/10),w1)
        else:
            
            w1=HEIGHT//153
            pygame.draw.line(window,(120,120,120),(0,HEIGHT/5+i*HEIGHT/10),(WIDTH,HEIGHT/5+i*HEIGHT/10),w1)
    if dugme.wait==59:
        font=pygame.sysfont.SysFont("B",45)
        if vedrict=="":
            vedrict="Resenje prihvaceno!"
        txts = font.render(f"{vedrict}", True, (15, 15, 15))
        w=len(vedrict)*(WIDTH/47.56476683937825)
        h=HEIGHT/24.67741935483871
        txt=pygame.transform.scale(txts,(w,h))
        
    
    if dugme.wait<=59:
        window.blit(txt,((WIDTH/2)-(w/2),(HEIGHT/10)*2-((HEIGHT/100)+dugme.h)))
    
    
    
    
    
    
    
    
    dugme.draw_and_check(window)
    if dugme.c==True:
        if dugme.wait%60==0:
            exec(dugme.lines[dugme.line])
            dugme.line+=1
    if dugme.wait==1:
        if dugme.t==1:
            if dugme.line==len(dugme.lines):
                kraj()
    for i in range(len(l_l)):
        l_l[i].draw(window)
    for i in range(len(l_z)):
        l_z[i].draw(window)
    karel.draw(window)
    pygame.display.update()
    clock.tick(60)