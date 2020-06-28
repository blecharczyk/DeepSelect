from random import shuffle


class Environment:
    def __init__(self):
        self.nodes = []

    def step(self):
        nodes = self.nodes[:]
        
        shuffle(nodes)
        for node in nodes:
            node.choose_actions()
            
        shuffle(nodes)
        for node in nodes:
            node.commit_actions()
            node.clear_unlisted()
