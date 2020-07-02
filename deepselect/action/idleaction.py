from deepselect.action.action import Action


class IdleAction(Action):
    def __init__(self, cost):
        Action.__init__(self, cost)
    
    def execute(self, agent):
        agent.resources = agent.resources - self.cost
