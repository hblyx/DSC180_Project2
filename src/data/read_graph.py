import networkx as nx

from collections import defaultdict



def read_twitch(features_path: str, edges_path: str) -> nx.Graph:
    g = nx.Graph()
    
    with open(edges_path, 'r') as file:
        next(file) # skip the header
        for line in file:
            u, v = line.strip().split(",") # undirected
            u, v = int(u), int(v)
            g.add_edge(u, v)
            
    features = defaultdict(dict)
    with open(features_path, 'r') as file:
        next(file) # skip the header
        for line in file:
            # read data
            views, mature, life_time, _, _, id, dead_account, language, affiliate = line.strip().split(",")
            # convert dtypes
            id = int(id)
            views = int(views)
            life_time = int(life_time)
            # assign features
            features[id]["view"] = views
            features[id]["mature"] = mature
            features[id]["life_time"] = life_time
            features[id]["dead_account"] = dead_account
            features[id]["language"] = language
            features[id]["affiliate"] = affiliate
            
    nx.set_node_attributes(g, features)
    
    return g