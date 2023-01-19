import sys
sys.path.append('..')

from src.data import random_graph as rg



def createTestGraph():
    RG = rg.RandomCommunitiesGraph()
    return RG.generate_random_com_graph(N=150,
                                        n_groups=3,
                                        p_in_group=0.3,
                                        p_out_group=0.01,
                                        seed=123)
    
def createTestData(G, actual_com):
    with open("test/testdata/test_graph.txt", 'w', encoding="UTF8") as f:
        for edge in G.edges:
            u = edge[0]
            v = edge[1]
            
            f.write(str(u) + " " + str(v) + "\n")
            
    with open("test/testdata/test_community.txt", 'w', encoding="UTF8") as f:
        for node in actual_com:
            community = actual_com[node]
            
            f.write(str(node) + " " + str(community) + "\n")