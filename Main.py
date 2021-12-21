#import pygame
import pygame, sys
from pygame.locals import *

#import files
import colors
import Player
import Wall
import level
# Initialize program
pygame.init()
 
# FPS
fps = 60
frame_per_sec = pygame.time.Clock()

# Setting up Variables
acc = 0.5
fric = -0.12
 
#Vector Math
vec = pygame.math.Vector2  # 2 for two dimensional

# Setup display with caption
display_surf = pygame.display.set_mode((level.width, level.height))
pygame.display.set_caption("DownBeat")

#Sprites
player1 = Player.Player(colors.green)
platform1 = Wall.Wall(level.width/2, level.height-20, level.width, 30)

#Sprite Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(platform1)

# Beginning Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    display_surf.fill((colors.white))

    for entity in all_sprites:
        display_surf.blit(entity.surf, entity.rect)

    pygame.display.update()
    frame_per_sec.tick(fps)