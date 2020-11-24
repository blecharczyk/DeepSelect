import math
from itertools import combinations

from deepselect.wizards.environment_wizards.environment_wizard import EnvironmentWizard
from deepselect.environment import Environment


class CompleteEnvironmentWizard(EnvironmentWizard):
    def __init__(self):
        pass

    def check_parameters(self, number_of_nodes, number_of_edges):
        if(number_of_edges <=0 or number_of_nodes <=0):
            raise Exception("Change parameters! Number of nodes and number of edges both must be greater than zero!")
        if number_of_edges != self.calculate_number_of_combinations(number_of_nodes):
            raise Exception("Wrong number of edges!")


    def create_env_structure(self, number_of_nodes):
        number_of_edges = self.calculate_number_of_combinations(number_of_nodes)
        self.check_parameters(number_of_nodes, number_of_edges)
        env = Environment(node_count=number_of_nodes)
        self.add_edges(env, number_of_nodes, number_of_edges)
        return env


    def add_edges(self, env, number_of_nodes, number_of_edges):
        edges = list(combinations(list(range(0, number_of_nodes)), 2))
        for x in edges:
            env.add_edge(x[0], x[1])


    def calculate_number_of_combinations(self, number):
        return ((math.factorial(number))//(math.factorial(2) * math.factorial(number-2)))