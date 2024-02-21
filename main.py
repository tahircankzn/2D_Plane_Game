import pygame
import os
import random
from pygame import mixer

pygame.display.set_caption("Gökyüzü Savaşçısı")



WIDHT = 1680#1000 # ekran genişliği
HEIGHT = 1050#562 # ekran yüksekliği
WIN = pygame.display.set_mode((WIDHT,HEIGHT)) # ekran oluşturma
STEP = 5
SOUND_OPTİONS = 0.3
SOUND_OPTİONS_COUNTER = 1
COOL_DOWN = 30 # fps değerinin yarısı

# OYUN TUŞLARI

B = pygame.image.load("assets/b.png")
B_RED = pygame.image.load("assets/b_RED.png")



# İMAGE yükleme

# arka plan
BG = pygame.image.load("assets/firewatch.JPg")

# gemi resim
MISSION_SHIP = pygame.image.load("assets/plane_poyraz.png") # plane_poyraz  mission_ship

#rocket
MISSION_SHIP_ROCKET = pygame.image.load("assets/blue_rocket1.png")
#rocket enemy
MISSION_ENEMY_ROCKET = pygame.image.load("assets/red_rocket.png")
#ulti
MISSION_ULTI = pygame.image.load("assets/ulti.png")
#Captain Marvel image
CaptainMarvel_image = pygame.image.load("assets/captainMarvel_image.png")
#Captain Marvel
CaptainMarvel1 = pygame.image.load("assets/captainmarvel1.png")
#Captain Marvel2
CaptainMarvel2 = pygame.image.load("assets/captainmarvel2.png")
#IRON MAN
IRONMAN = pygame.image.load("assets/iron_man.png")
IRONMAN_image = pygame.image.load("assets/tony_image.png")
#düşman aracı
ENEMY_SHİP = pygame.image.load("assets/enemy_ship_blue.png")
# shield
SHIELD = pygame.image.load("assets/plane_poyraz_shield.png") # shield
#Thor
THOR = pygame.image.load("assets/thor1.png")
THOR_image = pygame.image.load("assets/thor_image.png")
THOR_cloud = pygame.image.load("assets/cloud.png")
THOR_storm = pygame.image.load("assets/storm.png") # storm
# ses buton resmi , şimdilik çalışmıyor
SOUND = pygame.image.load("assets/sound.png")

exit = 1

class exits():
    def __init__(self,exit):
        self.exit = exit

bitir = exits(1)

# başlangıç ekranı 
def start(exit):
    x =-300 
    y = 250

    x1 = 1780
    y1 = 650

    x2 = 1680
    y2 = 700

    x3 = 1780
    y3 = 750

    
    WIN.blit(BG,(0,0)) # arka planı 0,0 noktasından koyması sağlandı
    pygame.display.update() # ekranın yenilenmesi için 
    run1 = True
    while run1:
        WIN.blit(BG,(0,0)) # arka planı 0,0 noktasından koyması sağlandı
        
        if x<1680:
            WIN.blit(MISSION_SHIP,(x,y))
            x+=5
        else:
            x = -300

        if x3>-50:
            WIN.blit(ENEMY_SHİP,(x1,y1)) # ekrana aracı çizdirir
            WIN.blit(ENEMY_SHİP,(x2,y2))
            WIN.blit(ENEMY_SHİP,(x3,y3))
            x1-=5
            x2-=5
            x3-=5

        else:
            x1 = 1780
            x2 = 1680
            x3 = 1780
            
         
        pygame.init() # ekrana yazı yazdırmak için gerekli

        font = pygame.font.SysFont("Algeria",120)                  #
        text = font.render("Başlamak İçin Tıkla",1,(255,255,255)) # akrana yazı yazdırma
        WIN.blit(text,(450,450))                                  #

        pygame.display.update() # ekranın yenilenmesi için 

        for event in pygame.event.get(): # kapatma tuşuna tıklanırsa kapatır  
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run1 = False
                    boom()

                if event.type == pygame.QUIT:
                    run1 = False
                    bitir.exit = 0


