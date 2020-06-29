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
        agent.resources = agent.resources - self.cost

        # Move agent to random neighbor of current node
        destination = random.choice(source.neighbors)
        agent.move_to(destination)
