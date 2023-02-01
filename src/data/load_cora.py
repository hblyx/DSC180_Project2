import networkx as nx
import matplotlib.pyplot as plt
import random

from torch_geometric.datasets import Planetoid
from torch_geometric.utils import to_networkx

def load():
    dataset = Planetoid(root='/tmp/Cora', name='Cora')
    graph = dataset[0]
    num_inputs=dataset.num_node_features
    num_outputs=dataset.num_classes
    
    return graph, num_inputs, num_outputs

def convert_to_networkx(graph, n_sample=None, seed=None):
    if seed != None:
        random.seed(seed)

    g = to_networkx(graph, node_attrs=["x"])
    y = graph.y.numpy()

    if n_sample is not None:
        sampled_nodes = random.sample(g.nodes, n_sample)
        g = g.subgraph(sampled_nodes)
        y = y[sampled_nodes]

    return g, y

def plot_graph(g, y, seed=None):
    nx.draw(g, pos=nx.spring_layout(g, seed=seed), node_size=30, arrows=False, node_color=y)
    plt.show() 