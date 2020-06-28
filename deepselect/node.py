from operator import attrgetter


class Node:
    def __init__(self, node_id, resources):
        self.node_id = node_id
        self.resources = resources
        self.neighbors = []
        self.agents = []
        self.objects = []
        
    
    def choose_actions(self):
        self._local_agents = self.agents.copy()
        for agent in self._local_agents:
            agent.choose_action()
            agent.reset_initiative()
            
    
    def commit_actions(self):
        # Sort agents by initiative
        self._local_agents.sort(key=attrgetter('initiative'), reverse=True)
        
        for agent in self._local_agents:
            if agent is not None:
                agent.commit_action()
    

    def unlist_agent(self, agent):
        self.agents.remove(agent)

        ix = self._local_agents.index(agent)
        self.agents[ix] = None

    def unlist_objects(self, object):
        self.objects.remove(object)
