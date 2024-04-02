from mesa import Model
from mesa.time import BaseScheduler
from agent import MyAgent
from grid_map_generator import generate_map
import networkx as nx
import matplotlib.pyplot as plt

class MyModel(Model):

    def __init__(self, n: int):
        super().__init__()
        self.schedule = BaseScheduler(self)
        self.num_agents = n
        self.map = generate_map(False)
        self.positions = []

        for i in range(self.num_agents):
            self.positions.append(None)
            a = MyAgent(i, self)
            self.schedule.add(a)

        self.show_map()

    def step(self):
        self.schedule.step()
        self.show_map()

    def show_map(self):
        color_map = []
        for node in self.map:
            if node in self.positions:
                color_map.append('red')
            else: 
                color_map.append('skyblue') 
        nx.draw(self.map, pos=nx.multipartite_layout(self.map), with_labels=True, font_weight='bold', node_size=300, node_color=color_map, font_color='black',
                font_size=8)
        plt.show()