# from .Pokemon import Pokemon
from db_info import *
from db_queries import *
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
    Creates the tables for the mysql db
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



