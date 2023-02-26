---
layout: page
title: "Introduction"
---
# Definition of Community Detection

Community detection, commonly referred to as graph clustering or network clustering, is a task in network analysis which is used to identify groups or communities within a given network. These groups are usually characteristic of dense connections between nodes within the group, as compared to the connections of these nodes to the nodes in the rest of the network.
Community detection in a network is important and interesting because it can provide useful insights to the structural organization of a network that can be applied to many diverse real-world networks. Since there is a tremendous amount of information stored in each network, if we could detect communities in each network it would provide us with important information and allow the study of the network easier. Furthermore, it could help us improve eﬀiciency for processing and analyzing network data. For example, in social media each user is a node, and the users’ friends whom they interact with form a connection and thus become a network. Social media companies could use community detection algorithms to keep people with common friends,common interests, and background tightly connected, so they could better personalize and establish a more eﬀicient recommendation system and advertisements. By analyzing the existence of communities, we can also learn about the processes of how a network is spreading in various settings. Another useful and important application of community detection is the prediction of missing links and identifying false links in a network because of errors. By applying a community detection algorithm it would allow users to assign and fix these links. There are a number of clustering algorithms which perform well but fail to make use of additional dataset or node features. We plan on exploring and evaluating the performance of different types of neural networks which make use of different features of the dataset to make predictions.

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

As we can see, the distribution of the degrees seems like a power-law distribution like other typical real networks. In other words, there are a few hubs, nodes connected to more other nodes, in the graph. That said, for the degree of nodes, most nodes have a low number of degrees, while a few nodes have higher degrees.

### Community analysis

For the label, we can see that all communities have higher internal density represented by the positive density gap. Accordingly, the average density illustrates a large density gap, 0.6199. Therefore, we can obviously see that community structure is obvious in this dataset in terms of community topology.

## Analysis of Twitch Gamer
### Degree distribution

As we can see, the distribution of the degrees seems like a power-law distribution like other typical real networks.As a result, we can see that the degree distribution follows the power-law like other typical real networks.

### Community analysis

For language as communities, even though there are some languages communities have less in-community density than out-community density, negative density gap, these density commonly have really small size. Therefore, the average density illustrates a large density gap, 0.799. In other words, although the EN community shows an obvious community structure, other communities are insignificant to detect. In conclusion, this dataset has a really weak community structure to detect in terms of community topology.