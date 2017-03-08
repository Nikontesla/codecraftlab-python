
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
        for x in range(3):
            self.images.append(pygame.image.load('fishy.png'))
            self.index = 0
            self.image = self.images[self.index]
            self.image.set_colorkey((255,255, 255), RLEACCEL)
            self.rect = self.image.get_rect()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.scale(self.image, (self.size[0]/5,self.size[1]/5))
            self.cooldown = 70
            self.old_time = pygame.time.get_ticks()
           
    
    def update(self):
        for i in range (random.randint(6,10)):
            self.rect.move_ip( 6*random.random()-3,  6*random.random()-3)
            sleep(.001)
    

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
            
pygame.init()
myfont=pygame.font.SysFont("monospace",16)
#create your screen
screen = pygame.display.set_mode((800, 600))

# instantiate our player; right now she's just a rectangle
player = Player()

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
all_sprites = pygame.sprite.Group()
all_sprites.add(player)



# Variable to keep our main loop running
running = True

#create game clock, create variable for frames per second (FPS), and get starting time
clock = pygame.time.Clock()
fps = 1000
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
    
 #       elif(event.type == ADDPLAYER):
           # new_player = Sasha()
         #   player.add(new_player)
        #    all_sprites.add(new_player)
    
    #draw background
    #screen.blit(background, (0, 0))
    screen.fill([255, 255, 255])
    screen.blit(background_img, screen.get_size())
    
    #update player position
    player.update()
    

    # Draw objects onto screen at its updated coordinates
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.flip()

sleep(5)
#exit the game
pygame.quit()

