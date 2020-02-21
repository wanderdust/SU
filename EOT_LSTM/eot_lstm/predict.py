from model import SentimentRNN
from preprocessing import Preprocessing
import numpy as np
import torch

class Predict:
    def __init__(self):
        self.prediction = ""

        self.preprocessing = Preprocessing()
        # Instantiate the model w/ hyperparams
        self.vocab_size = len(self.preprocessing.get_vocab())+1 # +1 for the 0 padding + our word tokens
        self.output_size = 1
        self.embedding_dim = 400
        self.hidden_dim = 256
        self.n_layers = 2

        self.net = SentimentRNN(
            self.vocab_size, self.output_size,
            self.embedding_dim, self.hidden_dim, self.n_layers)

        self.load_net_weights("models/RNN_EOT.pth")


    def predict(self, test_review, sequence_length=10):
        
        self.net.eval()
        
        # tokenize review
        test_ints = self.preprocessing.tokenize_review(test_review)
        
        # pad tokenized sequence
        features = self.preprocessing.pad_features(test_ints, sequence_length)
        
        # convert to tensor to pass into your model
        feature_tensor = torch.from_numpy(features)
        
        batch_size = feature_tensor.size(0)
        
        # initialize hidden state
        h = self.net.init_hidden(batch_size)
        
        #if(train_on_gpu):
        #    feature_tensor = feature_tensor.cuda()
        
        # get the output from the model
        output, h = self.net(feature_tensor, h)
        
        # convert output probabilities to predicted class (0 or 1)
        pred = torch.round(output.squeeze()) 
        # printing output value, before rounding
        confidence = output.item()

        print(pred.item())
        # print custom response
        if(pred.item()==1):
            #print("Complete sentence")
            self.prediction = "complete"
        else:
            #print("Icomplete sentence") 
            self.prediction = "incomplete"  

        """
        returns:
            the int prediction (1 complete, 0 incomplete)
            the string prediction
            the confidence of that prediction
        """
        return pred.item(), self.prediction, confidence

    def load_net_weights (self, path="models/RNN_EOT.pth"):
        self.net.load_state_dict(torch.load(path))
