
# The Button class - manages button functionality on the screen
# @author Peter Glenn
# @version 9.5.2019

import pygame
import Util

# Store Buttons in a list
buttons = []

class Button(object):

	width = 100
	height = 50
	pressed = False

	def __init__(self, n, c, x, y):
	    self.xLoc = x
	    self.yLoc = y
	    self.name = n
	    self.color = c
	    buttons.append(self)

	def draw(self, screen, screenX, screenY, scale, font):

		# Draw button name
		nameFont = font.render(self.name, False, self.color)
		screen.blit(nameFont, (self.xLoc + (self.width / 2) - (font.size(str(self.name))[0] / 2), self.yLoc + self.height))

		# Change color if pressed
		drawColor = self.color
		if self.pressed:
			drawColor = Util.percentDarker(drawColor, 50)

		buttonRect = pygame.Rect(self.xLoc, self.yLoc, self.width, self.height)
		pygame.draw.rect(screen, drawColor, buttonRect)

	def press(self):
		self.pressed = not self.pressed


