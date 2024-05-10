import os
import pygame
import time
from random import randint
pygame.init()
back=(200,255,255)

pygame.mixer.init()
l=os.path.join(os.path.abspath(__file__ + "/.."),'1.ogg') # абсолютый путь
pygame.mixer.music.load(l)
pygame.mixer.music.play()

width = 800
height = 600

window=pygame.display.set_mode((width,height))
#window.fill(back)


j=os.path.join(os.path.abspath(__file__ + "/.."),"background.png") # абсолютый путь
background = pygame.transform.scale(pygame.image.load(j), (width, height))# фон в виде картинки
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color 
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture (Area): 
    def __init__(self, filename,x=0, y=0, width=10, height=10): 
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None) 
        self.image = pygame.image.load(filename) 
        self.image = pygame.transform.scale(self.image, (width, height))
    def draw(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.image = pygame.font.SysFont("vernada",fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0): 
        self.fill() 
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

game=True

m=os.path.join(os.path.abspath(__file__ + "/.."),"platform.png") # абсолютый путь
platform=Picture (m, 200, 350, 120, 50)
b=os.path.join(os.path.abspath(__file__ + "/.."),"ball.png") # абсолютый путь
ball=Picture(b,200,250,30,30)
monsters=[]
n=9
x=5
y=5
e=os.path.join(os.path.abspath(__file__ + "/.."),"enemy.png") # абсолютый путь
for i in range(3):
    x=5+25*i
    for j in range(n):
        
        monster=Picture (e,x,y,50,50)
        monsters.append(monster)
        x+=55
    y=y+55
    n=n-1
move_left=False
move_right=False
dx=1
dy=1
finish=False
while game:
    #window.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT: 
                move_right=True
            if event.key==pygame.K_LEFT: 
                move_left=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT: 
                move_right=False
            if event.key==pygame.K_LEFT: 
                move_left=False
    
    if finish !=True:
        window.blit(background,(0,0))    
        platform.draw()
        ball.draw()
        for monster in monsters:
            monster.draw()
        
        if move_right:
            platform.rect.x+=5
        if move_left:
            platform.rect.x-=5
        ball.rect.x+=3*dx
        ball.rect.y+=3*dy
        if ball.rect.x<20 or ball.rect.x>450: 
            dx*=-1
        if ball.rect.y<20 or ball.rect.y>450: 
            dy*=-1
        if ball.colliderect(platform.rect):
            dy*=-1
        for monster in monsters:
            if monster.rect.colliderect(ball.rect):
                dy*=-1
                monsters.remove(monster)
        if ball.rect.y>400:
            lose=Label(200,200,100,100,background)
            lose.set_text("YOU LOSE",60,(255,0,0))
            lose.draw(0,0)
            finish=True

        if len(monsters)==0:
            win=Label(200,200,100,100,background)
            win.set_text("YOU WIN",60,(255,0,0))
            win.draw(0,0)
            finish=True

            
    pygame.display.update()
    clock.tick(60)
