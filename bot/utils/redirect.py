from bots.alana import request_alana
from bots.conversation import conversation, conversation_rasa

def check(utterance, toggle):
    utt_list = utterance.split()
    res = len(utt_list) 
    word = utt_list[-1]

    # According to the Split utterance research paper these are the most commun split points in a dialogue:
    antecedents = ['and','but','or','so','is','are','because','the','a','my','your'] 

    if word in antecedents:
        #redirect to our utterence completion bot
        conversation_rasa(utterance, toggle)
        
    else:
        conversation(utterance)