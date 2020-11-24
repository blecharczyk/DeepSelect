from deepselect.writers.writer import Writer

class EnvironmentStructureToFileWriter(Writer):
    def __init__(self, env):
        self.env = env


    def save_environment_map(self, filename, directory):
        self.init_directory(directory)
        file_name = "Environments/" + filename + ".txt"
        edges_set = self.prepare_edge_set()
        f = open(file_name, "a")
        f.write(str(len(self.env.nodes)) + "\n")
        for edge in edges_set:
            s = str(edge[0]) + " " + str(edge[1]) + "\n"
            f.write(s)
        f.close()


    def prepare_edge_set(self):
        nodes = set()
        for node in self.env.nodes:
            for n in node.neighbors:
                if(node.node_id < n.node_id):
                    nodes.add((node.node_id, n.node_id))
        return nodes