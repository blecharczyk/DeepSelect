import random
import deepselect as ds
import networkx as nx
import matplotlib.pyplot as plt
from time import sleep


# from deepselect.action import MoveAction


# Create the environment structure
from deepselect.action.idleaction import IdleAction
from deepselect.action.moveaction import MoveAction

res = ds.Resources(["food", "water", "apples"], [5, 10, 3])
env = ds.Environment(node_count=5, initial_resources=res)

env.add_edge(0, 2)
env.add_edge(1, 2)
env.add_edge(1, 4)
env.add_edge(1, 3)
env.add_edge(3, 4)

# Distribute resources between nodes
env.nodes[0].add_resources(ds.Resources(["food", "water", "apples"], [3, 4, 2]))
env.nodes[1].sub_resources(ds.Resources(["food", "water", "apples"], [1, 2, 0]))



# Print resources
for node in env.nodes:
    print(node.node_id)
    print(node.resources)

# Define agent actions
move_action = MoveAction(cost=ds.Resources(["food", "water", "apples"], [3, 2, 0]))
idle_action = IdleAction(cost=ds.Resources(["food", "water", "apples"], [1, 1, 0]))

# Define agent behavior
class RoamBehavior(ds.Behavior):
    def choose_action(self, agent, node):
        return random.choice([move_action, idle_action])

# Add agents
agent_a = ds.Agent("Agent_1", (10, 0.3), ds.Resources(["food", "water", "apples"], [17, 20, 0]), RoamBehavior())
agent_a.fallback_action = idle_action
env.nodes[0].add_agent(agent_a)

agent_b = ds.Agent("Agent_2", (20, 0.7), ds.Resources(["food", "water", "apples"], [14, 19, 0]), RoamBehavior())
agent_b.fallback_action = idle_action
env.nodes[1].add_agent(agent_b)

print("\nAgents in each node:\n" + str(env.get_agents_dict()) + "\n")

# Start simulation
vis = ds.Visualization(env, steps_per_frame=1)
vis.start(interval=500)