import colors
import pygame
#make a input of color
#make a setting of if hazard true
#wall movement?
class Wall(pygame.sprite.Sprite):
	def __init__(self, cx, cy, w, h):
		super().__init__()
		self.color = colors.red
		self.surf = pygame.Surface((w, h))
		self.surf.fill((self.color))
		self.rect = self.surf.get_rect(center = (cx, cy))
	
	def update_surface(self, cx, cy, w, h, color=None):
		color = color or self.color
		self.surf = pygame.Surface((abs(w), abs(h)))
		self.rect = self.surf.get_rect(center = (cx, cy))
		self.surf.fill((color))

	def handle_player1_collisions(self, player):
		pass