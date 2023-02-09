#!/usr/bin/env python

import sys
import json

from src.data import read_graph as read
from src.models import common_neighbor_community as cnc

def main(targets):
    if 'test' in targets:
        print("Test start")
        test_result, test_success = test()
        json_obj = json.dumps(test_result)
        with open("test/test_result.txt", 'w') as f:
            f.write(json_obj)
            
        print("Test Success:", test_success)
        
def test():
    G = read.createGraph("test/testdata/test_graph.txt")
    actual_com = read.createActualCommunity("test/testdata/test_community.txt")
    print("\tHas correct environment for network/graph test")

    CNC = cnc.CommonNeighborCommunity(G, actual_com)
    CNC.findAllCommunities(thres=0.1, weighted=True)
    print("\tHas correct test result:", CNC.getAvgAccuracy() == 1.0)
    return CNC.accuracy_per_actual, CNC.getAvgAccuracy() == 1.0

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)