import pandas as pd
import matplotlib.pyplot as plt

class NodeResourcesWizard():
    def __init__(self):
        pass

    def read_csv_file(self, filename):
        file_path = "Results/" + str(filename)
        return pd.read_csv(file_path)


    def show_node_id_chart(self, df):
        x = df[str(df.columns[0])].to_list()
        for col_name in df.columns[1:]:
            y=df[str(col_name)].to_list()
            plt.plot(x, y, marker=".", linestyle='None', markersize=10)
        self.set_plot_properties("Amount of resources in the node", 'Simulation step', "Amount")
        plt.legend(df.columns.to_list()[1:])
        plt.show()


    def set_plot_properties(self, title, x_label, y_label):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)