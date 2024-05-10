from pygame import *


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

level_width = len(level[0])*40
level_height = len(level)*40



W=1280
H=720
window = transform.scale(image.load("images/bgr.png"),(W,H))

display.set_caption("Mega Doom")

mixer.init()


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


class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, speed, img):
        super().__init__()

        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.speed= speed
        self.width = w
        self.height=h
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

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

class Mana(GameSprite):
    def __init__(self, x, y, w, h, speed, img, side):
        GameSprite.__init__(self, x, y, w, h, speed, img)

        self.side = side

    def update(self):
        global side, f

        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed

mana = Mana(0, -100, 25, 25, 35, power, 'left')

class Player(GameSprite):
    def r_l(self):
        global mana, img, f
        f = 1
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
            f=1
            mana.side = "left"
        if keys[K_d]:
            self.rect.x += self.speed
            mana.side = "right"
            f=0

        if f == 1:
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))
        if f == 0:
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))

    def u_d(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed 
        if keys[K_s]:
            self.rect.y += self.speed 

class Enemy(GameSprite):
    def __init__(self, x, y, w, h, speed, img, side):
        GameSprite.__init__(self, x, y, w, h, speed, img)

        self.side = side

    def update(self):
        global side 

        if self.side == 'right':
            self.rect.x -= self.speed
        if self.side == 'left':
            self.rect.x += self.speed 

class Button():
    def __init__(self, color, x, y, w, h, text, fsize, txt_color):

        self.width=w
        self.height=h
        self.color=color

        self.image = Surface([self.width, self.height])
        self.image.fill((color))

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

        self.fsize=fsize
        self.text=text
        self.txt_color=txt_color
        self.txt_image=font.Font('font/impact.ttf', fsize).render(text, True, txt_color)

    def draw(self, shift_x, shift_y):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))

#створення кнопок
btn_start = Button((178, 34, 34), 470, 300, 200, 70, 'START GAME', 50, (255, 255, 255))
btn_control = Button((178, 34, 34), 470, 450, 280, 70, 'HOW TO PLAY', 50, (255, 255, 255))
btn_exit = Button((178, 34, 34), 470, 600, 280, 70, 'EXIT GAME', 50, (255, 255, 255))
btn_menu = Button((178, 34, 34), 470, 600, 280, 70, 'BACK TO MENU', 50, (255, 255, 255))
btn_restart = Button((178, 34, 34), 470, 450, 280, 70, 'RESTART', 50, (255, 255, 255))
btn_continue = Button((178, 34, 34), 470, 350, 280, 70, 'CONTINUE', 50, (255, 255, 255))
btn_pause = Button((178, 34, 34), 1200, 15, 50, 50, 'I I', 40, (255, 255, 255))




