import speech_recognition as sr

def asr():

    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = False
        print("Microphone Listening")

        audio = r.listen(source, timeout=1, phrase_time_limit=5)

        print("Interpreting... ")

        try:
            user_input = r.recognize_google(audio)
        except:
            user_input = False
            print("I didn't get that")
    return user_input    
    