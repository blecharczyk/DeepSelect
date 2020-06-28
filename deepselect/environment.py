from random import shuffle

from deepselect.category import Category
from deepselect.categorizer import UniformCategorizer


class Environment:
    def __init__(self):
        self.nodes = []
        self.agent_categorizer = UniformCategorizer(Category(name='Agents', color='red'))
        self.object_categorizer = UniformCategorizer(Category(name='Objects', color='black'))

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
