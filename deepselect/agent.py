from deepselect.element import Element
from deepselect.action import IdleAction, DieAction


class Agent(Element):
    def __init__(self, agent_id, data, resources, behavior):
        Element.__init__(self, agent_id, data, resources)
        self.behavior = behavior
        
        
    def choose_action(self):
        self._next_action = self.behavior.choose_action(self, self.current_node)
        
        
    def reset_initiative(self):
        self.initiative = 0  #TODO: Calculate initiative.
        
    
    def commit_action(self):
        if self._next_action is None or self._next_action.cost > self.resources:
            self._next_action = DieAction()
                
        self._next_action.execute(self)


    def unlist_from_current_node(self):
        if self.current_node is not None:
            self.current_node.unlist_agent(self)
            self.current_node = None
