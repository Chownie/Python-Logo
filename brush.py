import os
import math

class Turtle():
	def __init__(self, image=None, x=None, y=None):
		self.proclist = []
		self.angle = 270
		self.ink = 1
		self.image = image
		self.x = x
		self.y = y
	
	def forward(self, amount):
			radians = float(math.pi) * float(self.angle) / 180
			dx = math.cos(float(radians))*float(amount)
			dy = math.sin(float(radians))*float(amount)

			self.x += int(dx)
			self.y += int(dy)

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