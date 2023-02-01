import torch 
import numpy as np
import pandas as pd

from torch_geometric.data import Data
from torch_geometric.data import Dataset
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder


def encode_data(feat_data: pd.DataFrame, onehot_feats: list, other_feats: list, label: str) -> tuple:
    all_features = onehot_feats + other_feats

    OHE = OneHotEncoder()
    CT = ColumnTransformer([("one hot encoding", OHE, onehot_feats)], remainder = "passthrough")

    feature_matrix = CT.fit_transform(feat_data[all_features])
    
    LE = LabelEncoder()
    label_vector = LE.fit_transform(feat_data[label])

    return feature_matrix, label_vector

def construct_graph(edge_data, feature_matrix: np.ndarray, label_vector: np.ndarray):
    if type(feature_matrix) != np.ndarray:
        feature_matrix = feature_matrix.todense()
    node_features = torch.tensor(feature_matrix)

    node_labels = torch.tensor(label_vector).long()
    
    edges_list = edge_data.values.tolist()
    # undirected make edge_index like [(u,v), (v,u)]
    edge_index1 = torch.tensor(edges_list, dtype = torch.long).T
    edge_index2 = torch.zeros(edge_index1.shape, dtype = torch.long)
    edge_index2[0,:] = edge_index1[1,:]
    edge_index2[1,:] = edge_index1[0,:]
    edge_index = torch.cat((edge_index1, edge_index2), axis=1)

    return Data(x=node_features, y=node_labels, edge_index=edge_index)