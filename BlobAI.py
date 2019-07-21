

# BlobAI
# @author Peter Glenn
# @version 7.13.2019

# Imports
import pygame
import random
from Fruit import Fruit
from Fruit import fruits
from Blob import Blob
from Blob import blobs
from Controls import controls
from Util import greyscale
from Util import addToColor

# Game constants
FRAMERATE = 60
SCREEN_X = 1333
SCREEN_Y = 750
SCALE = 1.0

# Game states
pause = False
stats = False

# Setting up pygame
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BlobAI")
clock = pygame.time.Clock()
ICON_IMAGE = pygame.image.load("icon.png")
BACKGROUND_IMAGE = pygame.image.load("background.png")

pygame.display.set_icon(ICON_IMAGE)

# Spawn initial Blobs
Blob.screenX = SCREEN_X
Blob.screenY = SCREEN_Y
for i in range(0, 20):
	Blob.makeInitialBlob()

# Spawn initial Fruits
for i in range(0, 20):
	fruit = Fruit(SCREEN_X, SCREEN_Y)

# Main Game Loop
loops = 0
running = True
while running:

	# Event Listeners
	for event in pygame.event.get():

		# Controls
		if event.type == pygame.KEYDOWN:
			controlWord = controls(pygame.key.get_pressed())

			# Pause
			if controlWord == "pause":
				pause = not pause

		# Closed window
		if event.type == pygame.QUIT:
			running = False


	### Game logic ###

	# Update Blobs if game unpaused
	if not pause:
		for blob in blobs:
			blob.update(loops)

	# Drawn Screen Background
	screen.fill((0,0,0))

	# Draw Blobs
	for blob in blobs:
		# Show Target Radius
		pygame.draw.circle(screen, (5,5,5), (int(blob.xLoc), int(blob.yLoc)), blob.radius() + blob.vision)
	for blob in blobs:
		# Show Target Lines
		pygame.draw.line(screen, (15,15,15), (blob.xLoc, blob.yLoc), blob.target, int(1 * SCALE))
	for blob in blobs:

		blobColor = blob.color

		# Draw blobs in greyscale if paused
		if pause:
			blobColor = greyscale(blobColor)

		pygame.draw.circle(screen, addToColor(blobColor, -20), (int(blob.xLoc), int(blob.yLoc)), int((blob.size / 2) * SCALE))
		pygame.draw.circle(screen, blobColor, (int(blob.xLoc), int(blob.yLoc)), (int((blob.size / 2) * SCALE)) - int(blob.radius() * 0.25))

	# Draw Fruits
	for fruit in fruits:

		fruitColor = (0, 255, 0)

		# Draw fruits in greyscale if paused
		if pause:
			fruitColor = greyscale(fruitColor)

		pygame.draw.circle(screen, addToColor(fruitColor, -20), [fruit.xLoc, fruit.yLoc], int(fruit.size / 2 * SCALE))
		pygame.draw.circle(screen, fruitColor, [fruit.xLoc, fruit.yLoc], int(fruit.size / 2 * SCALE) - 2)

	# Update display
	pygame.display.flip()

	# Count loops
	loops += 1

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()
