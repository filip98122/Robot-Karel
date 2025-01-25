import pygame
import time
import math
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
        w=65
        h=65
        scldimg=pygame.transform.scale(img, (w, h))
        window.blit(scldimg,(self.x+7,self.y+7))
class Loptica:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pokupljen=False
class Polje:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img=pygame.image.load("polje.png")
        h=765
        w=765
        self.img1=pygame.transform.scale(self.img,(w,h))
    def draw(self,window):
        window.blit(self.img1,(self.x,self.y))
     
bckg=Polje(0,0)
karel=Karel(0,153,"d",0)
     
     
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
        if i == 0 or i ==10:
            w=15
            pygame.draw.line(window,(0,0,0),(i*76.5,153),(i*76.5,765),w)
        else:
            w=5
            pygame.draw.line(window,(50,50,50),(i*76.5,153),(i*76.5,765),w)
    for i in range(9):
        if i == 0 or i ==10:
            w=15
            pygame.draw.line(window,(0,0,0),(0,153+i*76.5),(765,153+i*76.5),w)
        else:
            w=5
            pygame.draw.line(window,(50,50,50),(0,153+i*76.5),(765,153+i*76.5),w)
    
    karel.draw(window)
    pygame.display.update()
    clock.tick(60)