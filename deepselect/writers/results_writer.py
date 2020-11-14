from deepselect.writers.writer import Writer


class ResultsWriter(Writer):
    def __init__(self, env):
        self.env = env


    def write_results(self, dict, step):
        file_operator = [None] * len(self.env.nodes)
        nodes_id = []
        for i in self.env.nodes:
            nodes_id.append("Results/node_" + str(i.node_id))

        for i in range(len(nodes_id)):
            file_name = str(nodes_id[i]) + ".csv"
            file_operator[i] = open(file_name, "a")
            #file_operator[i].write(self.crop(step, i, dict))
            file_operator[i].write(self.crop_line(step, i, dict))
            #self.crop_line(step,i,dict)
            file_operator[i].close()


    def crop(self, step, i, dict):
        s = str(step) + " " + str(dict[i]) + "\n"
        return s


    def prepare_files(self, dict):
        file_operator = [None] * len(self.env.nodes)
        nodes_id = []
        for i in self.env.nodes:
            nodes_id.append("Results/node_" + str(i.node_id))
        for i in range(len(nodes_id)):
            file_name = str(nodes_id[i]) + ".csv"
            file_operator[i] = open(file_name, "a")
            file_operator[i].write(self.prepare_headlines(i, dict))
            file_operator[i].close()


    def prepare_headlines(self, i, dict):
        ss = "step"
        for key in dict[i]:
            ss = ss + "," + str(key)
        return ss + "\n"


    def crop_line(self, step, i, dict):
        ss = ""
        for key in dict[i]:
            ss = ss + "," + str(dict[i][key])
        s = str(step) + ss + "\n"
        return s