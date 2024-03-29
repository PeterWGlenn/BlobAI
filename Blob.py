
# The Blob class - holds the information for every Blob
# @author Peter Glenn
# @version 7.13.2019

import math
import random
import Fruit
import Graph
from Fruit import fruits
from Util import getDistance
from Util import combineGenes
from Util import randomGene

screenX = 1333
screenY = 750

# Store Blobs in list
blobs = []

class Blob(object): 

    isAlive = True

    xVel = 0
    yVel = 0
    speed = 1.2 * 1 #coefficient is a test

    color = (125, 125, 125)
    reachedTargetDistance = 3
    vision = 150
    matingSize = 40
    babySizeLoss = 10

    children = 0

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

    def update(self, loops):  

    	# Think every few loops
    	n = random.randint(1, 5)
    	if loops % n == 0:
    		self.think()

    	# Move
    	velAdjustmentValue = 40 / (self.size + 20)
    	if self.xLoc + self.xVel > self.size / 2 and self.xLoc + self.xVel < screenX - self.size / 2:
    		self.xLoc += self.xVel * velAdjustmentValue
    		self.burnCalories(loops)
    	else:
    		xVel = 0
    	if self.yLoc + self.yVel > self.size / 2 and self.yLoc + self.yVel < screenY - self.size / 2:
    		self.yLoc += self.yVel * velAdjustmentValue
    		self.burnCalories(loops)
    	else:
    		yVel = 0

    def think(self):

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
    					self.children += 1
    					blob.children += 1
    					self.makeBaby(blob)
    					self.size = self.size - self.babySizeLoss
    					blob.size = blob.size - blob.babySizeLoss


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

    	# Eat nearby fruits
    	for fruit in Fruit.fruits:
    		if self.eatClosebyFruits(fruit.xLoc, fruit.yLoc, fruit.size):
    			fruit.move(screenX, screenY, blobs)

    def burnCalories(self, loops):
    	# Every 80 loops
    	if loops % 80 == 0:
    		# Die if too small
    		if self.size - self.speed <= 3:
    			self.die()
    		else:
    			self.size -= self.speed

    def die(self):

    	self.isAlive = False

    	if self in blobs:
    		blobs.remove(self)

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
    		growthAmount = 8
    		newRadius = self.radius() + growthAmount/2
    		if newRadius + self.xLoc < screenX and newRadius + self.yLoc < screenY and self.xLoc - newRadius > 0 and self.yLoc - newRadius > 0:
    			self.size += growthAmount
    		return True
    	else:
    		return False

    def makeInitialBlob():
    	size = 30
    	blob = Blob(random.randint(int(size / 2), screenX - int(size / 2)), random.randint(int(size / 2), screenY - int(size / 2)), size)

    	blob.color =  (randomGene(0, 255), randomGene(0, 255), randomGene(0, 255))
    	blob.reachedTargetDistance = randomGene(0, 50)
    	blob.vision = randomGene(50, 500)
    	blob.matingSize = randomGene(10, 100)
    	blob.speed = randomGene(1, 2)

    def makeBaby(self, mate):

    	baby = Blob(self.xLoc, self.yLoc, self.babySizeLoss + mate.babySizeLoss)

    	baby.color =  (combineGenes(0, 255, self.color[0], mate.color[0]), combineGenes(0, 255, self.color[1], mate.color[1]), combineGenes(0, 255, self.color[2], mate.color[2]))
    	baby.reachedTargetDistance = combineGenes(1, 100, self.reachedTargetDistance, mate.reachedTargetDistance)
    	baby.vision = combineGenes(1, 750, self.vision, mate.vision)
    	baby.matingSize = combineGenes(10, 500, self.matingSize, mate.matingSize)
    	baby.babySizeLoss = combineGenes(2, 100, self.babySizeLoss, mate.babySizeLoss)
    	baby.speed = combineGenes(0.1, 4, self.speed, mate.speed)

    	# Update stats
    	avColor = (0, 0, 0)
    	avReachedTargetDistance = 0
    	avVision = 0
    	avMatingSize = 0
    	avBabySizeLoss = 0
    	avSpeed = 0

    	for blob in blobs:
    		avColor = (avColor[0] + blob.color[0], avColor[1] + blob.color[1], avColor[2] + blob.color[2])
    		avReachedTargetDistance += blob.reachedTargetDistance
    		avVision += blob.vision
    		avMatingSize += blob.matingSize
    		avBabySizeLoss += blob.babySizeLoss
    		avSpeed += blob.speed

    	avColor = (round(avColor[0] / len(blobs), 2), round(avColor[1] / len(blobs), 2), round(avColor[2] / len(blobs)), 2)
    	avReachedTargetDistance = round(avReachedTargetDistance / len(blobs), 2)
    	avVision = round(avVision / len(blobs), 2)
    	avMatingSize = round(avMatingSize / len(blobs), 2)
    	avBabySizeLoss = round(avBabySizeLoss / len(blobs), 2)
    	avSpeed = round(avSpeed / len(blobs), 2)

    	# Add new data to graph
    	Graph.visionData.append(avVision)
    	Graph.matingSizeData.append(avMatingSize)
    	Graph.reachedTargetDistanceData.append(avReachedTargetDistance)
    	Graph.babySizeData.append(avBabySizeLoss)
    	Graph.numberOfBlobsData.append(len(blobs))
    	Graph.speedData.append(avSpeed)

    	# Remove old data points from graph
    	tooManyItems = 700
    	if len(Graph.visionData) > tooManyItems:

    		i = 0
    		for d in Graph.numberOfBlobsData:

    			if i % 10 == 0:

    				Graph.visionData.remove(Graph.visionData[i])
    				Graph.matingSizeData.remove(Graph.matingSizeData[i])
    				Graph.reachedTargetDistanceData.remove(Graph.reachedTargetDistanceData[i])
    				Graph.babySizeData.remove(Graph.babySizeData[i])
    				Graph.numberOfBlobsData.remove(Graph.numberOfBlobsData[i])
    				Graph.speedData.remove(Graph.speedData[i])

    			i += 1

