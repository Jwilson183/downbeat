#import pygame
import pygame, sys
from pygame.locals import *
from pygame.math import disable_swizzling

#import files
import colors
import Player
import Wall

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

	def update(self):
		self.fill_display_surf()
		self.Scene.all_sprites.update()
		self.attatch_sprites()
		self.make_players()
		self.make_platforms()
		self.make_all_sprites_groups()

	def fill_display_surf(self):
		self.display_surf.fill((colors.white))

	def update_sprites(self):
		Scene.all_sprites.update()

	def attatch_sprites(self):
		for entity in self.all_sprites:
				#create a surf and rect by adding the screen location to the entity surf and rect, then blit the new surf and rect to the screen
				self.display_surf.blit(entity.surf, entity.rect)
	
	#does this need to be generalized?
	def make_players(self):
		self.player1 = Player.Player(colors.green, 0.5, -0.25, 0.5, 5, 20, self)
		self.players = pygame.sprite.Group()
		self.players.add (self.player1)
	
	def make_platforms(self):
		self.platform1 = Wall.Wall(self.display_width, self.display_height-20, self.display_width, 30)
		self.platforms = pygame.sprite.Group()
		self.platforms.add(self.platform1)

	def make_all_sprites_groups(self):
		all_sprites = pygame.sprite.Group()
		all_sprites.add(self.players)
		all_sprites.add(self.platforms)