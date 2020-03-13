"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""
import requests
from utils.redirect import check
from utils.alana import request_alana
from utils.conversation import conversation, conversation_rasa


utterance = input(">> Enter your utterance: ")

def redirect (utterance):

    response = requests.post(
        "http://127.0.0.1:5000/api/predict/",
        data= utterance )
    print(response.status_code)
    if response.status_code == 200:
        # Response from LSTM
        #   response.json()['pred_int'] == 0 --> incomplete
        #   response.json()['pred_int] == 1 --> complete

        if response.json()['pred_int'] == 0:
            # Redirect to our bot HERE!
            conversation_rasa(utterance)
        else:
            conversation(utterance)
    else:
        # Response from the script if lstm fails
        check(utterance)

# Run the script to for testing
redirect(utterance)
