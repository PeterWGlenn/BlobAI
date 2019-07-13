
# The Blob class - holds the information for every Blob
# @author Peter Glenn
# @version 7.13.2019

screenX = 1333
screenY = 750

class Blob(object):

    color = (0, 255, 255)
    xVel = 0
    yVel = 0
    target = (-1, -1)

    def __init__(self, x, y, s):
        self.xLoc = x
        self.yLoc = y
        self.size = s

    def update(self):

    	# Set Velocity Toward Target Location
    	if self.target[0] != -1:
    		if self.target[0] > self.xLoc:
    			self.xVel = 1
    		elif self.target[0] < self.xLoc:
    			self.xVel = -1
    		else:
    			self.xVel = 0
    	if self.target[1] != -1:
    		if self.target[1] > self.yLoc:
    			self.yVel = 1
    		elif self.target[1] < self.yLoc:
    			self.yVel = -1
    		else:
    			self.yVel = 0

    	# Move
    	if self.xLoc + self.xVel > self.size / 2 and self.xLoc + self.xVel < screenX - self.size / 2:
    		self.xLoc += self.xVel
    	if self.yLoc + self.yVel > self.size / 2 and self.yLoc + self.yVel < screenY - self.size / 2:
    		self.yLoc += self.yVel

    def setTarget(self, x, y):
    	self.target = (x, y)


