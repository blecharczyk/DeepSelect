import os
import shutil


class AgentLifeWriter:
    def __init__(self, env):
        self.env = env

    def init_agents_directory(self):
        dir_path = "./Agents"

        # Remove Agents directory if exists
        try:
            shutil.rmtree(dir_path)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))

        # Create Agents directory
        try:
            os.makedirs(dir_path)
        except OSError:
            print("Creation of the directory %s failed" % dir_path + "\n")
        else:
            print("Successfully created the directory %s" % dir_path + "\n")

    def write_results(self, step):
        tmp = "Agents/"
        for n in self.env.nodes:
            for a in n.agents:
                file_name = tmp + str(a.element_id) + ".txt"
                s = self.prepare_info(step, a)
                f = open(file_name, "a")
                f.write(s)
                f.close()


    def prepare_info(self, step, agent):
        s = "Simulation step: " + str(step) + "\n" + str(agent) + "\n"
        if(agent.current_node.node_id != None):
            s += "Agents is in node: " + str(agent.current_node.node_id) + "\n"
        return s



