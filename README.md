## Introduction

This project is inspired by  [Vincent D. Warmerdam's brain fart](https://twitter.com/fishnets88/status/1279731745483624453). 

You may train the most awesome model in the world but if you can't deploy it then people can't enjoy your work. Deployment in ML has always been an issue that gets least discussed during classes. It is assumed that you can just do this without any formal training. In my experience, it not as easy to deploy models that's why I thought it woulbe be great to create `serveitlearn`. It creates an extremely thin layer around FastAPI library which allows you to create an end point super fast.  More specifically, It provides `/predict` end point. You can only send POST request with JSON body. The following code sample will make it clear. 

### Code sample : 

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

## Installation

You need at least python 3.7. I will use conda for this 

1. Create environment (if you don't already have one)
    `conda create -n serveitlearn_env python=3.7`

2. Activate it
    `conda activate serveitlearn_env`

3. Install it
    `pip install serveitlearn`


## Hello World!


The example, loads iris dataset, trains a simple SVC model and deploys it using `serveitlearn`.


```
$ git clone https://github.com/samarpan-rai/serveitlearn

$ cd serveitlearn/examples/

$ pip install -r requirements.txt

$ uvicorn svc_iris_example:app --reload

$ curl --location --request POST 'localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"plant_dimensions" : [[5.1,3.5,1.4,0.2],[5.1,3.5,1.4,0.2]]}'
```

 Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to 


## Limitations

1. No authentication or security measures implemented. 
2. The documentation could be better.

