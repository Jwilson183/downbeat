from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_r, K_e
from pygame.math import Vector2 as vec
from Character import Character
import pygame
import os

class Player(Character):
	def __init__(
		self,
		color: tuple[int],
		max_acceleration: float,
		fric: float,
		gravity: float,
		jump_speed: float,
		max_jump: int,
		width: int,
		height: int,
		initial_pos: tuple
	):
	
		super().__init__(
			color, 
			max_acceleration,
			fric,
			gravity,
			jump_speed,
			width,
			height,
			initial_pos
		)

		self.jump_count = 0
		self.max_jump = max_jump
		self.has_jump = False
		self.initial_pos = initial_pos
		

	def get_input(self):
		super().get_input() #inherits all of the checks in the get_input method in Character

		if Player.should_reset(): #if should_reset has a value, player is moved to its initial pos and its vel/acc are set to 0
			self.pos = vec(self.initial_pos)
			self.gravity = self.gravity_const
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)

	def should_invert(self):
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_e]:
			return True

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
		super().jump()
		self.jump_count += 1
	
	def should_reset():
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_r]