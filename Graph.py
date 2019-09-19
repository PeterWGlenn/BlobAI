
# The Graph class - manages the graph that is displayed on the stats screen
# @author Peter Glenn
# @version 8.1.2019

import pygame
from enum import Enum

# Graph data points
numberOfBlobsData = []
visionData = []
matingSizeData = []
reachedTargetDistanceData = []
babySizeData = []
speedData = []

def convertDataPointToGraphYValue(dataPoint, dataSet, screenY):

	maxMinusMin = max(dataSet) - min(dataSet)

	if maxMinusMin > 0:
		valMinusMin = dataPoint - min(dataSet)
		screenPercent = valMinusMin / maxMinusMin

		screenYBuffer = 8

		return ((screenY - screenYBuffer) * (1 - screenPercent)) + screenYBuffer / 2
	else:
		return screenY / 2

def plotLine(dataSet, color, screen, screenX, screenY, scale):

	if len(dataSet) > 1:

		fromLeft = 80
		fromRight = 80
		fromTop = 80
		fromBottom = 240

		graphExpansionX = (screenX - fromRight - fromLeft) / (len(dataSet) - 1)

		for d in range(0, len(dataSet) - 1):
			pygame.draw.line(screen, color, 
				(d * graphExpansionX + fromLeft, convertDataPointToGraphYValue(dataSet[d], dataSet, screenY - fromBottom - fromTop) + fromTop), 
				((d + 1) * graphExpansionX + fromLeft, convertDataPointToGraphYValue(dataSet[d + 1], dataSet, screenY - fromBottom - fromTop) + fromTop), int(1 * scale))

