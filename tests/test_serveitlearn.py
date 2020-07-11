from serveitlearn.decorator  import app, predict
from starlette.testclient import TestClient
import logging
import json


@predict
def pingpong(query_dict):
   """
   This function returns whatever is given
   """
   return query_dict


def test_ping_pong_right_data():
   """
   This test sends a json dictionary to ping
   """
   client = TestClient(app)
   data_dict =   {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
   data_json_string =  json.dumps( data_dict )
   response = client.post("/predict", data=data_json_string)
   recieved_data = json.loads( response.content )
   assert recieved_data  == data_dict


def test_ping_pong_wrong_data():
   client = TestClient(app)
   data_dict =   {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
   data_json_string =  json.dumps( data_dict )
   response = client.post("/predict", data=data_json_string)
   recieved_data = json.loads( response.content )
   assert recieved_data  != {'test':'test'}


