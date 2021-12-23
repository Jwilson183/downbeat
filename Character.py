import pygame
#from pygame.locals import *
from pygame.math import Vector2 as vec
import gamerules

class Character(pygame.sprite.Sprite):
	def __init__(self, color: tuple[int], max_acceleration: float):
		super().__init__()

		#Velocity
		self.pos = vec((10, 400))
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		self.max_acceleration = max_acceleration

		#Drawing Initial Position
		self.surf = pygame.Surface((30, 30))
		self.surf.fill((color))

	def update(self):
		self.get_input()
		self.render()
		print(self.pos.x)

		#Movement
		if self.vel.x != 0:
			self.acc.x += self.vel.x/abs(self.vel.x) * gamerules.fric
		self.vel += self.acc
		self.pos += self.vel +0.5 * self.acc 	

	def get_input(self):
		self.acc = vec(0,0)

		#Inputs to movement
		if self.should_move_left():
			self.acc.x = -self.max_acceleration
		if self.should_move_right():
			self.acc.x = self.max_acceleration

	def should_move_left(self):
		pass
	def should_move_right(self):
		pass
	
	def render(self):
		self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))