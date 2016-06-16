import numpy as np
from ecs import System
from components import Location, Movement

class MovementSystem(System):

    def __init__(self):
        super().__init__(Location, Movement)

    def process(self, entity, deltaTime):
        location = entity.get_component(Location)
        movement = entity.get_component(Movement)
        
        velocity = np.multiply(movement.velocity, deltaTime)
        location.position = np.add(location.position, velocity)        
    
