import requests
import json
import random

def request_interface (command):
    url = "http://localhost:3000/webapp/api"
    json_data = json.dumps(command)
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data = json_data, headers=headers)


def request_su (utterance):
    """
    HOw to use rasa:
        - rasa run actions -v
        - rasa run
    """
    rand = random.randint(0,9)

    url = "http://localhost:5005/webhooks/rest/webhook"
    data = {"sender": str(rand), "message": utterance}
    json_data = json.dumps(data)

    r = requests.post(url, data = json_data)
    text = ""
    try: 
        text = json.loads(r.text)[1]["text"]
    except:
        text = False
    return text