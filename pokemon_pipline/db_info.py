# db info
import os

DB_HOST: str = os.environ.get('DB_HOST')
DB_USERNAME: str = os.environ.get('DB_USERNAME')
DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
SQL_ALCHEMY_CON_STRING: str = 'mysql+pymysql://'+DB_USERNAME+':'+DB_PASSWORD+'@'+DB_HOST+'/pokemondata'
