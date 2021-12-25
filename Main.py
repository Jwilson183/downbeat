#import pygame
import pygame, sys
from pygame.locals import *
from Scene import Scene

def main():
	pygame.init()

	fps = 60
	frame_per_sec = pygame.time.Clock()	

	scene = Scene(400, 450)

	# Beginning Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	
		scene.update()

		#Display Update
		pygame.display.update()

		#Next frame
		frame_per_sec.tick(fps)

if __name__ == "__main__":
	main()