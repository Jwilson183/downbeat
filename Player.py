from pygame.constants import K_LEFT, K_RIGHT
from Character import Character
import pygame

class Player(Character):
	def __init__(self, color: tuple[int], max_acceleration: float, fric: float, gravity: float):
		super().__init__(color, max_acceleration, fric, gravity)

	def should_move_left(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_LEFT]

	def should_move_right(self):
		pressed_keys = pygame.key.get_pressed()
		return pressed_keys[K_RIGHT]