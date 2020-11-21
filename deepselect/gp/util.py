# Workaround recommended by DEAP creators (see https://github.com/DEAP/deap/pull/106#issuecomment-158790599).
class Bool(object):
    pass


# Conditional instruction
def if_then_else(condition, output_if_true, output_if_false):
    return output_if_true if condition else output_if_false


# Average:
def avg(e):
    count = len(e)
    return sum(e) / count if count > 0 else 0.0
