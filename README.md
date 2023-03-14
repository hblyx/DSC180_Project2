# DSC180 Project 2 - Performance Evaluation of Community Detection on Neural Networks
#### Yaoxin Li, Justin Nguyen, Vivek Rayalu

### Introduction
As our previous work, we explored the traditional solutions of community detection, including Louvain, Girvan-Newman, and etc, we are also explring the solutions with neural networks. For this project, we explore the community detection solutions with machine learning, deep learning in particular. We specifically explore the performance of neural networks on task of community detection by implementing and training different neural networks, including Multiple Layers Perceptrons and Graph Neural Networks, to test whether neural networks can be a solution for community detection.

This repository contains all code for all findings and attempt related to this project.

### Files
* `checkpoints` contains best models' stats in format of PyTorch's `.pt`.
* `config` contains parameters used for models.
* `notebooks` contains notebooks which illustrates data analysis, the result,  and training process.
* `outputs` contains the training plots including loss and score plots of models.
* `references` contains all reference.
* `src` contains all source code used for data analysis, models, and training. 
    * `data` contains source code used for generate random and test data, data analysis, loading data for models, and some code for read specific format of data.
    * `features` contains code for feature engineering.
    * `models` contains the code for models, algorithms, and training.
* `test` contains the test data for `run.py`. Specifically, the test data are stored in `/test/testdata/`.
* `requiremetnts.txt` speficy the requirements of running this project.
* `run.py` can run a simple test for this project.
* `submission.json` contains information of Docker image for this project.

### Requirements
`submission.json` contains the Docker image which have all packages needed. Meanwhile, the specific requirements are in `requirements.txt`. The Docker image contains all needed environment exclude `torch` and `torch_geometric`. Specifically, since `torch` and `torch_geometric` requires specific version according to the device, CUDA version, we choose to leave them. Therefore, to reproduce our results, `torch` and `torch_geometric` needed to be installed correctly according to CUDA version or CPU only version. The details of installing `torch` and `torch_geometric` can be found in https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html and https://pytorch.org/get-started/locally/ .

### Run
To run the project, we left the test with `run.py`. However, since this project is  more about to explore the solutions for community detection, the content is relatively mass. It is really difficult to re-run all analysis, model training, and algorithms implemented in a short period of time. Therefore, in `test` of `run.py`, it will run our naive traditional community detection algorithm which depends on the number of common neighbors on the test dataset. It will just make sure the graph/network enviroment has been set correctly with test data. In addition, since the entire environment of the running models of Graph Neural Network depends on the hardware environment. Specifically, since the training process requires to specify the GPU/CPU, it must corporate with the correct version of PyTorch, `torch`, and `torch_geometric` which need to specify whether use CPU only or specific CUDA version. Since the device run these code might have different hardware environment, we leave this part free to change. However, all training results and process are reproducible in the notebooks and code.

Instead of presenting our results and code in `run.py`, we choose notebooks to show the results and process. Specifically `/notebooks` folder contains all attempts, models, and results we did, built, and ran. 

### Website

The project [website](https://hblyx.github.io/CommunityDetection/) and its source code is under the [gh-pages branch](https://github.com/hblyx/CommunityDetection/tree/gh-pages) of the same repository.
