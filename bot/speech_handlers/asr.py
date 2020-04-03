import speech_recognition as sr

# Automatic speech recognition
def asr(debug=False):

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

            if debug:
                print("You said: " + user_input)
        except:
            user_input = False
    return user_input    
    