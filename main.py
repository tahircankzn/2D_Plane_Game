import pygame
import os
import random
from pygame import mixer

pygame.display.set_caption("Kizil Elma")



WIDHT = 1000
HEIGHT = 562
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
STEP = 5
SOUND_OPTİONS = 0.1
SOUND_OPTİONS_COUNTER = 1

# İMAGE yükleme

# arka plan
BG = pygame.image.load("background_space.png")
# gemi resim
MISSION_SHIP = pygame.image.load("mission_ship.png")
#rocket
MISSION_SHIP_ROCKET = pygame.image.load("blue_rocket.png")

ENEMY_SHİP = pygame.image.load("enemy_ship_blue.png")

SOUND = pygame.image.load("sound.png")


def boom():
    boom = pygame.mixer.Sound("boom.wav")
    boom.set_volume(0.1)
    boom.play()


def game_music(SOUND_OPTİONS):
    #music
    # arka plan müziği
    #Instantiate mixer
    mixer.init()

    #Load audio file
    mixer.music.load('The Last of Us TV Show  Episode 1 Ending Song.wav')

    print("music started playing....")

    #Set preferred volume
    mixer.music.set_volume(SOUND_OPTİONS)

    #Play the music
    mixer.music.play(-1)

game_music(SOUND_OPTİONS) 



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
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_image = MISSION_SHIP


class EnemyShip(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = ENEMY_SHİP
        self.mask = pygame.mask.from_surface(self.ship_image)
    def move(self):
        self.x -=3

class Player_Rocket():
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = MISSION_SHIP_ROCKET
        self.mask = pygame.mask.from_surface(self.ship_image)
    def move(self):
        self.x +=5




# çarpışma
def colide(object1,rocketX,rocketY): 
    offset_x = rocketX - object1.x
    offset_y = rocketY - object1.y

    if MISSION_SHIP_ROCKET != None:
            mask_rocket = pygame.mask.from_surface(MISSION_SHIP_ROCKET)

    return object1.mask.overlap(mask_rocket, (offset_x,offset_y)) != None

rocketX = 20
rocketY = 300


def main(rocketX,rocketY,SOUND_OPTİONS,SOUND_OPTİONS_COUNTER):
    enemy_A = 1
    enemies = []
    enemy_lenght = 0
    level = 0

    kill = 0


    run = True
    gun = 0

    FPS = 60

    clock = pygame.time.Clock()

    player_rocket = []




    player = PlayerShip(10,250)


    

    #enemy = EnemyShip(900,250)

    def draws(rocketX,rocketY):
        WIN.blit(BG,(0,0)) # arka planı 0,0 noktasından koyması sağlandı
        player.draw(WIN)


        ## ses kapama resmi
        WIN.blit(SOUND,(10,10))

### yazı yazdırma
        pygame.init()
        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Enemy : {}".format(len(enemies)),1,(255,255,255))
        WIN.blit(text,(880,10))
###
### yazı yazdırma
        
        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Kill : {}".format(kill),1,(255,255,255))
        WIN.blit(text,(780,10))
###
###

        font = pygame.font.SysFont("Algeria",30)
        text = font.render("From",1,(0,0,255))
        WIN.blit(text,(400,20))

###
###

        font = pygame.font.SysFont("Algeria",30)
        text = font.render("Tahir Can Kozan",1,(255,255,255))
        WIN.blit(text,(460,20))

###


        if gun == 1:
            WIN.blit(MISSION_SHIP_ROCKET,(rocketX,rocketY))
            
        

        if enemy_A == 1:
            for i in enemies:
                i.draw(WIN)

        

        
                

        pygame.display.update() # ekranın yenilenmesi için 


    size = 0

    enemies_cpy = []
    while run:
        
        
        

        clock.tick(FPS)
        draws(rocketX,rocketY)

        

        if len(enemies) == 0:
            enemy_lenght +=2
            if enemy_lenght == 10:
                enemy_lenght = 0
            for i in range(enemy_lenght):
                enemies.append(EnemyShip(random.randint(1000,1400),random.randint(100,500)))
            enemies_cpy = enemies


    

        if gun == 1:
            rocketX +=5
            if rocketX >=800:
                rocketX = player.x + 10
                rocketY = player.y + 50
                gun = 0

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
                            







        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -=STEP
            if gun == 0:
                rocketX -=STEP
        if keys[pygame.K_RIGHT] and player.x < 200:
            player.x +=STEP
            if gun == 0:
                rocketX +=STEP

        if keys[pygame.K_UP] and player.y > 0:
            player.y -=STEP 
            if gun == 0:
                rocketY -=STEP 
        if keys[pygame.K_DOWN] and player.y < 500:
            player.y +=STEP
            if gun == 0:
                rocketY +=STEP
        
        if keys[pygame.K_SPACE]:
            
            gun = 1

        for i in enemies:
            i.move()

        for i in enemies:
            a = colide(i,rocketX,rocketY)
            #print(a) 
            if a == True:
                enemies.remove(i)
                boom()
                gun = 0
                size+=1
                kill+=1
    
                rocketX = player.x + 10
                rocketY = player.y + 50

        
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
            
            size = 0
            

        print(SOUND_OPTİONS)

      

main(rocketX,rocketY,SOUND_OPTİONS,SOUND_OPTİONS_COUNTER)
