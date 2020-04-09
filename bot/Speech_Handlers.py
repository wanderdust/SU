import os

class Speech_Handlers:

    def __init__(self):
        pass

    def asr(self):
        user_input = input(">> Your utterance:\n")

        if user_input.strip() == "":
            return False

        return user_input

    def tts(self, utterance):
        print(utterance)