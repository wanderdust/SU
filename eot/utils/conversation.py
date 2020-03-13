from utils.alana import request_alana
from utils.su import request_su
import json

# Loop that keeps the conversation going.
def conversation (initial_utterance="Hello"):
    print("Your sentence is complete! Redirecting to Alana!")
    print("Say 'Stop' to exit\n")

    request_alana(initial_utterance)
    
    while True:
        utterance = input(">> ")

        if utterance.lower() == "stop":
            print("Bye!")
            break
        alana_response = request_alana(utterance)


def conversation_rasa (initial_utterance):
    print("Sentence is incomplete. Redirecting to our bot!\n")

    # 1. send request to alana here with initial utterance
    # 1b. Get alana's response
    print("Did you mean lights? or heating? or tv? or music?\n")
    utterance = input(">> Enter your response as '[object] [status]. Example: lights on': ").split(" ")

    # 2. Send our response
    # 2b. Send utterance to alana
    print("Okay, turning {} {}".format(utterance[0], utterance[1]))
    command = {"object": utterance[0], "toggle": utterance[1]}
    request_su(command)