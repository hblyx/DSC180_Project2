---
layout: page
title: "Introduction"
---

# Summary of Findings

After evaluating each algorithm on the CORA dataset, the following observations were made:
1. The graph convolutional neural network performed the best in predicting communities with a relatively high classification accuracy of 90.04%.
2. While nowhere as high performing as the graph convolutional neural network, the multi-layer perceptron on node features performed the second best with an accuracy of 77.12%.
3. The multi-layer perceptron on graph data was the least accurate model, having yielded an accuracy of 72.69%.

Overall, both multi-layer perceptron models have relatively similar results, but when compared to the graph convolutional neural network, the presence of both graph data and node features clearly gave it a significant boost in performance. Of course, it is important to note that these algorithms were only evaluated on one dataset, and the models’ performances are dependent on the predictive power and patterns found in the data, let alone separate hyperparameters like learning rate of each model, input / output of each layer, etc. Nonetheless, accounting for both the node features and graph data proved to be best, as the graph convolutional neural network was most suited to detecting communities in the data.

Also, evaluating each model on the Twitch dataset, we suppose that our findings from the CORA dataset does not change. We still assume that, generally, giving the model both graph structure and relevant node features can lead to a better performance. Nevertheless, we additionally found that the possibility that bad features or bad community structure might negatively affect the prediction capability of the models.

# Recommendations and Implications for Further Research

So far, the models included in this analysis were assumed to work on graph datasets where the edges were undirected, unweighted, and had no features. Assuming and going off of the result that the neural network that employed more data performed better, it may be interesting to further look into either creating new models or complicating our graph convolutional neural network that can account for datasets with directed / directed and undirected edges, edge weights, and edge features to better improve predictions. A possible place to start could be inputting edge weights into the graph convolutional layers included in our graph convolutional neural network since edge weights are an optional input to feed into the layer, suggesting it should be possible to work with edge weights. Then from there, dive deeper into bringing in more data like edge directions and features.