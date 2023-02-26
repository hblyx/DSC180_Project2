---
layout: page
title: "Introduction"
---

# Performance Metric for the Algorithms (classification accuracy)

Each neural network was evaluated by their classification accuracy as the proportion of nodes correctly categorized to their true community divided by the total number of nodes in the data. A high classification accuracy suggests that the model performs well in predicting which community a node belongs to while a low classification accuracy implies that the model is poor at classifying which nodes belong to which community. Accuracy was chosen as the metric for its simplicity and the fact that other metrics like sensitivity and specificity work on the assumption that the prediction task is classification. Since we work with more than 2 possible communities, both sensitivity and specificity are not viable for our analysis.

## CORA

The result of the CORA dataset shows that the GCN which uses both node features and graph topology gives the best performance, and the other two models give less than 80% classification accuracy. These results are expected, since the CORA dataset have relevant node features and obvious community structure in the network. Specifically, since the relevant node features can also be independently used for the community detection, we expect to see that the model of MLP with node features provides a not bad accuracy. Similarly, the model of MLP with graph structures should also give a similar accuracy. Then, since both node features and graph topology can lead predictions, the simple GCN can naturally offer a better performance than other two models.

## Twitch

The models’ performances on the CORA dataset is displayed in the table below:


Unlike what we observed for the CORA dataset, the results from the Twitch Gamer dataset give quite different results. To be specific, the best performance model is the model of MLP with graph structure. Although the GCN model gets both node features and graph structure, it does not get more power for prediction. Admittedly, even though we implemented adaptive learning rate to avoid over-fitting,  overfitting of models is still possible. Nevertheless, we also got some insight from these results of the Twitch Gamer dataset. From the data analysis for the Twitch Gamer dataset, we found that the EN language community is approximately 74% of the dataset. Therefore, the models with node features and the GCN model both demonstrate about 74% accuracy. Thus, we assume that these two models are unable to fit the data, and they might only make predictions like randomness. Also from the dataset analysis, we knew that the node features are views, mature, lifetime, is dead account, and affiliate, and we think they might not be quite related to the community. In other words, we suppose that these node features are possibly unable to get the model fit the data, and, then, the model cannot really make nice predictions based on these node features. Next, we can see the model of MLP with graph structure provides best performance, 89.10%, so we believe that graph structure might be able to make predictions. Therefore, the GCN model is possibly negatively affected by the node features, although the GCN model also takes the graph structure information into account.
