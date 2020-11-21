import deepselect as ds


class Language:
    def __init__(self, name, variables, actions, primitive_set):
        self.name = name
        self.variables = variables
        self.actions = actions
        self.primitive_set = primitive_set
        self.behavior = ds.gp.GPBehavior(self)

    def generate_expression(self, gen, min_, max_):
        expr = gen(self.primitive_set, min_, max_)
        return ds.gp.Expression(self, expr)
