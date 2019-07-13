
# The Blob class - holds the information for every Blob
# @author Peter Glenn
# @version 7.13.2019

class Blob(object):

    color = (0, 255, 255)
    xVel = 0
    yVel = 0

    def __init__(self, x, y, s):
        self.xLoc = x
        self.yLoc = y
        self.size = s

    def update(self):

    	# Move
    	self.xLoc = self.xLoc + self.xVel
    	self.yLoc = self.yLoc + self.yVel

