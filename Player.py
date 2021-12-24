from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from Character import Character
import pygame

class Player(Character):
	def __init__(
		self,
		color: tuple[int],
		max_acceleration: float,
		fric: float,
		gravity: float,
		jump_speed: float,
		max_jump: int
	):
	
		super().__init__(color, max_acceleration, fric, gravity, jump_speed)

		self.jump_count = 0
		self.max_jump = max_jump

	def should_move_left(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_LEFT]

	def should_move_right(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_RIGHT]
	
	def should_jump(self):
		pressed_keys = pygame.key.get_pressed()

		#if not pressing up don't jump and can't jump mid jump if let go
		if not pressed_keys[K_UP]:
			self.has_jump = False
			return False

		#if pressing up and on ground, jump. Gives has_jump
		if self.is_on_ground:
			self.jump_count = 0
			self.has_jump = True
			return True

		#if reached max_jumps, stop jumping
		if self.jump_count == self.max_jump:
			return False

		#if still holding up jump
		if self.has_jump:
			return True

	def should_move_up(self):
		return False

	def should_move_down(self):
		return False
		
	def jump(self):
		if self.should_jump:
			self.pos.y -= self.jump_speed 
			self.vel.y = -self.jump_speed
			self.jump_count += 1