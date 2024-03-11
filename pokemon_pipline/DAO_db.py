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


def insert_types_data_to_db(pokemon_type_list: List[str]) -> None:
    """
    inserts the pokemon types into the types sql db table
    :param pokemon_type_list: list of pokemon types
    :return:
    """
    engine = create_engine(SQL_ALCHEMY_CON_STRING)

    df = pd.DataFrame(pokemon_type_list, columns=["pokemonType"])
    df["typeID"] = [i for i in range(len(pokemon_type_list))]

    try:
        df.to_sql("types", engine, if_exists="append", index=False)
    except IntegrityError:
        print("Type data already in table: Rerun insert_types_data after clearing table")
