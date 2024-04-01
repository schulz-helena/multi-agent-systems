from mesa import Agent
from mesa import Model
from mesa.time import BaseScheduler


class MyAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        print(f"Hi, I am an agent, you can call me {str(self.unique_id)}.")


class MyModel(Model):

    def __init__(self, n: int):
        super().__init__()
        self.schedule = BaseScheduler(self)
        self.num_agents = n

        for i in range(self.num_agents):
            a = MyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()


model = MyModel(5)
model.step()