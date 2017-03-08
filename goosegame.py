#goosegame
#import library
import pygame
import random
from random import randint
from pygame.locals import *
from time import sleep



class Player(pygame.sprite.Sprite):
    #def __init__(self):
        # super(Player, self).__init__()
        # self.surf = pygame.Surface((75, 75))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect()
    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        for x in range(1):
            self.images.append(pygame.image.load('chrisgoose' + str(x) + '.gif').convert())
            self.index = 0
            self.image = self.images[self.index]
            self.image.set_colorkey((255,255, 255), RLEACCEL)
            self.rect = self.image.get_rect()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.scale(self.image, (self.size[0]/5,self.size[1]/5))
            self.cooldown = 70
            self.old_time = pygame.time.get_ticks()
        
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

        new_time = pygame.time.get_ticks()
        if new_time - self.old_time >= self.cooldown:
            self.old_time = new_time
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
            #size = self.image.get_size()
            #self.image = pygame.transform.scale(self.image, (size[0]/5,size[1]/5))
            
# SASHA CLASS

class Sasha(pygame.sprite.Sprite):
     def __init__(self):
        super(Sasha, self).__init__() 
        self.images = []
        for x in range(1):
            self.images.append(pygame.image.load('greengoose/' + str(x) + '.gif').convert())
            self.index = 0
            self.image = self.images[self.index]
            self.image.set_colorkey((255,255, 255), RLEACCEL)
            self.rect = self.image.get_rect()
         #self.size = self.image.get_size()
        #self.image = pygame.transform.scale(self.image, (self.size[0]/5,self.size[1]/5))
            self.cooldown = 70
            self.old_time = pygame.time.get_ticks()
        #self.surf = pygame.Surface((75, 75))
        #self.surf.fill((255, 255, 255))
        #self.rect = self.surf.get_rect()
      #  self.image = pygame.image.load("cat5.jpg").convert()
      #  self.image.set_colorkey((255,255, 255), RLEACCEL)
      #  self.rect = self.image.get_rect()

     def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_a]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(2, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

        new_time = pygame.time.get_ticks()
        if new_time - self.old_time >= self.cooldown:
            self.old_time = new_time
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.image.set_colorkey((255, 255, 255), RLEACCEL)

class GoodPizzaOpponent(pygame.sprite.Sprite):
    # def __init__(self):
        # super(Opponent, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        # self.speed = random.randint(0, 2)
        
    def __init__(self):
        super(GoodPizzaOpponent, self).__init__()
      #  self.image = pygame.image.load('eevee8.jpg').convert()
        #self.image.set_colorkey((255, 255, 255), RLEACCEL)
       # self.rect = self.image.get_rect(
       #     center=(random.randint(820, 900), random.randint(0, 600))
       # )
        self.speed = 1
        self.images = []
        for x in range(1):
            self.images.append(pygame.image.load('pizza/' + str(x) + '.gif').convert())
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.cooldown = 500
        self.old_time = pygame.time.get_ticks()
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        new_time = pygame.time.get_ticks()
        if new_time - self.old_time >= self.cooldown:
            self.old_time = new_time
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            size = self.image.get_size()
            #self.image = pygame.transform.scale(self.image, (size[0]/5,size[1]/5))

class EvilPizzaOpponent(pygame.sprite.Sprite):
    # def __init__(self):
        # super(Opponent, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        # self.speed = random.randint(0, 2)
        
    def __init__(self):
        super(EvilPizzaOpponent, self).__init__()
      #  self.image = pygame.image.load('eevee8.jpg').convert()
        #self.image.set_colorkey((255, 255, 255), RLEACCEL)
       # self.rect = self.image.get_rect(
       #     center=(random.randint(820, 900), random.randint(0, 600))
       # )
        self.speed = 1
        self.images = []
        for x in range(2):
            self.images.append(pygame.image.load('evil pizza/' + str(x) + '.gif').convert())
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.cooldown = 500
        self.old_time = pygame.time.get_ticks()
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        new_time = pygame.time.get_ticks()
        if new_time - self.old_time >= self.cooldown:
            self.old_time = new_time
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            size = self.image.get_size()
            #self.image = pygame.transform.scale(self.image, (size[0]/5,size[1]/5))


#initialize pygame modules
pygame.init()
myfont=pygame.font.SysFont("monospace",16)
Pinky= 0
Pepper= 0
#create your screen
screen = pygame.display.set_mode((800, 600))

# instantiate our player; right now she's just a rectangle
player = Player()
player2= Sasha()

#set background color
background = pygame.Surface(screen.get_size())
#background.fill((235, 246, 255))


# Create the surface and pass in a tuple with its length and width
#surf = pygame.Surface((75, 75))

# Give the surface a color to differentiate it from the background
#surf.fill((255, 255, 255))
#rect = surf.get_rect()


#Create Groups and add game objects
players = pygame.sprite.Group()
goodpizzas = pygame.sprite.Group()
badpizzas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)

