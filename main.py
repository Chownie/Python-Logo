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
	turtle = brush.Turtle(pygame.image.load("turtle.png"), 160, 160)

	Parser = parser.Parser("logo.imp")
	Parser.Interpret(turtle)

	while True:
		for i in range(0, len(turtle.proclist)):
			if turtle.proclist[i].endpoint != None:
				for l in range(i, 0, -1):
					if turtle.proclist[l].endpoint != None:
						if l == 0:
							pass
						else:
							pygame.draw.line(screen, (0,0,0), turtle.proclist[l].endpoint,
							turtle.proclist[i].endpoint, turtle.ink)
							break

			elif turtle.proclist[i].ink != None:
				turtle.ink = turtle.proclist[i].ink

		screen.blit(turtle.image, (turtle.x, turtle.y))

		pygame.display.flip()
		screen.fill((255,255,255))
		clock.tick(10)
main()