import numpy as np

from itertools import permutations 



def computeAccuracies(actual, predictions, overlapping=False) -> float:
        max_avg_acc = 0.0
        
        for order in orderPermutations(actual):
            avg_acc = computeOrder(order, predictions, overlapping=overlapping)
            max_avg_acc = max(avg_acc, max_avg_acc)
            
        return max_avg_acc
        
        
def orderPermutations(actual) -> permutations:
    return permutations(actual)

def computeOrder(actual: list, predictions: list, overlapping=False):
    max_intersection = [0] * len(actual)
    used_preds = set() # keep track of which prediction communities are considered as prediction of actual community
    
    for i in range(len(actual)):
            max_pred = None
            
            for j in  range(len(predictions)):
                # if we have used this prediction community,
                # we cannot think this also is prediction for another actual community
                if j in used_preds: 
                    continue
                
                num_intersection = len(actual[i].intersection(predictions[j]))
                #print("num_intersection", num_intersection)
                if num_intersection > max_intersection[i]:
                    max_intersection[i] = num_intersection
                    max_pred = j
                        
            # assign the max intersected prediction to actual communities, if the actual communities are not overlapping
            if not overlapping:
                used_preds.add(max_pred)
                #print("added", max_pred)
            
            # calculate accuracy
            max_intersection[i] = max_intersection[i] / len(actual[i])
                
    #print(max_intersection)
    
    return np.mean(max_intersection)