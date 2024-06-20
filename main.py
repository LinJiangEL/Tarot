import os
import pprint
import requests
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(filename='.env'), verbose=True, override=True, encoding='utf-8')

api_key = os.getenv('API_KEY')
gate_url = os.getenv('GATE_URL') # gateurl + 'Free/querymerchant'

request_data = {
    'api_key': api_key,
}

response = requests.post(gate_url + 'Free/querymerchant', data=request_data)
pprint.pprint(response.json())
