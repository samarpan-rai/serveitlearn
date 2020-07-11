## Introduction

You may train the most awesome model in the world but if you can't deploy it then people can enjoy your work. Deoployment in ML has always been an issue that we never gets discussed in courses. It is assumed that you can just do this without any training. However, in my experience, I found it not as easy to deploy my models with much flexibility. That's why I decided to create `serve-it-learn`. The idea for the name purely from  [Vincent D. Warmerdam's brain fart](https://twitter.com/fishnets88/status/1279731745483624453). 


## Installation

I prefer conda but you do you. You need at least python 3.7

1. Create environment (if you don't already have one)
    `conda create -n serve_scikit_model python=3.7`

2. Activate it
    `conda activate serve_scikit_model`

3. Install it
    `pip install serveitlearn`



## Getting started

This is a dummy example. You need to add your own code to load the model and perform predictions. 


```py

from serveitlearn.decorator import app, predict, initalize

# Declare function that initalizes the model and any other data sources
@initalize
def my_initalization():
    pass

# Declare function that will make the prediction based on the query

@predict
def my_prediction(query_dict):
    pass
```

If you want to see a full example, then you can try running [this](https://github.com/samarpan-rai/serveitlearn/blob/master/examples/svc_iris_example.py). Please note that it has few requirements. You can install it by running `pip install -r https://github.com/samarpan-rai/serveitlearn/blob/master/examples/requirements.txt`


