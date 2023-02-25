import os

SOURCE_URL = 'https://justjoin.it/api/offers'

QUERY_PARAMS = {
    'marker_icon': ['data'],
    'experience_level': ['junior', 'mid'],
    'city': ['Warszawa'],
    'workplace_type': ['partly_remote', 'office']
}

CONNECTION_STRING = f"postgresql://postgres:{os.environ['POSTGRES_PASSWORD']}@localhost:5432/{os.environ['POSTGRES_DB']}"

#docker build -t my-postgres-db --build-arg POSTGRES_PASSWORD=$POSTGRES_PASSWORD --build-arg POSTGRES_DB=$POSTGRES_DB .
#docker run -d --name my-postgresdb-container -p 5432:5432 my-postgres-db          