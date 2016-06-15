import unittest
from unittest.mock import MagicMock
from ecs import Component, Entity, System, Manager

class EntityTest(unittest.TestCase):

    def setUp(self):
        self.entity = Entity(0)
    
    def test_add_component(self):
        self.entity.add_component(Component())
        self.assertIn(Component, self.entity.components)

        with self.assertRaises(Exception):
            self.entity.add_component(Component())

    def test_has_component(self):
        self.entity.add_component(Component())
        self.assertTrue(self.entity.has_component(Component))

    def test_get_component(self):
        component = Component()
        self.entity.add_component(component)
        returned = self.entity.get_component(Component)
        self.assertEqual(component, returned)

class SystemTest(unittest.TestCase):

    def test_matches(self):
        system = System(MockComponentA, MockComponentB)

        entity = Entity(0)
        self.assertFalse(system.matches(entity))

        entity.add_component(MockComponentA())
        self.assertFalse(system.matches(entity))

        entity.add_component(MockComponentB())
        self.assertTrue(system.matches(entity))

    def test_update_entity_registration(self):
        system = System(MockComponentA, MockComponentB)
        entity = Entity(0)
        # Entity is not registered in the system, but it does match
        entity.has_component = MagicMock(return_value=True)
        system.update_entity_registration(entity)
        self.assertIn(0, system.entity_ids)

        entity.has_component.return_value = False
        system.update_entity_registration(entity)
        self.assertNotIn(0, system.entity_ids)

class ManagerTest(unittest.TestCase):

    def test_create_entity(self):
        manager = Manager()
        entity = manager.create_entity()
        self.assertEqual(entity.id, 0)

    def test_add_component_to_entity(self):
        manager = Manager()
        entity = manager.create_entity()
        manager.add_component_to_entity(entity, Component())
        self.assertTrue(entity.has_component(Component))

    def test_update(self):
        manager = Manager()

        system = System()
        system.update = MagicMock()
        
        manager.add_system(system)
        manager.update(10)

        system.update.assert_called_with(10)

    def test_update_entity_registration(self):
        manager = Manager()
        system = System(MockComponentA)
        manager.add_system(system)
        
        system.update_entity_registration = MagicMock()
        
        entity = manager.create_entity()
        manager.add_component_to_entity(entity, MockComponentA())

        system.update_entity_registration.assert_called_with(entity)
        
        
class MockComponentA(Component):
    pass

class MockComponentB(Component):
    pass

unittest.main()
