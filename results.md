---
layout: page
title: "Results"
---

# Performance Metric for the Algorithms (classification accuracy)

Each neural network was evaluated by their classification accuracy as the proportion of nodes correctly categorized to their true community divided by the total number of nodes in the data. A high classification accuracy suggests that the model performs well in predicting which community a node belongs to while a low classification accuracy implies that the model is poor at classifying which nodes belong to which community. Accuracy was chosen as the metric for its simplicity and the fact that other metrics like sensitivity and specificity work on the assumption that the prediction task is classification. Since there are many more communities than two, metrics like sensitivity and specificity are not viable for our analysis.

## CORA

| Model         | Accuracy         |
|------------------|------------------|
| Multi-Layer Perceptron on Node Features      | 77.12%     |
| Multi-Layer Perceptron on Graph Data     | 72.69%      |
| Graph Convolutional Neural Network     | 90.04%      |

The results of the models on the CORA dataset demonstrate that the GCN incorporating both node features and graph topology resulted in the highest classification accuracy when compared to the other two models evaluated. The other two models yielded sub-par accuracies of around $75\%$. These results were expected since the CORA dataset has relevant node features and a well-defined community structure which makes it well suited for community detection.  More specifically, since the relevant node features can be utilized independently for community detection, we anticipated that the MLP model employing node features would yield somewhat satisfactory classification accuracy. We also expected that the MLP model using graph structure would provide similar performance. Hence, since both node features and graph topology contribute to predictive accuracy, the GCN model is naturally capable of delivering superior performance relative to the other two models.

## Twitch

The models’ performances on the CORA dataset is displayed in the table below:

| Model         | Accuracy         |
|------------------|------------------|
| Multi-Layer Perceptron on Node Features      | 74.16%     |
| Multi-Layer Perceptron on Graph Data     | 89.10%      |
| Graph Convolutional Neural Network     | 74.08%      |

Unlike what we observed for the CORA dataset, the results from the Twitch Gamer dataset are counter intuitive. The model with the best performance is the model of MLP with graph structure. Despite the GCN using node features and graph topology, it does not lead to a better classification accuracy. Although we did implement adaptive learning rate to avoid over-fitting the models, it is still possible to over-fit. The findings from the analysis of the Twitch Gamer dataset provide valuable insights. The data revealed that the EN (English) language community constitutes approximately $74\%$ of the dataset which makes sense since most Twitch streamers stream in English. The MLP model which uses node features and the GCN model had similar accuracies of around $74\%$. It is possible that these two models were unable to fit the data and only generate random predictions. Upon analyzing the dataset, we identified that the node features including views, maturity, lifetime, account status, and affiliate may not be closely related to the community, which could explain the inability of the models to fit the data. The MLP model with graph structure demonstrated the best performance, achieving $89.10\%$ accuracy, which shows that using solely graph structure might be more suitable depending on the type of network. Therefore, it is likely that utilizing node features negatively impacted the performance of the GCN model, despite its incorporation of graph structure information.
