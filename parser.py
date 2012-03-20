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
		if self.tokens[pos][0] == "FORWARD" or self.tokens[pos][0] == "FD":
			length = self.tokens[pos+1][0]
			turtle.forward(length)
		elif self.tokens[pos][0] == "RIGHT" or self.tokens[pos][0] == "RT":
			turtle.turnright(self.tokens[pos+1][0])
		elif self.tokens[pos][0] == "LEFT" or self.tokens[pos][0] == "LT":
			turtle.turnleft(self.tokens[pos+1][0])

	def BOOLEAN(self, pos, turtle):
		if self.tokens[pos][0] == "PENUP":
			turtle.penup()
		elif self.tokens[pos][0] == "PENDOWN":
			turtle.pendown()

	def COMMENT(self, pos, turtle):
		print self.tokens[pos][0]