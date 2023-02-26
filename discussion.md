---
layout: page
title: "Discussion"
---

# Strengths and Weaknesses of each Algorithm
## MLP on Node Features

The Multi-Layer Perceptron working solely based on node features makes it a simple algorithm to utilize for community detection. The model does not need a set of nodes and edges to deploy, so it is able to perform in the absence of graph data. However, its simple dependence on the node features means if the node features are not predictive of which community a node belongs to, the model is bound to perform poorly. Also, the model can only perform so well in the absence of further information like the nodes and edges of the graph data.

## MLP on Graph Data 

The strengths of using a MLP for community detection using only graph data are its simplicity and flexibility. MLPs are straightforward models that can easily handle simple linear relationships between input and output data, making them well-suited for processing graph data. They are also flexible and can be easily modified to accommodate different types of graph data. Additionally, MLPs can generalize well to unseen data, making them well-suited for community detection tasks where predictions need to be made on new, previously unseen nodes. The weaknesses of using an MLP for community detection include limited model capacity, the potential for overfitting, and insensitivity to graph structure. MLPs are limited in their ability to capture complex non-linear relationships between input and output data, which can result in suboptimal performance on large and complex graphs.


## GNN on Node Features + Graph Data

The graph convolutional neural network makes use of both the node features and set of nodes and edges given in the data to predict communities. The model depends on the existence of both the features and graph data, so having both is a prerequisite to implement this neural network. To its advantage, it has more potential to perform well precisely because it can use more data to make predictions.

# Comparison of Results

A comparison of the results of three models for community detection on CORA dataset shows that the GNN performed the best, achieving an accuracy of 90.04%. The MLP which used node features had the second-best performance, with an accuracy of 77.12%. However, the MLP which used graph data showed a lower accuracy of 72.69%. These results indicate that incorporating node feature information into the model can lead to improved performance in community detection tasks. The GNN, which was specifically designed to process node features and graph data, demonstrated the best results, while the MLP on Node Features showed a significant drop in accuracy when only using node features. These results highlight the importance of considering both node features and graph structure information in community detection tasks.

# Twitch Gamers Dataset

From the results of the Twitch Gamer dataset, we found that node features might negatively affect the prediction power of the model. Even though the results from CORA dataset shows that when models take more information, taking graph structure and node features, can give a better performance, the Twitch dataset gives the possibility that bad node features might reduce the predictability of the models. As we stated previously, since the node features of the Twitch Gamers dataset are not really relevant to language communities, taking these irrelevant node features into the models significantly negatively affects the prediction power of the models.

# Limitation of Graph Neural Networks

The Graph Neural Networks generally require node features, and, thus, it is limited to detect the communities on graphs which contain the node features. In other words, for the simple graphs which have only graph structure but no node features, it is not natural to use GNN to detect the communities.

The GNNs are also unable to detect the weak community with weak features. Specifically, when the community structure of the graph is not obvious, such as a really low or negative community density difference, the community structures are not obvious to detect for  both GNNs and traditional algorithms, Louvains algorithms for example. Thus, the graph structure cannot help the model to detect the communities. Nevertheless, the GNNs can also use node features to fit the model. But, if the node features can also not help the model fit, the GNNs are also unable to detect the communities.  In our attempts, we also used another Twitch Gamers Dataset to test the models as CORA dataset, but no models and even traditional algorithms cannot detect the communities of the graph. In other words, if the graph has both weak community structures and weak features, the GNNs cannot detect the communities.