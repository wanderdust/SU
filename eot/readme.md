# Install requirements.txt

`pip install -r requirements.txt`

If you have any problems with the library pyaudio, used for speech recognition, try to run:

`conda install nwani::portaudio nwani::pyaudio`

If you have any problems with `mpg123 not found` make sure you have installed that library. This library is used to play .mp3 files from the os. In linux: `sudo apt-get install mpg123` or `sudo apt-get install mpg321`.


## Start the server

```
./start.sh
```

## Use requests to send a request

It returns a tuple with three elements:

    1. Prediction as an integer (0 incomplete, 1 complete)
    2. Prediction as string ("complete" or "incomplete")
    3. Level of confidence for the prediction (as a percentage)


Example found in `bot/main.py`
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