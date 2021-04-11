import requests
import json


class data_request:

    api_key = '579b464db66ec23bdd00000138ba8e153b6f4e7e7065009210338f2b'
    url = f'https://api.data.gov.in/resource/8e0bd482-4aba-4d99-9cb9-ff124f6f1c2f?api-key={api_key}&format=json&offset=0&limit=10000000'

    data = requests.get(url).json()

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
