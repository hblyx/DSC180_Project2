---
layout: page
title: "Data Analysis"
---

# Overview of Dataset
## CORA Dataset

The CORA dataset is a benchmark dataset used in the field of machine learning and natural language processing. It contains research papers from computer science and contains the following information: title, abstract, authors, publication venue, content, citation information. In the context of community detection, the CORA dataset can be represented as a citation network, where papers are represented as nodes and citations between papers are represented as edges. The dataset has 2708 nodes and 10556 edges. The node features, the features of papers, consists of 1433 word vectors through the natural language processed already. This citation network can then be used to study the underlying structure of scientific communities.The papers are classified into one of seven classes which are:

* Case Based
* Genetic Algorithms
* Neural Networks
* Probabilistic Methods
* Reinforcement Learning
* Rule Learning
* Theory

The CORA dataset is commonly used as a testbed for evaluating text classification models, graph-based machine learning algorithms, and semi-supervised learning algorithms. It has been widely used in various research papers and has been instrumental in advancing the state of the art in these areas. For this reason, we decided to use this dataset for our performance evaluation of neural networks on community detection.

## Twitch Gamer Dataset

The Twitch Gamer dataset is a dataset collected by public APIs in Spring 2018. The dataset consists of users of Twitch as nodes of the network, and the node features including views, mature, lifetime, is dead account, and affiliate. The community we attempted to detect is the languages, and, in other words, the communities are determined through the language the user says. The dataset contains 168114 nodes and 6797557 edges. 

The Twitch Gamer dataset can possibly be applied on tasks such as commonly used as node regression, node classification, link prediction, and community detection.

# Analysis of Dataset

We basically did analysis on degree distribution and community structure in terms of community topology. Specifically for the community topology, to know whether there are communities, we need to find out the community density. If the community structure exists in the graph, we will see the higher density within communities than the density connected communities. More specifically, the density is defined by the density of edges. If edges connected two nodes within a same community, this edge is an in-community edge. Otherwise, the edge is an out-community edge. Therefore, the in-community density is defined by:

$$density = \frac{edges\_in\_community}{edges\_out\_community}$$

## Analysis of CORA
### Degree distribution

![CORA_degree](/figures/cora_log_degree_distribution.jpg)

As we can see, the distribution of the degrees seems like a power-law distribution like other typical real networks. In other words, there are a few hubs, nodes connected to more other nodes, in the graph. That said, for the degree of nodes, most nodes have a low number of degrees, while a few nodes have higher degrees.

### Community analysis

For the label, we can see that all communities have higher internal density represented by the positive density gap. Accordingly, the average density illustrates a large density gap, 0.6199. Therefore, we can obviously see that community structure is obvious in this dataset in terms of community topology.

## Analysis of Twitch Gamer
### Degree distribution

![CORA_degree](/figures/twitch_log_degree_distribution.jpg)

As we can see, the distribution of the degrees seems like a power-law distribution like other typical real networks.As a result, we can see that the degree distribution follows the power-law like other typical real networks.

### Community analysis

For language as communities, even though there are some languages communities have less in-community density than out-community density, negative density gap, these density commonly have really small size. Therefore, the average density illustrates a large density gap, 0.799. In other words, although the EN community shows an obvious community structure, other communities are insignificant to detect. In conclusion, this dataset has a really weak community structure to detect in terms of community topology.