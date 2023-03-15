---
layout: page
title: "Performance Evaluation of Neural Networks on Community Detection"
---

#### Authors: Yaoxin Li, Justin Nguyen, Vivek Rayalu


# Abstract

This project investigates the performance of three machine learning approaches for community detection on two distinct datasets: the CORA academic citation network and a Twitch user dataset. The CORA dataset presents a challenging testbed for community detection algorithms as it represents a citation network of scientific papers in computer science, while the Twitch Gamer dataset captures the mutual friend relationships between Twitch users. Our first approach uses a Multi-Layer Perceptron (MLP) that considers only node features, while the second approach uses another MLP that only considers graph data. The third approach employs a graph convolutional neural network (GCN) that combines both node features and graph data. We evaluate the performance of these models on both datasets by comparing the results to the ground-truth labels provided by the authors of the datasets. Our results demonstrate that the GCN model outperforms the two MLP models on the CORA dataset, whereas on the Twitch dataset, the MLP model that uses graph data performs better. However, further investigation is necessary to improve the performance of the GCN model that combines both graph and node features. This study emphasizes the importance of considering both node features and graph data for community detection in complex networks and underscores the potential of GCNs for this task.

![community_detection](figures/community_detection.png) 

[CommunityDetection](https://towardsdatascience.com/community-detection-algorithms-9bd8951e7dae) by Thamindu Dilshan Jayawickrama
