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
	temp = pygame.display.get_surface()
	temp.convert_alpha()
	temp.fill((255,255,255))
	turtle = brush.Turtle(temp, pygame.image.load("turtle.png"), 160, 160)

	Parser = parser.Parser("logo.imp")
	Parser.Interpret(turtle)

	while True:
		screen.blit(turtle.image, (turtle.x, turtle.y))

		pygame.display.flip()
		screen.blit(temp, (turtle.x, turtle.y))
		clock.tick(10)
main()