import random

from deepselect.wizards.environment_wizards.continous_environment_wizard import ContinousEnvironmentWizard
from deepselect.wizards.environment_wizards.random_environment_wizard import RandomEnvironmentWizard
from deepselect.action.moveaction import MoveAction
from deepselect.action.idleaction import IdleAction
from deepselect.behavior import Behavior
from deepselect.resources import Resources
from deepselect.visualization import Visualization
from deepselect.parsers.environment_parser import EnvironmentParser
from deepselect.agent import Agent
from deepselect.wizards.environment_wizards.complete_environment_wizard import CompleteEnvironmentWizard
from deepselect.wizards.environment_wizards.cycle_environment_wizard import CycleEnvironmentWizard
from deepselect.wizards.environment_wizards.path_environment_wizard import PathEnvironmentWizard

# Create the environment structure
res = Resources(["food", "water"], [35, 60])
#cew = ContinousEnvironmentWizard()
#cew = RandomEnvironmentWizard()
#cew = CompleteEnvironmentWizard()
#cew = CycleEnvironmentWizard()
cew = PathEnvironmentWizard()

#Get env from file
ep = EnvironmentParser()
env = ep.make_environment("Environments/env1.txt")

#modify parameters
#env = cew.create_env_structure(7, 10)

# Distribute resources between nodes
cew.add_resources_to_every_node(env, res)

# Print resources
for node in env.nodes:
    print(node.node_id)
    print(node.resources)

# Define agent actions
move_action = MoveAction(cost=Resources(["food", "water"], [3, 2]))
idle_action = IdleAction(cost=Resources(["food", "water"], [1, 1]))
#
# Define agent behavior
class RoamBehavior(Behavior):
    def choose_action(self, agent, node):
        return random.choice([move_action, idle_action])
#
# Add agents
agent_a = Agent("First_type", (10, 0.3), Resources(["food", "water"], [17, 20]), RoamBehavior())
agent_a.fallback_action = idle_action
cew.add_agents_to_every_node(env, agent_a, 2)
#
# agent_b = ds.Agent("Agent_2", (20, 0.7), ds.Resources(["food", "water"], [14, 19]), RoamBehavior())
# agent_b.fallback_action = idle_action
# env.nodes[1].add_agent(agent_b)

print("\nAgents in each node:\n" + str(env.get_agents_dict()) + "\n")

# Start simulation
vis = Visualization(env, steps_per_frame=1)
vis.start(interval=500)