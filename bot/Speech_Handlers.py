import speech_recognition as sr
import os
from gtts import gTTS
from abc import ABC, abstractmethod

class Speech_Handlers:

    def __init__(self):
        pass

    def asr(self):
        """
        Automatic Speech Recognition:
            Listens to the user and returns text.
            * If utterance is understood, returns utterance
            * If there is an error, returns Boolean False
        """
        r = sr.Recognizer()

        mic = sr.Microphone()

        with mic as source:
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = False
            print("Microphone Listening")

            try:
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
            except:
                user_input = False

            print("Interpreting... ")

            try:
                user_input = r.recognize_google(audio)

            except:
                user_input = False
        return user_input

    def tts(self, utterance):
        """
        Text to speech. 
            Takes some text and converts it to speech.
        """
        language = "en"
        myobj = gTTS(text=utterance, lang=language, slow=False)
        myobj.save("audio/text.mp3") 
        os.system("mpg123 audio/text.mp3")