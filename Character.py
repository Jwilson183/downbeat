from typing import AsyncContextManager
import pygame
import gamerules

class Player(pygame.sprite.Sprite):
	def __init__(self, c):
		#Drawing Character
		super().__init__()
		self.surf = pygame.Surface((30, 30))
		self.surf.fill((c))
		self.rect = self.surf.get_rect(center = (30, 400))

		#Velocity
		self.pos = gamerules.vec((10, 385))
		self.vel = gamerules.vec(0,0)
		self.acc = gamerules.vec(0,0)

		#Movement
		self.acc.x += self.vel.x * gamerules.fric
		self.vel += self.acc
		self.pos += self.vel +0.5 * self.acc 	

	def move(self):
		self.acc = vec(0,0)
		#Inputs to movement
		if input_left == True:
			self.acc.x = -acc
		if input_right == True:
			self.acc.x = acc

