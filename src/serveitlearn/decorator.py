"""Main module."""
import functools
import json
from json.decoder import JSONDecodeError
from fastapi import FastAPI, Depends
import logging
from typing import Any, Dict
from urllib import parse


# initiate API

app = FastAPI()


# Initalize wrapper
def initalize(func):
    @app.on_event("startup")
    def startup_wrapper():
        func()
    return startup_wrapper

# Prediction wrapper
def predict(func):
    @app.post("/predict")
    def prediction_wrapper(request: Dict[Any, Any]):
        # Pipe the dict to the function
        value =  func(request)
        # Do something after
        return value
        
    return prediction_wrapper

