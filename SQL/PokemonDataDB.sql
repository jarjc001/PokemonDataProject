-- Defines the data base and creates the tables in it

-- Drops any existing databases, then rebuilds a database with the same name. It will then be ready to use

DROP DATABASE IF exists pokemondata;
CREATE DATABASE pokemondata;
USE pokemondata;

-- type table
Drop Table if exists types;
CREATE TABLE types (
    typeId TINYINT PRIMARY KEY,
    pokemonType VARCHAR(10) NOT NULL
);

-- pokemon table
DROP TABLE IF EXISTS pokemon;
CREATE TABLE pokemon (
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
DROP TABLE IF EXISTS pokemontypes;
CREATE TABLE pokemontypes(
	pokemonId smallint,
    typeId tinyint, 
    constraint PK_pokemontypes
		PRIMARY KEY(pokemonId,typeId),
	CONSTRAINT fk_pokemontypes_types
		foreign key (typeId)
        references types(typeId)
        ON DELETE CASCADE
		ON UPDATE CASCADE,
	constraint fk_pokemontypes_pokemona
		foreign key (pokemonId)
        references pokemon(pokemonId)
);

select * from types;
select * from pokemon;
select * from pokemontypes;

-- insert data into many-many pokemontypes
INSERT INTO pokemontypes (pokemonId, typeId)
VALUES (2,2);


