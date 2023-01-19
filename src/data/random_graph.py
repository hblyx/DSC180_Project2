import networkx as nx


def setGroupColors(G, actual_com):
        colors = ['red', 'blue','orange','green', 'yellow', 'purple', 'olive']
        node_color = [colors[actual_com[i] % 7] for i in G.nodes]
            
        return node_color



class RandomCommunitiesGraph:
    def __init__(self) -> None:
        self.G = None
        self.actual_com = {}
    
    def generate_random_com_graph(self, N: int, n_groups: int, p_in_group: float, p_out_group: float, seed: int = None):
        self.G = nx.planted_partition_graph(n_groups, N // n_groups, p_in_group, p_out_group, seed=seed)
        self.getCommunity()
        
        return self.G, self.actual_com
        
    def getCommunity(self):
        for i in self.G.nodes:
            com = self.G.nodes[i]["block"]
            self.actual_com[i] = com
            del self.G.nodes[i]["block"]
            
    def draw(self, seed=None):
        nx.draw(self.G, pos=nx.spring_layout(self.G, seed=seed), node_color=setGroupColors(self.G, self.actual_com))