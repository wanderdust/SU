# -*- coding: utf-8 -*-
"""
@author: AG
"""

import speech_recognition as s_r
 
 
 
def main():
 
    f = s_r.Recognizer()
 
    with s_r.Microphone() as source:
        f.adjust_for_ambient_noise(source)
 
        print("Microphone Listening")
        
        audio = f.listen(source)
 
        print("Interpreting... ")
 
    
 
        try:
            print("=> " + f.recognize_google(audio))
            print(" \n Success (?) \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
 
        with open("Mic_Record", "wb") as r:
            r.write(audio.get_wav_data())


if __name__ == "__main__":
    main()