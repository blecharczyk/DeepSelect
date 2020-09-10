import random
import deepselect as ds
import networkx as nx

from deepselect.action import MoveAction


# Create the environment structure
res = ds.Resources(["food", "water"], [5, 10])
env = ds.Environment(node_count=5, initial_resources=res)

env.add_edge(0, 2)
env.add_edge(1, 2)
env.add_edge(1, 4)
env.add_edge(1, 3)
env.add_edge(3, 4)

# Distribute resources between nodes
env.nodes[0].add_resources(ds.Resources(["food", "water"], [3, 4]))
env.nodes[1].sub_resources(ds.Resources(["food", "water"], [1, 2]))

# Print resources
for node in env.nodes:
    print(node.node_id)
    print(node.resources)

# Define agent actions
move_action = MoveAction(cost=ds.Resources(["food", "water"], [3, 2]))
idle_action = ds.IdleAction(cost=ds.Resources(["food", "water"], [1, 1]))

# Define agent behavior
class RoamBehavior(ds.Behavior):
    def choose_action(self, agent, node):
        return random.choice([move_action, idle_action])

# Add agents
agent_a = ds.Agent(1, (10, 0.3), ds.Resources(["food", "water"], [17, 20]), RoamBehavior())
agent_a.fallback_action = idle_action
env.nodes[0].add_agent(agent_a)

agent_b = ds.Agent(1, (20, 0.7), ds.Resources(["food", "water"], [14, 19]), RoamBehavior())
agent_b.fallback_action = idle_action
env.nodes[1].add_agent(agent_b)

# Start simulation
vis = ds.Visualization(env, steps_per_frame=100)
vis.start(interval=500)