import torch
import torch.nn.functional as F

from torch_geometric.nn import GCNConv, BatchNorm, SAGEConv, SGConv, ChebConv

__num_output__ = 21



class baseline_net(torch.nn.Module):
    def __init__(self, num_feat, f):
        super(baseline_net, self).__init__()
        
        self.conv1 = GCNConv(num_feat, f)
        
        self.conv2 = GCNConv(f, __num_output__)
        
    def forward(self, x, edge_index):
        x = x.float()
        x = self.conv1(x=x, edge_index=edge_index)
        x = F.relu(x)
        
        x = self.conv2(x, edge_index)
        
        return x