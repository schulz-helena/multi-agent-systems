from mesa import Agent
import networkx as nx
from random import choice


class MyAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.pos = choice(list(self.model.map.nodes()))
        self.destination = choice(list(self.model.map.nodes()))
        print(f"Agent {str(self.unique_id)} has destination: {self.destination}.")
        self.path = []
        self.present = True

        self.model.positions[self.unique_id] = self.pos
        print(f"Agent {str(self.unique_id)} start position: {self.pos}.")

    def step(self):
        if not self.present:
            print(f"Agent {str(self.unique_id)} left the map.")
            self.model.positions[self.unique_id] = None
        else:
            if not self.path:
                self.path = nx.shortest_path(self.model.map, source=self.pos, target=self.destination, method="dijkstra")
                self.path.pop(0) # first node in path is always the current position
                print(f"Agent {str(self.unique_id)} updated path to: {self.path}.")
            self.pos = self.path.pop(0)
            if self.pos == self.destination:
                self.present = False
            self.model.positions[self.unique_id] = self.pos
            print(f"Agent {str(self.unique_id)} current position: {self.pos}.")