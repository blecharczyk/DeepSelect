import pandas as pd
import matplotlib.pyplot as plt

class ChartWizard():
    def __init__(self):
        pass

    def read_csv_file(self, filename):
        file_path = "simplified_agent_life/" + str(filename)
        return pd.read_csv(file_path)

    def show_node_id_chart(self, df):
        x = df.step.to_list()
        y = df.current_node.to_list()
        plt.plot(x, y, marker=".", linestyle = 'None', markersize = 10)
        self.set_plot_properties("Nodes visited by the agent", 'Simulation step', "Node_id")
        plt.show()

    def show_resources_chart(self, df, title):
        for r in df.columns[2:]:
            plt.plot(df['step'], df[r].to_list(), marker=".", linestyle = 'None', markersize = 10)
        self.set_resources_plot_properties(df, title)
        plt.show()

    def set_resources_plot_properties(self, df, title):
        self.set_plot_properties(title, 'Simulation step', 'Amount of resources')
        plt.legend(df.columns.to_list()[2:])
        plt.marker = "."

    def set_plot_properties(self, title, x_label, y_label):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)