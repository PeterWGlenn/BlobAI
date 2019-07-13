

# BlobAI
# @author Peter Glenn
# @version 7.13.2019

# Imports
import pygame
import random
from Blob import Blob

# Game constants
FRAMERATE = 60
SCREEN_X = 1333
SCREEN_Y = 750
SCALE = 1.0

# Setting up pygame
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BlobAI")
clock = pygame.time.Clock()
ICON_IMAGE = pygame.image.load("icon.png")

pygame.display.set_icon(ICON_IMAGE)

# Defining colors
BLACK = (0, 0, 0)

# Main blobs list
blobs = []

# Spawn initial Blobs
for i in range(0, 10):
	size = random.randint(10, 50)
	blob = Blob(random.randint(int(size / 2), SCREEN_X - int(size / 2)), random.randint(int(size / 2), SCREEN_Y - int(size / 2)), size)
	blobs.append(blob)

# Main Game Loop
running = True
while running:

	# Event Listeners
	for event in pygame.event.get():
		# Closed window
		if event.type == pygame.QUIT:
			running = False


	### Game logic ###

	# Update Blobs
	for blob in blobs:
		blob.update()

	# Draw Screen 
	screen.fill(BLACK)

	# Draw Blobs
	for blob in blobs:
		pygame.draw.circle(screen, blob.color, [blob.xLoc, blob.yLoc], int((blob.size / 2) * SCALE))

	# Draw Watermelons

	# Update display
	pygame.display.flip()

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()
