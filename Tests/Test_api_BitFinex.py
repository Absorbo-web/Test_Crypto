import requests
import json
import pytest
# from Get_tkt_crypto import get_all_tikers


def get_all_tikers():
    r = requests.get('https://api-pub.bitfinex.com/v2/conf/pub:list:pair:exchange')
    tikers_list = json.loads(r.text)[0]
    return tikers_list


def test_check_avalible():
    r = requests.get('https://api-pub.bitfinex.com/v2/platform/status')
    assert json.loads(r.text)[0] == 1


def test_get_all_tikers_response():
    r = requests.get('https://api-pub.bitfinex.com/v2/conf/pub:list:pair:exchange')
    assert r.status_code == 200


def test_avalible_BTCUSD():
    tikers_list = get_all_tikers()
    assert 'BTCUSD' in tikers_list


def test_count_tikers():
    tikers_list = get_all_tikers()
    assert len(tikers_list) >= 100


test_check_avalible()
test_get_all_tikers_response()
test_avalible_BTCUSD()
test_count_tikers()
