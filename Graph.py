
# The Graph class - manages the graph that is displayed on the stats screen
# @author Peter Glenn
# @version 8.1.2019

import pygame

# Graph data points
numberOfBlobsData = []
visionData = []
matingSizeData = []
reachedTargetDistanceData = []
babySizeData = []

def convertDataPointToGraphYValue(dataPoint, dataSet, screenY):

	maxMinusMin = max(dataSet) - min(dataSet)

	if maxMinusMin > 0:
		valMinusMin = dataPoint - min(dataSet)
		screenPercent = valMinusMin / maxMinusMin

		screenYBuffer = 50

		return ((screenY - screenYBuffer) * (1 - screenPercent)) + screenYBuffer / 2
	else:
		return screenY / 2

def plotLine(dataSet, color, screen, screenX, screenY, scale):
	if len(dataSet) > 1:

		graphExpansionX = (screenX - 50) / len(dataSet)

		for d in range(0, len(dataSet) - 1):
			pygame.draw.line(screen, color, 
				(d * graphExpansionX, convertDataPointToGraphYValue(dataSet[d], dataSet, screenY)), 
				((d + 1) * graphExpansionX, convertDataPointToGraphYValue(dataSet[d + 1], dataSet, screenY)), int(1 * scale))

