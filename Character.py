import pygame
#from pygame.locals import *
from pygame.math import Vector2 as vec

class Character(pygame.sprite.Sprite):
	def __init__(
		self,
		color: tuple[int],
		max_acceleration: float,
		fric: float,
		gravity: float,
		jump_speed: float,
		width: int,
		height: int,
		initial_pos: tuple,
	):
		super().__init__()

		#Velocity
		self.pos = vec(initial_pos)
		self.vel = vec(0,0)
		self.acc = vec(0, 0)

		#Physics
		self.fric = fric
		self.gravity_const = gravity
		self.gravity_inverted = 1
		self.gravity = gravity
		
		#Movement speed
		self.max_acceleration = max_acceleration
		self.jump_speed = jump_speed
		self.is_on_ground = False

		#Drawing Initial Position
		self.surf = pygame.Surface((width, height))
		self.surf.fill((color))
		self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))

	def update(self):
		self.get_input()
		self.move()
		self.render()

	def move(self):
		if self.vel.x != 0:
			self.acc.x += self.vel.x/abs(self.vel.x) * self.fric
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc 	
		self.is_on_ground = False

	def invert_gravity(self):
		self.gravity *= -1
		self.gravity_inverted *= -1

	def get_input(self):
		self.acc = vec(0, self.gravity)

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

		if self.should_invert():
			self.invert_gravity()

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

	def should_invert(self):
		pass

	def jump(self):
		self.pos.y -= (self.jump_speed * self.gravity_inverted)
		self.vel.y = -1 * (self.jump_speed * self.gravity_inverted)

	def render(self):
		self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))
		self.rect.midbottom = self.pos

	def handle_wall_collisions(self, wall):
		"""Uses the position of the Character relative to the object that Character is colliding with to 
		decern which side Character is colliding with so that character can be moved in the proper direction"""

		#Order of checked needs self.bottom, self.left, self.right, and then self.top. Collisions with
		#the bottom of Character need to happen first and collisions with the 
		#top of Character need to happen last to ensure that the correct side is detected.
		
		if self.gravity > 0: # When gravity is pulling down
			#Bottom of Character
			if self.rect.centery <= wall.rect.top:
				self.pos.y = wall.rect.top + 1
				self.vel.y = 0
				self.is_on_ground = True

			#Top of Character
			elif self.rect.top + self.rect.height/2 >= wall.rect.bottom:
				self.pos.y = wall.rect.bottom + self.rect.height * 1.25
				self.vel.y = 0

			#Left of Character
			elif self.rect.left + self.rect.width/2 <= wall.rect.left:
				self.pos.x = wall.rect.left - self.rect.width/2
				self.vel.x = 0

			#Right of Character
			elif self.rect.right - self.rect.width/2 >= wall.rect.right:
				self.pos.x = wall.rect.right + self.rect.width/2
				self.vel.x = 0

		if self.gravity < 0: #if gravity is inverted
			#Top of Character
			if self.rect.top <= wall.rect.bottom and self.rect.bottom > wall.rect.bottom:
				self.pos.y = wall.rect.bottom + (self.rect.height - 1)
				self.vel.y = 0
				self.is_on_ground = True

			#Bottom of Character
			elif self.rect.centery - self.rect.height/2 >= wall.rect.top:
				self.pos.y = wall.rect.bottom - self.rect.height * 1.25
				self.vel.y = 0

			#Left of Character
			elif self.rect.left + self.rect.width/2 <= wall.rect.left:
				self.pos.x = wall.rect.left - self.rect.width/2
				self.vel.x = 0

			#Right of Character
			elif self.rect.right - self.rect.width/2 >= wall.rect.right:
				self.pos.x = wall.rect.right + self.rect.width/2
				self.vel.x = 0
