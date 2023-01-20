import pygame, sys
from pygame import *

# Initialize Pygame
pygame.init()

# Set screen size and caption
screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Side-Scrolling Example")


# time 
fpsClock = pygame.time.Clock()
FPS = 60

# player class
class Player():

    velx = 0
    vely = 0
    quickness = 15
    gravity = 3
    
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("blue_Bird.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.centery = screen_height // 2
        

# Load background image
bg_width = 2500
bg_height = 1250
bg_image = pygame.transform.scale(pygame.image.load("entrance.png"), (bg_width, bg_height))
bg_rect = bg_image.get_rect()
bg_rect.x = 0
bg_rect.y = 0
bg_surf = pygame.Surface((1600, 1200))
bg_surf.blit(bg_image, bg_rect)



# Game loop
player = Player()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.velx = 0
    player.vely = player.gravity
    


    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.velx = -player.quickness
        
    if keys[pygame.K_RIGHT]:
        player.velx = player.quickness
        
    if keys[pygame.K_UP]:
        player.vely -= player.quickness
        
    if keys[pygame.K_DOWN]:
        player.vely += player.quickness
        
    player.rect.x += player.velx
    player.rect.y += player.vely

    if player.rect.top <= screen_height / 8:
        player.rect.y -= player.vely
        bg_rect.y -= player.vely

    if player.rect.left <= screen_width / 8:
        player.rect.x -= player.velx
        bg_rect.x -= player.velx
    
    if player.rect.bottom >= (7/8) * screen_height:
        player.rect.y -= player.vely
        bg_rect.y -= player.vely

    if player.rect.right >= (7/8) * screen_width:
        player.rect.x -= player.velx
        bg_rect.x -= player.velx


    # these second two if statments must also take away velx or vely since if they were activated then velx or vely would itself be a negative number
    # taking away a negative number is addition
  
        

    # Keep player within the background surface
    if player.rect.left <= bg_rect.left + screen_width / 8 :
        player.rect.left = bg_rect.left + screen_width / 8
    if player.rect.right  >= bg_rect.right - screen_width / 8 :
        player.rect.right = bg_rect.right - screen_width / 8 
    if player.rect.top <= bg_rect.top + screen_height / 8:
        player.rect.top = bg_rect.top + screen_height / 8
    if player.rect.bottom >= bg_rect.bottom - screen_height / 8:
        player.rect.bottom = bg_rect.bottom - screen_height / 8


    player.image = pygame.transform.scale(pygame.image.load("blue_Bird.png"), (100, 100))
    if player.velx > 0:
        player.image = pygame.transform.flip(player.image, True, False)
        



  
    screen.fill((0, 0, 0))
    screen.blit(bg_image, bg_rect)
    screen.blit(player.image, player.rect)

    formatted_score = (f'PLAYER RECT: {player.rect}  Velx: {player.velx}')
    fontObj = pygame.font.Font('Pixeltype.ttf', 30)
    scoretxtSurf = fontObj.render(formatted_score, True, (0, 0 ,0))
    scoretxt_rect = scoretxtSurf.get_rect()
    scoretxt_rect.center = (400, 400)
    screen.blit(scoretxtSurf, scoretxt_rect)


    pygame.display.update()
    fpsClock.tick(FPS)


