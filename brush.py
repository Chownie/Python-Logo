import os
import math
import pygame

class Turtle():
	def __init__(self, screen, image, x, y):
		self.angle = 270
		self.ink = 1
		self.color = (0,0,0)
		self.image = image
		self.x = x
		self.y = y
		self.screen = screen
	
	def forward(self, amount):
		prevpos = self.x, self.y
		radians = float(math.pi) * float(self.angle) / 180
		dx = math.cos(float(radians))*float(amount)
		dy = math.sin(float(radians))*float(amount)

		self.x += int(dx)
		self.y += int(dy)
		pygame.draw.line(self.screen, self.color, prevpos, (self.x, self.y), self.ink)

	def turnright(self, amount):
		self.angle += float(amount)

	def turnleft(self, amount):
		self.angle -= float(amount)

	def penup(self):
		self.ink = 0

	def pendown(self):
		self.ink = 1

class Procedure():
	def __init__(self, ink=None, endpoint=None):
		self.endpoint = endpoint
		self.ink = ink