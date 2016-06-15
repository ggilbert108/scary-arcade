
class Component:
    pass

class Entity:

    def __init__(self, id):
        self.id = id
        self.components = {}

    def add_component(self, component):
        if type(component) in self.components:
            raise Exception("This entity already has a component of that type")

        # Since there is only one of each type of component, they are stored by type
        self.components[type(component)] = component

    def has_component(self, component_type):
        return component_type in self.components

    def get_component(self, component_type):
        return self.components[component_type]