def boom():
    boom = pygame.mixer.Sound("sound/boom.wav")
    boom.set_volume(0.05)
    boom.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT+1)

def CaptainMarvel_voice():
    boom = pygame.mixer.Sound("sound/captainMARVEL.wav")
    boom.set_volume(0.5)
    boom.play()

def IronMan_voice():
    boom = pygame.mixer.Sound("sound/IronMan.wav")
    boom.set_volume(0.5)
    boom.play()


def Thor_voice():
    boom = pygame.mixer.Sound("sound/THOR2.wav")
    boom.set_volume(0.5)
    boom.play()

def game_music(SOUND_OPTİONS):
    mixer.init()
    mixer.music.load('sound/back_ground.wav') # back_ground.wav  # The Last of Us TV Show  Episode 1 Ending Song.wav
    print("music started playing....")
    mixer.music.set_volume(SOUND_OPTİONS)
    mixer.music.play(-1)
    


class Keys():
    def __init__(self):

        self.B = pygame.image.load("assets/b.png")
        self.B_RED = pygame.image.load("assets/b_RED.png")

        self.M = pygame.image.load("assets/m.png")
        self.M_RED = pygame.image.load("assets/m_RED.png")

        self.V = pygame.image.load("assets/v.png")
        self.V_RED = pygame.image.load("assets/v_RED.png")


        self.SPACE = pygame.image.load("assets/space.png")
        self.SPACE_RED = pygame.image.load("assets/space_RED.png")

        self.HAREKET_DOWN = pygame.image.load("assets/destinity_key_asagi.png")
        self.HAREKET_UP = pygame.image.load("assets/destinity_keys_yukari.png")
        self.HAREKET_UP_LEFT = pygame.image.load("assets/destinity_keys_SOL_YUKARİ.png")
        self.HAREKET_UP_RİGHT = pygame.image.load("assets/destinity_keys_sag_yukari.png")
        self.HAREKET_DOWN_LEFT = pygame.image.load("assets/destinity_keysol_asagi.png")
        self.HAREKET_DOWN_RİGHT = pygame.image.load("assets/destinity_keys_sol_asagi.png")
        self.HAREKET = pygame.image.load("assets/destinity_keys.png")
        self.HAREKET_RİGHT = pygame.image.load("assets/destinity_keys_sag.png")
        self.HAREKET_LEFT = pygame.image.load("assets/destinity_keys_sol.png")


        self.yön = self.HAREKET
        self.v = self.V
        self.b = self.B
        self.m = self.M
        self.space = self.SPACE


# gemi
class Ship():
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
    def draw(self,window):
        window.blit(self.ship_image,(self.x,self.y))

# oyuncu gemisi

class PlayerShip(Ship):
    def __init__(self,x,y,health=200):
        super().__init__(x,y,health)
        self.ship_image = MISSION_SHIP


class EnemyShip(Ship):
    def __init__(self, x, y, health=100,speed = 3):
        super().__init__(x, y, health)
        self.ship_image = ENEMY_SHİP
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.speed = speed
    def move(self):
        self.x -= self.speed

class Enemy_Rocket():
    def __init__(self, x, y,speed = 5):
        self.x = x
        self.y = y
        self.ship_image = MISSION_ENEMY_ROCKET
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.speed = speed
    def draw(self,window):
        window.blit(self.ship_image,(self.x,self.y))
    def move(self):
        self.x -= self.speed

class Player_Rocket():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_image = MISSION_SHIP_ROCKET
        self.mask = pygame.mask.from_surface(self.ship_image)
    def draw(self,window):
        window.blit(self.ship_image,(self.x,self.y))
    def move(self):
        self.x +=10


class Ulti():   #######################
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_image = MISSION_ULTI
        self.mask = pygame.mask.from_surface(self.ship_image)
    def draw(self,window):
        window.blit(self.ship_image,(self.x,self.y))
    def move(self,x1,y1):
        if x1 > self.x:
            self.x +=10
        elif x1 < self.x:
            self.x -=10
        if y1 < self.y:
            self.y -=5
        elif y1 > self.y:
            self.y +=5


