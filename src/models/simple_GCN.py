import torch
import torch.nn.functional as F

from torch_geometric.nn import GCNConv



class GCN(torch.nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super().__init__()
        self.conv1 = GCNConv(num_inputs, 64)
        self.conv2 = GCNConv(64, num_outputs)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index

        x = self.conv1(x, edge_index)
        x = F.relu(x)
        output = self.conv2(x, edge_index)

        return output