import operator

from deepselect.gp.util import avg

# Sensible defaults:
DEFAULT_RESOURCE_MAPPERS = [min, max, avg]
DEFAULT_FLOAT_OPS = [(operator.add, 2), (operator.sub, 2), (operator.mul, 2), (operator.abs, 1), (operator.neg, 1)]
DEFAULT_FLOAT_CONSTS = [0.0, 1.0]
DEFAULT_FLOAT_COMPARATORS = [(operator.lt, 2), (operator.le, 2), (operator.gt, 2), (operator.ge, 2)]
DEFAULT_BOOL_OPS = [(operator.and_, 2), (operator.or_, 2), (operator.not_, 1)]
DEFAULT_BOOL_CONSTS = [True, False]
