from random import shuffle

from deepselect.categorizer import Categorizer


class Environment:
    def __init__(self):
        self.nodes = []
        self.agent_categorizer = Categorizer()
        self.object_categorizer = Categorizer()

    def step(self):
        nodes = self.nodes[:]
        
        shuffle(nodes)
        for node in nodes:
            node.choose_actions()
            
        shuffle(nodes)
        for node in nodes:
            node.commit_actions()
            node.categorize_agents(self.agent_categorizer)
            node.categorize_objects(self.object_categorizer)
