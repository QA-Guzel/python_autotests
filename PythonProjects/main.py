import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3cfa950c4c8dfb8094903b8a1c8771ca'
HEADER = {'Content-type': 'application/json', 'trainer_token': TOKEN}
id = "41776"

body_create = {
     "name": "Ричи2",
    "photo_id": 15
}
body_name = {
    "pokemon_id": id,
    "name": "Друг",
    "photo_id": 10
}
body_in_pokeboll = {
    "pokemon_id": id
}
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

response_in_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeboll)
print(response_in_pokeboll.text)