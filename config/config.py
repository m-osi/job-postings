import os

SOURCE_URL = 'https://justjoin.it/api/offers'

QUERY_PARAMS = {
    'marker_icon': ['data'],
    'experience_level': ['junior', 'mid'],
    'city': ['Warszawa'],
    'workplace_type': ['partly_remote', 'office']
}

CONNECTION_STRING = f"postgresql://postgres:{os.environ['POSTGRES_PASSWORD']}@localhost:5432/{os.environ['POSTGRES_DB']}"  