from pokemon_pipline import Pokemon
import requests


# the base url that you add the id to get each pokemon
base_url: str = "https://pokeapi.co/api/v2/pokemon/"

# last index of Pokédex
last_pokemon: int = 4#1025

def import_data_to_df(first_index:int = 1, last_index: int = last_pokemon) -> list:
    """
    Import the data from api requests into a list,
    no 0 index
    :param first_index: first pokemon to add
    :param last_index: last pokemon to add
    :return:
    """

    pokedex_list: list = []
    try:
        for i in range(first_index, last_index+1):
            it_url: str = base_url + str(i)
            response = requests.get(it_url)
            if response.status_code == 200:
                it_json = response.json()
                it_pokemon = Pokemon(it_json)
                pokedex_list.append(it_pokemon)
    except IndexError as e:
        print("Input correct first and last indexes")
    finally:
        return pokedex_list


