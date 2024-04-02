import random

import matplotlib.pyplot as plt
import networkx as nx

def generate_map (show: bool):

    neighborhood = [-11, -10, -9, -1, +1, +9, +10, +11]  # all 8 neighbors of a node
    G = nx.Graph()

    # Generate nodes in 10 subsets of 10 nodes each
    for i in range(10):
        nodes_set = range(1 + i, 101 + i, 10) # i=0 gives set of nodes [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
        G.add_nodes_from(nodes_set, bipartite=i, subset=f'set{i}') # bipartite indicates which subset these nodes belong to, subset defines the name of the subset

    # Add random edges to each node
    for node in G.nodes():
        num_already_existing_edges = len([n for n in G.neighbors(node)])
        num_of_edges = random.randint(1, 7 - num_already_existing_edges)
        indices = random.sample(neighborhood, num_of_edges)
        for i in indices:
            if (node % 10 == 1) and i in [-11, -1, +9]:
                pass
            elif (node % 10 == 0) and i in [-9, +1, +11]:
                pass
            else:
                if node + i in G.nodes():
                    G.add_edge(node, node + i)
    
    if show:
        nx.draw(G, pos=nx.multipartite_layout(G), with_labels=True, font_weight='bold', node_size=300, node_color='skyblue', font_color='black',
                font_size=8) # Use multipartite layout to draw graph as grid of 10x10

        plt.show()
    
    return G
