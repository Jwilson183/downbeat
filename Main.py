#import pygame
import pygame, sys
from pygame.locals import *
pygame.init()

#import files
import colors
import sprites
import Player
import Wall
import gamerules
 
# FPS
fps = 60
frame_per_sec = pygame.time.Clock()

# Setup display with caption
display_surf = pygame.display.set_mode((gamerules.width, gamerules.height))
pygame.display.set_caption("DownBeat")

# Beginning Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    display_surf.fill((colors.white))
    sprites.all_sprites.update()

    for entity in sprites.all_sprites:
        display_surf.blit(entity.surf, entity.rect)

    pygame.display.update()
    frame_per_sec.tick(fps)