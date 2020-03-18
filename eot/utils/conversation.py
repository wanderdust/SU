from utils.alana import request_alana
from utils.su import request_interface, request_su
import json
from utils.asr import asr
from utils.tts import tts

# Loop that keeps the conversation going.
def conversation (initial_utterance="Hello"):
    print("Your sentence is complete! Redirecting to Alana!")
    print("Say 'Stop' to exit\n")

    alana_init = request_alana(initial_utterance)
    tts(alana_init)
    
    print(alana_init)    

    while True:
        utterance = asr()

        if utterance.lower() == "stop":
            print("Bye!")
            break
        alana_response = request_alana(utterance)
        print(alana_response)
        tts(alana_response)


def conversation_rasa (initial_utterance):
    print("Sentence is incomplete. Redirecting to our bot!\n")

    # 1. send request to alana here with initial utterance
    # 1b. Get alana's response
    text = request_su(initial_utterance)
    tts(text)

    if text == None:
        print("Sorry I didn't get that ")
        return

    print(text)
    utterance = asr()

    # 2. Send our response
    # 2b. Send utterance to alana
    print("Okay, turning {} {}".format(utterance[0], utterance[1]))
    command = {"object": utterance[0], "toggle": utterance[1]}
    request_interface(command)