#create opponent event
ADDOPPONENT = pygame.USEREVENT + 1

#set timer for opponent event to occur every 250ms
pygame.time.set_timer(ADDOPPONENT, 250)


# Variable to keep our main loop running
running = True

#create game clock, create variable for frames per second (FPS), and get starting time
clock = pygame.time.Clock()
fps = 1000
scoretext= myfont.render("",1,(0,0,0))
pepper_wins_img = pygame.image.load('PepperWins.png')
pinky_wins_img = pygame.image.load('PinkyWins.png')
background_img = pygame.image.load('backgroundformypug.png')

gameover = False
winner = None

# Our main loop!
while running:    
    #set game FPS
    clock.tick(fps)

    
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDO50) WN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        # Check for Opponent event; if ADDOPPONENT, create and add opponent
        elif(event.type == ADDOPPONENT):
            new_opponent1 = GoodPizzaOpponent()
            goodpizzas.add(new_opponent1)
            all_sprites.add(new_opponent1)
            
            rnum=randint(0,1)
            if rnum== 0:
                new_opponent2 = EvilPizzaOpponent()
                badpizzas.add(new_opponent2)
                all_sprites.add(new_opponent2)
 #       elif(event.type == ADDPLAYER):
           # new_player = Sasha()
         #   player.add(new_player)
        #    all_sprites.add(new_player)
    
    #draw background
    #screen.blit(background, (0, 0))
    screen.fill([255, 255, 255])
    screen.blit(background_img, screen.get_size())
    #get pressed keys
    pressed_keys = pygame.key.get_pressed()
    
    #update player position
    player.update(pressed_keys)
    player2.update(pressed_keys)
    
    #update opponent position
    goodpizzas.update()
    badpizzas.update()

    # Draw objects onto screen at its updated coordinates
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        
    #kill player if player and opponent collide
    opp_spr1 = pygame.sprite.spritecollideany(player, goodpizzas)
    
    if opp_spr1:
        #player.kill()
        opp_spr1.kill()
        Pepper+=1
        
    opp_spr2 = pygame.sprite.spritecollideany(player2, goodpizzas)
    if opp_spr2:
        #player.kill()
        opp_spr2.kill()
        Pinky+=1

    opp_spr1 = pygame.sprite.spritecollideany(player, badpizzas)
    
    if opp_spr1:
        #player.kill()
        opp_spr1.kill()
        Pepper-=1
        
    opp_spr2 = pygame.sprite.spritecollideany(player2, badpizzas)
    if opp_spr2:
        #player.kill()
        opp_spr2.kill()
        Pinky-=1


    scoretext= myfont.render("Pinky: "+str(Pinky)+" Pepper: "+str(Pepper),1,(0,0,0))
    screen.blit(scoretext, (5,10))
    if  not gameover and Pinky >= 420:
        winner = pinky_wins_img
        gameover = True
        
    if  not gameover and Pepper >= 420:
        winner = pepper_wins_img
        gameover = True

    if gameover:
        screen.blit(winner,(0,0))

    pygame.display.flip()

sleep(5)
#exit the game
pygame.quit()
