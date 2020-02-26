"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""
import requests
from utils.redirect import check
from utils.alana import request_alana

utterance = "Can you please turn the "

def redirect (utterance):

    response = requests.post(
        "http://127.0.0.1:5000/api/predict/",
        data= utterance )

    if response.status_code == 200:
        # Response from LSTM
        #   response.json()['pred_int'] == 0 --> incomplete
        #   response.json()['pred_int] == 1 --> complete

        if response.json()['pred_int'] == 0:
            print("Sentence is incomplete. Redirecting to our bot!\n")
            # Redirect to our bot HERE!
        else:
            print("Sentence is complete. Redirecting to Alana\n")
            alana_response = request_alana(utterance)
    else:
        # Response from the script if lstm fails
        check(utterance)

# Run the script to for testing it
redirect(utterance)
