# The Util class - holds utility methods
# @author Peter Glenn
# @version 7.16.2019

import math

def getDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)