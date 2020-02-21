from preprocessing import Preprocessing
from predict import Predict

utterance = "volume up please"

predict = Predict()
print(predict.predict(utterance))