DB_NAME: str = "pokemondata"

CREATE_DB_1: str = f"DROP DATABASE IF exists {DB_NAME};"
CREATE_DB_2: str = f"CREATE DATABASE {DB_NAME};"

CREATE_TABLE_TYPES_1: str = \
    """ 
        Drop Table if exists types;
    """

CREATE_TABLE_TYPES_2: str = \
    """
        CREATE TABLE types (
            typeId TINYINT PRIMARY KEY,
            pokemonType VARCHAR(8) NOT NULL
        );
    """

CREATE_TABLE_POKEMON_1: str = \
    """
        DROP TABLE IF EXISTS pokemon;
    """

CREATE_TABLE_POKEMON_2: str = \
    """
        CREATE TABLE pokemon(
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
    """

CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_1: str = \
    """
        DROP TABLE IF EXISTS pokemontypes;
    """

CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY_2: str = \
    """
        CREATE TABLE pokemontypes(
            pokemonId smallint,
            typeId tinyint, 
        CONSTRAINT PK_pokemontypes
            PRIMARY KEY(pokemonId,typeId),
        CONSTRAINT fk_pokemonTypeData_types
            foreign key (typeId)
            references types(typeId) 
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        CONSTRAINT fk_pokemontypes_pokemon
            foreign key (pokemonId)
            references pokemon(pokemonId)
        );
    """

INSERT_TABLE_POKEMON_TYPE_SINGLE_LINE: str = \
    """
        INSERT INTO pokemontypes (pokemonId, typeId)
        VALUES (%s,%s)
    """


