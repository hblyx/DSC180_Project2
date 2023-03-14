---
layout: page
title: "Data Analysis"
---

# Analysis of Dataset

We basically did analysis on degree distribution and community structure in terms of community topology. Specifically for the community topology, to know whether there are communities, we need to find out the community density. If the community structure exists in the graph, we will see the higher density within communities than the density connected communities. More specifically, the density is defined by the density of edges. If edges connected two nodes within a same community, this edge is an in-community edge. Otherwise, the edge is an out-community edge. Therefore, the in-community density is defined by:

$$density = \frac{edges\_in\_community}{edges\_out\_community}$$

## Analysis of CORA
### Degree distribution

![CORA_degree](/figures/cora_log_degree_distribution.jpg)

For the CORA dataset, the distribution of the degrees seems like a power-law distribution like other typical real networks. In other words, there are a few hubs, nodes connected to more other nodes, in the graph. That said, for the degree of nodes, most nodes have a low number of degrees, while a few nodes have higher degrees.

### Community analysis

For the CORA paper communities, all communities have higher internal density represented by the positive density gap. Accordingly, the average density illustrates a large density gap, 0.6199. Therefore, we can obviously see that community structure is obvious in this dataset in terms of community topology.

## Analysis of Twitch Gamer
### Degree distribution

![CORA_degree](/figures/twitch_log_degree_distribution.jpg)

For the Twitch dataset, the distribution of the degrees seems like a power-law distribution like other typical real networks.As a result, we can see that the degree distribution follows the power-law like other typical real networks.

### Community analysis

For Twitch language as communities, even though there are some languages communities have less in-community density than out-community density, negative density gap, these density commonly have really small size. Therefore, the average density illustrates a large density gap, 0.799. In other words, although the EN community shows an obvious community structure, other communities are insignificant to detect. In conclusion, this dataset has a really weak community structure to detect in terms of community topology.
