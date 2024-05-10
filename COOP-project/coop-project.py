from pygame import *


class Settings(sprite. Sprite):
    def _init__(self, x, y, w, h, speed, img):
        super()._init__()
        
        self.speed = speed
        self.width = w
        self.height = h
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

mixer.init()

#В основной
music_menu = mixer.Sound('sounds/music_menu.ogg') #Музыка в меню
music_menu.play()

music_game = mixer.Sound('sounds/music_game.ogg') #Основная музыка
music_game.play()

fire = mixer.Sound('sounds/fire.ogg') #Выстрел, игрока и врага
kick = mixer.Sound('sounds/kick.ogg') #Получение урона
walk = mixer.Sound('sounds/walk.ogg') #Ходьба
jump = mixer.Sound('sounds/jump.ogg') #Прыжок
coincol = mixer.Sound('sounds/coincol.ogg') #Сбор монет
tp = mixer.Sound('sounds/teleport.ogg') #Переход на следующий уровень
click = mixer.Sound('sounds/click.ogg') #Нажатие на кнопки

font.init()

font1 = font.SysFont('font/ariblk.ttf', 200)
gname = font1.render('Blockada', True, (106, 90, 205))

font2 = font.SysFont('font/ariblk.ttf', 60)
e_tap = font2.render('press (e)', True, (255, 0, 255))
k_need = font2.render('You need a key to open!', True, (255, 0, 255))
space = font2.render('press (space) to kill the enemy', True, (255, 0, 255))

font3 = font.SysFont('font/calibrib.ttf', 45)
wasd_b = font3.render('WASD move buttons. You can only go up and down the stairs', True, (255, 0, 0))
space_b = font3.render('Space shoot button. You are a wizard who only knows one spell', True, (255, 0, 0))
e_b = font3.render('E interaction button. Open doors, collect keys, activate portals', True, (255, 0, 0))

font4 = font.SysFont('font/ariblk.ttf', 150)
done = font4.render('LEVEL DONE!', True, (8, 255, 0))
lose = font4.render('YOU LOSE!', True, (255, 0, 0))
pausa = font4.render('PAUSE', True, (255, 0, 0))

#Главный персонаж
hero_r = "images/hero_r.png" #Персонаж смотрит направо
hero_l = "images/hero_l.png" #Персонаж смотрит налево

#Враг
enemy_r = "images/enemy_r.png" #Враг смотрит направ
enemy_l = "images/enemy_l.png" #Враг смотрит налево


platform = "images/platform.png" #Платформа
coin = "images/coin.png" #Монета
ladder = "images/ladder.png" #Лестница
portal = "images/portal.png" #Переход на другой уровень
nothing = "images/nothing.png" #Пустая картинка
Kkey = "image/key.png" #Ключ
door = "image/door.png" #Дверь

chest_close = "image/chest_close.png" #Сундук закрытый
chest_open = "image/chest_open.png" #Сундук открытый



# - платформа
# 0 монетка
# l левый барьер
# r правый барьер
# / лестница
# e враг
# @ Портал, переход на другой уровень
# > Сундук
# & Ключ

blocks_r=[]
blocks_l=[]
stairs=[]
coins=[]
platforms=[]

items=sprite.Group()
manas=sprite.Group()


level = [
    "l                                                                             r",
    "l                                                                             r",
    "l                                    l@  00    e*r                            r",
    "l   l  00              r              -----------                             r",
    "l    ------------------                    l /    00  e         0  r          r",
    "l                 l / r                     -----------------------           r",
    "l                 l e     0 r                               l / r             r",
    "l                  ---------                                l         0 r     r",
    "l                    l / r                       l   00     r -----------     r",
    "l          l  000e       r                        ----------     l / r        r",
    "l           -------------                               l /   e   0  r        r",
    "l                   l / r                                ------------         r",
    "l                   l / r                                  l / r              r",
    "l               l           0   r                    l 00       r             r",
    "l                ---------------                      ----------              r",
    "l                      l / r                               l / r              r",
    "l                                      00           e                         r",
    "-------------------------------------------------------------------------------"]

game = True

def pause(): #Пауза
    stop = True

    mixer.music.stop()

    while stop:
        for e in event.get():
            if e .type == QUIT:
                stop = False

        time.delay(15)

        win.fill((0,0,0))
        win.blit(pausa, (440,200))

        btn_continue.draw(50.5)
        btn_restart.draw(60,5)
        btn_menu.draw(0,5)

        pos_x, pos_y = mouse.get_pos()
        
        for e in event.get():
            if btn_continue.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBOTTONDOWN:
                click.play()
                stop = False
                mixer.music.stop()
                lvl_1()
            if btn_restart.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBOTTONDOWN:
                click.play()
                mixer.music.stop()
                res_pos()
                stop = False
                lvl_1()
            if btn_menu.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBOTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False
                gam = False
                menu()
        display.update()


def restart():

    over = True

    mixer.music.stop
    mixer.music.load("sound/game_over.ogg")
    mixer.music.play

    while over:
        

        for e in event.get():
            if e.type == QUIT:
                over = False

        time.delay(15)

        win.fill(0,0,0)
        win.blit(lose, (350,200))

        btn.restart.draw(60,5)
        btn_menu.draw(0,5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if btn_restart.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBOTTONDOWN:
                click.play()
                mixer.music.stop()
                over = False
                res_pos()
                lvl_1()
            if btn_menu.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBOTTONDOWN:
                click.play()
                over = False
                menu()

        display.update()


while game:
    x=y=0
    for r in level:
        for c in r:
            if c =="r": #Правый угол
                r1 = Settings(x,y,40,40,nothing)
                blocks_r.append(r1)
                items.add(r1)
            if c == "l": #Левый угол
                r1 = Settings(x,y,40,40,nothing)
                blocks_l.append(r1)
                items.add(r1)
            if c == "/": #Лестница
                r2 = Settings(x,y-40,40,180,0,ladder)
                stairs.append(r2)
                items.add(r2)
            if c == "0": #Монета
                r3 = Settings(x,y,40,40,0,coin)
                coins.append(r3)
                items.add(r3)
            if c == "-": #Платформа
                r5 = Settings(x,y,40,40,0,platform)
                platforms.append(r5)
                items.add(r5)
            if c == ">": #Платформа
                r6 = Settings(x,y,-40,80,80,0,chest_close)
                items.add(r6)
            x += 40
        y+= 40
        x = 0