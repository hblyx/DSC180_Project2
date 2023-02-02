import torch
import torch.nn as nn
from torch_geometric.utils import to_dense_adj 



class MLPGraph(nn.Module):
    def __init__(self, num_inputs, num_outputs, seed = None):
        super().__init__()
        if seed != None:
            torch.manual_seed(seed)
            torch.cuda.manual_seed(seed)

        self.layers = nn.Sequential(
            nn.Linear(num_inputs, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, num_outputs)
        )

    def forward(self, graph):
        # this model is a simple MLP that is fed only the adjacency matrix
        x = to_dense_adj(graph.edge_index).squeeze()

        output = self.layers(x)
        return output