class Captain_Marvel_CLASS():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = CaptainMarvel1
    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
    def move(self):
        self.x += 5

class Iron_Man_CLASS(Captain_Marvel_CLASS):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = IRONMAN

class Thor_CLASS(Captain_Marvel_CLASS):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = THOR

    def move(self):
        if self.x < 750:
            self.x +=5
        if self.y > 400:
            self.y -=4
    def move_run(self):
        self.x +=5
        self.y -=4

class STORM():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = THOR_storm
        

# çarpışma
def colide(object1,object2): 
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y

    

    if MISSION_SHIP_ROCKET != None:
            mask_rocket = pygame.mask.from_surface(MISSION_SHIP_ROCKET)

    return object1.mask.overlap(mask_rocket, (offset_x,offset_y)) != None

def thor_colide(object1,object2): 
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y

    

    if MISSION_SHIP_ROCKET != None:
            mask_rocket = pygame.mask.from_surface(THOR)

    return object1.mask.overlap(mask_rocket, (offset_x,offset_y)) != None

def colide_storm(object1,object2): 
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y

    mask_rocket = pygame.mask.from_surface(THOR_storm)

    return object1.mask.overlap(mask_rocket, (offset_x,offset_y)) != None

def colide_ship(object1,object2): 
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y

    

    if MISSION_SHIP_ROCKET != None:
            mask_rocket = pygame.mask.from_surface(MISSION_SHIP)

    return object1.mask.overlap(mask_rocket, (offset_x,offset_y)) != None
key_image = Keys()

Shield = False
strom2 = 0

class Hold_storm():
    def __init__(self,storm=None):
        self.storm = storm

hold_storm = Hold_storm()     
def main(SOUND_OPTİONS,SOUND_OPTİONS_COUNTER):
    game_music(SOUND_OPTİONS) 
    enemy_A = 1
    enemies = []
    enemy_lenght = 0
    level = 0

    kill = 0
    rocket_A = 1
    run = True
    
    gun = 0

    FPS = 60

    

    clock = pygame.time.Clock()

    player_rockets = []

    enemy_rockets = []

    player = PlayerShip(10,250)

    rocket_down = 30 # 30

    rocke_enemy_down = 180

    #enemy = EnemyShip(900,250)
    animation_counter = 1

    captain_counter = 0
    tony_counter = 0    
    thor_counter = 0

    thor_clouds = []
    thor_storms = []
    
    thor_storms_wait = 0    
    storm_kill = 0
    def draws(animation_counter):
         
        

        WIN.blit(BG,(0,0)) # arka planı 0,0 noktasından koyması sağlandı
        # captain
        if captain_counter == 1:
            WIN.blit(CaptainMarvel_image,(-50,290))
        if tony_counter == 1:
            WIN.blit(IRONMAN_image,(-25,290))
        if thor_counter == 1:
            WIN.blit(THOR_image,(-25,310))
            
        player.draw(WIN)

        if len(thor_clouds) > 1:
            for i in thor_clouds:
                WIN.blit(THOR_cloud,i) # THOR_storm , THOR_cloud
        
        if len(thor_storms) > 1:
            global hold_storm
            if thor_storms_wait  < 30:
                if thor_storms_wait == 0:
                    storm1 = random.choice(thor_storms)
                    ################# DENEME
                    """global strom2
                    storm1 = thor_storms[strom2]
                    strom2 +=1
                    if strom2 >=2:
                        strom2 -= 2"""
                    #################
                    hold_storm.storm = storm1
                if hold_storm.storm != None:
                    WIN.blit(hold_storm.storm.image,(hold_storm.storm.x,hold_storm.storm.y))
                """if strom2 >=2:
                        strom2 -= 2"""
            """for i in thor_storms:
                WIN.blit(THOR_storm,i)"""
        

        # tuşlar 
        global key_image
        a = 150
        WIN.blit(key_image.yön,(100+a,800))
        WIN.blit(key_image.space,(400+a,892))
        WIN.blit(key_image.b,(800+a,892))
        WIN.blit(key_image.m,(1000+a,892))
        WIN.blit(key_image.v,(1200+a,886))
        

        #################
        

        ## ses kapama resmi
        WIN.blit(SOUND,(10,10))

