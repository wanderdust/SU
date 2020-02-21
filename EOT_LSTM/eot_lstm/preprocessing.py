from string import punctuation
import json

class Preprocessing:
    def __init__(self):

        with open('utils/vocab_to_int.json', 'r') as file:
            data = file.read()

        self.vocab_to_int = json.loads(data)

    def tokenize_review(self, utterance):
        utterance = utterance.lower() # lowercase
        # get rid of punctuation
        utterance = ''.join([c for c in utterance if c not in punctuation])

        # splitting by spaces
        test_words = utterance.split()

        # tokens
        test_ints = []
        test_ints.append([self.vocab_to_int[word] for word in test_words])

        return test_ints