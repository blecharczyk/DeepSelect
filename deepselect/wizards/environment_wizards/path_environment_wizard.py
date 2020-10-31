from deepselect.wizards.environment_wizards.environment_wizard import EnvironmentWizard

from deepselect.environment import Environment


class PathEnvironmentWizard(EnvironmentWizard):
    def __init__(self):
        pass

    def check_parameters(self, number_of_nodes, number_of_edges):
        if(number_of_edges <=0 or number_of_nodes <=0):
            raise Exception("Change parameters! Number of nodes and number of edges both must be greater than zero!")
        if number_of_edges != (number_of_nodes - 1):
            raise Exception("The number of edges must be one less than the number of nodes!")


    def create_env_structure(self, number_of_nodes):
        number_of_edges = number_of_nodes - 1
        self.check_parameters(number_of_nodes, number_of_edges)
        env = Environment(node_count=number_of_nodes)
        self.add_edges(env, number_of_nodes, number_of_edges)
        return env


    def add_edges(self, env, number_of_nodes, number_of_edges):
        for node_number in range(number_of_nodes - 1):
            env.add_edge(node_number, node_number+1)

