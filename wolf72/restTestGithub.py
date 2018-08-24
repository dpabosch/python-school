import requests
import pprint


api_token = '24c5b9290795cc23c1fbfb8296bde06efdd2e076'
api_url_base = 'https://api.github.com/user'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def get_account_info():
    response = requests.get(api_url_base, headers=headers)
    user=response.json()
    pprint.pprint(user)


get_account_info()