import pygame, sys
from pygame.locals import *
from pymouse import PyMouse
import time
m = PyMouse()
pygame.init()

x = 0
y = 0
colorchange = 1
r = 5
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
#draw
DISPLAY.fill(white)



while True:
	colorchange = colorchange + 1
	r = r +1
	x = m.position()
	if colorchange >= 1:
		color = purple
	if colorchange >= 11:
		color = red
	if colorchange >= 21:
		color = yellow
	if colorchange >= 31:
		color = green
	if colorchange >= 41:
		color = blue
		colorchange = 0
	if r > 20:
		r = 5
	print (colorchange)
	pygame.draw.circle(DISPLAY, color, x, r, 0)
	pygame.display.update()
	
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()