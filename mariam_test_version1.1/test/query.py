import requests
import json

utterance = input(">> Enter your utterance: ")
url = "http://localhost:5005/webhooks/rest/webhook"
data = {"sender": "Rasa1", "message": utterance}
json_data = json.dumps(data)

r = requests.post(url, data = json_data)

print(r)
print(r.text)