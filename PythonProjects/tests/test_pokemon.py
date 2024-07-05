import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3cfa950c4c8dfb8094903b8a1c8771ca'
HEADER = {'Content-type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID= '4433'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Madam'