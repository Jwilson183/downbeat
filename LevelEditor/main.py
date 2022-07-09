import pygame, sys
from pygame.locals import *
from Editor import Editor

def main():

	pygame.init()

	fps = 120

	frame_per_sec = pygame.time.Clock()	

	editor = Editor(400, 450, "test3.json")

	# Beginning Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				if input("Would you like to save? y/n\n").lower().strip() == "y":
					editor.save_level()
				pygame.quit()
				sys.exit()
	
		editor.update()

		#Editor Update
		pygame.display.update()

		#Next frame
		frame_per_sec.tick(fps)
		
if __name__ == "__main__":
	main()