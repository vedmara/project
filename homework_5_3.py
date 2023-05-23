import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon)
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])
pokem = pokemon 
with open('pokemon.txt', 'w') as pokemon_file:
    pokemon_file.write(pokem)
with open('pokemon.txt', 'r') as pokemon_file:
    contents = pokemon_file.read()
print(contents)
