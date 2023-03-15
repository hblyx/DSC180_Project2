---
layout: page
title: "Introduction"
---

# Definition of Community Detection

![community_detection](figures/community_detection.png)

[CommunityDetection](https://towardsdatascience.com/community-detection-algorithms-9bd8951e7dae) by Thamindu Dilshan Jayawickrama

Community detection, commonly referred to as graph clustering or network clustering, is a task in network analysis which is used to identify groups or communities within a given network. These groups are usually characteristic of dense connections between nodes within the group, as compared to the connections of these nodes to the nodes in the rest of the network.

Community detection in a network is important and interesting because it can provide useful insights to the structural organization of a network that can be applied to many diverse real-world networks. Given the enormous amount of information contained in each network, the detection of communities within them would provide valuable insights and facilitate the study of the network. Moreover, the detection of communities within networks can enhance the efficiency of processing and analyzing network data. For instance, in social media, each user represents a node, and the users' interactions with their friends create connections that form a network. Community detection algorithms can be leveraged by social media companies to identify groups of users with common friends, interests, and backgrounds, thereby improving the personalization and effectiveness of recommendation systems and advertisements. The identification of communities within a network can also provide insights into the mechanisms by which the network spreads in different contexts. Community detection has another valuable and significant application in finding missing or erroneous links within a network. By leveraging community detection algorithms, users can assign and rectify these links. Although several clustering algorithms have demonstrated good performance, they fail to incorporate additional dataset or node features. To address this limitation, we aim to investigate and compare the performance of various neural network models that leverage different features of the dataset for link prediction.

# Overview of Dataset
## CORA Dataset

The CORA dataset is a benchmark dataset used in the field of machine learning and natural language processing. It contains research papers from computer science and contains the following information: title, abstract, authors, publication venue, content, citation information. In the context of community detection, the CORA dataset can be represented as a citation network, where papers are represented as nodes and citations between papers are represented as edges. The dataset has 2708 nodes and 10,556 edges. The node features we use in our models consist of 1433 word vectors that were pre processed using natural language processing. Our models utilize node features comprising 1433 word vectors, which underwent pre-processing via natural language processing techniques. These word vectors are derived from the most frequently occurring words in all the papers and will be employed to gauge the similarities between them. This citation network can then be used to study the underlying structure of scientific communities.The papers are classified into one of seven classes which are:

* Case Based
* Genetic Algorithms
* Neural Networks
* Probabilistic Methods
* Reinforcement Learning
* Rule Learning
* Theory

The CORA dataset is a widely adopted benchmark for assessing the efficacy of text classification models, graph-based machine learning algorithms, and semi-supervised learning algorithms. Given its prevalent usage in research and considerable contributions in diverse domains, we selected this dataset as the standard benchmark for evaluating the performance of neural networks on community detection.

## Twitch Gamer Dataset

The Twitch Gamer dataset was compiled using public APIs in the spring  2018. This dataset comprises nodes representing Twitch users, while node features include attributes such as views, maturity rating, lifetime, account status, and affiliate status. The  objective of our investigation was to detect communities, with the communities being defined based on the language spoken by the users. The dataset consists of 168,114 nodes and 6,797,557 edges, and is well-suited for a variety of tasks, including node regression, node classification, link prediction, and community detection.

Given the broad range of available node features, the Twitch Gamer dataset can potentially enable the development of innovative approaches for community detection that leverage diverse characteristics of the network's nodes. For instance, incorporating the lifetime feature into a neural network model may enable the identification of long-term users who are more likely to be part of stable communities, while the affiliate status feature may provide insights into the type of content that users consume and promote.

Overall, the Twitch Gamer dataset represents a valuable network to explore the effectiveness of machine learning models for analyzing social network data. By evaluating the performance of different approaches on this dataset, we can gain insights into the strengths and limitations of various machine learning algorithms, and further advance our understanding of how to leverage node features to improve the accuracy of community detection models.