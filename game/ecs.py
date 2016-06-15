
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

    def bind_manager(self, manager):
        self.manager = manager
        
    def update(self, deltaTime):
        begin()

        for entity_id in self.entity_ids:
            entity = self.manager.get_entity_by_id()
            process(entity, deltaTime)
            
        end()

    # Overridden in the base class to specify functionality of system
    def process(self, entity, deltaTime):
        pass

    # Can be overridden if you want to do something before the first entity is processed
    def begin():
        pass

    # Can be overridden if you want to do something after the last entity is processed
    def end():
        pass

    def update_entity_registration(self, entity):
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

class Manager:

    def __init__(self):
        self.entities = {}
        self.current_id = 0

        self.systems = []
        
    def create_entity(self):
        entity = Entity(self.current_id)
        self.current_id += 1

        self.entities[entity.id] = entity
        return entity

    # Use this to add components, not the entity method!! Wish there was a way to enforce that in python
    def add_component_to_entity(self, entity, component):
        entity.add_component(component)
        self.update_entity_registration(entity)
    
    def add_system(self, system):
        self.systems.append(system)

    def update(self, deltaTime):
        for system in self.systems:
            system.update(deltaTime)

    def update_entity_registration(self, entity):
        for system in self.systems:
            system.update_entity_registration(entity)
