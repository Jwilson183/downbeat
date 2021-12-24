from pygame.constants import K_LEFT, K_RIGHT, K_UP
from Character import Character
import pygame

class Player(Character):
	def __init__(self, color: tuple[int], max_acceleration: float, fric: float, gravity: float, jump_speed: float, max_jump: int):
		super().__init__(color, max_acceleration, fric, gravity, jump_speed, max_jump)

	def should_move_left(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_LEFT]

	def should_move_right(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_RIGHT]
	
	def should_jump(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_UP]

	def should_move_up(self):
		return False

	def should_move_down(self):
		return False
		
	def jump(self):
		if self.is_on_ground:
			self.has_jump = True
			self.jump_count = 0
			self.current_jump = 0
		if self.jump_count == self.max_jump:
			self.has_jump = False
		if self.has_jump:
			self.pos.y -= self.jump_speed 
			self.vel.y = -self.jump_speed
			self.jump_count += 1
		if self.current_jump < self.vel.y:
			self.current_jump = self.vel.y
		if self.current_jump > self.vel.y:
			#self.has_jump = False
			print ("test")