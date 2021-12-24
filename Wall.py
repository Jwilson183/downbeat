import colors
import pygame
#make a input of color
#make a setting of if hazard true
#wall movement?
class Wall(pygame.sprite.Sprite):
	def __init__(self, cx, cy, w, h):
		super().__init__()
		self.surf = pygame.Surface((w, h))
		self.surf.fill((colors.red))
		self.rect = self.surf.get_rect(center = (cx, cy))

