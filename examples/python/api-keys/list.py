import requests
import json

#Please substitute YOUR_ENDPOINT and YOUR_API_KEY
endpoint = 'YOUR_ENDPOINT'
headers = {
	'Content-Type': 'application/vnd.api+json',
	'Authorization': 'ApiKey YOUR_API_KEY'
}

resp = requests.get(endpoint, headers=headers)

print json.dumps(resp.json(), indent=4, sort_keys=True)
