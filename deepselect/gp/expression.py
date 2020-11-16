import deap.gp


# Expression class:
class Expression:
    def __init__(self, language, expr):
        self.language = language
        self.raw = expr
        self.tree = deap.gp.PrimitiveTree(self.raw)
        self.compiled_function = deap.gp.compile(self.tree, self.language.primitive_set)

    def __call__(self, *args):
        return self.compiled_function(*args)
