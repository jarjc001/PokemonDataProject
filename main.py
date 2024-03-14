
import pokemon_pipline as pk
import pandas as pd

# # create datadb
# pk.create_db()
# pk.create_db_tables()

# get pokemon data into list
pokemon_list: list = pk.import_pokemon_data_to_list(4)
print(pokemon_list[0])

# list pokemon data into pd
pokemon_df: pd.DataFrame = pk.list_pokemon_data_to_pd(pokemon_list)
print(pokemon_df.head())

print(pokemon_df.describe())

#
# # # insert pokemon df into db
# # pk.insert_pokemon_data_to_db(pokemon_df)
# #
# # # download pokemon_pd to csv and parquet
# # pk.data_pd_to_csv(pokemon_df)
# # pk.data_pd_to_parquet(pokemon_df)
#
# get pokemon types data into list
pokemon_types: list = pk.import_type_data_to_list()
print(pokemon_types)

# list of types into pd
types_df: pd.DataFrame = pk.list_types_data_to_pd(pokemon_types)
print(types_df.head())
#
# # # insert pokemon types data into db
# # pk.insert_types_data_to_db(types_df)
#
#
# pk.insert_many_many_data_to_db(pokemon_df,types_df)