### yazı yazdırma
        pygame.init()
        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Düşman : {}".format(len(enemies)),1,(255,255,255))
        WIN.blit(text,(1080+50,20))
###
### yazı yazdırma
        
        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Leş : {}".format(kill),1,(255,255,255))
        WIN.blit(text,(980+50,20))
###
###

        font = pygame.font.SysFont("Algeria",30)
        text = font.render("From",1,(0,0,255))
        WIN.blit(text,(600+100,20))

###
###

        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Tahir Can Kozan",1,(255,255,255))
        WIN.blit(text,(660+100,20))

###
        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Can {}".format(player.health),1,(255,255,255))
        WIN.blit(text,(320+50,20))

        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Ateş",1,(255,255,255))
        WIN.blit(text,(680,870))


        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Güdümlü Füze",1,(255,255,255))
        WIN.blit(text,(925,870))


        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Süper Yardım",1,(255,255,255))
        WIN.blit(text,(1125,870))


        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Zırh",1,(255,255,255))
        WIN.blit(text,(1370,870))

        if kill < 20:

            font = pygame.font.SysFont("Algeria",30)
            text = font.render(f"Zırh {kill*5}%",1,(255,255,255))
            WIN.blit(text,(450+50,20))
        else:
            global Shield
            Shield = True
            font = pygame.font.SysFont("Algeria",30)
            text = font.render("Zırh 100%",1,(255,255,255))
            WIN.blit(text,(450+50,20))
            

        for i in enemy_rockets:
            i.draw(WIN)

        for i in ulti:
            i.draw(WIN)

        if rocket_A == 1:
            for i in player_rockets:
                i.draw(WIN)
            
        for i in supermans:
            i.draw(WIN)

        if enemy_A == 1:
            for i in enemies:
                i.draw(WIN)
       
                
        #print(animation_counter)
        pygame.display.update() # ekranın yenilenmesi için 


    size = 0
    supermans = []
    superman_counter = 1
    ulti = []
    ulti_counter = 1

    enemies_cpy = []

    storm_counter = 1
    
    while run:
        
        
        if rocket_down != 30:
            rocket_down+=1

        if rocke_enemy_down == 180: # 180
            rocke_enemy_down = 0
            for i in enemies:
                enemy_rockets.append(Enemy_Rocket(i.x,i.y,speed=5+enemy_lenght))
        else:
            rocke_enemy_down+=1

        clock.tick(FPS)
        draws(animation_counter)


        for i in enemy_rockets:
            i.move()

    
        if len(enemies) == 0:
            enemy_lenght +=2
            if enemy_lenght == 10: # 10
                enemy_lenght = 0
            for i in range(enemy_lenght):
                enemies.append(EnemyShip(random.randint(1680,1800),random.randint(100,650),speed=enemy_lenght-1))
            enemies_cpy = enemies
 

        for event in pygame.event.get(): # kapatma tuşuna tıklanırsa kapatır
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                print(mouse_x,mouse_y)
                
                if mouse_x > 0 and mouse_x <60:
                    
                    if mouse_y > 0 and mouse_y <60:
                        
                        if SOUND_OPTİONS_COUNTER%2 != 0:
                            SOUND_OPTİONS -= 0.1
                            SOUND_OPTİONS_COUNTER +=1

                        elif SOUND_OPTİONS_COUNTER%2 == 0:
                            SOUND_OPTİONS += 0.1  
                            SOUND_OPTİONS_COUNTER +=1 
                            

        global key_image
        key_list = []
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -=STEP
            key_image.yön = key_image.HAREKET_LEFT
            key_list.append("left")

        if keys[pygame.K_RIGHT] and player.x < 600:
            player.x +=STEP
            key_image.yön = key_image.HAREKET_RİGHT
            key_list.append("right")

        if keys[pygame.K_UP] and player.y > 0:
            player.y -=STEP 
            key_image.yön = key_image.HAREKET_UP
            key_list.append("up")
             
        if keys[pygame.K_DOWN] and player.y < 750:
            player.y +=STEP
            key_image.yön = key_image.HAREKET_DOWN
            key_list.append("down")
            
        if keys[pygame.K_v] and Shield == True:
            player.ship_image = SHIELD
            key_image.v = key_image.V_RED
        
        if keys[pygame.K_SPACE]:
            if rocket_down == COOL_DOWN:
                player_rockets.append(Player_Rocket(player.x+300,player.y+100))   # Player_Rocket(player.x+150,player.y+30)
                rocket_down = 0
            key_image.space = key_image.SPACE_RED

        if keys[pygame.K_m]:
            if superman_counter == 1:
                superman_counter = 0
                hero = random.randint(1,3)
                if hero == 1:
                    supermans.append(Captain_Marvel_CLASS(-200,player.y))
                    CaptainMarvel_voice()
                    captain_counter = 1
                elif hero == 2:
                    supermans.append(Iron_Man_CLASS(-200,player.y))
                    IronMan_voice()
                    tony_counter = 1
                elif hero == 3:
                    supermans.append(Thor_CLASS(-200,1050))
                    Thor_voice()
                    thor_counter = 1
            key_image.m = key_image.M_RED

        if keys[pygame.K_b]:
            if ulti_counter == 1:
                ulti_counter = 0
                ulti.append(Ulti(player.x+150,player.y+30))
                pass
            key_image.b = key_image.B_RED

        if keys[pygame.K_b] == False and keys[pygame.K_RIGHT] == False and keys[pygame.K_UP] == False and keys[pygame.K_DOWN] == False and keys[pygame.K_v] == False and keys[pygame.K_SPACE] == False and keys[pygame.K_m] == False and keys[pygame.K_b] == False:
            key_image.yön = key_image.HAREKET
            key_image.v = key_image.V
            key_image.b = key_image.B
            key_image.m = key_image.M
            key_image.space = key_image.SPACE
            
        if "left" in key_list and "up" in key_list:
            key_image.yön = key_image.HAREKET_UP_LEFT
        elif "right" in key_list and "up" in key_list:
            key_image.yön = key_image.HAREKET_UP_RİGHT
        elif "left" in key_list and "down" in key_list:
            key_image.yön = key_image.HAREKET_DOWN_LEFT
        elif "right" in key_list and "down" in key_list:
            key_image.yön = key_image.HAREKET_DOWN_RİGHT

        key_list.clear()

        for i in player_rockets:
            if i.x >= 1680:
                
                player_rockets.remove(i)

        for i in player_rockets:
            i.move()

        for i in ulti: ##################
            if enemies != []:
                i.move(enemies[0].x,enemies[0].y)
        
        for i in supermans:
            if thor_counter == 1:
                if storm_kill < 4:
                    i.move()
                else:
                    i.move_run()
                
            else:
                i.move()

        for i in supermans:
            if i.x > 1680:
                supermans.clear()
                captain_counter = 0
                tony_counter = 0
                superman_counter = 1
                if thor_counter == 1:
                    thor_counter = 0
                    thor_clouds.clear()
                    thor_storms.clear()
                    hold_storm.storm = None
                    storm_kill = 0
                    thor_storms_wait = 0
                    storm_counter = 1

        if thor_counter == 1:
            
            if supermans[0].x == 750 and supermans[0].y == 398 and storm_counter == 1:
                #thor_clouds.append([50,10])
                #thor_clouds.append([550,10])
                #thor_clouds.append([1050,10])


                print(1111)
                thor_storms.append(STORM(100,100)) # 100
                thor_storms.append(STORM(600,100))
                thor_storms.append(STORM(1100,100))
                storm_counter = 0

            if thor_storms_wait == 30:
                thor_storms_wait = 0
            else:
                thor_storms_wait+=1
                

        for i in supermans:
            if i.x > 450:
                if captain_counter == 1:
                    i.image = CaptainMarvel2
                

        for i in enemies:
            i.move()

        if player.ship_image != SHIELD:
            for i in enemy_rockets:
                
                a = colide_ship(i,player)
                    
                if a == True:
                        

                    if i in enemy_rockets:
                        enemy_rockets.remove(i)
                    

                    boom()
                    player.health -=20
                        
                    
        else:
            for i in enemy_rockets:
                
                a = colide_ship(i,player)
                    
                if a == True:
                        

                    if i in enemy_rockets:
                        enemy_rockets.remove(i)
                    

                    boom()
                    
        
        for i in enemy_rockets:
            if i.x < 5:
                enemy_rockets.remove(i)

        for i in enemies:
            if hold_storm.storm != None:
                a = colide_storm(i,hold_storm.storm)
                 
                if a == True:
                    

                    if i in enemies:
                        enemies.remove(i)
                    

                    boom()
                    storm_kill +=1
                    size+=1
                    kill+=1

            for k in player_rockets:
                a = colide(i,k)
                 
                if a == True:
                    

                    if i in enemies:
                        enemies.remove(i)
                    player_rockets.remove(k)

                    boom()
                    
                    size+=1
                    kill+=1
            
            for s in supermans:
                if thor_counter != 1:
                    a = colide(i,s)
                    
                    if a == True:
                        

                        if i in enemies:
                            enemies.remove(i)
                        
                        boom()
                        
                        size+=1
                        kill+=1
                else:
                    
                    a = thor_colide(i,s)
                    
                    if a == True:
                        

                        if i in enemies:
                            enemies.remove(i)
                        
                        boom()
                        
                        size+=1
                        kill+=1

            for u in ulti:
                a = colide(i,u)
                
                if a == True:
                    

                    if i in enemies:
                        enemies.remove(i)
                    
                    boom()
                    ulti.clear()
                    ulti_counter = 1
                    size+=1
                    kill+=1

            
            if player.ship_image != SHIELD:
                a = colide_ship(i,player)
                   
                if a == True:
                        

                    if i in enemies:
                        enemies.remove(i)
                    

                    boom()
                    player.health -=10
                        
                    size+=1
                    kill+=1
            else:
                a = colide_ship(i,player)
                    
                if a == True:
                    
                    if i in enemies:
                        enemies.remove(i)

                    boom()
           
                    size+=1
                    kill+=1

 
        for i in enemies_cpy:
            if i.x <= 0:
                size+=1
                enemies_cpy.remove(i)
                  
        
        #print(size,enemy_lenght)        
        if size == enemy_lenght:
            enemy_A=0
            #enemy_lenght+=2
            enemies.clear()
            enemy_A=1
            player_rockets.clear()
            
            size = 0
          

        if player.health == 0:
            
            
            WIN.blit(BG,(0,0)) # arka planı 0,0 noktasından koyması sağlandı
            pygame.display.update() # ekranın yenilenmesi için 
            run1 = True
            while run1:
                WIN.blit(BG,(0,0)) # arka planı 0,0 noktasından koyması sağlandı

                pygame.init() # ekrana yazı yazdırmak için gerekli

                font = pygame.font.SysFont("Algeria",25)                  #
                text = font.render("Kaybettin - Tekar oynamak için (n) - Çıkış yapmak için pencereyi kapaın",1,(255,255,255)) # akrana yazı yazdırma
                WIN.blit(text,(200,250))                                  #

                pygame.display.update() # ekranın yenilenmesi için 

                for event in pygame.event.get():   
                            
                        if event.type == pygame.QUIT: # kapatma tuşuna tıklanırsa kapatır
                            run1 = False
                            run = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_n] :
                    run1 = False

                    enemy_A = 1
                    enemies = []
                    enemy_lenght = 0
                    level = 0

                    kill = 0
                    rocket_A = 1
                    run = True
                    
                    gun = 0

                    FPS = 60

                    clock = pygame.time.Clock()

                    player_rockets = []

                    player = PlayerShip(10,250)

                    rocket_down = 30

                    animation_counter = 1

                    size = 0
                    supermans = []
                    superman_counter = 1

                    enemies_cpy = []
   
start(exit)

if bitir.exit == 1:
    main(SOUND_OPTİONS,SOUND_OPTİONS_COUNTER)
