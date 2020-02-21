from model import SentimentRNN

class Predict:
    def __init__(self):
        self.prediction = ""

        # Instantiate the model w/ hyperparams
        vocab_size = len(vocab_to_int)+1 # +1 for the 0 padding + our word tokens
        self.output_size = 1
        self.embedding_dim = 400
        self.hidden_dim = 256
        self.n_layers = 2

        self.net = SentimentRNN(self.vocab_size, output_size, embedding_dim, hidden_dim, self.n_layers)

    def predict(test_review, sequence_length=10):
        
        self.net.eval()
        
        # tokenize review
        test_ints = tokenize_review(test_review)
        
        # pad tokenized sequence
        seq_length=sequence_length
        features = pad_features(test_ints, seq_length)
        
        # convert to tensor to pass into your model
        feature_tensor = torch.from_numpy(features)
        
        batch_size = feature_tensor.size(0)
        
        # initialize hidden state
        h = self.net.init_hidden(batch_size)
        
        if(train_on_gpu):
            feature_tensor = feature_tensor.cuda()
        
        # get the output from the model
        output, h = self.net(feature_tensor, h)
        
        # convert output probabilities to predicted class (0 or 1)
        pred = torch.round(output.squeeze()) 
        # printing output value, before rounding
        print('Prediction value, pre-rounding: {:.6f}'.format(output.item()))
        print(pred.item())
        # print custom response
        if(pred.item()==1):
            #print("Complete sentence")
            self.prediction = "complete"
        else:
            #print("Icomplete sentence") 
            self.prediction = "incomplete"  

    def load_net_weights (self):
        pass
