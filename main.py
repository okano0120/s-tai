import requests
import json

livemoni = requests.get('https://www.supertaikyu.live/json/livemoni.json')

# print(['LiveData'])
# data = json.loads(livemoni.json())
print(json.dumps(livemoni.json(), indent=2))
