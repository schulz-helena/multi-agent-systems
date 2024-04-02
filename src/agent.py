from mesa import Agent
import networkx as nx
from random import choice


class MyAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
        self.pos = choice(list(self.model.map.nodes()))
        self.model.positions[self.unique_id] = self.pos
        print(f"I am agent {str(self.unique_id)} and I'm starting at node {self.pos}.")

    def step(self):
        self.pos = choice([n for n in self.model.map.neighbors(self.pos)])
        self.model.positions[self.unique_id] = self.pos
        print(f"I am agent {str(self.unique_id)} and I'm currently at node {self.pos}.")