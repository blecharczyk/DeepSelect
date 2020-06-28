from deepselect.action.action import Action


class DieAction(Action):
    def __init__(self):
        Action.__init__(self, None)
    
    def execute(self, agent):
        agent.die()
