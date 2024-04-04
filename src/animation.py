import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.axes import Axes
import networkx as nx

class Animation:

    @staticmethod
    def map_animation(map: nx.Graph, positions_all_timesteps: list):

        def update(frame_num: int, ax: Axes, map: nx.Graph, positions_all_timesteps: list):
            
            ax.clear()
            positions = positions_all_timesteps[frame_num]
            color_map = []
            for node in map:
                if node in positions:
                    color_map.append('red')
                else: 
                    color_map.append('skyblue') 
            nx.draw(map, pos=nx.multipartite_layout(map), with_labels=True, font_weight='bold', node_size=300, node_color=color_map, font_color='black',
                    font_size=8)

        fig, ax = plt.subplots() # Build plot
        frames = len(positions_all_timesteps) # as much frames as there are timesteps in the simulation
        ani = animation.FuncAnimation(fig, update, interval = 800, frames=frames, fargs=(ax, map, positions_all_timesteps)) # interval in milliseconds(default 200)

        return ani