from serveitlearn.decorator import app, initalize, predict
import pickle
import spacy
from joblib import  load

clf = None
nlp = None


def argmax(array):
      return array.index(max(array))

@initalize
def import_model():
    global clf, nlp
    clf = load('models/random_forest_clf.pkl')
    nlp = spacy.load('nl_core_news_lg') 


@predict
def predict(query):
    if 'text' in query:
        print(query)
        text = query['text']
        doc = nlp(text)

        validation_data = [(token.text, token.vector) for token in doc if token.pos_ == "NOUN"]

        if len(validation_data) > 0:

            word_list   = [v[0] for v in validation_data]

            vector_list = [v[1] for v in validation_data]


            # make prediction with pure-predict object
            predictions = clf.predict_proba(vector_list)

            json_result_list = []
            prediction_text = ['de','het']
            for prediction, word in zip(predictions,word_list):
                json_result = {}
                json_result['woord'] = word
                highest_proba_index = argmax(prediction)
                highest_proba = prediction[highest_proba_index]
                highest_proba_name = prediction_text[highest_proba_index]
                json_result['predicition'] = {highest_proba_name : highest_proba }
                json_result_list.append(json_result)
                result =  {'msg':'success', 'predictions' : json_result_list }
        else:
            result =  {'msg':'fail','detail': 'Cannot find any Nouns in the given sentence(s)'}
        return result

