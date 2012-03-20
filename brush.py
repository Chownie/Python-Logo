import os
import math
import pygame

class Turtle():
	def __init__(self, display, image, x, y):
		self.angle = 270
		self.ink = 1
		self.color = (0,0,0)
		self.image = image
		self.x = x
		self.y = y
		self.display = display
		self.temp = pygame.display.get_surface()
		self.temp.convert_alpha()
		self.temp.fill((255,255,255))
	
	def forward(self, amount):
		prevpos = self.x, self.y
		radians = float(math.pi) * float(self.angle) / 180
		dx = math.cos(float(radians))*float(amount)
		dy = math.sin(float(radians))*float(amount)

		self.x += int(dx)
		self.y += int(dy)
		pygame.draw.line(self.temp, self.color, prevpos, (self.x, self.y), self.ink)
		self.paint()

	def turnright(self, amount):
		self.angle += float(amount)
		self.paint()

	def turnleft(self, amount):
		self.angle -= float(amount)
		self.paint()

	def penup(self):
		self.ink = 0
		self.paint()

	def pendown(self):
		self.ink = 1
		self.paint()

	def paint(self):
		self.display.blit(self.temp, (0,0))
		self.display.blit(self.image, (self.x-8, self.y-8))
		pygame.display.flip()

class Procedure():
	def __init__(self, ink=None, endpoint=None):
		self.endpoint = endpoint
		self.ink = ink