import os
import socket
import time

class Speech_Handlers:

    def __init__(self):

        pass

    def asr(self):
        #data = 'asr - get speech data'
        #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.connect(('localhost', 9999))
        #client.send(data.encode())
        #user_input = client.recv(4096)
        #user_input = (user_input.decode('utf-8'))
        #client.close()


        f = open("furhat.txt", "r")

        user_input = str(f.read())

        #user_input = input(">> Your utterance:\n")

        #if user_input.strip() == "":
        #    return False

        while not user_input:
            f = open("furhat.txt", "r")

            user_input = str(f.read())

        print (user_input)
        f = open("furhat.txt", "w")
        f.write("")
        f.close()
        return user_input


    def tts(self, utterance):
        #utterance = "from the bot+"+utterance
        #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.connect(('localhost', 9999))
        #client.send(utterance.encode())

        #client.close()
        f = open("furhat.txt", "w")
        f.write(utterance)
        f.close()

        f = open("resp.txt", "w")
        f.write(utterance)
        f.close()
        time.sleep(10)
