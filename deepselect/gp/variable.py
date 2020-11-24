class Variable:
    def __init__(self, name):
        self.name = name

    def evaluate(self, node, agent):
        raise NotImplementedError


class AggregateVariable(Variable):
    def __init__(self, prefix, resource_type, aggregate):
        super().__init__(f"{prefix}_RES{resource_type}_{aggregate}")
        self.resource_type = resource_type
        self.aggregate = aggregate

    def evaluate(self, node, agent):
        amounts = self._list_amounts(node, agent)
        return self.aggregate(amounts) if len(amounts) > 0 else 0.0

    def _list_amounts(self, node, agent):
        raise NotImplementedError


class AgentAggregateVariable(AggregateVariable):
    def __init__(self, resource_type, aggregate):
        super().__init__("AGENT", resource_type, aggregate)

    def _list_amounts(self, node, agent):
        return [a.resources[self.resource_type] for a in node.agents if a != agent]


class ObjectAggregateVariable(AggregateVariable):
    def __init__(self, resource_type, aggregate):
        super().__init__("OBJECT", resource_type, aggregate)

    def _list_amounts(self, node, agent):
        return [o.resources[self.resource_type] for o in node.objects]


class SelfResourceVariable(Variable):
    def __init__(self, resource_type):
        super().__init__(f"SELF_RES{resource_type}")
        self.resource_type = resource_type

    def evaluate(self, node, agent):
        return agent.resources[self.resource_type]


class NodeResourceVariable(Variable):
    def __init__(self, resource_type):
        super().__init__(f"NODE_RES{resource_type}")
        self.resource_type = resource_type

    def evaluate(self, node, agent):
        return node.resources[self.resource_type]


class NodeStatVariable(Variable):
    def __init__(self, name, stat):
        super().__init__(f"STAT_{name}")
        self.stat = stat

    def evaluate(self, node, agent):
        return self.stat(node)

