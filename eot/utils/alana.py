import requests

def request_alana(utterance):
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

    r= requests.post(url='http://52.23.135.246:5000', json=data)
    response = r.json()

    print(response['result'])