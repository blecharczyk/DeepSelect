import random
import math
from itertools import combinations

from deepselect.wizards.environment_wizards.environment_wizard import EnvironmentWizard

class RandomEnvironmentWizard(EnvironmentWizard):
    def __init__(self):
        pass


    def check_parameters(self, number_of_nodes, number_of_edges):
        if(number_of_edges <=0 or number_of_nodes <=0):
            raise Exception("Change parameters! Number of nodes and number of edges both must be greater than zero!")
        if number_of_edges > ((number_of_nodes * (number_of_nodes -1))//2):
            raise Exception("Too many edges!")


    def create_list_of_pairs(self, number_of_nodes):
        return list(combinations(list(range(0, number_of_nodes)), 2))


    def prepare_edges(self, number_of_nodes, number_of_edges):
        return random.sample(range(0, self.calculate_number_of_combinations(number_of_nodes)), number_of_edges)


    def add_edges(self, env, number_of_nodes, number_of_edges):
        all_possible_edges = self.create_list_of_pairs(number_of_nodes)
        edges = self.prepare_edges(number_of_nodes, number_of_edges)
        for i in edges:
            edge = all_possible_edges[i]
            env.add_edge(edge[0], edge[1])


    def calculate_number_of_combinations(self, number):
        return ((math.factorial(number))//(math.factorial(2) * math.factorial(number-2)))