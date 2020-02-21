from string import punctuation
import json
import numpy as np

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

    def pad_features(self, reviews_ints, seq_length = 10):
        ''' Return features of review_ints, where each review is padded with 0's 
            or truncated to the input seq_length.
        '''
        
        # getting the correct rows x cols shape
        features = np.zeros((len(reviews_ints), seq_length), dtype=int)

        # for each review, I grab that review and 
        for i, row in enumerate(reviews_ints):
            if len(row) > seq_length:
                row = row[-seq_length:]
            features[i, -len(row):] = np.array(row)[:seq_length]
        
        return features


    def get_vocab (self):
        return self.vocab_to_int