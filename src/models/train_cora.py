import torch
import matplotlib.pyplot as plt


def GPU():
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        print(f"Can run on GPU ({device})")
    else:
        device = None
        print(f"Can NOT run on GPU ({device})")
        
    return device

def start_train(model, graph, criterion, model_name, lr=0.001, weight_decay=5e-4, epochs=100, device=None):
    print("\nPre-training prepare")
    if device != None:
        model.to(device)
        graph.to(device)
    print("\tRun on:", device if device != None else "CPU")
        
    optimizer=torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    print(f"\tOptimizer with {lr} leraning rate and {weight_decay} weight_dacay")
    print()
    
    print("Begin to train:")
    model, train_l, val_l, test_l, train_s, val_s, test_s, best_test_score = train(model, graph, optimizer, criterion, epochs, model_name)
    print("End of training")
    
    print("\nTraining Summary:")
    print("Best test score:", best_test_score.numpy())
    # loss plot
    plt.plot(train_l, label="train")  
    plt.plot(val_l, label="validation")
    plt.plot(test_l, label="test") 
    plt.title(f"Loss Plot of {model_name}")
    plt.legend()
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.savefig(f"../outputs/{model_name}_loss.jpg")
    plt.show()
    plt.close() 
    # score plot
    plt.plot(train_s, label="train")  
    plt.plot(val_s, label="validation")
    plt.plot(test_s, label="test") 
    plt.title(f"Score Plot of {model_name}")
    plt.xlabel("Epochs")
    plt.ylabel("Score")
    plt.legend()
    plt.savefig(f"../outputs/{model_name}_score.jpg")
    plt.show()
    plt.close() 

def train(model, graph, optimizer, criterion, epochs, model_name):
    train_l, val_l, test_l = [], [], []
    train_s, val_s, test_s = [], [], []
    
    checkpoint_name = model_name + ".pt"
    best_test_score = 0.0
    
    for ep in range(0, epochs):
        model.train() # turn to training mode
        optimizer.zero_grad()
        out = model(graph)
        train_loss = criterion(out[graph.train_mask], graph.y[graph.train_mask])
        train_loss.backward()
        optimizer.step()
        
        train_l += [train_loss.detach().cpu()]
        
        predictions = out.argmax(dim=1)
        train_score = ((predictions[graph.train_mask] == graph.y[graph.train_mask]).sum() / graph.train_mask.sum()).cpu() # training accuracy
        
        train_s += [train_score]
        
        # evaluate validation and test
        val_loss, val_score, test_loss, test_score = eval(model, graph, criterion) # validation accuracy
        val_loss, val_score, test_loss, test_score = val_loss.cpu(), val_score.cpu(), test_loss.cpu(), test_score.cpu()
        val_l += [val_loss]
        test_l += [test_loss]
        val_s += [val_score]
        test_s += [test_score]
        
        if ep == 0 or (ep + 1) % 10 == 0:
            print(f"\tEpoch: {ep + 1}, Training Loss: {train_loss}, Validation Score: {val_score}, Test Score: {test_score}")
    
        # save the best model based on test accuracy
        if test_score > best_test_score: 
            best_test_score = test_score
            torch.save(model.state_dict(), "../checkpoints/" + checkpoint_name)
            
    return model, train_l, val_l, test_l, train_s, val_s, test_s, best_test_score

    
def eval(model, graph, criterion, val=False):
    model.eval() # turn onto evaluation mode (weights won't change)
    
    out = model(graph)
    
    # get losses
    val_loss = criterion(out[graph.val_mask], graph.y[graph.val_mask]).detach()
    test_loss = criterion(out[graph.test_mask], graph.y[graph.test_mask]).detach()
    
    # get scores (accuracy)
    predictions = out.argmax(dim=1)
    
    val_score = (predictions[graph.val_mask] == graph.y[graph.val_mask]).sum() / graph.val_mask.sum()
    test_score = (predictions[graph.test_mask] == graph.y[graph.test_mask]).sum() / graph.test_mask.sum()
    
    return val_loss, val_score, test_loss, test_score