import pygame

class Collisions():
	def __init__(
		self,
		sprite_class,
		sprite_group,
		delete_bool: bool,
		):

		#Attributes
		self.sprite_or_class = sprite_class
		self.sprite_group = sprite_group
		self.delete_bool = delete_bool
		self.hits = 0

	def detect_collisions(self):
		self.hits = pygame.sprite.spritecollide(self.sprite_or_class, self.sprite_group, self.delete_bool)
		return self.hits


		