import pygame
import Player
import Wall
import gamerules
import colors

#Sprites
player1 = Player.Player(colors.green, 0.5, -0.25, 0.5)
platform1 = Wall.Wall(gamerules.width/2, gamerules.height-20, gamerules.width, 30)

#Sprite Groups
obsticales = pygame.sprite.Group()
obsticales.add(platform1)

all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(obsticales)