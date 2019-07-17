
# The Blob class - holds the information for every Blob
# @author Peter Glenn
# @version 7.13.2019

import math
import random
import Fruit
from Fruit import fruits
from Util import getDistance
from Util import combineGenes

screenX = 1333
screenY = 750

# Store Blobs in list
blobs = []

class Blob(object):

    xVel = 0
    yVel = 0
    speed = 1

    color = (125, 125, 125)
    reachedTargetDistance = 5
    vision = 100
    matingSize = 30

    state = 'w' # w = wandering, f = food targeting, m = mating

    def __init__(self, x, y, s):
        self.xLoc = x
        self.yLoc = y
        self.size = s
        self.target = (x, y)
        blobs.append(self)

    def radius(self):
    	return int(self.size / 2)

    def location(self):
    	return (self.xLoc, self.yLoc)

    def update(self):  

    	# Search for mate
    	foundMate = False
    	if self.size >= self.matingSize:
    		for blob in blobs:
    			if self != blob and getDistance(self.location(), blob.location()) <= self.vision + self.radius() and blob.size >= blob.matingSize:
    				# If first mate, set target
    				if not foundMate:
    					self.setTarget(blob.xLoc, blob.yLoc)
    				# Found mate within sight
    				foundMate = True
    				state = 'm'
    				# If found mate, set target to closest mate
    				if foundMate and getDistance(self.location(), self.target) > getDistance(self.location(), blob.location()):
    					self.setTarget(blob.xLoc, blob.yLoc)
    				# If in contact, and other blob is willing, mate
    				if self.size >= self.matingSize and blob.size >= blob.matingSize and getDistance(self.location(), blob.location()) < self.radius() + blob.radius():
    					self.makeBaby(blob)
    					self.size = int((2 * self.size) / 3)
    					blob.size = int((2 * blob.size) / 3)


    	# Search for food
    	foundFood = False 
    	if not foundMate:
    		for fruit in fruits:
    			if getDistance((self.xLoc, self.yLoc), (fruit.xLoc, fruit.yLoc)) <= self.vision + self.radius():
    				# If first food, set target
    				if not foundFood:
    					self.setTarget(fruit.xLoc, fruit.yLoc)
    				# Found food within sight
    				foundFood = True
    				state = 'f'
    				# If found food, set target to closest food
    				if foundFood and getDistance(self.location(), self.target) > getDistance(self.location(), (fruit.xLoc, fruit.yLoc)):
    					self.setTarget(fruit.xLoc, fruit.yLoc)

    	# If no food is found, wander

    	# If target location is reached, set new target location
    	if not foundFood and not foundMate and getDistance((self.xLoc, self.yLoc), self.target) <= self.reachedTargetDistance + self.radius():

    		state = 'w'

    		# Pick random coordinate within visible range
    		randomRadian = 2 * math.pi * random.random()
    		randomRadius = (self.vision + self.radius()) * random.random()
    		x, y = randomRadius * math.cos(randomRadian) + self.xLoc, randomRadius * math.sin(randomRadian) + self.yLoc

 			# Set target to that coordinate
    		self.setTarget(min(max(x, self.radius()), screenX - self.radius()), min(max(y, self.radius()), screenY - self.radius()))

    	# Set Velocity Toward Target Location
    	if self.target[0] != -1:
    		if self.target[0] > self.xLoc + math.sqrt(self.reachedTargetDistance):
    			self.xVel = self.speed
    		elif self.target[0] + math.sqrt(self.reachedTargetDistance) < self.xLoc:
    			self.xVel = -self.speed
    		else:
    			self.xVel = 0
    	else:
    		self.xVel = 0
    	if self.target[1] != -1:
    		if self.target[1] > self.yLoc + math.sqrt(self.reachedTargetDistance):
    			self.yVel = self.speed
    		elif self.target[1] + math.sqrt(self.reachedTargetDistance) < self.yLoc:
    			self.yVel = -self.speed
    		else:
    			self.yVel = 0
    	else:
    		self.yVel = 0

    	# Move
    	if self.xLoc + self.xVel > self.size / 2 and self.xLoc + self.xVel < screenX - self.size / 2:
    		self.xLoc += self.xVel
    	else:
    		xVel = 0
    	if self.yLoc + self.yVel > self.size / 2 and self.yLoc + self.yVel < screenY - self.size / 2:
    		self.yLoc += self.yVel
    	else:
    		yVel = 0

    	# Eat nearby fruits
    	for f in Fruit.fruits:
    		if self.eatClosebyFruits(f.xLoc, f.yLoc, f.size):
    			fruits.remove(f)
    			fruit = Fruit.Fruit(screenX, screenY)

    def setTarget(self, x, y):
    	self.target = (x, y)

    def hasTarget(self):
    	if self.target == (-1, -1):
    		return False
    	else:
    		return True

    def clearTarget(self):
    	self.setTarget(-1, -1)

    def eatClosebyFruits(self, fX, fY, fS):
    	if getDistance((self.xLoc, self.yLoc), (fX, fY)) < abs(self.size / 2 + fS / 2):
    		growthAmount = 10
    		newRadius = self.radius() + growthAmount/2
    		if newRadius + self.xLoc < screenX and newRadius + self.yLoc < screenY and self.xLoc - newRadius > 0 and self.yLoc - newRadius > 0:
    			self.size += growthAmount
    		return True
    	else:
    		return False

    def makeInitialBlob():
    	size = 20
    	blob = Blob(random.randint(int(size / 2), screenX - int(size / 2)), random.randint(int(size / 2), screenY - int(size / 2)), size)

    def makeBaby(self, mate):
    	baby = Blob(self.xLoc, self.yLoc, int((self.size + mate.size) / 3))

    	baby.color =  (combineGenes(0, 255, self.color[0], mate.color[0]), combineGenes(0, 255, self.color[1], mate.color[1]), combineGenes(0, 255, self.color[2], mate.color[2]))
    	reachedTargetDistance = combineGenes(0, 100, self.reachedTargetDistance, mate.reachedTargetDistance)
    	vision = combineGenes(1, 750, self.vision, mate.vision)
    	matingSize = combineGenes(10, 500, self.matingSize, mate.matingSize)

    	print("Blobs: ", len(blobs))




