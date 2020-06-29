import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Visualization:
    def __init__(self, env, steps_per_frame):
        self.env = env
        self.steps_per_frame = steps_per_frame
        self.total_steps = 0


    def start(self, interval=500):
        self._pos = nx.spring_layout(self.env.graph)
        self._fig, self._ax = plt.subplots(figsize=(6, 4))

        self._fig.canvas.set_window_title("DeepSelect")
        self._animation = FuncAnimation(self._fig, self._update, interval=interval)
        plt.show()


    def _update(self, frame):
        for _ in range(self.steps_per_frame):
            self.env.step()
            self.total_steps += 1

        self._ax.clear()

        nx.draw_networkx(self.env.graph, pos=self._pos, ax=self._ax)

        self._ax.set_title(f"Simulation step: {self.total_steps}")
        self._ax.set_xticks([])
        self._ax.set_yticks([])
