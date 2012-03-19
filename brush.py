import os

class Turtle():
	def __init__(self, image=None, x=None, y=None):
		self.proclist = []
		self.angle = 270
		self.ink = 1
		self.image = image
		self.x = x
		self.y = y

class Procedure():
	def __init__(self, ink=None, endpoint=None):
		self.endpoint = endpoint
		self.ink = ink