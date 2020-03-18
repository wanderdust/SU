from gtts import gTTS
import os

def tts(utterance):
    language = "en"
    myobj = gTTS(text=utterance, lang=language, slow=False)
    myobj.save("audio/text.mp3") 
    os.system("mpg123 audio/text.mp3")
