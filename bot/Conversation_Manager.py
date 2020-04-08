import requests
from Utils import Utils
from Bots import Bots
from Speech_Handlers import Speech_Handlers


class Conversation_Manager:
    def __init__(self):
        self.bots = Bots()
        self.speech = Speech_Handlers()
        self.utils = Utils()
    
    def redirect (self, utterance):
        """
        Check if utterance is complete or incomplete and re-direct it.
        """
        # This handles error in case of timeout in the ASR when utterance is emtpy.
        if utterance == False:
            self.speech.tts("Sorry I didn't hear you. Bye!")
            return

        toggle = self.utils.find_toggle(utterance) # Catches the intent "on" or "off"

        response = requests.post(
            "http://127.0.0.1:5000/api/predict/",
            data= utterance )

        if response.status_code == 200:
            # Response from LSTM
            #   response.json()['pred_int'] == 0 --> incomplete
            #   response.json()['pred_int] == 1 --> complete

            if response.json()['pred_int'] == 0:
                # Redirect to our bot HERE!
                self.bots.conversation_rasa(utterance, toggle)
            else:
                # if response is 1 it is complete. Redirect to Alana.
                self.bots.conversation_alana(utterance)
        else:
            # Response from the script if lstm fails
            bot = self.utils.check(utterance, toggle)

            if bot == "rasa":
                self.bots.conversation_rasa(utterance, toggle)
            else:
                self.bots.conversation_alana(utterance)

        