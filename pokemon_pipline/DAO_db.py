from .db_info import *
from .db_queries import *

from typing import List
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError


# sql alemy
# create_engine = create_engine(CON_STRING)


def set_db_name(new_name: str) -> None:
    """
    Change the name of the current db
    :param new_name: the new db name
    """
    DB_NAME = new_name


def create_db() -> None:
    """
    Create the db in mysql
    """
    connection = mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        auth_plugin='mysql_native_password'
    )

    cursor = connection.cursor()
    cursor.execute(CREATE_DB_1)
    cursor.execute(CREATE_DB_2)
    connection.close()
    cursor.close()


def create_db_connection() -> mysql.connector:
    """
    create the connection to the mysql db using mysql.connector
    :return: connection
    """
    connection = mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
        auth_plugin='mysql_native_password'
    )

    return connection


def create_db_tables() -> None:
    """
    Creates all tables for the mysql db
    """

    connection = create_db_connection()
    cursor = connection.cursor()

    cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_1)
    cursor.execute(CREATE_TABLE_TYPES_1)
    cursor.execute(CREATE_TABLE_POKEMON_1)
    cursor.execute(CREATE_TABLE_TYPES_2)
    cursor.execute(CREATE_TABLE_POKEMON_2)
    cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_2)

    connection.close()
    cursor.close()


def reset_db_table(which_table: str = "all") -> None:
    """
    resets the tables of the db
    -"all" - all the tables
    -"types" - reset types and many-many
    -"pokemon" - resets pokemon and many-many
    -"many", resets many-many
    :param which_table: "all","types","pokemon","many"
    """

    connection = create_db_connection()
    cursor = connection.cursor()

    match which_table:
        case "all":
            create_db_tables()
        case "types":
            cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_1)
            cursor.execute(CREATE_TABLE_TYPES_1)
            cursor.execute(CREATE_TABLE_POKEMON_1)
            cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_2)
        case "pokemon":
            cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_1)
            cursor.execute(CREATE_TABLE_TYPES_2)
            cursor.execute(CREATE_TABLE_POKEMON_2)
            cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_2)
        case "many":
            cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_1)
            cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_2)

    connection.close()
    cursor.close()


def insert_types_data_to_db(type_df: pd.DataFrame) -> None:
    """
    inserts the pokemon types into the types mysql db table
    :param type_df: df of pokemon types
    """
    engine = create_engine(SQL_ALCHEMY_CON_STRING)

    try:
        type_df.to_sql("types", engine, if_exists="append", index=False)
    except IntegrityError:
        print("Type data already in table: Rerun insert_types_data after clearing table")


def insert_pokemon_data_to_db(pokemon_df: pd.DataFrame) -> None:
    """
    inserts the pokemon data (apart from its types) into the pokemon mysql db table
    :param pokemon_df: dataframe of pokemon data
    """

    engine = create_engine(SQL_ALCHEMY_CON_STRING)

    # drops types from the database
    df = pokemon_df.drop(columns=['type1', 'type2'])

    try:
        df.to_sql("pokemon", engine, if_exists="append", index=False)
    except IntegrityError:
        print("pokemon data already in table: Rerun insert_pokemon_data_to_db after clearing table")


def insert_many_many_data_to_db(pokemon_df: pd.DataFrame, type_df: pd.DataFrame) -> None:
    """
    Inserts the pokemonId and TypeId for each pokemon into the pokemontypes many-to-many table
    :param pokemon_df: df of pokemon data
    :param type_df: df of type data
    """
    connection = create_db_connection()
    cursor = connection.cursor()

    last_pokemon: int = max(pokemon_df["pokemonId"])

    # loop through 1 - pokemon last,

    for i in range(0, last_pokemon):
        pokemon_id: int = int(pokemon_df["pokemonId"][i])

        pokemon_types: tuple = (pokemon_df["type1"][i], pokemon_df["type2"][i])

        for p_type in pokemon_types:
            if p_type is None:
                continue
            type_id = int(type_df.loc[type_df["pokemonType"] == p_type]["typeID"].values.item())

            input_tuple = (pokemon_id, type_id)  #

            cursor.execute(INSERT_TABLE_POKEMON_TYPE_SINGLE_LINE, input_tuple)
            connection.commit()

    connection.close()
    cursor.close()
