import math
import random
from itertools import combinations

from deepselect.wizards.environment_wizards.environment_wizard import EnvironmentWizard
from deepselect.environment import Environment


class ContinousEnvironmentWizard(EnvironmentWizard):
    def __init__(self):
        pass

    def create_env_structure(self, number_of_nodes, number_of_edges=0):
        self.check_parameters(number_of_nodes, number_of_edges)
        env = Environment(node_count=number_of_nodes)
        self.add_edges(env, number_of_nodes, number_of_edges)
        return env


    def check_parameters(self, number_of_nodes, number_of_edges):
        if(number_of_edges <=0 or number_of_nodes <=0):
            raise Exception("Change parameters! Number of nodes and number of edges both must be greater than zero!")
        if number_of_edges > self.calculate_number_of_combinations(number_of_nodes):
            raise Exception("Too many edges!")
        if number_of_edges < number_of_nodes - 1:
            raise Exception("The number of edges must be at least the number of nodes minus one!")


    def add_edges(self, env, number_of_nodes, number_of_edges):
        l = list(combinations(list(range(0, number_of_nodes)), 2))
        r = random.randint(0, len(l) - 1)
        edge = l[r]
        l.pop(r)
        used_nodes = set()
        used_nodes.add(edge[0])
        used_nodes.add(edge[1])
        i = 1
        while i <= (number_of_edges):
            r = random.randint(0, len(l) - 1)
            edge = l[r]
            if edge[0] in used_nodes or edge[1] in used_nodes:
                l.pop(r)
                used_nodes.add(edge[0])
                used_nodes.add(edge[1])
                env.add_edge(edge[0], edge[1])
                i += 1


    def calculate_number_of_combinations(self, number):
        return ((math.factorial(number))//(math.factorial(2) * math.factorial(number-2)))


