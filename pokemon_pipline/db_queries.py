DB_NAME: str = "pokemondata"

CREATE_DB: str = f"DROP DATABASE IF exists {DB_NAME}; CREATE DATABASE {DB_NAME};"

CREATE_TABLE_TYPES: str =\
    """ 
        Drop Table if exists pokemontypes;
    `               CREATE TABLE pokemontypes (
            typeId TINYINT PRIMARY KEY,
            pokemonType VARCHAR(10) NOT NULL
        );
    """

CREATE_TABLE_POKEMON: str =\
    """
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
    """

CREATE_TABLE_POKEMON_TYPES_MANY_TO_MANY: str =\
    """
        DROP TABLE IF EXISTS pokemonTypeData;
        CREATE TABLE pokemonTypeData(
            pokemonId smallint,
            typeId tinyint, 
        CONSTRAINT PK_pokemonTypeData
            PRIMARY KEY(pokemonId,typeId),
        CONSTRAINT fk_pokemonTypeData_pokemontypes
            foreign key (typeId)
            references pokemontypes(typeId),
        CONSTRAINT fk_pokemonTypeData_pokemondata
            foreign key (pokemonId)
            references pokemondata(pokemonId)
        );
    """
