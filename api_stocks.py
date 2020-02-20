import requests
import json
from pprint import pprint
import time


def get_all_stocks():

    r = requests.get(
        'https://financialmodelingprep.com/api/v3/company/stock/list')
    r = r.json()
    r = json.dumps(r)
    print(type(r))

    with open('stocks', 'w') as file:
        file.write(r)

    with open('stocks', 'r') as xyz:
        abc = json.load(xyz)
        print(type(abc))


while True:
    get_all_stocks()
    time.sleep(60)  # sleep for 60 seconds


def get_stocks_realtime():
    r = requests.get(
        'https://financialmodelingprep.com/api/v3/stock/real-time-price')
    r = r.json()
    r = json.dumps(r)
    print(type(r))

    with open('stocks_real_time', 'w') as file:
        file.write(r)

    with open('stocks_real_time', 'r') as xyz:
        abc = json.load(xyz)
        print(type(abc))


while True:
    get_stocks_realtime()
    time.sleep(60)  # sleep for 60 seconds
