"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""
import requests
from utils.redirect import check
from utils.find_toggle import find_toggle
from bots.alana import request_alana
from bots.conversation import conversation, conversation_rasa
from speech_handlers.asr import asr
from speech_handlers.tts import tts


utterance = asr(debug=True)

def redirect (utterance):
    # This handles error in case of timeout in the ASR
    if utterance == False:
        tts("Sorry I didn't hear you. Bye!")
        return

    toggle = find_toggle(utterance) # Catches the intent "on" or "off"

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
            conversation_rasa(utterance, toggle)
        else:
            # if response is 1 it is complete. Redirect to Alana.
            conversation(utterance)
    else:
        # Response from the script if lstm fails
        check(utterance, toggle)

# Run the script to for testing
redirect(utterance)
