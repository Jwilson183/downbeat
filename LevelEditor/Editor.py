import json
import pygame
from pygame.locals import *
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN
from pygame.math import Vector2 as vec
import colors
from Wall import Wall

class Editor:
	def __init__(
		self,
		display_width: int,
		display_height: int,
		level_file_name: str,
	):


		#Display
		self.display_width = display_width
		self.display_height = display_height

		#Establish Pan Variables
		self.x_pan_offset = 0
		self.y_pan_offset = 0

		#File Name
		self.level_file_name = level_file_name

		#Make Display
		self.display_surf = pygame.display.set_mode((self.display_width, self.display_height))
		pygame.display.set_caption("DownBeat Level Editor")

		#Sprites
		self.all_sprites = pygame.sprite.Group()
		self.walls       = pygame.sprite.Group()

	def update(self):
		self.get_input()
		self.render()
		self.make_walls()
		
	def get_input(self):
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_RIGHT]:
			self.x_pan_offset += self.display_width/30
		if pressed_keys[K_LEFT]:
			self.x_pan_offset -= self.display_width/30
		if pressed_keys[K_UP]:
			self.y_pan_offset -= self.display_height/30
		if pressed_keys[K_DOWN]:
			self.y_pan_offset += self.display_height/30

	def render(self):
		self.display_surf.fill((colors.white))
		for entity in self.all_sprites:
			self.display_surf.blit(entity.surf, (entity.rect.left - self.x_pan_offset, entity.rect.top - self.y_pan_offset))

	def make_walls(self):
		if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
			cursor_pos = pygame.mouse.get_pos()
			self.walls.add(Wall(cursor_pos[0] + self.x_pan_offset, cursor_pos[1] + self.y_pan_offset, 30, 30))
			self.all_sprites.add(self.walls)
	
	def save_level(self):
		level_dict = {}
		save_sprite_group(self.walls, "Walls", level_dict)

		with open(self.level_file_name, "w") as outfile:
			json.dump(level_dict, outfile)

def get_dict_from_rect(rect):
	return {
		"cx": rect.centerx,
		"cy": rect.centery,
		"w": rect.width,
		"h": rect.height
	}

def save_sprite_group(group, level_dict_key, destination_dictionary):
	sprites = []
	for sprite in group:
		sprites.append(get_dict_from_rect(sprite.rect))
		print(sprites)
		destination_dictionary[level_dict_key] = sprites