#import pygame
import pygame, sys
from pygame.locals import *
from Character import Character
from Wall import Wall

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

		#Sprites
		self.all_sprites = pygame.sprite.Group()
		self.players     = pygame.sprite.Group()
		self.platforms   = pygame.sprite.Group()

		self.create_sprites()

	#some of these things shouldn't happen every frame
	def update(self):
		self.register_collisions()
		self.update_sprites()
		self.render()

	def update_sprites(self):
		self.all_sprites.update()

	def render(self):
		self.display_surf.fill((colors.white))
		for entity in self.all_sprites:
			#create a surf and rect by adding the screen location to the entity surf and rect, then blit the new surf and rect to the screen
			self.display_surf.blit(entity.surf, entity.rect)

	def create_sprites(self):
		""" Create all sprites and add them to their respective groups. """
		#players
		self.player1 = Player(
			colors.green,
			max_acceleration = 0.5,
			fric       = -0.25,
			gravity    = 0.5,
			jump_speed = 5,
			max_jump   = 10
		)

		self.players.add (self.player1)
		self.all_sprites.add(self.players)

		#platforms
		self.platform1 = Wall(self.display_width/2, self.display_height-20, self.display_width, 30)
		self.platform2 = Wall(self.display_width/2 + 100, self.display_height-50, 30, 90)
		self.platform3 = Wall(self.display_width/8, self.display_height-150, self.display_width - 150, 30)
		
		#platform group
		self.platforms.add(self.platform1)
		self.platforms.add(self.platform2)
		self.platforms.add(self.platform3)
		self.all_sprites.add(self.platforms)
		
	def register_collisions(self):
		#for player in self.players:	
		hits = pygame.sprite.spritecollide(self.player1, self.platforms, False)
		for platform in hits:
			self.player1.handle_platform_collisions(platform)
			platform.handle_player1_collisions(self.player1)
