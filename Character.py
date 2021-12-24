import pygame
#from pygame.locals import *
from pygame.math import Vector2 as vec
import sprites

class Character(pygame.sprite.Sprite):
	def __init__(self, color: tuple[int], max_acceleration: float, fric: float, gravity: float):
		super().__init__()

		#Velocity
		self.pos = vec(10, 0)
		self.vel = vec(0,0)
		self.acc = vec(0, 0)
		
		#Physics
		self.fric = fric
		self.gravity = gravity
		self.max_acceleration = max_acceleration

		#Drawing Initial Position
		self.surf = pygame.Surface((30, 30))
		self.surf.fill((color))

	def update(self):
		self.get_input()
		self.move()
		self.handle_collisions()
		self.render()

	def get_input(self):
		self.acc = vec(0,self.gravity)

		#Inputs to movement
		if self.should_move_left():
			self.acc.x = -self.max_acceleration
		if self.should_move_right():
			self.acc.x = self.max_acceleration
		if self.should_move_up():
			self.acc.y = -self.max_acceleration
		if self.should_move_down():
			self.acc.y = self.max_acceleration
			
		if self.should_jump():
			self.jump()
	
	def should_move_left(self):
		pass
	def should_move_right(self):
		pass
	def should_move_up(self):
		pass
	def should_move_down(self):
		pass

	def should_jump(self):
		pass
	
	#def jump(self):
		#self.vel.y = -15

	def move(self):
		if self.vel.x != 0:
			self.acc.x += self.vel.x/abs(self.vel.x) * self.fric
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc 	

	def handle_collisions(self):
		hits = pygame.sprite.spritecollide(self, sprites.platforms, False)
		if hits:
			self.pos.y = hits[0].rect.top + 1
			self.vel.y = 0
	
	def render(self):
		self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))
		self.rect.midbottom = self.pos