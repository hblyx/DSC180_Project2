import networkx as nx

from collections import defaultdict

def read_graph(path: str) -> nx.Graph:
        return nx.read_edgelist(path, nodetype=int)

def read_ground_truth(path: str, nodewise: bool=False) -> dict:
    ground_truth = defaultdict(list)
    com_idx = 0
    
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for node in line.strip().split("\t"):
                if nodewise:
                    ground_truth[node].append(com_idx)
                else:
                    ground_truth[com_idx].append(node)
                    
            com_idx += 1
    
    return ground_truth