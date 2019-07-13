

# BlobAI
# @author Peter Glenn
# @version 7.13.2019

# Game constants
FRAMERATE = 60
SCREEN_X = 600
SCREEN_Y = 400

# Random
import random

# Setting up pygame
import pygame
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BlobAI")
clock = pygame.time.Clock()
ICON_IMAGE = pygame.image.load("icon.png")

pygame.display.set_icon(ICON_IMAGE)

# Defining colors
BLACK = (0, 0, 0)

# Main Game Loop
running = True
while running:

	# Event Listeners
	for event in pygame.event.get():
		# Closed window
		if event.type == pygame.QUIT:
			running = False


	### Game logic ###

	# Draw Screen 
	screen.fill(BLACK)

	# Update display
	pygame.display.flip()

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()
