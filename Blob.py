
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
    reachedTargetDistance = 4
    vision = 50

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
    			self.setTarget(random.randint(self.radius(), screenX - self.radius()), random.randint(self.radius(), screenY - self.radius()))
    		else:
    			# No valid state, do nothing
    			self.setTarget(-1, -1)

    	# Set Velocity Toward Target Location
    	if self.target[0] != -self.speed:
    		if self.target[0] > self.xLoc + math.sqrt(self.reachedTargetDistance):
    			self.xVel = self.speed
    		elif self.target[0] + math.sqrt(self.reachedTargetDistance) < self.xLoc:
    			self.xVel = -self.speed
    		else:
    			self.xVel = 0
    	else:
    		self.xVel = 0
    	if self.target[1] != -self.speed:
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
    	if self.yLoc + self.yVel > self.size / 2 and self.yLoc + self.yVel < screenY - self.size / 2:
    		self.yLoc += self.yVel

    def setTarget(self, x, y):
    	self.target = (x, y)

    def eatClosebyFruits(self, fX, fY, fS):
    	if getDistance((self.xLoc, self.yLoc), (fX, fY)) < abs(self.size / 2 + fS / 2):
    		if self.size < 500:
    			self.size += 10
    		return True
    	else:
    		return False


