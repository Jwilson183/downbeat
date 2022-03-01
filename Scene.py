#import pygame
import pygame
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
		self.test_lines  = pygame.sprite.Group()
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
			max_jump    = 20,
			width       = 30,
			height      = 30,
			initial_pos = (100, 150)
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
		
		#Test Line
		'''
		self.test_lines.add(self.topleft_line)
		self.test_lines.add(self.topright_line)
		self.test_lines.add(self.bottomleft_line)
		self.test_lines.add(self.bottomright_line)
		self.all_sprites.add(self.test_lines)
		'''
		
	def register_collisions(self):
		#for player in self.players:	
	#for player in self.players:	
		hits = pygame.sprite.spritecollide(self.player1, self.walls, False)
		for wall in hits:
			self.player1.handle_wall_collisions(wall)
			wall.handle_player1_collisions(self.player1)
	

	
	'''	This code used to be in register collisions for line collision
	self.keep_checking = True
	self.register_collisions_corners(self.player1.rect.topleft)
	self.register_collisions_corners(self.player1.rect.topright)
	self.register_collisions_corners(self.player1.rect.bottomleft)
	self.register_collisions_corners(self.player1.rect.bottomright)
	'''

'''
	def register_collisions_corners(self, corner):
			
			if self.keep_checking:
			player1_last_pos = corner - (self.player1.vel + 0.5 *self.player1.acc)
			line = pygame.draw.line(self.display_surf, colors.blue, player1_last_pos, corner)
			for wall in self.walls:
				line_in_rect = wall.rect.clipline(line)
				print(line_in_rect)
				if line_in_rect:
					self.player1.handle_wall_collisions(wall, player1_last_pos)
					self.keep_checking = False
		
		#tests top left line with all walls
		self.player1_tl_last_pos = self.player1.rect.topleft - (self.player1.vel + 0.5 * self.player1.acc)
		self.topleft_line = pygame.draw.line(self.display_surf, colors.blue, self.player1_tl_last_pos, self.player1.rect.topleft)		
		
		for wall in self.walls:
			self.line_in_rect = wall.rect.clipline(self.topleft_line)

		if self.line_in_rect:
			self.player1.handle_wall_collisions(wall, self.player1_tl_last_pos)

		#test top right line with all walls
		self.player1_tr_last_pos = self.player1.rect.topright - (self.player1.vel + 0.5 * self.player1.acc)
		self.topright_line = pygame.draw.line(self.display_surf, colors.blue, self.player1_tr_last_pos, self.player1.rect.topright)		
		
		for wall in self.walls:
			self.line_in_rect = wall.rect.clipline(self.topright_line)

		if self.line_in_rect:
			self.player1.handle_wall_collisions(wall, self.player1_tr_last_pos)

		#test bottom left line with all walls
		self.player1_bl_last_pos = self.player1.rect.bottomleft - (self.player1.vel + 0.5 * self.player1.acc)
		self.bottomleft_line = pygame.draw.line(self.display_surf, colors.blue, self.player1_bl_last_pos, self.player1.rect.bottomleft)		
		
		for wall in self.walls:
			self.line_in_rect = wall.rect.clipline(self.bottomleft_line)

		if self.line_in_rect:
			self.player1.handle_wall_collisions(wall, self.player1_bl_last_pos)

		#test bottom right line with all walls
		self.player1_br_last_pos = self.player1.rect.bottomright - (self.player1.vel + 0.5 * self.player1.acc)
		self.bottomright_line = pygame.draw.line(self.display_surf, colors.blue, self.player1_br_last_pos, self.player1.rect.bottomright)		
		
		for wall in self.walls:
			self.line_in_rect = wall.rect.clipline(self.bottomright_line)

		if self.line_in_rect:
			self.player1.handle_wall_collisions(wall, self.player1_br_last_pos)
		'''

