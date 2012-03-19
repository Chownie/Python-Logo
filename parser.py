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
		for i in range(0, len(self.tokens)):
			getattr(self, self.tokens[i][1])(i, turtle)

	def INT(self, pos, turtle):
		pass

	def ID(self, pos, turtle):
		pass
	
	def RESERVED(self, pos, turtle):
		#-----------MOVES FORWARD IN FACING DIRECTION----------------------
		if self.tokens[pos][0] == "FORWARD" or self.tokens[pos][0] == "FD":
			length = self.tokens[pos+1][0]
			pi = math.pi
			radians = float(pi) * float(turtle.angle) / 180
			DX = math.cos(float(radians))*float(length)+160
			DY = math.sin(float(radians))*float(length)+160
			print "TOKEN: %s %s" % (self.tokens[pos][0], self.tokens[pos+1][0])
			print "DX: %s\nDY: %s\nAngle: %s\nRad: %s" % (DX, DY, turtle.angle, radians)
			turtle.proclist.append(brush.Procedure(None, [int(DX), int(DY)]))
			turtle.x = int(DX)
			turtle.y = int(DY)


		#-----------CHANGES FACING DIRECTION CLOCKWISE---------------------
		elif self.tokens[pos][0] == "RIGHT" or self.tokens[pos][0] == "RT":
			angle = self.tokens[pos+1][0]
			turtle.angle = turtle.angle+float(angle)

		#-----------CHANGES FACING DIRECTION ANTI-CLOCKWISE---------------
		elif self.tokens[pos][0] == "LEFT" or self.tokens[pos][0] == "LT":
			angle = self.tokens[pos+1][0]
			turtle.angle = turtle.angle-float(angle)
			print "ANGLE: %s" % turtle.angle
	def BOOLEAN(self, pos, turtle):
		if self.tokens[pos][0] == "PENUP":
			turtle.proclist.append(brush.Procedure(0, None))
		elif self.tokens[pos][0] == "PENDOWN":
			turtle.proclist.append(brush.Procedure(1, None))

	def COMMENT(self, pos, turtle):
		print self.tokens[pos][0]