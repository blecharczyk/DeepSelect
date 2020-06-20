class Element:
    def __init__(self, element_id, data, resources):
        self.element_id = element_id
        self.data = data
        self.resources = resources
        self.current_node = None
        self.category = None
