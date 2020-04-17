from Conversation_Manager import Conversation_Manager
from Speech_Handlers import Speech_Handlers

class Start:
    def __init__(self):
        self.manager = Conversation_Manager()
        self.speech = Speech_Handlers
        self.start_files()

    def start(self):
        utterance = self.start_utterance()
        self.manager.redirect(utterance)

    def start_utterance(self):
        return self.speech.asr(" ")

    def start_files(self):
        f = open("furhat.txt", "w+")
        f.close()
        f = open("resp.txt", "w+")
        f.close() 

print("Starting start.py")
bot = Start()
bot.start()
