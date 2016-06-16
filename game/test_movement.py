import unittest
import numpy as np
from ecs import System, Manager
from systems import MovementSystem
from components import Location, Movement

class TestMovement(unittest.TestCase):

    def test_move(self):

        manager = Manager()
        manager.add_system(MovementSystem())

        location = Location(np.array([5, 5]))
        
        entity = manager.create_entity()        
        manager.add_component_to_entity(entity, location)
        manager.add_component_to_entity(entity, Movement(np.array([1, 1])))

        manager.update(1)

        print(location.position)
        self.assertTrue(np.array_equal(location.position, np.array([6, 6])))

unittest.main()
