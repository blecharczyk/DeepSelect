from deepselect.element import Element

class Object(Element):
    def __init__(self, object_id, data, resources):
        Element.__init__(self, object_id, data, resources)


    def unlist_from_current_node(self):
        if self.current_node is not None:
            self.current_node.remove_object(self)
            self.current_node = None


    def __str__(self):
        return "Object_id: " + str(self.element_id) + "; data: " + str(self.data) + "; resources: " + \
               str(self.resources) + "."
