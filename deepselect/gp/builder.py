from typing import Any, List, Tuple

import deap.gp

from deepselect import Action
from deepselect.gp import Language, Variable
from deepselect.gp.util import if_then_else, Bool
from deepselect.gp.defaults import *


class Builder:
    def __init__(self, name):
        self.name = str(name)
        self.clear()

    def clear(self):
        self.variables = []
        self.actions = []

        self.float_operators = []
        self.float_ephemeral = []
        self.float_constants = []
        self.float_comparators = []

        self.bool_operators = []
        self.bool_constants = []

    variables: List[Variable]
    actions: List[Action]

    float_operators: List[Tuple[Any, int]]
    float_ephemeral: List[Tuple[str, Any]]
    float_constants: List[float]
    float_comparators: List[Tuple[Any, int]]

    bool_operators: List[Tuple[Any, int]]
    bool_constants: List[bool]

    def with_action(self, action):
        self.actions.append(action)
        return self

    def with_actions(self, actions):
        self.actions.extend(actions)
        return self

    def with_variable(self, variable):
        self.variables.append(variable)
        return self

    def with_variables(self, variables):
        self.variables.extend(variables)
        return self

    def with_float_operator(self, op, args):
        self.float_operators.append((op, args))
        return self

    def with_float_operators(self, ops_and_args):
        for (op, arg) in ops_and_args:
            self.with_float_operator(op, arg)
        return self

    def with_default_float_operators(self):
        return self.with_float_operators(DEFAULT_FLOAT_OPS)

    def with_float_ephemeral(self, name, fn):
        self.float_ephemeral.append((name, fn))
        return self

    def with_float_constant(self, const):
        self.float_constants.append(const)
        return self

    def with_float_constants(self, consts):
        self.float_constants.extend(consts)
        return self

    def with_default_float_constants(self):
        return self.with_float_constants(DEFAULT_FLOAT_CONSTS)

    def with_float_comparator(self, cmp, args=2):
        self.float_comparators.append((cmp, args))
        return self

    def with_float_comparators(self, cmps_and_args):
        for (cmp, args) in cmps_and_args:
            self.with_float_comparator(cmp, args)
        return self

    def with_default_float_comparators(self):
        return self.with_float_comparators(DEFAULT_FLOAT_COMPARATORS)

    def with_bool_operator(self, op, args):
        self.bool_operators.append((op, args))
        return self

    def with_bool_operators(self, ops_and_args):
        for (op, args) in ops_and_args:
            self.with_bool_operator(op, args)
        return self

    def with_default_bool_operators(self):
        return self.with_bool_operators(DEFAULT_BOOL_OPS)

    def with_bool_constant(self, const):
        self.bool_constants.append(const)
        return self

    def with_bool_constants(self, consts):
        self.bool_constants.extend(consts)
        return self

    def with_default_bool_constants(self):
        return self.with_bool_constants(DEFAULT_BOOL_CONSTS)

    def build(self):
        # Validate configuration:
        self.validate()

        # Create a typed primitive set:
        pset = deap.gp.PrimitiveSetTyped(self.name, [float] * len(self.variables), int)

        # Define a conditional instruction:
        pset.addPrimitive(if_then_else, [Bool, int, int], int)

        # Define floating point arithmetic:
        for (op, args) in self.float_operators:
            pset.addPrimitive(op, [float] * args, float)

        for (name, fn) in self.float_ephemeral:
            pset.addEphemeralConstant(name, fn, float)

        for const in self.float_constants:
            pset.addTerminal(const, float)

        # Define ordering of floats:
        for (cmp, args) in self.float_comparators:
            pset.addPrimitive(cmp, [float] * args, Bool)

        # Define boolean logic:
        for (op, args) in self.bool_operators:
            pset.addPrimitive(op, [Bool] * args, Bool)

        for const in self.bool_constants:
            pset.addTerminal(const, Bool)

        # Define action terminals:
        for action_idx in range(len(self.actions)):
            pset.addTerminal(action_idx, int)

        # Construct the language definition object:
        language = Language(self.name, self.variables, self.actions, pset)

        # Clear the builder instance to allow repeated use:
        self.clear()

        # Return the language:
        return language

    def validate(self):
        if len(self.variables) == 0:
            raise ValueError("At least one variable must be defined")
        if len(self.actions) == 0:
            raise ValueError("No actions defined for the agent to take")
        if len(self.float_comparators) == 0:
            raise ValueError("At least one float comparison function must be provided")
