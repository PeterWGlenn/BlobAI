
# The Fruit class - holds the information for every Fruit
# @author Peter Glenn
# @version 7.13.2019

import random
from Util import getDistance

# Store Fruits in lists
fruits = []

class Fruit(object):

    size = 10

    def __init__(self, sX, sY):
        self.xLoc = random.randint(int(self.size / 2), sX - int(self.size / 2))
        self.yLoc = random.randint(int(self.size / 2), sY - int(self.size / 2))
        fruits.append(self)

    def location(self):
    	return (self.xLoc, self.yLoc)

    def radius(self):
    	return self.size / 2

    def move(self, sX, sY, blobs):
    	newLocation = self.getEmptyLocation(sX, sY, blobs)
    	self.xLoc = newLocation[0]
    	self.yLoc = newLocation[1]

    def getEmptyLocation(self, sX, sY, blobs):
    	return self.getEmptyLocationHelper(sX, sY, blobs, 0)

    def getEmptyLocationHelper(self, sX, sY, blobs, timeOut):

    	newLocation = (random.randint(int(self.size / 2), sX - int(self.size / 2)), random.randint(int(self.size / 2), sY - int(self.size / 2)))

    	# Timeout detector
    	if timeOut > 100:
    		return newLocation
    	else:

    		for blob in blobs:
    			if getDistance(newLocation, blob.location()) <= blob.radius():
    				return self.getEmptyLocationHelper(sX, sY, blobs, timeOut + 1)

    		return newLocation


