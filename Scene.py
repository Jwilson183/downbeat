#import pygame
import pygame, sys
from pygame.locals import *
from pygame.math import disable_swizzling
from Character import Character
from Wall import Wall
from Collisions import Collisions

#import files
import colors
from Player import Player
from Wall import Wall

class Scene:
	def __init__(
		self,
		display_width: int,
		display_height: int,
	):
		#Display
		self.display_width = display_width
		self.display_height = display_height

		#Make Display
		self.display_surf = pygame.display.set_mode((self.display_width, self.display_height))
		pygame.display.set_caption("DownBeat")	
		self.display_surf.fill((colors.white))

		#Sprites
		self.all_sprites = pygame.sprite.Group()
		self.players     = pygame.sprite.Group()
		self.platforms   = pygame.sprite.Group()

		self.create_sprites()

	#some of these things shouldn't happen every frame
	def update(self):
		self.update_sprites()
		self.render()

	def update_sprites(self):
		self.all_sprites.update()

	def render(self):
		for entity in self.all_sprites:
			#create a surf and rect by adding the screen location to the entity surf and rect, then blit the new surf and rect to the screen
			self.display_surf.blit(entity.surf, entity.rect)

	def create_sprites(self):
		""" Create all sprites and add them to their respective groups. """
		#players
		self.player1 = Player(colors.green, 0.5, -0.25, 0.5, 5, 20)
		self.players.add (self.player1)
		self.all_sprites.add(self.players)

		#platforms
		self.platform1 = Wall(self.display_width, self.display_height-20, self.display_width, 30)
		self.platforms.add(self.platform1)
		self.all_sprites.add(self.platforms)

	def detect_collisions(self):
		self.Player_Platform_Collision = Collisions(Player, self.platforms, False)
		if Collisions.detect_collisions:
			Character.handle_collisions()
			Wall.handle_collisions()
		else:
			Character.handle_no_collisions()
			Wall.handle_no_collisions()