import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

from deepselect import Resources

from deepselect.writers.agent_life_writer import AgentLifeWriter
from deepselect.writers.results_writer import ResultsWriter

clear = lambda: os.system('cls')



class Visualization:
    def __init__(self, env, steps_per_frame):
        self.env = env
        self.steps_per_frame = steps_per_frame
        self.total_steps = 0
        self.rw = ResultsWriter(self.env)
        self.alw = AgentLifeWriter(self.env)


    def start(self, interval=500):
        self._pos = nx.spring_layout(self.env.graph)
        self._fig, self._ax = plt.subplots(figsize=(6, 4))

        self._fig.canvas.set_window_title("DeepSelect")
        self._animation = FuncAnimation(self._fig, self._update, interval=interval)

        self.alw.init_directory("./Agents")
        self.rw.init_directory("./Results")
        self.alw.init_directory("./simplified_agent_life")

        self.alw.prepare_files()

        plt.show()


    def _update(self, frame):
        for _ in range(self.steps_per_frame):
            self.env.step()
            self.total_steps += 1

        self._ax.clear()

        if(self.total_steps % 4 == 0):
            self.env.nodes[0].add_resources(Resources(["food", "water"], [1, 1]))

        nx.draw_networkx(self.env.graph, pos=self._pos, ax=self._ax)
        os.system('cls')
        print("Simulation step: " + str(self.total_steps))
        print(self.env.print_env_components())
        self.rw.write_results(self.env.get_resources_dict(), self.total_steps)
        self.alw.write_simplified_results(self.total_steps)
        self.alw.write_results(self.total_steps)
        self._ax.set_title(f"Simulation step: {self.total_steps}")
        self._ax.set_xticks([])
        self._ax.set_yticks([])