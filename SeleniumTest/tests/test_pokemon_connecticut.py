import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': '8575331e0b41e9a84d32f5b74962bf33'}
TOKEN = '8575331e0b41e9a84d32f5b74962bf33'

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {"trainer_id" : 2173})
    assert response.status_code == 200

    def test_part_of_response():
        response = requests.get(url = f'{URL}trainers', params = {"trainer_id" : 2173})
        assert response.json()['trainer_name'] == 'Dench'