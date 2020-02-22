# Using the API

Use main.py for instructions on how to use.

## Start the server

```
./start.sh
```

## Use requests to send a request

It returns a tuple with three elements:

    1. Prediction as an integer (0 incomplete, 1 complete)
    2. Prediction as string ("complete" or "incomplete")
    3. Level of confidence for the prediction (as a percentage)


Run the code
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