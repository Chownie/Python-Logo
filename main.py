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
	turtle = brush.Turtle(screen, pygame.image.load("turtle.png"), 160, 160)

	Parser = parser.Parser("logo.imp")
	Parser.Interpret(turtle)

	while True:
		turtle.paint()
		clock.tick(10)
main()