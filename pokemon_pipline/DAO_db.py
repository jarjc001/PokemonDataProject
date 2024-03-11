from .Pokemon import Pokemon
from .db_info import *
from .db_queries import *
import pandas as pd
import mysql.connector


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
        ssl_disabled=True
    )

    cursor = connection.cursor()
    cursor.execute(CREATE_DB)
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
        ssl_disabled=True
    )

    return connection


def create_db_tables() -> None:
    """
    Creates the tables for the mysql db
    """
    connection = create_db_connection()
    cursor = connection.cursor()

    cursor.execute(CREATE_TABLE_TYPES)
    cursor.execute(CREATE_TABLE_POKEMON)
    cursor.execute(CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY)

    connection.close()
    cursor.close()
