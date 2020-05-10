from deepselect.element import Element


class Object(Element):
    def __init__(self, object_id, data, resources):
        Element.__init__(self, object_id, data, resources)
