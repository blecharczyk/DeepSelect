from operator import attrgetter


class Node:
    def __init__(self, node_id, resources):
        self.node_id = node_id
        self.resources = resources
        self.neighbors = []
        self.agents = []
        self.objects = []


    def add_resources(self, resources):
        self.resources = self.resources + resources


    def sub_resources(self, resources):
        self.resources = self.resources - resources


    def add_agent(self, agent):
        self.agents.append(agent)
        agent.current_node = self


    def add_object(self, object):
        self.objects.append(object)
        object.current_node = self


    def get_agent_by_id(self, agent_id):
        for agent in self.agents:
            if agent.element_id == agent_id:
                return agent
        raise ValueError(f"No agent with id {agent_id} present")


    def get_object_by_id(self, object_id):
        for object in self.objects:
            if object.element_id == object_id:
                return object
        raise ValueError(f"No object with id {object_id} present")


    def remove_agent(self, agent):
        self.agents.remove(agent)

        if agent in self._local_agents:
            ix = self._local_agents.index(agent)
            self.agents[ix] = None


    def remove_object(self, object):
        self.objects.remove(object)


    def remove_agent_by_id(self, agent_id):
        agent = self.get_agent_by_id(agent_id)
        self.remove_agent(agent)


    def remove_object_by_id(self, object_id):
        object = self.get_object_by_id(object_id)
        self.remove_object(object)
    
    
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

    
    def categorize_agents(self, categorizer):
        for agent in self.agents:
            agent.update_category(categorizer)

    
    def categorize_objects(self, categorizer):
        for object in self.objects:
            object.update_category(categorizer)
