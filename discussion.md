---
layout: page
title: "Discussion"
---

# Strengths and Weaknesses of each Algorithm
## MLP on Node Features

The Multi-Layer Perceptron (MLP) working solely based on node features makes it a simple algorithm to utilize for community detection. The model does not need a set of nodes and edges to deploy, so it is able to perform in the absence of graph data. However, its simple dependence on the node features means if the node features are not predictive of which community a node belongs to, the model is bound to perform poorly. Also, the model can only perform so well in the absence of further information like the nodes and edges of the graph data.

## MLP on Graph Data 

The strengths of using a MLP for community detection using only graph data are its simplicity and flexibility. MLPs are straightforward models that can easily handle simple linear relationships between input and output data, making them well-suited for processing graph data. They are also flexible and can be easily modified to accommodate different types of graph data. Additionally, MLPs can generalize well to unseen data, making them well-suited for community detection tasks where predictions need to be made on new, previously unseen nodes. The weaknesses of using an MLP for community detection include limited model capacity, the potential for overfitting, and insensitivity to graph structure. MLPs are limited in their ability to capture complex non-linear relationships between input and output data, which can result in suboptimal performance on large and complex graphs.

## GNN on Node Features + Graph Data

The graph convolutional neural network makes use of both the node features and set of nodes and edges given in the data to predict communities. The model depends on the existence and quality of both the node features and graph data, so having both is a prerequisite to implement this neural network. To its advantage, it has more potential to perform well precisely because it can use more data to make predictions. A disadvantage of the GCN is that it can result in flawed predictions when the node features are not closely related to the underlying communities they belong to. Another disadvantage can occur when the community structure of a network is indistinct, indicated by a low or negative community density difference. In such cases, the graph structure does not facilitate community detection for traditional clustering algorithms or the GCN. However, GCNs can leverage node features to optimize the model, which gives them an edge over traditional algorithms. 

# Comparison of Results

## CORA dataset
A comparison of the results of three models for community detection on CORA dataset shows that the GCN performed the best, achieving an accuracy of 90.04%. The MLP which used node features had the second-best performance, with an accuracy of 77.12%. However, the MLP which used graph data showed a lower accuracy of 72.69%. These results indicate that incorporating node feature information into the model can lead to improved performance in community detection tasks. The GCN, which was specifically designed to process node features and graph data, demonstrated the best results, while the MLP on Node Features showed a significant drop in accuracy when only using node features. These results highlight the importance of considering both node features and graph structure information in community detection tasks.

## Twitch Gamers Dataset

The analysis of the Twitch Gamer dataset revealed that node features can sometimes have a detrimental effect on the predictive capacity of the models. While the results from the CORA dataset suggest that incorporating both graph structure and node features can improve performance, the findings from the Twitch dataset indicate that irrelevant node features can reduce the predictability of the models. As previously mentioned, the node features in the Twitch Gamers dataset are probably not directly related to language communities, and including these extraneous features in the models substantially diminishes their predictive power.
