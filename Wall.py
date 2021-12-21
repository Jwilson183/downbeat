from pygame.constants import WINDOWHITTEST
import colors
import pygame

class Wall(pygame.sprite.Sprite):
	def __init__(self, w, h):
		super(Sprite, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface((30, 30))
		self.suf = pygame.Surface((w, 20))
		self.surf.fill((colors.white))
		self.rect = self.surf.get_rect(center = (w, h))

