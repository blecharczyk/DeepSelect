from deap.gp import genHalfAndHalf, genFull

import deepselect as ds

# Create the environment structure
res = ds.Resources(["food", "water"], [5, 10])
env = ds.Environment(node_count=5, initial_resources=res)

env.add_edge(0, 2)
env.add_edge(1, 2)
env.add_edge(1, 4)
env.add_edge(1, 3)
env.add_edge(3, 4)

# Distribute resources between nodes
env.nodes[0].add_resources(ds.Resources(["food", "water"], [3, 4]))
env.nodes[1].sub_resources(ds.Resources(["food", "water"], [1, 2]))

# Define agent actions
move_action = ds.MoveAction(cost=ds.Resources(["food", "water"], [3, 2]))
idle_action = ds.IdleAction(cost=ds.Resources(["food", "water"], [1, 1]))

# Define agent behavior
language = ds.gp.Builder("Example")\
    .with_action(move_action)\
    .with_action(idle_action)\
    .with_variable(ds.gp.AgentAggregateVariable("food", min))\
    .with_variable(ds.gp.AgentAggregateVariable("food", max))\
    .with_variable(ds.gp.AgentAggregateVariable("food", ds.gp.util.avg))\
    .with_variable(ds.gp.AgentAggregateVariable("water", min))\
    .with_variable(ds.gp.AgentAggregateVariable("water", max))\
    .with_variable(ds.gp.AgentAggregateVariable("water", ds.gp.util.avg))\
    .with_variable(ds.gp.SelfResourceVariable("food"))\
    .with_variable(ds.gp.SelfResourceVariable("water"))\
    .with_variable(ds.gp.NodeResourceVariable("food"))\
    .with_variable(ds.gp.NodeResourceVariable("water"))\
    .with_default_float_operators()\
    .with_default_float_comparators()\
    .with_default_bool_operators()\
    .with_default_bool_constants()\
    .build()

gp_behavior = language.behavior

# Add agents
expr_a = language.generate_expression(genHalfAndHalf, min_=3, max_=7)
print(expr_a.tree)
agent_a = ds.Agent("Agent_1", expr_a, ds.Resources(["food", "water"], [17, 20]), gp_behavior)
agent_a.fallback_action = idle_action
env.nodes[0].add_agent(agent_a)

expr_b = language.generate_expression(genFull, min_=3, max_=5)
print(expr_b.tree)
agent_b = ds.Agent("Agent_2", expr_b, ds.Resources(["food", "water"], [14, 19]), gp_behavior)
agent_b.fallback_action = idle_action
env.nodes[1].add_agent(agent_b)

print("\nAgents in each node:\n" + str(env.get_agents_dict()) + "\n")

# Start simulation
vis = ds.Visualization(env, steps_per_frame=1)
vis.start(interval=500)








