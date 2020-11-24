from deepselect.resources import Resources
#from deepselect.res import Resources


class Element:
    def __init__(self, element_id, data, resources):
        self.element_id = element_id
        self.data = data
        self.resources = resources
        self.current_node = None
        self.category = None
        self.alive = True


    def update_category(self, categorizer):
        new_category = categorizer.get_category_of(self)
        self.category = new_category


    def die(self):
        # Mark the element as dead
        self.alive = False

        # Return all unused resources to the local environment
        self.current_node.resources = self.current_node.resources + self.resources
        self.resources = self.resources.zeroed()

        # Remove the reference to the element from the local environment
        self.unlist_from_current_node()


    def unlist_from_current_node(self):
        pass
