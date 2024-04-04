import requests

URL = 'https://api.pokemonbattle.me/v2/'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': '8575331e0b41e9a84d32f5b74962bf33'}
TOKEN = '8575331e0b41e9a84d32f5b74962bf33'

body = {
    "name": "Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_confirm = {
    "pokemon_id": "16169",
    "name": "Бульбарас",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_confirm2 = {
    "pokemon_id": "16169"
}

response = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body)

print(response.text)

response_confirm = requests.put(url = f'{URL}pokemons', headers = HEADERS, json = body_confirm)

print(response_confirm.text)

response_confirm2 = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body_confirm2)

print(response_confirm2.text)