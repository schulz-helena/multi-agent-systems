from mesa import Model
from mesa.time import BaseScheduler
from agent import MyAgent
from grid_map_generator import generate_map
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

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
        positions_copy = deepcopy(self.positions)
        self.positions_all_timesteps = [positions_copy]
        

    def step(self):
        self.schedule.step()
        positions_copy = deepcopy(self.positions)
        self.positions_all_timesteps.append(positions_copy)