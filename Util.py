# The Util class - holds utility methods
# @author Peter Glenn
# @version 7.16.2019

import math
import random

def getDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def mutation(number, percent):
	p = percent / 100
	amount = int(p*number)
	return random.randint(-amount, amount)

def combineGenes(minimum, maximum, gene1, gene2):
	combined = ((gene1 + gene2) / 2)
	newGene = combined + mutation(20, combined)
	return int(min(max(newGene, minimum), maximum))

def randomGene(minimum, maximum):
	return random.randint(minimum, maximum)

def greyscale(color):
	averageValue = (color[0] + color[1] + color[2]) / 3
	return (averageValue, averageValue, averageValue)

def addToColor(color, number):
	newColor = (abs(color[0] + number), abs(color[1] + number), abs(color[2] + number)) 
	return newColor

def percentDarker(color, percent):
	percent = 1 - (percent / 100)
	newColor = (int(color[0] * percent), int(color[1] * percent), int(color[2] * percent)) 

	return newColor