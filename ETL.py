import random
import requests
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.exc import SQLAlchemyError

# Define MySQL connection parameters
user = 'root'
password = 'rootpassword'
host = 'localhost'
port = 3306
database = 'bosta_asses'

# Create SQLAlchemy engine
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
db_engine = create_engine(connection_string)

# Fetch data from the API
response = requests.get("https://randomuser.me/api/")
data = response.json()
result = data['results'][0]
info = data['info']

# Create User ID
user_id = random.randint(1, 10000)

# Create DataFrames from the fetched data
user_df = pd.DataFrame([{
    'user_id': user_id,
    'gender': result['gender'],
    'email': result['email'],
    'dob_date': pd.to_datetime(result['dob']['date']).strftime('%Y-%m-%d'),
    'dob_age': result['dob']['age'],
    'registered_date': pd.to_datetime(result['registered']['date']).strftime('%Y-%m-%d'),
    'registered_age': result['registered']['age'],
    'phone': result['phone'],
    'cell': result['cell'],
    'nationality': result['nat'],
}])

name_df = pd.DataFrame([{
    'user_id': user_id,
    'title': result['name']['title'],
    'first': result['name']['first'],
    'last': result['name']['last'],
}])

login_df = pd.DataFrame([{
    'user_id': user_id,
    'uuid': result['login']['uuid'],
    'username': result['login']['username'],
    'password': result['login']['password'],
    'salt': result['login']['salt'],
    'md5': result['login']['md5'],
    'sha1': result['login']['sha1'],
    'sha256': result['login']['sha256'],
}])


location_df = pd.DataFrame([{
    'user_id': user_id,
    'street_number': result['location']['street']['number'],
    'street_name': result['location']['street']['name'],
    'city': result['location']['city'],
    'state': result['location']['state'],
    'country': result['location']['country'],
    'postcode': str(result['location']['postcode']).replace(' ', ''),
    'coordinates_latitude': result['location']['coordinates']['latitude'],
    'coordinates_longitude': result['location']['coordinates']['longitude'],
    'timezone_offset': result['location']['timezone']['offset'],
    'timezone_description': result['location']['timezone']['description'],
}])

pictures_df = pd.DataFrame([{
    'user_id': user_id,
    'picture_large': result['picture']['large'],
    'picture_medium': result['picture']['medium'],
    'picture_thumbnail': result['picture']['thumbnail'],
}])

info_df = pd.DataFrame([{
    'user_id': user_id,
    'seed': info['seed'],
    'version': info['version'],
}])

# Define the tables metadata
metadata = MetaData(bind=db_engine)
users_table = Table('UserFact', metadata, autoload=True)
locations_table = Table('LocationDimension', metadata, autoload=True)
pictures_table = Table('PictureDimension', metadata, autoload=True)
login_table = Table('LoginDimension', metadata, autoload=True)
name_table = Table('NameDimension', metadata, autoload=True)
info_table = Table('InfoDimension', metadata, autoload=True)

# Insert data into the database
all_successful = True

def insert_data(table, data):
    global all_successful
    try:
        with db_engine.connect() as conn:
            conn.execute(table.insert().values(data.to_dict(orient='records')))
    except SQLAlchemyError as e:
        print(f"Error inserting data into the '{table.name}' table: {e}")
        all_successful = False

insert_data(users_table, user_df)
insert_data(locations_table, location_df)
insert_data(pictures_table, pictures_df)
insert_data(login_table, login_df)
insert_data(name_table, name_df)
insert_data(info_table, info_df)

if all_successful:
    print("One record has been inserted successfully.")
