import requests
import pokemon_pipline as pk

test_url: str = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(test_url)
status = response.status_code
print(status)

content: dict = response.json()
print(content['name'])
print(type(content))
content_keys = content.keys()
print(content_keys)

# dict_keys(['abilities', 'base_experience', 'cries',
#           'forms', 'game_indices', 'height', 'held_items',
#           'id', 'is_default', 'location_area_encounters',
#           'moves', 'name', 'order', 'past_abilities',
#           'past_types', 'species', 'sprites', 'stats', 'types', 'weight'])

# want 'id', 'name', 'stats', 'types', 'height', 'weight'

# print(content_dict)


# the last Pokemon for the dex
test_url2: str = "https://pokeapi.co/api/v2/pokemon/1025"

response2 = requests.get(test_url2)
if response2.status_code == 200:
    content2: dict = response2.json()
    print(content2['name'])

# pokemon with more than 1 form
# will only do default form
test_url3: str = "https://pokeapi.co/api/v2/pokemon/50"

response3 = requests.get(test_url3)
if response3.status_code == 200:
    content3: dict = response3.json()
    print(content3.keys())
    print(content3["name"])
    print(content3["stats"])

ditto = pk.Pokemon(132, "ditto",
                   [{'slot': 1, 'type': {'name': 'ground', 'url': 'https://pokeapi.co/api/v2/type/5/'}}],
                   3, 40,
                   {"hp": 48, "attack": 48, "defense": 48, "special-attack": 48, "special-defense": 48, "speed": 48})

print(ditto)


print(content3["stats"][0])

test_url4: str = "https://pokeapi.co/api/v2/pokemon/6"
response4 = requests.get(test_url4)
if response4.status_code == 200:
    content4: dict = response4.json()
    print(content4["name"])
    print(content3["types"])
    print(content4["types"])


print(ditto.marshal_pokemon_type_data(ditto.types))