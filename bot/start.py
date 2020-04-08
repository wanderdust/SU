from Conversation_Manager import Conversation_Manager
from Speech_Handlers import Speech_Handlers

class Start:
    def __init__(self):
        self.manager = Conversation_Manager()
        self.speech = Speech_Handlers

    def start(self):
        #utterance = self.start_utterance()
        utterance = "Can you turn on the"
        self.manager.redirect(utterance)

    def start_utterance(self):
        return self.speech.asr(" ")

bot = Start()
bot.start()
