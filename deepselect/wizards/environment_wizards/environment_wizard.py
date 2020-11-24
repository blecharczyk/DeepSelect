import copy
from abc import ABC, abstractmethod
import random

from deepselect.resources import Resources
from deepselect.environment import Environment

class EnvironmentWizard(ABC):

    def create_env_structure(self, number_of_nodes, number_of_edges=0):
        self.check_parameters(number_of_nodes, number_of_edges)
        env = Environment(node_count=number_of_nodes)
        self.add_edges(env, number_of_nodes, number_of_edges)
        return env

    def check_parameters(self, number_of_nodes, number_of_edges):
        pass

    def add_edges(self, env, number_of_nodes, number_of_edges):
        pass

    def add_resources_to_every_node(self, env, res):
        if len(env.nodes) != 0:
            for node in env.nodes:
                node.resources = res


    def distribute_resources_equally_and_add_excess_to_the_last_node(self, env, res):
        self.distribute_resources_equally_ignoring_excess(env, res)
        res_last = []
        for i in res.amounts:
            res_last.append((i % len(env.nodes)))
        env.nodes[-1].resources += Resources(res.names, res_last)


    def distribute_resources_equally_ignoring_excess(self, env, res):
        if len(env.nodes) != 0:
            units = []
            for i in res.amounts:
                units.append((i//len(env.nodes)))
            for node in env.nodes:
                node.resources = Resources(res.names, units)
            print(res)


    def add_agents_to_every_node(self, env, agent, number_of_agents):
        id_counter = 0
        for i in env.nodes:
            for _ in range (number_of_agents):
                agent_copy = copy.deepcopy(agent)
                agent_copy.element_id = agent.element_id + str(id_counter)
                id_counter += 1
                i.add_agent(agent_copy)


    def split_agents_randomly(self, env, agent, number_of_agents):
        id_counter = 0
        for _ in range (number_of_agents):
            agent_copy = copy.deepcopy(agent)
            agent_copy.element_id = agent.element_id + str(id_counter)
            id_counter += 1
            rand = random.randint(0, len(env.nodes) - 1)
            env.nodes[rand].add_agent(agent_copy)