class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configue(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, = -1 + W / 2, -t + H / 2

    l = min(0, 1)
    l = max(-(camera.width - W), l)
    t = max(-(camera.height - H), t)
    t = min(0, t)

    return Rect(l, t, w, h)

def res_pos(): # ця функція дає мождивість перезапускати гру
    # всі активні змінні, списки та об'єкти потрібно занести в область глобальної видимості 
    global items, manas, coins, platforms, stairs, blocks_r, blocks_l
    global hero, en1, en2, en3, en4, door, key1, key2, portal, chest, camera
    global k_door, k_chest, o_chest, c_count
        
    # створюємо спрайти
    hero = Player(300, 650, 50, 50, 5, hero_l)
    en1 = Enemy(400, 480, 50, 50, 3, enemy_l, 'left')
    en2 = Enemy(230, 320, 50, 50, 3, enemy_l, 'left')
    en3 = Enemy(1800, 160, 50, 50, 3, enemy_l, 'left')
    en4 = Enemy(1700, 320, 50, 50, 3, enemy_l, 'left')
    door = Settings(1000, 580, 40, 120, 0, door)
    key1 = Settings(160, 300, 50, 20, 0, kkey)
    key2 = Settings(1500, 30, 50, 20, 0, kkey)
    portal = Settings(2700, 600, 100, 100, 0, portal)
    chest = Settings(450, 130, 80, 80, 0, chest_close)
    camera = Camera(camera_configue, level_width, level_height)

    blocks_r=[]
    blocks_l=[]
    stairs=[]
    coins=[]
    platforms=[]


# УРОВЕНЬ - делал Андрюша🥰
# молодец Андрюша! (Krisnak) Спасибки🥰





# - платформа
# 0 монетка
# l левый барьер
# r правый барьер
# / лестница
# e враг
# @ Портал, переход на другой уровень
# > Сундук
# & Ключ



items = sprite.Group() # в цю группу додаємо всі об'єкти, які будуть відображатися в камері
manas = sprite.Group() # группа що клонує атакуючі шари

#створення спрайтів
hero = Player(300, 650, 50, 50, 5, hero_1)

en1 = Enemy(400, 480, 50, 50, 3, enemy_1, 'left')
en2 = Enemy(230, 320, 50, 50, 3, enemy_1, 'left')
en3 = Enemy(1800, 160, 50, 50, 3, enemy_1, 'left')
en4 = Enemy(1700, 320, 50, 50, 3, enemy_1, 'left')

door = GameSprite(1000, 580, 40, 120, 0, door)

key1 = GameSprite(160, 350, 50, 20, 0, key)
key2 = GameSprite(1500, 350, 50, 20, 0, key)

portal = GameSprite(2700, 600, 100, 100, 0, port)

chest = GameSprite(450, 130, 80, 80, 0, chest_close)

camera = Camera(camera_configue, level_width, level_height)

def collider(): # тут прописані всі взаємодії між об'єктами гри Поліна
    global k_door, k_chest, o_ches, c_count
    keys = key.get_pressed()
    for r in blocks_r:
        if sprite.spritecollide(r, manas, True):
            kick.play()
            items.remove(mana)
    
        if sprite.collide_rect(hero,r):
            hero.rect.x = r.rect.x + hero.width - 5
    
        if sprite.collide_rect(en1, r):
            en1.side = 'left'
            en1.image = transform.scale(image.load(enemy_l), (en1.width, en1.height))
    
        if sprite.collide_rect(en2, r):
            en2.side = 'left'
            en2.image = transform.scale(image.load(enemy_l), (en2.width, en2.height))
    
        if sprite.collide_rect(en3, r):
            en3.side = 'left'
            en3.image = transform.scale(image.load(enemy_l), (en3.width, en3.height))
    
        if sprite.collide_rect(en4, r):
            en4.side = 'left'
            en4.image = transform.scale(image.load(enemy_l), (en4.width, en4.height))
    
    for l in blocks_l:
        if sprite.spritecollide(l, manas, True):
            kick.play()
            items.remove(mana)
    
        if sprite.collide_rect(hero,l):
            hero.rect.x = l.rect.x - hero.width 
    
        if sprite.collide_rect(en1, l):
            en1.side = 'right'
            en1.image = transform.scale(image.load(enemy_r), (en1.width, en1.height))
    
        if sprite.collide_rect(en2, l):
            en2.side = 'right'
            en2.image = transform.scale(image.load(enemy_r), (en2.width, en2.height))
    
        if sprite.collide_rect(en3, l):
            en3.side = 'right'
            en3.image = transform.scale(image.load(enemy_r), (en3.width, en3.height))
        
        if sprite.collide_rect(en4, l):
            en4.side = 'right'
            en4.image = transform.scale(image.load(enemy_r), (en4.width, en4.height))

    coin_c = font2.render(': ' + str(c_count), True, (255,255,255))
    window.blit(transform.scale(image.load('???.png'), (50,50)), (10,10))
    window.blit(coin_c, (55, 15))
    
    for c in coins:
        if sprite.collide_rect(hero, c):
            c_coll.play()
            c_count += 1
            coins.remove(c)
            items.remove(c)
            
    for s in stairs:
        if sprite.spritecollide(s, manas, True):
            kick.play()
            items.remove(mana)
    
        if sprite.collide_rect(hero,s):
            hero.u_d()
    
            if hero.rect.y <= (s.rect.y - 40):
                hero.rect.y = s.rect.y - 40
            
            if hero.rect.y >= (s.rect.y + 130):
                hero.rect.y = s.rect.y + 130

    if sprite.collide_rect (hero, key1):
        window.blit(e_tap, (500,50))
        if keys[K_e]:
            k_chest = True
            key1.rect.y = -100
            items.remove(key1)
            K_UP.play()
        
    if sprite.collide_rect (hero, key2):
        window.blit(e_tap, (500,50))
        if keys[K_e]:
            k_door = True
            key2.rect.y = -100
            items.remove(key2)
            K_UP.play()
        
    if sprite.collide_rect(hero, door) and k_door == False:
        window.blit(k_need, (450,50))
        hero.rect.x = door.rect.x - 47
    
    if sprite.collide_rect (hero, door) and k_door == True:
        hero.rect.x = door.rect.x - 47
        window.blit(e_tap, (500,50))
        if keys[K_e]:
            door.rect.x += 1500
            d_o.play()
            k_door = False

    if sprite.collide_ect(hero, chest) and k_chest == False:
        window.blit(k_need, (450, 50))

    if aprite.collide_rect(hero, chest) and k_chest == True and c_count != 15:
        window.blit(e_tap, (500, 50))
        if keys[K_e]:
            o_chest = True
            c_count += 10
            chest.image = transform.scale(image.load(chest_open), (chest_width, chest_height))
            cst_o.play()
            k_door = True
    if sprite.spritecollide(en1, manas, True):
        en1.rect.y = -150
        items.remove(mana)
        kick.play()
    if sprite.spritecollide(en2, manas, True):
        en2.rect.y = -150
        items.remove(mana)
        kick.play()
    if sprite.spritecollide(en3, manas, True):
        en3.rect.y = -150
        items.remove(mana)
        kick.play()
    if sprite.spritecollide(en4, manas, True):
        en4.rect.y = -150
        items.remove(mana)
        kick.play()

def menu(): #меню
    menu = True
    mixer.music.load('sounds/menu.ogg')
    mixer.music.play()

    while menu:

        for e in event.get(): 
            if e.type == QUIT:
                menu = False

        time.delay(15)
        pos_x, pos_y = mouse.get_pos()

        window.blit(bg, (0, 0))
        window.blit(gname, (320, 70))

        btn_start.draw(15, 5)
        btn_control.draw(10,5)
        btn_exit.draw(37, 5)

        for e in event.get():
            if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                menu = False
                res_pos()
                lvl_1()
            if btn_control.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                menu = False
                rules()
            if btn_exit.rect.collidep((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                menu = False
                a = 0
            if e.type == QUIT:
                menu = False
                a = 0
        display.update()

game = True

def pause(): #Пауза
    stop = True

    mixer.music.stop()

    while stop:
        for e in event.get():
            if e .type == QUIT:
                stop = False

        time.delay(15)

        window.fill((0,0,0))
        window.blit(pausa, (440,200))

        btn_continue.draw(50.5)
        btn_restart.draw(60,5)
        btn_menu.draw(0,5)

        pos_x, pos_y = mouse.get_pos()
        
        for e in event.get():
            if btn_continue.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                stop = False
                mixer.music.stop()
                lvl_1()
            if btn_restart.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                res_pos()
                stop = False
                lvl_1()
            if btn_menu.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBUTTONDOWN:
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

        window.fill(0,0,0)
        window.blit(lose, (350,200))

        btn.restart.draw(60,5)
        btn_menu.draw(0,5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if btn_restart.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                over = False
                res_pos()
                lvl_1()
            if btn_menu.rect.collidepoint((pos_x,pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                over = False
                menu()

        display.update()



def rules(): #правила
   
    rule = True
    mixer.music.stop()

    while rule:

        for e in event.get():
            if e.type == QUIT:
                    rule = False

            time.delay(15)

            window.blit(bg, (0, 0))
            window.blit(gname, (320, 70))
            window.blit(wasd_b, (50, 250))
            window.blit(space_b, (50, 350))
            window.blit(e_b, (50, 450))
            btn_menu.draw(0, 5)

            pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                rule = False
                menu()
            if e.type == QUIT:
                rule = False
        
        display.update()

def lvl_end(): #рівень пройдено

    stop = True

    mixer.music.stop()
    mixer.music.load('sounds/game_over.ogg')
    mixer.music.play()

    while stop: 

        for e in event.get():
            if e.type == QUIT:
                stop = False

        time.delay(15)

        window.fill((0, 0, 0))
        window.blit(done, (300, 200))

        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False
                res_pos()
                lvl_1()
            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False
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
                r2 = Settings(x,y,40,40,0,platform)
                platforms.append(r5)
                items.add(r5)
            if c == ">": #Сундук
                r6 = Settings(x,y,-40,80,80,0,chest_close)
                items.add(r6)
            x += 40
        y+= 40
        x = 0
game = True

FPS = 60
clock = time.Clock()



def lvl_1():
    mixer.music.load('sounds/game.ogg')
    mixer.music.play()
    game = True

    while game:
        time.delay(5)
        window.blit(bg, (0, 0))
        keys = key.get_pressed()
        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if e.type == QUIT:
                game = False
            if btn_pause.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                pause()
                game = False
        
        en1.update()
        en2.update()
        en3.update()
        en4.update()
        hero.r_l()
        mana.update()
        btn_pause.draw(10, 0)
        collider()
        if keys[K_SPACE]:
            mana.rect.x, mana.rect.y = hero.rect.centerx, hero.rect.top
            manas.add(mana)
            items.add(mana)
            fire_s.play()

        camera.update(hero)
        for i in items:
            window.blit(i.image, camera.apply(i))
        if sprite.collide_rect(hero, en1) or sprite.collide_rect(hero, en2) or sprite.collide_rect(hero,en3) or sprite.collide_rect(hero, en4):
            restart()
            game = False
        if sprite.collide_rect(hero, portal):
            tp.play()
            lvl_end()
            game = False
        display.update()
menu()