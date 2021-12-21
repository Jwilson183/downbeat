import colors
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, c):
		super().__init__()
		self.surf = pygame.Surface((30, 30))
		self.surf.fill((c))
		self.rect = self.surf.get_rect(center = (30, 400))
		
