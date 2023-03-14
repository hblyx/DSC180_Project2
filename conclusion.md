---
layout: page
title: "Conclusion"
---

# Summary of Findings

The GNN model which used graph data and node features worked best at detecting communities on the CORA dataset, and, thus, we can get following conclusions:

* Using both components of the data led to a substantial improvement in accuracy, when both graph structure and node features are predictive.

The MLP on solely the graph structure performed the best on the Twitch Gamers dataset, and, hence, we can say that:

* Using node features brought the accuracy down, and since the MLP on node features and GNN incorporated it, they had lower accuracy. Therefore, the node features are not as predictive as the graph data, and node features will mislead the model.

In other words, we can conclude that, if both graph structure and node features are predictive, applying both graph structure and node features will give a better performance. As the model receives more predictive information it will result in better performance, giving more predictive information, node features and graph structure simultaneously, to the model can naturally cause better performance. Nevertheless, if the information we pass to the model might be misleading or not predictive, the information is not helpful for the performance of the model. All in all, the best performing model depends on the predictivity of the data, so it is important to be flexible and use whichever is best for the situation.

# Recommendations and Implications for Further Research

So far, the models included in this analysis were assumed to work on graph datasets where the edges were undirected, unweighted, and had no features. Assuming and going off of the result that the neural network that employed more data performed better, it may be interesting to further look into either creating new models or complicating our graph convolutional neural network that can account for datasets with directed / directed and undirected edges, edge weights, and edge features to better improve predictions. A possible place to start could be inputting edge weights into the graph convolutional layers included in our graph convolutional neural network since edge weights are an optional input to feed into the layer, suggesting it should be possible to work with edge weights. Then from there, dive deeper into bringing in more data like edge directions and features.