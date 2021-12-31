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
		self.walls       = pygame.sprite.Group()

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
			fric        = -0.25,
			gravity     = 0.5,
			jump_speed  = 5,
			max_jump    = 200,
			width       = 30,
			height      = 30,
			initial_pos = (100, 300)
		)

		self.players.add (self.player1)
		self.all_sprites.add(self.players)

		#walls
		self.wall1 = Wall(self.display_width/2, self.display_height-20, self.display_width, 30)
		self.wall2 = Wall(self.display_width/2 + 100, self.display_height-50, 30, 90)
		self.wall3 = Wall(self.display_width/8, self.display_height-150, self.display_width - 150, 30)
		
		#wall group
		self.walls.add(self.wall1)
		self.walls.add(self.wall2)
		self.walls.add(self.wall3)
		self.all_sprites.add(self.walls)
		
	def register_collisions(self):
		#for player in self.players:	
		hits = pygame.sprite.spritecollide(self.player1, self.walls, False)
		for wall in hits:
			self.player1.handle_wall_collisions(wall)
			wall.handle_player1_collisions(self.player1)
