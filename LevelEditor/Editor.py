import json
import pygame
from pygame.locals import *
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN
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
		
		#Making Sprites
		self.clicked_last_frame = False
		self.clicked_last_last_frame = False
		self.first_point = None
		self.second_point = None
		self.sprite_cx = None
		self.sprite_cy = None
		self.sprite_width = 0
		self.sprite_height = 0
		self.temporary_sprite_top = 0
		self.temporary_sprite_left = 0
		self.temporary_sprite = None

		#Sprites
		self.all_sprites = pygame.sprite.Group()
		self.walls       = pygame.sprite.Group()
		
		
	def update(self):
		self.get_input()
		self.render()
	
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

		clicking = pygame.mouse.get_pressed(num_buttons=3)[0] == True
		if clicking:
			self.make_walls()
		else:
			if self.clicked_last_last_frame == True and self.clicked_last_frame == True:
				self.temporary_sprite = None
	
		self.clicked_last_last_frame = self.clicked_last_frame
		self.clicked_last_frame = clicking

	def render(self):
		self.display_surf.fill((colors.white))
		for entity in self.all_sprites:
			self.display_surf.blit(entity.surf, (entity.rect.left - self.x_pan_offset, entity.rect.top - self.y_pan_offset))
	
	def make_walls(self):
		cursor_pos = pygame.mouse.get_pos()
		if self.clicked_last_frame == False:
			self.first_point = (cursor_pos[0] + self.x_pan_offset, cursor_pos[1] + self.y_pan_offset)

		elif self.clicked_last_frame == True:
			self.second_point = (cursor_pos[0] + self.x_pan_offset, cursor_pos[1] + self.y_pan_offset)
			
			#Determining top left coordinates for update
			if self.first_point[0] <= self.second_point[0]:
				self.temporary_sprite_left = self.first_point[0]
			else:
				self.temporary_sprite_left = self.second_point[0]
			if self.first_point[1] <= self.second_point[1]:
				self.temporary_sprite_top = self.first_point[1]
			else:
				self.temporary_sprite_top = self.second_point[1]

			self.sprite_width = self.first_point[0] - self.second_point[0]
			self.sprite_height = self.first_point[1] - self.second_point[1]
			self.sprite_cx = self.first_point[0] - self.sprite_width/2
			self.sprite_cy = self.first_point[1] - self.sprite_height/2

			if self.temporary_sprite == None:


				self.temporary_sprite = Wall(self.sprite_cx, self.sprite_cy, abs(self.sprite_width), abs(self.sprite_height))
				self.walls.add(self.temporary_sprite)
				self.all_sprites.add(self.walls)
				print(self.all_sprites)
			else:
				self.temporary_sprite.update_surface(self.sprite_cx, self.sprite_cy, self.sprite_width, self.sprite_height)
				print("updating")
				print(f"Width{self.sprite_width=} {self.sprite_height=}")
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