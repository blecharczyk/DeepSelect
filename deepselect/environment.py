import networkx as nx
from random import shuffle

from deepselect.category import Category
from deepselect.categorizer import BehaviorCategorizer, UniformCategorizer
from deepselect.node import Node


class Environment:
    def __init__(self):
        self.nodes = []
        self.graph = nx.Graph()
        self.agent_categorizer = BehaviorCategorizer()
        self.object_categorizer = UniformCategorizer(Category(name='Objects', color='black'))


    def add_node(self, initial_resources):
        node_id = len(self.nodes)
        node = Node(node_id, initial_resources)

        self.nodes.append(node)
        self.graph.add_node(node_id, node=node)

        return node


    def add_edge(self, from_node, to_node):
        if not self.graph.has_edge(from_node, to_node):
            self.nodes[from_node].neighbors.append(to_node)
            self.nodes[to_node].neighbors.append(from_node)
            self.graph.add_edge(from_node, to_node)


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



def from_graph(G, initial_resources):
    nodes = []
    for i in range(len(G)):
        node = Node(i, initial_resources)

        for neighbor in G[i]:
            node.neighbors.append(neighbor)

        G.nodes[i]['node'] = node
        nodes.append(node)
    
    env = Environment()
    env.graph = G
    env.nodes = nodes

    return env
