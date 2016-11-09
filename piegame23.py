#import library
import pygame
import random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    #def __init__(self):
        # super(Player, self).__init__()
        # self.surf = pygame.Surface((75, 75))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect()
    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        for x in range(7):
            self.images.append(pygame.image.load('pug/' + str(x) + '.gif').convert())
        self.index = 0
        self.image = self.images[self.index]
        #self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.scale(self.image, (self.size[0]/5,self.size[1]/5))
        self.cooldown = 70
        self.old_time = pygame.time.get_ticks()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

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

class Opponent(pygame.sprite.Sprite):
    # def __init__(self):
        # super(Opponent, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        # self.speed = random.randint(0, 2)
        
    def __init__(self):
        super(Opponent, self).__init__()
        self.image = pygame.image.load('eevee8.jpg').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = 1
        

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()            

#initialize pygame modules
pygame.init()

#create your screen
screen = pygame.display.set_mode((800, 600))

# instantiate our player; right now he's just a rectangle
player = Player()

#set background color
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

# Create the surface and pass in a tuple with its length and width
#surf = pygame.Surface((75, 75))

# Give the surface a color to differentiate it from the background
#surf.fill((255, 255, 255))
#rect = surf.get_rect()


#Create Groups and add game objects
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#create opponent event
ADDOPPONENT = pygame.USEREVENT + 1

#set timer for opponent event to occur every 250ms
pygame.time.set_timer(ADDOPPONENT, 250)


# Variable to keep our main loop running
running = True

#create game clock, create variable for frames per second (FPS), and get starting time
clock = pygame.time.Clock()
fps = 1000

# Our main loop!
while running:
    #set game FPS
    clock.tick(fps)
    
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        # Check for Opponent event; if ADDOPPONENT, create and add opponent
        elif(event.type == ADDOPPONENT):
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
    
    #draw background
    screen.blit(background, (0, 0))
    
    #get pressed keys
    pressed_keys = pygame.key.get_pressed()
    
    #update player position
    player.update(pressed_keys)
    
    #update opponent position
    opponents.update()

    # Draw objects onto screen at its updated coordinates
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        
    #kill player if player and opponent collide
    opp_spr = pygame.sprite.spritecollideany(player, opponents)
    if opp_spr:
        #player.kill()
        opp_spr.kill()

    pygame.display.flip()

#exit the game
pygame.quit()
