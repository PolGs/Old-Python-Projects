import pygame, sys
from pygame.locals import *

pygame.init()

#Set up display
DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Radar")

#Set up colors
white = (255,255,255)
purple = (153,0,153)
yellow = (204,204,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#White Background
DISPLAY.fill(white)

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	
	pygame.draw.rectangle
	
	
	
	pygame.display.update()