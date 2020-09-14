import os
import shutil


class ResultsWriter:
    def __init__(self, env):
        self.env = env

    def init_result_directory(self):
        dir_path = "./Results"

        # Remove Results directory if exists
        try:
            shutil.rmtree(dir_path)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))

        # Create Results directory
        try:
            os.makedirs(dir_path)
        except OSError:
            print("Creation of the directory %s failed" % dir_path + "\n")
        else:
            print("Successfully created the directory %s" % dir_path + "\n")

    def write_results(self, dict, step):
        file_operator = [None] * len(self.env.nodes)
        nodes_id = []
        for i in self.env.nodes:
            nodes_id.append("Results/node_" + str(i.node_id))

        for i in range(len(nodes_id)):
            file_operator[i] = open(nodes_id[i], "a")
            file_operator[i].write(self.crop(step, i, dict))
            file_operator[i].close()

    def crop(self, step, i, dict):
        s = "Simulation step: " + str(step) + " " + str(dict[i]) + "\n"
        return s
