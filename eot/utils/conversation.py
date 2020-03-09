from utils.alana import request_alana

# Loop that keeps the conversation going.
def conversation (initial_utterance="Hello"):
    print("Your sentence is complete! Redirecting to Alana!")
    print("Say 'Stop' to exit\n")

    request_alana(initial_utterance)
    
    while True:
        utterance = input(">> ")

        if utterance.lower() == "stop":
            print("Bye!")
            break
        alana_response = request_alana(utterance)