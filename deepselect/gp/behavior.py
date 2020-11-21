from deepselect import Behavior


class GPBehavior(Behavior):
    def __init__(self, language):
        self.language = language

    def choose_action(self, agent, node):
        # Describe the local environment state:
        args = list([v.evaluate(node, agent) for v in self.language.variables])

        # Extract the algorithm from the current agent:
        algorithm = agent.data

        # Pass the local environment state to the algorithm:
        ret_val = algorithm(*args)

        # Return the correct action.
        return self.language.actions[ret_val]
