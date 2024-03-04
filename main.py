import requests

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


class Pokemon:
    """
    id: int - the id of the pokemon
    name: str - name of the pokemon
    types: tuple(str) - (main type, sub type)
    height: float
    weight: float
    stats: dict(tuple(str,int)) - {(name,base_stat)} hp, attack, defense, special-attack, special-defense, speed
    """
    def __init__(self, ID: int, name: str, types: tuple, height: float, weight: float, stats: dict) -> None:
        self.id = ID
        self.name = name
        self.types = types
        self.height = height
        self.weight = weight
        self.stats = stats

    def __str__(self) -> str:
        return f""