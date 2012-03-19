import pygame
#std lib
import os
import math
#own files
import brush
import parser

pygame.init()
height = 320
width = 320
window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
pygame.display.set_caption('Logo')
screen = pygame.display.get_surface()
screen.convert_alpha()
clock = pygame.time.Clock()

def main():
	turtle = brush.Turtle(pygame.image.load("turtle.png"), 200, 200)

	Parser = parser.Parser("logo.imp")
	Parser.Interpret(turtle)

	while True:
		linelist = [[160,160]]
		for i in range(0, len(turtle.proclist)):
			if turtle.proclist[i].endpoint != None:
				linelist.append(turtle.proclist[i].endpoint)

		for i in range(0, len(linelist)): 
			if i == 0:
				pass
			else:
				#print "DRAWING FROM %s to %s" % (linelist[i-1], linelist[i])
				pygame.draw.line(screen, (0,0,0), linelist[i-1], linelist[i], turtle.ink)

		screen.blit(turtle.image, (turtle.x, turtle.y))

		pygame.display.flip()
		screen.fill((255,255,255))
		clock.tick(10)
main()