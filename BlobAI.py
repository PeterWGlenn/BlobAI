

# BlobAI
# @author Peter Glenn
# @version 7.13.2019

# Imports
import pygame
import random
from Blob import Blob
from Fruit import Fruit

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

# Store Blobs and Fruits in lists
blobs = []
fruits = []

# Spawn initial Blobs
for i in range(0, 10):
	size = random.randint(20, 70)
	blob = Blob(random.randint(int(size / 2), SCREEN_X - int(size / 2)), random.randint(int(size / 2), SCREEN_Y - int(size / 2)), size)
	blobs.append(blob)

# Spawn initial Fruits
for i in range(0, 10):
	size = 30
	fruit = Fruit(random.randint(int(size / 2), SCREEN_X - int(size / 2)), random.randint(int(size / 2), SCREEN_Y - int(size / 2)), size)
	fruits.append(fruit)

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
		pygame.draw.circle(screen, (abs(blob.color[0] - 100), abs(blob.color[1] - 100), abs(blob.color[2] - 100)), [blob.xLoc, blob.yLoc], int((blob.size / 2) * SCALE))
		pygame.draw.circle(screen, blob.color, [blob.xLoc, blob.yLoc], (int((blob.size / 2) * SCALE)) - 5)

	# Draw Fruits
	for fruit in fruits:
		pygame.draw.circle(screen, (0, 255, 0), [fruit.xLoc, fruit.yLoc], int(fruit.size / 2 * SCALE))

	# Update display
	pygame.display.flip()

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()
