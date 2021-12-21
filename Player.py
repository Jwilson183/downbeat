from pygame.constants import GL_GREEN_SIZE
import colors

Class Player(pygame.sprite.Sprite)
	def __init__(self):
		super().__init__()
		self.surf = pygame.Surface((30, 30))
		self.surf.fill((colors.green))
		self.rect = self.surf.get_rect(center = (10, 420))
		
#wall
#hazard