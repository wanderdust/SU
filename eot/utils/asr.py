import speech_recognition as sr

def asr():

    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
    
        print("Microphone Listening")

        audio = r.listen(source)

        print("Interpreting... ")

        try:
            user_input = r.recognize_google(audio)
        except:
            user_input = None
            print("I didn't get that")
    return user_input    
    