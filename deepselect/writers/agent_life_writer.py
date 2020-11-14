from deepselect.writers.writer import Writer


class AgentLifeWriter(Writer):
    def __init__(self, env = None):
        self.env = env


    def write_results(self, step):
        tmp = "Agents/"
        for n in self.env.nodes:
            for a in n.agents:
                file_name = tmp + str(a.element_id) + ".txt"
                result = self.prepare_info(step, a)
                self.write_to_file(file_name, result)


    def prepare_info(self, step, agent):
        s = "Simulation step: " + str(step) + "\n" + str(agent) + "\n"
        if(agent.current_node.node_id != None):
            s += "Agents is in node: " + str(agent.current_node.node_id) + "\n"
        return s


    def prepare_simplified_results(self, step, agent):
        return str(step) + "," + str(agent.current_node.node_id) + "," + self.prepare_resources_amount(agent.resources)


    def write_simplified_results_title(self, agent):
        title = self.prepare_columns_title(agent)
        file_name = "simplified_agent_life/" + str(agent.element_id) + ".csv"
        self.write_to_file(file_name, title)


    def write_simplified_results(self, step):
        for n in self.env.nodes:
            for agent in n.agents:
                file_name = "simplified_agent_life/" + str(agent.element_id) + ".csv"
                content = self.prepare_simplified_results(step, agent) + "\n"
                self.write_to_file(file_name, content)


    def prepare_files(self):
        for n in self.env.nodes:
            for agent in n.agents:
                self.write_simplified_results_title(agent)

    def prepare_resurces_names(self, agent_resources):
        names = ''
        for name in agent_resources.names[:-1]:
            names += name + ","
        names += agent_resources.names[-1]
        return names


    def prepare_columns_title(self, agent):
        #self.init_directory("./simplified_agent_life")
        return "step,current_node," + self.prepare_resurces_names(agent.resources) +"\n"


    def write_to_file(self, file_name, content):
        f = open(file_name, "a")
        f.write(content)
        f.close()


    def prepare_resources_amount(self, agent_resources):
        amounts = ""
        for amount in agent_resources.amounts[:-1]:
            amounts += str(amount) + ","
        amounts += str(agent_resources.amounts[-1])
        return amounts