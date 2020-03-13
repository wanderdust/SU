import requests
import json

def request_su (command):
    url = "http://localhost:3000/webapp/api"
    json_data = json.dumps(command)
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data = json_data, headers=headers)
