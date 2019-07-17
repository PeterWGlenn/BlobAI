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
	newGene = combined + mutation(50, combined)
	return int(min(max(newGene, minimum), maximum))