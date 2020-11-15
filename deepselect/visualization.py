import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from termcolor import colored

from deepselect.writers.agent_life_writer import AgentLifeWriter
from deepselect.writers.results_writer import ResultsWriter

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
        self.rw.prepare_files(self.env.get_resources_dict())
        self.alw.init_directory("./simplified_agent_life")
        self.alw.prepare_files()
        plt.show()

    def kill_program_if_no_agents_in_environment(self):
        flag = True
        for i in self.env.nodes:
            if(len(i.agents) != 0):
                flag = False
                break
        if flag:
            quit()


    def _update(self, frame):
        self.kill_program_if_no_agents_in_environment()
        for _ in range(self.steps_per_frame):
            self.env.step()
            self.total_steps += 1


        nx.draw_networkx(self.env.graph, pos=self._pos, ax=self._ax)
        print(colored("Simulation step: " + str(self.total_steps), 'red'))
        print("Number of agents in the environment: " + colored(str(self.env.get_number_of_agents()), 'green'))
        self.rw.write_results(self.env.get_resources_dict(), self.total_steps)
        self.alw.write_simplified_results(self.total_steps)
        self.alw.write_results(self.total_steps)
        self._ax.set_title(f"Simulation step: {self.total_steps}")
        self._ax.set_xticks([])
        self._ax.set_yticks([])
