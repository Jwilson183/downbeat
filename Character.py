from sys import platform
import pygame
#from pygame.locals import *
from pygame.math import Vector2 as vec
import sprites
#Character class needs to take starting position
#Character class is a moving sprite that takes (color, max_acceleration, fric)
class Character(pygame.sprite.Sprite):
	def __init__(self, color: tuple[int], max_acceleration: float, fric: float, gravity: float):
		super().__init__()

		#Variables
		self.max_acceleration = max_acceleration
		self.fric = fric
		self.gravity_constant = gravity
		self.gravity = self.gravity_constant

		#Velocity
		self.pos = vec((10, 200))
		self.vel = vec(0, 0)
		self.acc = vec(0, self.gravity)

		#Drawing Initial Position
		self.surf = pygame.Surface((30, 30))
		self.surf.fill((color))

	def update(self):
		self.get_input()
		self.render()
		#self.platform_collision()
		
		#Movement
		if self.vel.x != 0:
			before = self.acc.x
			self.acc.x += self.vel.x/abs(self.vel.x) * self.fric
			after = self.acc.x
			if (before > 0) != (after > 0):
				self.vel.x = 0
				self.acc.x = 0
		self.rect.midbottom = self.pos
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc 	
		#print(f"{self.acc=}, {self.vel=}, {self.pos=}")
		
		#Gravity
		self.acc = vec(self.acc.x, self.gravity)
	def get_input(self):
		
		#Inputs to movement
		if self.should_move_left():
			self.acc.x = -self.max_acceleration
		if self.should_move_right():
			self.acc.x = self.max_acceleration

	def should_move_left(self):
		pass

	def should_move_right(self):
		pass

	def should_move_up(self):
		pass

	def render(self):
		self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))
		
	def platform_collision(self):
		hits = pygame.sprite.spritecollide(self, sprites.platforms, False)	
		if hits:
			print("hits")
			self.gravity = 0
			self.vel.y = 0
			print(self.acc)
		else:
			self.gravity = self.gravity_constant
			print("not hits")