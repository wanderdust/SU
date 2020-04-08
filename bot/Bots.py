import json
import sys
import random
from Bot_Requests import Bot_Requests
from Speech_Handlers import Speech_Handlers
from Utils import Utils

class Bots:
    def __init__(self):
        self.bot_requests = Bot_Requests()
        self.speech = Speech_Handlers()
        self.utils = Utils()

    def conversation_alana (self, initial_utterance="Hello"):
        """
        Start a conversation with Alana in a loop.
        """
        print("Your sentence is complete! Redirecting to Alana!")
        print("Say 'Stop' to exit\n")

        alana_init = self.bot_requests.request_alana(initial_utterance)
        self.speech.tts(alana_init)   

        while True:
            utterance = self.speech.asr()

            if utterance == False or utterance.lower() == "stop":
                break
            alana_response =  self.bot_requests.request_alana(utterance)
            print(alana_response)
            self.speech.tts(alana_response)

    def conversation_rasa (self, initial_utterance, toggle):
        """
        Start a conversation with Rasa in a loop:
            1. Sends request to rasa from user's input
            2. Listen from user's input to choose an option
            3. Identify what object the user has selected (TV, Heating...)
            4. Send the command to the interface
        """
        print("Sentence is incomplete. Redirecting to our bot!\n")
            
        # 1. send request to rasa here with initial utterance
        rasa_outptut = self.bot_requests.request_rasa(initial_utterance)

        # If rasa's response is empty, end conversation.
        if rasa_outptut == False:
            self.speech.tts("Sorry I didn't get that") # text to speech "Sorry I didn't get that"
            return

        # 2. Gives the user 2 chances to give a utterance
        for i in range(2):
            self.speech.tts(rasa_outptut) # text to speech of Rasa's output. Eg. "Do you mean lights? Do you mean heating?""

            user_utterance = self.speech.asr() # Listen to user's new input

            if user_utterance == False:
                # user_Utterance is not recognised by tts. ASR returns false.
                self.speech.tts("Sorry I didn't get that")
            elif self.utils.find_item(user_utterance, rasa_outptut) == None:
                # Item specified by user is not found in known items.eg. "Turn on the kettle"
                self.speech.tts("Sorry I couldn't find that device")
            elif user_utterance:
                # If user_utterance is recognised, exit the loop.
                break
            else:
                # If user_utterance not recognised.
                self.speech.tts("Sorry I didn't get that.")
            
            # After two iterations, if communication fails, shut down.
            if i == 1:
                self.speech.tts("Okay, bye")
                sys.exit()
        
        # Make it lowercase to avoid uppercase inconsistencies
        user_utterance_lower = user_utterance.lower()

        # 3. Find what item the user said (eg. Heating, music, etc)
        item = self.utils.find_item(user_utterance_lower, rasa_outptut)

        # 4. Sending the request to the interface
        rasa_final_output = self.bot_requests.request_rasa(user_utterance)
        
        try:
            self.speech.tts(rasa_final_output)
        except:
            self.speech.tts("Okay")
        print(item + " ********** "+toggle)
        command = {"object": item, "toggle": toggle}
        self.bot_requests.request_interface(command)