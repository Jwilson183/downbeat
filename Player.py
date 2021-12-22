import Character
import pygame, sys
from pygame.locals import *

class Player(Character.Character):
	def __init__(self, c):
		pygame.sprite.Sprite.__init__(self)