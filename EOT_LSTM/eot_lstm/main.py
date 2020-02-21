"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""
import requests

utterance = "Turn the "

r = requests.post(
    "http://127.0.0.1:5000/api/predict/",
    data= utterance ).json()

print(r['pred_str'])