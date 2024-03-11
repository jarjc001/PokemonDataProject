from .Pokemon import Pokemon
import requests
import pandas as pd

# the base url that you add the id to get each pokemon
base_url: str = "https://pokeapi.co/api/v2/pokemon/"

# last index of Pokédex
last_pokemon: int = 4  # 1025


def import_data_to_list(last_index: int = last_pokemon, first_index: int = 1) -> list:
    """
    Import the data from api requests into a list,
    no 0 index for pokemon API
    :param first_index: first pokemon to add
    :param last_index: last pokemon to add
    :return: list of pokemon data
    """

    pokemon_list: list = []
    try:
        for i in range(first_index, last_index + 1):
            i_url: str = base_url + str(i)
            response = requests.get(i_url)
            if response.status_code == 200:
                i_json = response.json()
                i_pokemon = Pokemon(i_json)
                pokemon_list.append(i_pokemon)
    except IndexError as e:
        print("Input correct first and last indexes")
    finally:
        return pokemon_list


def list_data_to_pd(pokemon_list: list) -> pd.DataFrame:
    """
    Transfers a list of pokemon data into a pd.dataframe
    :param pokemon_list: list created by import_data_to_list()
    :return: pd.dataframe
    """
    df = pd.DataFrame(
        columns=['id', 'name', 'type1', 'type2', 'height', 'weight', 'hp', 'attack', 'defense', 'special-attack',
                 'special-defense', 'speed'])
    df['id'] = [i.id for i in pokemon_list]
    df['name'] = [i.name for i in pokemon_list]
    df['type1'] = [i.types[0] for i in pokemon_list]
    df['type2'] = [i.types[1] for i in pokemon_list]
    df['height'] = [i.height for i in pokemon_list]
    df['weight'] = [i.weight for i in pokemon_list]
    df['hp'] = [i.stats['hp'] for i in pokemon_list]
    df['attack'] = [i.stats['attack'] for i in pokemon_list]
    df['defense'] = [i.stats['defense'] for i in pokemon_list]
    df['special-attack'] = [i.stats['special-attack'] for i in pokemon_list]
    df['special-defense'] = [i.stats['special-defense'] for i in pokemon_list]
    df['speed'] = [i.stats['speed'] for i in pokemon_list]

    return df


def data_pd_to_csv(pokemon_df: pd.DataFrame) -> None:
    """
    dataframe into csv
    :param pokemon_df:
    """
    pokemon_df.to_csv('data_export/pokemon_csv.csv', index=False)


def data_pd_to_Parquet(pokemon_df: pd.DataFrame) -> None:
    """
    dataframe into parquet
    :param pokemon_df:
    """
    pokemon_df.to_parquet('data_export/pokemon_parquet.parquet', index=False)
