import requests
import random
import json

class Bot_Requests:
    def __init__(self):
        pass
    
    def request_alana(self, utterance):
        """
        Requests for get an answer from Alana
        """

        data = {
            'user_id': 'test-user',
            'question': utterance,
            'session_id': '123456789',
            'projectId': 'CA2020',
            'overrides': {
                        'BOT_LIST': ['coherence_bot',
                        'news_bot_v2', 'wiki_bot_mongo'],
                        'PRIORITY_BOTS': [['news_bot_v2', 'wiki_bot_mongo'], 'coherence_bot']
                        }
                }

        r= requests.post(url='http://52.56.181.83:5000', json=data)
        response = r.json()


        return response['result']

    def request_rasa (self, utterance):
        """
        Request for an answer from Rasa
        """

        url = "http://localhost:5005/webhooks/rest/webhook"
        data = {"message": utterance}
        json_data = json.dumps(data)

        r = requests.post(url, data = json_data)
        text = ""
        try: 
            text = json.loads(r.text)[0]["text"]
        except:
            text = False
        return text

    def request_interface (self, command):
        """
        Sends a request to the interface to turn on/off something
        """
        url = "http://localhost:3000/webapp/api"
        json_data = json.dumps(command)
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, data = json_data, headers=headers)