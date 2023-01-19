import networkx as nx

def createGraph(path):
        return nx.read_edgelist(path, nodetype=int)

def createActualCommunity(path):
    actual_com = dict()
    
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            splited = line.strip().split(" ")
            node = int(splited[0])
            com = int(splited[1])

            actual_com[node] = com
            
    return actual_com

