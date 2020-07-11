import pandas as pd
import numpy as np
import json
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from joblib import dump, load
from serveitlearn.decorator import app, initalize, predict

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

# Initalize model
clf = SVC(probability=True)
clf.fit(iris.data, iris.target)

# Please note that there are security issues with such pickling https://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations. I wouldn't recommend this during production 
dump(clf, 'iris_svc_model.joblib') 

# Delete the clf and load it from the disk during initalizaion
del clf

### Important 
 
# You need to have some sort of global object that can be used to do inferences. In this example, I am making a simple global object
model = None

@initalize
def my_initalization():
    # Initailze your model
    global model
    
    model = load("iris_svc_model.joblib")

    print("My model initalized")
    


# For this example, I will assume that the request will have the format as below in the POST request's body
# 
# ```
#     {
#         'plant_dimensions' : [[1,2,3,4],[5,6,7,8]]
#     }
# ```


@predict
def my_prediction(query_dict):
    global model
    if 'plant_dimensions' in query_dict:
        # Extract query from dictionary
        plant_dimensions = query_dict['plant_dimensions']
        
        # Make prediction if it's a list
        if isinstance(plant_dimensions, list):
            # COnvert to np array 
            plant_dimensions = np.array(plant_dimensions)
            print(plant_dimensions)
            if plant_dimensions.shape[0] == 1: # If there is only one sample then reshape it
                plant_dimensions = plant_dimensions.reshape(1, -1)
            
            print(plant_dimensions) 
            predictions = model.predict_proba(plant_dimensions)
            
            
            prediction_classes = ['setosa', 'versicolor', 'virginica']
            json_result_list= []
            for prediction, plant_dimension in zip(predictions,plant_dimensions):
                
                json_result = {}
                highest_proba_index = np.argmax(prediction)
                highest_proba = prediction[highest_proba_index]
                highest_proba_name = prediction_classes[highest_proba_index]
                json_result['predicition'] = {
                    'given_plant_array' : plant_dimension.tolist(),
                    highest_proba_name : highest_proba
                    
                    }
                json_result_list.append(json_result)
            print(json_result_list)
            return {'msg':'success', 'predictions' : json_result_list }
            


    


