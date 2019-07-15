
# The Blob class - holds the information for every Blob
# @author Peter Glenn
# @version 7.13.2019

import math
import random

screenX = 1333
screenY = 750

def getDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class Blob(object):

    color = (0, 255, 255)
    xVel = 0
    yVel = 0
    speed = 3
    target = (-1, -1)
    reachedTargetDistance = 10
    vision = 100

    state = 0 # 0 = wandering, 1 = food targeting

    def __init__(self, x, y, s):
        self.xLoc = x
        self.yLoc = y
        self.size = s

    def radius(self):
    	return int(self.size / 2)

    def update(self):  

    	# If target location is reached, set new target location
    	if getDistance((self.xLoc, self.yLoc), self.target) <= self.reachedTargetDistance + self.radius():
    		if self.state == 0:
    			# Wandering

    			# Pick random coordinate within visible range
    			randomRadian = 2 * math.pi * random.random()
    			randomRadius = (self.vision + self.radius()) * random.random()
    			x, y = randomRadius * math.cos(randomRadian) + self.xLoc, randomRadius * math.sin(randomRadian) + self.yLoc

 				# Set target to that coordinate
    			self.setTarget(min(max(x, self.radius()), screenX - self.radius()), min(max(y, self.radius()), screenY - self.radius()))
    		else:
    			# No valid state, do nothing
    			self.setTarget(-1, -1)

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


