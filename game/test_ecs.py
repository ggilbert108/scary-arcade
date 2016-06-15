import unittest
from ecs import Component, Entity

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

unittest.main()
