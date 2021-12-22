#import pygame
import pygame, sys
from pygame.locals import *

#import files
import colors
import Character
import Player
import Wall
import gamerules
# Initialize program
pygame.init()
 
# FPS
fps = 60
frame_per_sec = pygame.time.Clock()

# Setup display with caption
display_surf = pygame.display.set_mode((gamerules.width, gamerules.height))
pygame.display.set_caption("DownBeat")

#Sprites
player1 = Player.Player(colors.green)
platform1 = Wall.Wall(gamerules.width/2, gamerules.height-20, gamerules.width, 30)

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