import requests
import json

api_token = 'your_api_tokenasfa'
api_url_base = 'https://api.predic8.de/shop/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def getProducts():
    response = requests.get(api_url_base+"products/", headers=headers)
    print(response.text)
    print(response.status_code)
    products=response.json()['products']
    print(products)
    for p in products:
        print([p['name']])


getProducts()