import requests
import json
import random

# Request to rasa bot (su)
def request_su (utterance):
    """
    HOw to use rasa:
        - rasa run actions -v
        - rasa run
    """
    rand = random.randint(0,100000)

    url = "http://localhost:5005/webhooks/rest/webhook"
    data = {"sender": "user", "message": utterance}
    json_data = json.dumps(data)

    r = requests.post(url, data = json_data)
    text = ""

    try: 
        text = json.loads(r.text)[0]["text"]
    except:
        text = False
    return text

# Request to the interface to turn on/off lights/heating/tv/music
def request_interface (command):
    url = "http://localhost:3000/webapp/api"
    json_data = json.dumps(command)
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data = json_data, headers=headers)