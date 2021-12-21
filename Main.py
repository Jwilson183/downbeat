import pygame, sys
from pygame.locals import *
import colors 
# Initialize program
pygame.init()
 
# FPS
fps = 60
frame_per_sec = pygame.time.Clock()

# Setting up Variables
height = 450
width = 400
acc = 0.5
fric = -0.12
 
#Vector Math

# Setup display with caption
display_surf = pygame.display.set_mode((300,300))
display_surf.fill(white)
pygame.display.set_caption("DownBeat")



# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    frame_per_sec.tick(fps)