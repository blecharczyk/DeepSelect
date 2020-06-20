from deepselect.element import Element


class Agent(Element):
    def __init__(self, agent_id, data, resources, behavior):
        Element.__init__(self, agent_id, data, resources)
        self.behavior = behavior
