from django.shortcuts import render
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def index(request):
    
    data=get_crypto_currency()
    
    context={"data":data}

    
    return render(request,"bitcoin/index.html",context)
     
def get_crypto_currency():
    s='1'
    for k in range(2,26):
        s=s+','
        s=s+str(k)
    print(s)

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {   
    'id':s,
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '59a0eb9e-6199-4447-80c7-fe0569295d12',}
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        data=dict()

    return data['data']
