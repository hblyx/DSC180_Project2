import torch
import numpy as np
import matplotlib.pyplot as plt

from torch_geometric.transforms import RandomNodeSplit
from torch_geometric.loader import DataLoader



def split_graph_data(data):
    split = RandomNodeSplit(split = "train_rest", num_splits = 1, num_val = 0.2, num_test = 0.1)
    data = split(data)
    print(data, "\n")
    print("training samples", torch.sum(data.train_mask).item())
    print("validation samples", torch.sum(data.val_mask).item())
    print("test samples", torch.sum(data.test_mask).item())
    
    return data

def data_loader(data, batch_size=10):
    return DataLoader(data, batch_size=batch_size, shuffle=True)

def masked_loss(predictions,labels,mask, criterion=torch.nn.CrossEntropyLoss()):
    mask=mask.float()
    mask=mask/torch.mean(mask)
    loss=criterion(predictions,labels)
    loss=loss*mask
    loss=torch.mean(loss)
    return (loss)    

def masked_accuracy(predictions,labels,mask):
    mask=mask.float()
    mask/=torch.mean(mask)
    accuracy=(torch.argmax(predictions,axis=1)==labels).long()
    accuracy=mask*accuracy
    accuracy=torch.mean(accuracy)
    return (accuracy) 

def train(network, data, max_epochs=10, lr=0.01, device=None):
    optimizer = torch.optim.Adam(network.parameters(), lr=lr)
    best_accuracy=0.0
    
    train_losses=[]
    train_accuracies=[]

    val_losses=[]
    val_accuracies=[]

    test_losses=[]
    test_accuracies=[]
    
    if device != None:
        network.to(device)
    
    for ep in range(max_epochs):
        if device != None:
            data.x.to(device)
            data.edge_index.to(device)
            data.y.to(device)
        
        optimizer.zero_grad()
        out=network(data.x, data.edge_index)
        loss=masked_loss(predictions=out,
                        labels=data.y,
                        mask=data.train_mask)
        loss.backward()
        optimizer.step()
        train_losses+=[loss.detach()]
        train_accuracy=masked_accuracy(predictions=out,
                                    labels=data.y, 
                                    mask=data.train_mask)
        train_accuracies+=[train_accuracy]
        
        val_loss=masked_loss(predictions=out,
                            labels=data.y, 
                            mask=data.val_mask)
        val_losses+=[val_loss.detach()]
        
        val_accuracy=masked_accuracy(predictions=out,
                                    labels=data.y, 
                                    mask=data.val_mask)
        val_accuracies+=[val_accuracy]

        test_accuracy=masked_accuracy(predictions=out,
                                    labels=data.y, 
                                    mask=data.test_mask)
        test_accuracies+=[test_accuracy]
        if np.round(val_accuracy,4)> np.round(best_accuracy ,4):
            print("Epoch {}/{}, Train_Loss: {:.4f}, Train_Accuracy: {:.4f}, Val_Accuracy: {:.4f}, Test_Accuracy: {:.4f}"
                    .format(ep+1,epochs, loss.item(), train_accuracy, val_accuracy,  test_accuracy))
            best_accuracy=val_accuracy

    print(train_losses,type(train_losses))
    plt.plot(train_losses)  
    plt.plot(val_losses)
    plt.plot(test_losses)  

    plt.show()
    
    plt.plot(train_accuracies) 
    plt.plot(val_accuracies)
    plt.plot(test_accuracies) 
    plt.show()   