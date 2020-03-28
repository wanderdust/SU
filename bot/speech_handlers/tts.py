from gtts import gTTS
import os

# Text to speech
def tts(utterance, empty=False):
    if empty:
        os.system("mpg123 audio/sorry.mp3")

    language = "en"
    myobj = gTTS(text=utterance, lang=language, slow=False)
    myobj.save("audio/text.mp3") 
    os.system("mpg123 audio/text.mp3")
