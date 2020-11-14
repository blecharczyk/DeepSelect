import networkx as nx
from random import shuffle
from deepselect.category import Category
from deepselect.node import Node
from deepselect.categorizer.behavior_categorizer import BehaviorCategorizer
from deepselect.categorizer.uniform_categorizer import UniformCategorizer

class Environment:
    def __init__(self, node_count=None, initial_resources=None):
        self.nodes = []
        self.graph = nx.Graph()
        self.agent_categorizer = BehaviorCategorizer()
        self.object_categorizer = UniformCategorizer(Category(name='Objects', color='black'))

        if node_count is not None:
            for _ in range(node_count):
                self.add_node(initial_resources)

    def add_node(self, initial_resources):
        node_id = len(self.nodes)
        node = Node(node_id, initial_resources)

        self.nodes.append(node)
        self.graph.add_node(node_id, node=node)

        return node

    def add_edge(self, from_node, to_node):
        if not self.graph.has_edge(from_node, to_node):
            self.nodes[from_node].neighbors.append(self.nodes[to_node])
            self.nodes[to_node].neighbors.append(self.nodes[from_node])
            self.graph.add_edge(from_node, to_node)

    def remove_edge(self, from_node, to_node):
        if self.graph.has_edge(from_node, to_node):
            self.nodes[from_node].neighbors.remove(self.nodes[to_node])
            self.nodes[to_node].neighbors.remove(self.nodes[from_node])
            self.graph.remove_edge(from_node, to_node)

    def step(self):
        nodes = self.nodes[:]

        shuffle(nodes)
        for node in nodes:
            node.choose_actions()

        shuffle(nodes)
        for node in nodes:
            node.commit_actions()

        # Categorization needs to happen in a separate loop,
        # otherwise it may exclude nodes which changed location
        # in this step.
        for node in nodes:
            node.categorize_agents(self.agent_categorizer)
            node.categorize_objects(self.object_categorizer)

    def get_resources_dict(self):
        resources_dict = {}
        for e in self.nodes:
            resources_dict[e.node_id] = {}
            for f in range(len(e.resources)):
                resources_dict[e.node_id][e.resources.names[f]] = e.resources.amounts[f]
        return resources_dict

    def get_agents_dict(self):
        agents_dict = {}
        for e in self.nodes:
            agents_dict[e.node_id] = len(e.agents)
        return agents_dict

    def print_env_components(self):
        resources = self.get_resources_dict()
        agents = self.get_agents_dict()
        for n in resources:
            print("Node_id:", n)
            for m in resources[n]:
                print(m, ':', resources[n][m])
            print("Agents:", agents[n])


    def get_number_of_agents(self):
        sum = 0
        for i in self.nodes:
            sum = sum + len(i.agents)
        return sum

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
