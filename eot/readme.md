# Install requirements.txt

`pip install -r requirements.txt`

(Optional) If you have any problems while installing the library pyaudio, used for speech recognition, try to run:

`conda install nwani::portaudio nwani::pyaudio`

If you have any problems with `mpg123 not found` make sure you have installed that library. This library is used to play .mp3 files from the os. In linux: `sudo apt-get install mpg123` or `sudo apt-get install mpg321`.


## Start the server

```
./start.sh
```
_____________

**Only follow the instructions below if you want to test the API. Otherwise **IGNORE**.**

## Use requests to send a request

It returns a tuple with three elements:

`(pred_int, pred_string, confidence)`

    1. Prediction as an integer (0 incomplete, 1 complete)
    2. Prediction as string ("complete" or "incomplete")
    3. Level of confidence for the prediction. Closer to 0 is incomplete. Closer to 1 is complete.


How to make a request to the API.
```
import requests

utterance = "Turn the "

r = requests.post(
    "http://127.0.0.1:5000/api/predict/",
    data= utterance ).json()

print(r['pred_int'])
print(r['pred_str'])
print(r['confidence'])

# output
>>> 0.0
>>> incomplete
>>> 2.0784675143659115e-05
```