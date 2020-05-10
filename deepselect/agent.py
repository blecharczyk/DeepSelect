from deepselect.element import Element


class Agent(Element):
    def __init__(self, agent_id, data, resources, agent_type):
        Element.__init__(self, agent_id, data, resources)
        self.agent_type = agent_type
