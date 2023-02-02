# DSC180 Project 2 - Community Detection with Machine Learning
## Explore Community Detection with Machine Learning
#### Yaoxin Li, Justin Nguyen, Vivek Rayalu

### Introduction
For this project, we explore the community detection solutions with machine learning, deep learning in particular. 

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
`submission.json` contains the Docker image which have all packages needed. Meanwhile, the specific requirements are in `requirements.txt`.

### Run
To run the project, we left the test with `run.py`. However, since this project is  more about to explore the solutions for community detection, the content is relatively mass. It is really difficult to re-run all analysis, model training, and algorithms implemented in a short period of time. Therefore, in `test` of `run.py`, it will run our naive traditional community detection algorithm which depends on the number of common neighbors on the test dataset. It will make sure the graph related things can successful run.

Instead of letting our result and presenting our result in `run.py`, we choose notebooks to show the results and process. Specifically `/notebooks` folder contains all attempts and models we build and run. 