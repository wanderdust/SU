"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""
import requests
from utils.redirect import check

utterance = "Can you please turn the "

def redirect (utterance):

    response = requests.post(
        "http://127.0.0.1:5000/api/predict/",
        data= utterance )

    if response.status_code == 200:
        # Response from LSTM
        print(response.json()['pred_int'])
        print(response.json()['pred_str'])
        print(response.json()['confidence'])

        if response.json()['pred_int'] == 0:
            print("Sentence is incomplete. Redirecting to our bot!")
        else:
            print("Sentence is complete. Redirecting to Alana")
    else:
        # Response from the script if lstm fails
        check(utterance)

# Run the script to for testing it
redirect(utterance)