import torch
import torch.nn as nn



class MLP(nn.Module):
    def __init__(self, num_inputs, num_outputs, seed=None):
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
        # the baseline model is a simple MLP which only use node features
        x = graph.x  
        
        output = self.layers(x)
        return output