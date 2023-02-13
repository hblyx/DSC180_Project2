import torch
import torch.nn as nn
from torch_geometric.utils import to_dense_adj, to_torch_coo_tensor



class MLPGraph(nn.Module):
    def __init__(self, num_inputs, num_outputs, seed = None, sparse=False):
        super().__init__()
        if seed != None:
            torch.manual_seed(seed)
            torch.cuda.manual_seed(seed)
        
        self.sparse = sparse

        self.layers = nn.Sequential(
            nn.Linear(num_inputs, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, num_outputs)
        )

    def forward(self, graph):
        # this model is a simple MLP that is fed only the adjacency matrix
        if self.sparse:
            x = to_torch_coo_tensor(graph.edge_index)
        else:
            x = to_dense_adj(graph.edge_index).squeeze()

        output = self.layers(x)
        return output