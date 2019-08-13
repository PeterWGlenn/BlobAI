

# BlobAI
# @author Peter Glenn
# @version 7.13.2019

# Imports
import pygame
import random
import Graph
from Fruit import Fruit
from Fruit import fruits
from Blob import Blob
from Blob import blobs
from Controls import controls
from Util import greyscale
from Util import addToColor
from Util import percentDarker
from Util import getDistance

# Game constants
FRAMERATE = 60
SCREEN_X = 1333
SCREEN_Y = 750
SCALE = 1.0

# Game states
pause = False
stats = False
showBlobAI = False

# Save selected blob
selectedBlob = None

# Setting up pygame
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BlobAI")
clock = pygame.time.Clock()
ICON_IMAGE = pygame.image.load("icon.png")
BACKGROUND_IMAGE = pygame.image.load("background.png")
GAME_FONT = pygame.font.Font('Quesha.ttf', 30)

pygame.display.set_icon(ICON_IMAGE)

# Spawn initial Blobs
Blob.screenX = SCREEN_X
Blob.screenY = SCREEN_Y
for i in range(0, 50):
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

			# Toggle showBlobAI
			if controlWord == "showBlobAI" and not pause and not stats:
				showBlobAI = not showBlobAI

			# Toggle Stats Screen
			if controlWord == "stats":
				stats = not stats

		# Mouse click
		if event.type == pygame.MOUSEBUTTONDOWN and not stats:
			mLoc = pygame.mouse.get_pos()

			clickedBlob = False
			for blob in blobs:
				if getDistance(blob.location(), mLoc) <= blob.radius():
					selectedBlob = blob
					clickedBlob = True

			if not clickedBlob:
				selectedBlob = None

		# Closed window
		if event.type == pygame.QUIT:
			running = False


	### Game logic ###

	# Update Blobs and stats if game unpaused
	if not pause:
		for blob in blobs:
			blob.update(loops)

	# Draw game when not in stats screen
	if not stats:

		# Drawn Screen Background
		screen.fill((0,0,0))

		# Draw Blob AI Information
		if showBlobAI:
			for blob in blobs:
				# Show Target Radius
				pygame.draw.circle(screen, (20, 20, 20), (int(blob.xLoc), int(blob.yLoc)), blob.radius() + blob.vision)
			for blob in blobs:
				# Show Target Lines
				pygame.draw.line(screen, percentDarker(blob.color, 50), (blob.xLoc, blob.yLoc), blob.target, int(1 * SCALE))
	
		# Draw Fruits
		for fruit in fruits:
	
			fruitColor = (0, 255, 0)
	
			# Draw fruits in greyscale if paused
			if pause:
				fruitColor = greyscale(fruitColor)
	
			pygame.draw.circle(screen, percentDarker(fruitColor, 20), [fruit.xLoc, fruit.yLoc], int(fruit.size / 2 * SCALE))
			pygame.draw.circle(screen, fruitColor, [fruit.xLoc, fruit.yLoc], int(fruit.size / 2 * SCALE) - 2)

		# Draw Blobs
		for blob in blobs:
	
			blobColor = blob.color
	
			# Draw blobs in greyscale if paused
			if pause:
				blobColor = greyscale(blobColor)

			pygame.draw.circle(screen, percentDarker(blobColor, 20), (int(blob.xLoc), int(blob.yLoc)), int((blob.size / 2) * SCALE))
			pygame.draw.circle(screen, blobColor, (int(blob.xLoc), int(blob.yLoc)), (int((blob.size / 2) * SCALE)) - int(blob.radius() * 0.25))

		# Draw selected blob stats
		if selectedBlob != None and selectedBlob.isAlive:

			visionStr = "Vision: " + str(selectedBlob.vision)
			matingSizeStr = "Mating Size: " + str(selectedBlob.matingSize)
			sizeStr = "Size: " + str(round(selectedBlob.size, 2))
			childrenStr = "Children: " + str(selectedBlob.children)

			fontVisionS = GAME_FONT.size(visionStr)
			fontMatingSizeS = GAME_FONT.size(matingSizeStr)
			fontSizeS = GAME_FONT.size(sizeStr)
			fontChildrenS = GAME_FONT.size(childrenStr)

			fontX = selectedBlob.xLoc - max(fontVisionS[0], fontMatingSizeS[0], fontSizeS[0], fontChildrenS[0]) / 2
			fontY = selectedBlob.yLoc - 4 - selectedBlob.radius() - fontVisionS[1] - fontMatingSizeS[1] - fontSizeS[1] - fontChildrenS[1]

			pygame.draw.rect(screen, (50,50,50), [fontX - 4, fontY - 2, max(fontMatingSizeS[0], fontVisionS[0], fontSizeS[0], fontChildrenS[0]) + 4, fontVisionS[1] + fontMatingSizeS[1] + fontSizeS[1] + fontChildrenS[1]])

			textSurfaceVision = GAME_FONT.render(visionStr, False, addToColor(selectedBlob.color, 100, 100, 100))
			textSurfaceMatingSize = GAME_FONT.render(matingSizeStr, False, addToColor(selectedBlob.color, 100, 100, 100))
			textSurfaceSize = GAME_FONT.render(sizeStr, False, addToColor(selectedBlob.color, 100, 100, 100))
			textSurfaceChildren = GAME_FONT.render(childrenStr, False, addToColor(selectedBlob.color, 100, 100, 100))

			screen.blit(textSurfaceVision, (fontX, fontY))
			screen.blit(textSurfaceMatingSize, (fontX, fontY + fontMatingSizeS[1]))
			screen.blit(textSurfaceSize, (fontX, fontY + fontMatingSizeS[1] + fontSizeS[1]))
			screen.blit(textSurfaceChildren, (fontX, fontY + fontMatingSizeS[1] + fontSizeS[1] + fontChildrenS[1]))

	# If stat screen is toggled, render stats screen
	else:
		if loops % 4 == 0:	

			# Drawn Screen Background
			screen.fill((0,0,0))

			# Drawn Graph Background
			fromLeft = 80
			fromRight = 80
			fromTop = 80
			fromBottom = 240
			pygame.draw.rect(screen, (40,40,40), [fromLeft, fromTop, SCREEN_X - fromLeft - fromRight, SCREEN_Y - fromBottom - fromTop], 0)

			Graph.plotLine(Graph.visionData, (0, 255, 0), screen, SCREEN_X, SCREEN_Y, SCALE)
			Graph.plotLine(Graph.matingSizeData, (255, 0, 0), screen, SCREEN_X, SCREEN_Y, SCALE)
			Graph.plotLine(Graph.reachedTargetDistanceData, (0, 0, 255), screen, SCREEN_X, SCREEN_Y, SCALE)
			Graph.plotLine(Graph.babySizeData, (0, 255, 255), screen, SCREEN_X, SCREEN_Y, SCALE)
			Graph.plotLine(Graph.numberOfBlobsData, (255,255,255), screen, SCREEN_X, SCREEN_Y, SCALE)


	# Update display
	pygame.display.flip()

	# Count loops
	loops += 1

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()
