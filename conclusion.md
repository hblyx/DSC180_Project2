---
layout: page
title: "Conclusion"
---

# Summary of Findings

### The GCN model which used graph data and node features worked best at detecting communities on the CORA dataset, and, thus, we can get following conclusions:

* Using both components of the data led to a substantial improvement in accuracy, when both graph structure and node features are predictive.

### The MLP on solely the graph structure performed the best on the Twitch Gamers dataset, and, hence, we can say that:

* Using node features could have brought the accuracy down, and since the MLP on node features and GCN incorporated it, they had lower accuracy. Therefore, the node features are not as predictive as the graph data on the Twitch dataset, and node features mislead the model.

### Conclusion
We can conclude that incorporating both graph structure and node features in a model, when both are predictive, would result in improved performance. This is because the model can leverage more predictive information, which would naturally improve its performance. However, if the information provided to the model is unhelpful or misleading, it would not contribute to its performance and may even bring it down. All in all, the best performing model depends on the quality of the data, so it is important to be flexible and use whichever is best for the situation.

# Recommendations and Implications for Further Research

So far, the models included in this analysis were assumed to work on graph datasets where the edges were undirected, unweighted, and had no features. Assuming and going off of the result that the neural network that employed more data performed better, it may be interesting to further look into either creating new models or complicating our graph convolutional neural network that can account for datasets with directed and undirected edges, edge weights, and edge features to better improve predictions. A possible place to start could be inputting edge weights into the graph convolutional layers included in our graph convolutional neural network since edge weights are an optional input to feed into the layer, suggesting it should be possible to work with edge weights. Then from there, dive deeper into bringing in more data like edge directions and features.
