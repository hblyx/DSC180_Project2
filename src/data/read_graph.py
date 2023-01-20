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
                ground_truth[com_idx].append(node)
                
            com_idx += 1
    
    if nodewise:
        ground_truth = convert_ground_truth_nodewise(ground_truth)        
    
    return ground_truth


def convert_ground_truth_nodewise(ground_truth: dict) -> dict:
    output = defaultdict(list)
    
    for community in ground_truth:
        for node in ground_truth[community]:
            output[node].append(community)
            
    return output
