import pygame, sys
from pygame.locals import *
import time
from math import cos, radians, sin
pygame.init()

#Set up display
DISPLAY = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Drawing")

#Set up colors
white = (255,255,255)
purple = (153,0,153)
yellow = (204,204,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color = white

#Background
DISPLAY.fill(white)

#Variables
circlecenterx = 960
circlecentery = 540
circleradius = 40

dx = 0
dy = 0
drawerradius = 10
drawerpos = (dx, dy)

angle = 0

while True:
	angle = angle + 1
	xvar = circleradius * cos(angle)
	yvar = circleradius * sin(angle)
	
	dx = circlecenterx + xvar
	dy = circlecentery + yvar
	drawerpos = (dx, dy)

	
	
	
	
	
	pygame.draw.circle(DISPLAY, blue, (dcirclecenterx + xvar, circlecentery + yvar), drawerradius, 0)
	print(xvar)
	pygame.display.update()
	
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()