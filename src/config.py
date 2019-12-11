import os
import sqlalchemy.dialects.sqlite

'''
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']
'''
user = 'test'
password = 'password'
host = 'localhost'
database = 'example'
port = '3306'

DATABASE_CONNECTION_URI = f'mysql+pyodbc://{user}:{password}@{host}:{port}/{database}'

'''
    f'mysql+psycopg2://{user}:{password}@{host}:{port}/{database}'
'''