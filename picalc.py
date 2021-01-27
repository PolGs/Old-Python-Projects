from __future__ import division
import pygame, random
from pygame.locals import *
import time
import math

pygame.init()

#Set up display
DISPLAY = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pi calculator PolGs")
DISPLAY.fill((255,255,255))

#summon random points
x = random.randint(0,100)
y = random.randint(0,100)

#Variables
total = 0
inside = 0
x1=0
y1=0
d = 0

#pygame.draw.circle(DISPLAY, (0,255,255), (0,0), 10)

while True:
	x = random.randint[0,500]
	y = random.randint[0,500]	
	total = total + 1
	x1 = 250 - x
	y1 = 250 - y
	d = math.sqrt(x1*x1+y1*y1)
	print "x:" + str(x) + "  y:" + str(y) + "  d:" + str(d) 
	if (d <= 250):
		pygame.draw.circle(DISPLAY, (255,0,0), (x, y), 2, )
		inside = inside + 1	
	else:
		pygame.draw.circle(DISPLAY, (0,255,0), (x, y), 2, )
	pygame.display.update()
	
	print("inside:" + str(inside))
	print("total:" + str(total))
	pi = (inside / total)
	pi = pi*4
	print ("pi:" + str(pi))
