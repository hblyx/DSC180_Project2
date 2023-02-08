import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

from collections import defaultdict

def degree_statistics(g: nx.Graph, log=False) -> None:
    degrees = []
    for node in g.nodes:
        degrees.append(g.degree[node])
    
    print("Average Degree:", np.mean(degrees))
        
    print("Maximum Degree:", np.max(degrees))
    
    print("Minimum Degree:", np.min(degrees))
    
    # Log-scale the degrees only, as the degree is obviously different
    sns.displot(degrees, bins=50, log_scale=(log, log))
    plt.title("Degree Distribution Plot")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.show()
    plt.close()
    
    degree_loglog(degrees, np.max(degrees))
    
def degree_loglog(degrees: list, max_degree: int) -> None:
    prob, _ = np.histogram(degrees, bins=max_degree)
    prob = prob / sum(prob)
    pdf = [k ** -1.5 for k in range(1, max_degree)]
    
    plt.loglog(list(range(max_degree)), prob, label="degree distribution")
    plt.loglog(list(range(max_degree))[1:], pdf, label="power law")
    plt.title("Log-log Plot of Degree Distribution")
    plt.xlabel("Degree")
    plt.xlabel("Probability")
    plt.ylim(1e-5)
    plt.legend()
    plt.show()
    plt.close()
    
def community_analysis(g: nx.Graph, community_label: str) -> pd.DataFrame:
    out_edges = defaultdict(int)
    within_edges = defaultdict(int)
    for e in g.edges:
        com_u, com_v = g.nodes[e[0]][community_label], g.nodes[e[1]][community_label]
        if com_u == com_v:
            within_edges[com_u] += 2
        else:
            out_edges[com_u] += 1
            out_edges[com_v] += 1

    df = pd.DataFrame({"in_community_edges": within_edges, "out_community_edges": out_edges})
    df["in_community_density"] = df["in_community_edges"] / (df["in_community_edges"] + df["out_community_edges"])
    df["out_community_density"] = df["out_community_edges"] / (df["in_community_edges"] + df["out_community_edges"])
    df["density_gap"] = df["in_community_density"] - df["out_community_density"]

    avg_in_density = np.sum(df["in_community_edges"]) / (np.sum(df["in_community_edges"]) + np.sum(df["out_community_edges"]))
    avg_out_density = np.sum(df["out_community_edges"]) / (np.sum(df["in_community_edges"]) + np.sum(df["out_community_edges"]))
    print("Average In-Community Density:", avg_in_density)
    print("Average Out-Community Density:", avg_out_density)
    print("Average Density Gap:", avg_in_density - avg_out_density)

    return df