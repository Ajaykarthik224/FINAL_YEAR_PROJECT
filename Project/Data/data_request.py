import requests
import json
import config


class data_request:

    api_key = config.api_key
    url = f'https://api.data.gov.in/resource/8e0bd482-4aba-4d99-9cb9-ff124f6f1c2f?api-key={api_key}&format=json&offset=0&limit=10000000'

    data = requests.get(url).json()

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
