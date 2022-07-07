import pygame, sys
from pygame.locals import *
from Player import Player
from Scene import Scene
from ScrollScene import ScrollScene

def main():
	pygame.init()

	fps = 60

	frame_per_sec = pygame.time.Clock()	

	scene = ScrollScene(400, 450, "Custom Levels/test3.json", 0.5)
	scene.focus = scene.player1

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