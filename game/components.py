import numpy as np
from ecs import Component

class Location(Component):

    # position - a numpy array (2 vector)
    def __init__(self, position):
        self.position = position

class Movement(Component):

    # velocity - a numpy array (2 vector)
    def __init__(self, velocity):
        self.velocity = velocity
