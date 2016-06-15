
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

class System:

    def __init__(self, *required):
        self.required = required
        self.entity_ids = set()

    def update_entity(self, entity):
        contains = entity.id in self.entity_ids
        matches = self.matches(entity)

        # Already exists, but no longer matches
        if contains and not matches:
            self.entity_ids.remove(entity.id)
        # Doesn't exist, but does match
        elif not contains and matches:
            self.entity_ids.add(entity.id)
        
    def matches(self, entity):
        for required in self.required:
            if not entity.has_component(required):
                return False

        return True
