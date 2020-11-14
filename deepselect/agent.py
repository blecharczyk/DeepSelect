from deepselect.element import Element

from deepselect.action.idleaction import IdleAction
from deepselect.action.dieaction import DieAction


class Agent(Element):
    def __init__(self, agent_id, data, resources, behavior):
        Element.__init__(self, agent_id, data, resources)
        self.behavior = behavior
        self.fallback_action = IdleAction(resources.zeroed())

    def move_to(self, destination):
        # Remove the reference to the element from the source node
        self.unlist_from_current_node()

        # Place the element in the destination node
        destination.add_agent(self)

    def choose_action(self):
        self._next_action = self.behavior.choose_action(self, self.current_node)

    def reset_initiative(self):
        self.initiative = 0  # TODO: Calculate initiative.

    def commit_action(self):
        if self._next_action is None or not self._next_action.cost <= self.resources:
            self._next_action = self.fallback_action

            if self._next_action is None or not self._next_action.cost <= self.resources:
                self._next_action = DieAction(self.resources.zeroed())

        self._next_action.execute(self)

    def unlist_from_current_node(self):
        if self.current_node is not None:
            self.current_node.remove_agent(self)
            self.current_node = None

    def __str__(self):
        return "Agent_id: " + str(self.element_id) + "; data: " + str(self.data) + "; resources: " + str(
            self.resources) + "."
