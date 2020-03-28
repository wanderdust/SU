from bots.alana import request_alana
from bots.su import request_interface, request_su
import json
from speech_handlers.asr import asr
from speech_handlers.tts import tts

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
def conversation_rasa (initial_utterance):
    print("Sentence is incomplete. Redirecting to our bot!\n")
        
    # 1. send request to alana here with initial utterance
    # 1b. Get alana's response
    text = request_su(initial_utterance)

    if text == False:
        tts(None, empty=True)
        return

    tts(text)
    print(text)
    utterance = asr()

    # 2. Send our response
    # 2b. Send utterance to alana
    utt_split = utterance.split(" ")
    print("Okay, turning {} {}".format(utt_split[0], utt_split[1]))
    
    try:
        tts("Okay, turning {} {}".format(utt_split[0], utt_split[1]))
    except:
        tts("Okay")

    command = {"object": utt_split[0], "toggle": utt_split[1]}
    request_interface(command)