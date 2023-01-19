import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from collections import defaultdict



class GraphStats:
    def __init__(self, G: nx.graph, communities: dict) -> None:
        self.G = G.copy()
        
        nx.set_node_attributes(self.G, communities, name="community")

    def getCommunityStats(self):
        """
        for the G, there are N nodes, each communitiy has m nodes
        
        for in-group connected probability p, each node has m - 1 possible within group edges
        for each community, there is m(m-1) possible edges
        let the number of within community edges is m'
        thus, p = m' / m(m-1)
        
        for out-group connected probability q, each node has n - m possible out group edges
        for each community, there is m(n - m) possible edges
        let the number of out community edges is o'
        thus, q = o' / m(n - m)
        """

        n = self.G.order()
        
        communities_count = defaultdict(int) # m for each communties
        degree_within = defaultdict(int) # m' for each communities
        degree_out = defaultdict(int) # o' for each communties

        for i in self.G.nodes:
            com = self.G.nodes[i]["community"]
            communities_count[com] += 1

        for e in self.G.edges:
            u = e[0]
            v = e[1]
            
            com_u = self.G.nodes[u]["community"]
            com_v = self.G.nodes[v]["community"]
            
            # if two nodes are within the same communities
            if com_u == com_v:
                degree_within[com_u] += 2
            else:
                degree_out[com_u] += 1
                degree_out[com_v] += 1
                
        p = {}
        q = {}
        for com in communities_count:
            m = communities_count[com]
            
            if m == 1:
                p[com] = degree_within[com] / 1.0
                q[com] = degree_out[com] / (m * (n - m))
            else:
                p[com] = degree_within[com] / (m * (m - 1))
                q[com] = degree_out[com] / (m * (n - m))
                
        output = pd.DataFrame({"number_of_nodes": communities_count,
                            "in_group_degree": degree_within,
                            "in_group_probability": p,
                            "out_group_degree": degree_out,
                            "out_group_probability": q}).fillna(value=0).sort_index()
        
        print("Average in-group probability:", round(np.mean(output["in_group_probability"]), 4))
        print("Average out-group probability:", round(np.mean(output["out_group_probability"]), 4))
        
        return output

    def draw(self, seed=None, with_labels=False):
        communities = nx.get_node_attributes(self.G, "community").values()
        
        layout = nx.spring_layout(self.G, seed=seed)
        
        nx.draw_networkx_nodes(self.G, 
                            pos=layout,
                            node_color=list(communities),
                            vmin=0, vmax=max(communities),
                            cmap = plt.cm.rainbow,
                            node_size=50)
        nx.draw_networkx_edges(self.G,
                            pos=layout,
                            alpha=0.3)
        if with_labels:
            nx.draw_networkx_labels(self.G,
                                    pos=layout,
                                    font_size=10)
        
        plt.title("Actual Community plot")
        plt.show()
        plt.close()