import random

from deepselect.action.action import Action


class MoveAction(Action):
    def __init__(self, cost):
        Action.__init__(self, cost)
    
    def execute(self, agent):
        source = agent.current_node
        if len(source.neighbors) == 0:
            raise RuntimeError("No neighboring nodes present")

        # Use resources to move to another node
        agent.resources -= self.cost

        # Unlist agent from the source node (agent will be removed at the end of the simulation step)
        source.unlist_from_current_node()

        # Add agent to the destination node
        destination = random.choice(source.neighbors)
        destination.agents.append(agent)
