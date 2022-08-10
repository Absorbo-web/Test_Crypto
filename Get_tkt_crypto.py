import requests
import json


def get_all_tikers():
    r = requests.get('https://api-pub.bitfinex.com/v2/conf/pub:list:pair:exchange')
    tikers_list = json.loads(r.text)[0]
    return tikers_list


if __name__ == '__main__':
    for tiker in get_all_tikers():
        print(tiker)
