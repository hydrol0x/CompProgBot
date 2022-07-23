import json

with open('response.json') as f:
    API_data = json.load(f)
API_data = json.loads(API_data)
