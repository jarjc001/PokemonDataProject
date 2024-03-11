from .Pokemon import Pokemon
from .db_info import *
import pandas as pd
import mysql.connector

# sql alemy
# create_engine = create_engine(CON_STRING)

db_name = "pokemondata"


def set_db_name(new_name: str) -> None:
    db_name = new_name


def create_db() -> None:
    connection = mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        ssl_disabled=True
    )

    cursor = connection.cursor()

    cursor.execute(f"DROP DATABASE IF exists {db_name};"
                   f"CREATE DATABASE {db_name};")

    connection.close()
    cursor.close()


def create_db_tables():
    connection = create_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
                -- type table
            Drop Table if exists pokemontypes;
            CREATE TABLE pokemontypes (
                typeId TINYINT PRIMARY KEY,
                pokemonType VARCHAR(10) NOT NULL
            );
            
            -- pokemon table
            DROP TABLE IF EXISTS pokemondata;
            CREATE TABLE pokemondata (
                pokemonId SMALLINT PRIMARY KEY,
                name VARCHAR(25) NOT NULL,
                height FLOAT NOT NULL,
                weight FLOAT NOT NULL,
                hp SMALLINT NOT NULL,
                attack SMALLINT NOT NULL,
                defense SMALLINT NOT NULL,
                special_attack SMALLINT NOT NULL,
                special_defense SMALLINT NOT NULL,
                speed SMALLINT NOT NULL
            );
            
            -- related tables
            -- pokemom type for many to many
            DROP TABLE IF EXISTS pokemonTypeData;
            CREATE TABLE pokemonTypeData(
                pokemonId smallint,
                typeId tinyint, 
                constraint PK_pokemonTypeData
                    PRIMARY KEY(pokemonId,typeId),
                CONSTRAINT fk_pokemonTypeData_pokemontypes
                    foreign key (typeId)
                    references pokemontypes(typeId),
                constraint fk_pokemonTypeData_pokemondata
                    foreign key (pokemonId)
                    references pokemondata(pokemonId)
            );
            """)

    connection.close()
    cursor.close()


def create_db_connection() -> mysql.connector:
    connection = mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=db_name,
        ssl_disabled=True
    )

    return connection
