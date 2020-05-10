class Node:
    def __init__(self, node_id, resources):
        self.node_id = node_id
        self.resources = resources
        self.neighbors = []
        self.agents = []
        self.objects = []
