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


    def clear_unlisted(self):
        self.agents = filter(lambda a: a is not None, self.agents)
        self.objects = filter(lambda o: o is not None, self.objects)



    def unlist_agent(self, agent):
        ix = self.agents.index(agent)
        self.agents[ix] = None

    def unlist_objects(self, object):
        ix = self.objects.index(object)
        self.objects[ix] = None
