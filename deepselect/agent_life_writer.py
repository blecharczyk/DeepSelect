class Agent_life_writer:
    def __init__(self, env):
        self.env = env


    def write_results(self, step):
        tmp = "Agents/"
        for n in self.env.nodes:
            for a in n.agents:
                file_name = tmp + str(a.element_id) + ".txt"
                s = self.prepare_info(step, a);
                f = open(file_name, "a")
                f.write(s)
                f.close()
                #print(a.current_node.node_id)


    def prepare_info(self, step, agent):
        s = "Simulation step: " + str(step) + "\n" + str(agent) + "\n"
        if(agent.current_node.node_id != None):
            s += "Agents is in node: " + str(agent.current_node.node_id) + "\n"
        return s



