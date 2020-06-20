from operator import attrgetter


class Node:
    def __init__(self, node_id, resources):
        self.node_id = node_id
        self.resources = resources
        self.neighbors = []
        self.agents = []
        self.objects = []
        
    
    def choose_actions(self):
        for agent in self.agents:
            agent.choose_action()
            agent.reset_initiative()
            
    
    def commit_actions(self):
        # Sort agents by initiative
        self.agents.sort(key=attrgetter('initiative'), reverse=True)
        
        for agent in self.agents:
            agent.commit_action()

