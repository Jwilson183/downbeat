import pygame
from pygame import display
import colors
from pygame.sprite import spritecollide
from Character import Character
from Scene import Scene
from pygame.math import Vector2 as vec

class ScrollScene(Scene):

	def __init__(self, width, height, level_file, focus_size: float):
		super().__init__(width, height, level_file)

		self.offset = vec(0, 0)
		self.focus_size = focus_size

		self.focus_rect = pygame.sprite.Sprite()
		self.focus_rect.rect = pygame.Rect(
			self.display_width * (1 - focus_size)/2,  #left
			self.display_height * (1 - focus_size)/2, #top
			self.display_width * focus_size,          #width
			self.display_height * focus_size          #height
		)
		self.focus_rect_group = pygame.sprite.Group()
		self.focus_rect_group.add(self.focus_rect)

		#This is temporary and has to be set externally after ScrollScene is called. AHHHHHH
		self.focus = self.focus_rect
		
	def find_offset(self):
		in_rect = pygame.sprite.spritecollide(self.focus, self.focus_rect_group, False)
		if in_rect:
			return

		#Top of focus_rect
		elif self.focus.rect.bottom <= self.focus_rect.rect.top:
			self.offset.y += self.focus.rect.bottom - self.focus_rect.rect.top
	
		#Right of focus_rect
		if self.focus.rect.left >= self.focus_rect.rect.right:
			self.offset.x += self.focus.rect.left - self.focus_rect.rect.right

		#Left of focus_rect
		if self.focus.rect.right <= self.focus_rect.rect.left:
			self.offset.x += self.focus.rect.right - self.focus_rect.rect.left
		#Bottom of focus_rect
		if self.focus.rect.top >= self.focus_rect.rect.bottom:
			self.offset.y += self.focus.rect.top - self.focus_rect.rect.bottom

	def update_focus_rect(self):
		self.focus_rect.rect.topleft = (
			self.display_width * (1 - self.focus_size)/2 + self.offset.x,
			self.display_height * (1 - self.focus_size)/2 + self.offset.y
		)

	def render(self):
		self.find_offset()
		self.update_focus_rect()
		
		
		self.display_surf.fill((colors.white))

		for entity in self.all_sprites:
			#create a surf and rect by adding the screen location to the entity surf and rect, then blit the new surf and rect to the screen
			self.display_surf.blit(entity.surf, (entity.rect.left - self.offset.x, entity.rect.top - self.offset.y))

# find the difference between focus pos and focus_rect
# blit sprites using a for loop with their pos's offset by offset
# keep a running tally on offset
# ACTUAL camera pos must be changed by self.render
