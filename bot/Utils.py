class Utils:
    def __init__(self):
        pass

    def find_toggle(self, utterance):
        """
        Finds the "on" or "off" within a sentence
        """
        toggle = "off" #default
        split_utterance = utterance.split(" ")

        if ("on" in split_utterance):
            toggle ="on"

        return toggle

    def find_item(self, utterance, rasa_output):
        """
        Finds the object the user wants to select
        """
        item = "" # This is the variable that will hold the item
        split_utterance = utterance.split(" ") # Split the user's input
        split_rasa_output = " ".join(rasa_output.lower().split("?")).split(" ") # Split Rasa's output

        items = [item for item in split_rasa_output if item == "music" 
               or item == "heating" or item == "tv" or item == "light"] # Identify the relevant items from Rasa's output]

        # Identifies the item to be chosen from the user input
        if ("music" in split_utterance):
            item = "music"
        elif ("tv" in split_utterance or "television" in split_utterance or "telly" in split_utterance):
            item = "tv"
        elif ("heating" in split_utterance):
            item = "heating"
        elif ("lights" in split_utterance or "light" in split_utterance):
            item = "lights"
        elif ("first" in split_utterance): 
            item = items[0]
        elif ("second" in split_utterance): 
            item = items[1]
        elif ("third" in split_utterance or "last" in split_utterance): 
            item = items[2]
        else:
            return None

        return item

    def check(self, utterance, toggle):
        utt_list = utterance.split()
        res = len(utt_list) 
        word = utt_list[-1]

        # According to the Split utterance research paper these are the most commun split points in a dialogue:
        antecedents = ['and','but','or','so','is','are','because','the','a','my','your'] 

        if word in antecedents:
            #redirect to our utterence completion bot
            return "rasa"
            
        else:
            return "alana"