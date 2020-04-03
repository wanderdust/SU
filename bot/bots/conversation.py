import json
import sys
from bots.alana import request_alana
from bots.su import request_interface, request_su
from speech_handlers.asr import asr
from speech_handlers.tts import tts
from utils.find_item import find_item

# Loop that keeps the conversation going with alana.
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

# Loop that keeps the conversation going with rasa.
def conversation_rasa (initial_utterance, toggle):
    print("Sentence is incomplete. Redirecting to our bot!\n")
        
    # 1. send request to rasa here with initial utterance
    # 1b. Get rasa's response
    text = request_su(initial_utterance)

    # If rasa's response is empty, end conversation.
    if text == False:
        tts("Sorry I didn't get that") # Text to speech "Sorry I didn't get that"
        return

    # Gives the user 2 chances to give a utterance
    for i in range(2):
        tts(text) # Text to speech of Rasa's output. Eg. "Do you mean lights? Do you mean heating?""
        print(text)

        utterance = asr() # Listen to users new input

        if utterance == False:
            tts("Sorry I didn't get that")
        elif find_item(utterance) == None:
            tts("Sorry I didn't get that")
        elif utterance:
            break
        else:
            tts("Sorry I didn't get that")
        
        if i == 1:
            tts("Okay, bye")
            sys.exit()
            
    utterance_lower = utterance.lower() # Make it lowercase to avoid uppercase inconsistencies

    # PRovisional. Find what item the user said (eg. Heating, music, etc)
    item = find_item(utterance_lower, text)

    # 2. Send our response
    # 2b. Send utterance to alana
    print("Okay, turning {} {}".format(item, toggle))
    
    try:
        tts("Okay, turning {} {}".format(item, toggle))
    except:
        tts("Okay")

    command = {"object": item, "toggle": toggle}
    request_interface(command)