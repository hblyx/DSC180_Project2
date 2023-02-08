import torch

from torch_geometric import transforms


def split(graph, num_val=0.2, num_test=0.1, seed=None):
    if seed != None:
        torch.manual_seed(seed)
        
    split = transforms.RandomNodeSplit(num_splits=1, num_val=num_val, num_test=num_test)
    graph = split(graph)
    print(graph)
    print("training samples", torch.sum(graph.train_mask).item())
    print("validation samples", torch.sum(graph.val_mask).item())
    print("test samples", torch.sum(graph.test_mask).item())
    
    return graph