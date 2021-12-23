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
		self.gravity = gravity
		
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
		self.collision()

		#Movement
		if self.vel.x != 0:
			self.acc.x += self.vel.x/abs(self.vel.x) * self.fric
		self.vel += self.acc
		self.pos += self.vel +0.5 * self.acc 	

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

	def should_jump(self):
		pass

	def render(self):
		self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))
		
	def collision(self):
		hits = pygame.sprite.spritecollide(self, sprites.obsticales, False)	
		if hits:
			self.pos.y = hits[0].rect.top - 15 
			self.vel.y = 0