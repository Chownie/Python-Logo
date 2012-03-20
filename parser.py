from imp_lexer import *
import brush
import math

class Parser():
	def __init__(self, filename=None):
		file = open(filename)
		characters = file.read()
		file.close()
		self.tokens = imp_lex(characters)

	def Interpret(self, turtle):
		turtle.proclist.append(brush.Procedure(None, [turtle.x, turtle.y]))
		for i in range(0, len(self.tokens)):
			getattr(self, self.tokens[i][1])(i, turtle)

	def INT(self, pos, turtle):
		pass

	def ID(self, pos, turtle):
		pass
	
	def RESERVED(self, pos, turtle):
		#Moving forward
		if self.tokens[pos][0] == "FORWARD" or self.tokens[pos][0] == "FD":
			length = self.tokens[pos+1][0]
			radians = float(math.pi) * float(turtle.angle) / 180
			dx = math.cos(float(radians))*float(length)
			dy = math.sin(float(radians))*float(length)

			turtle.x += int(dx)
			turtle.y += int(dy)
			turtle.proclist.append(brush.Procedure(None, [turtle.x, turtle.y]))

		#Angles clockwise
		elif self.tokens[pos][0] == "RIGHT" or self.tokens[pos][0] == "RT":
			angle = self.tokens[pos+1][0]
			turtle.angle = turtle.angle+float(angle)

		#Angles counterclockwise
		elif self.tokens[pos][0] == "LEFT" or self.tokens[pos][0] == "LT":
			angle = self.tokens[pos+1][0]
			turtle.angle = turtle.angle-float(angle)

	def BOOLEAN(self, pos, turtle):
		if self.tokens[pos][0] == "PENUP":
			turtle.proclist.append(brush.Procedure(0, None))
		elif self.tokens[pos][0] == "PENDOWN":
			turtle.proclist.append(brush.Procedure(1, None))

	def COMMENT(self, pos, turtle):
		print self.tokens[pos][0]