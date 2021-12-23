#import pygame
import pygame, sys
from pygame.locals import *
pygame.init()

#import files
import colors
import Character
import Player
import Wall
import gamerules
 
# FPS
fps = 60
frame_per_sec = pygame.time.Clock()

# Setup display with caption
display_surf = pygame.display.set_mode((gamerules.width, gamerules.height))
pygame.display.set_caption("DownBeat")

#Sprites
player1 = Player.Player(colors.green, 0.5)
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
    all_sprites.update()

    for entity in all_sprites:
        display_surf.blit(entity.surf, entity.rect)

    pygame.display.update()
    frame_per_sec.tick(fps)