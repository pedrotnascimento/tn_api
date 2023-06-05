# tn_api
API for a recruiting process

## Setting Development
> python -m venv venv
> pip install -r requirements.txt

## Running
> flask run

## Testing
> python -m coverage run -m unittest 
> python -m coverage html

Register your tests into ./tests.py file 

## Loading Database
With the docker-compose.yml running
> docker-compose-up

> flask db upgrade

Run the script to load operations
> psql -h localhost -U postgres -d db_local -f initial_load.sql

Create an user by using the api: 

POST - http://127.0.0.1:5000/v1/users
BODY:
> { "username": [string], "password": [string] }

