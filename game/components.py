import numpy as np
from ecs import Component

class Location(Component):

    def __init__(self, position):
        self.position = position

class Movement(Component):

    def __init__(self, velocity):
        self.velocity = velocity
