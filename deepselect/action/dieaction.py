from deepselect.action.action import Action


class DieAction(Action):
    def __init__(self, cost):
        Action.__init__(self, cost)
    
    def execute(self, agent):
        agent.die()
