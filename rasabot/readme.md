## Start rasa server

```
# Use any model inside models. Example: 20200309-121538.tar.gz
rasa run -m models/{model_here.tar.gz} --enable-api --log-file out.log
```

## Send a request

```
import requests
import json

utterance = "Where is my"
url = "http://localhost:5005/webhooks/rest/webhook"
data = {"sender": "Rasa1", "message": utterance}
json_data = json.dumps(data)

r = requests.post(url, data = json_data)

print(r.text)
```