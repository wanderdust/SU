from utils.alana import request_alana

def check(utterance):
    utt_list = utterance.split()
    res = len(utt_list) 
    word = utt_list[-1]

    # According to the Split utterance research paper these are the most commun split points in a dialogue:
    antecedents = ['and','but','or','so','is','are','because','the','a','my','your'] 

    if word in antecedents:
        print("Your sentence is incomplete. Redirecting to our bot!\n")
        #redirect to our utterence completion bot
    else:
        print("Your sentence is complete! Redirecting to Alana\n")
        alana_response = request_alana(utterance)
