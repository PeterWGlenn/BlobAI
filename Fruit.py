
# The Fruit class - holds the information for every Fruit
# @author Peter Glenn
# @version 7.13.2019

import random

# Store Fruits in lists
fruits = []

class Fruit(object):

    size = 10

    def __init__(self, sX, sY):
        self.xLoc = random.randint(int(self.size / 2), sX - int(self.size / 2))
        self.yLoc = random.randint(int(self.size / 2), sY - int(self.size / 2))
        fruits.append(self)



