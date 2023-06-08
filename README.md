# tn_api
API for a recruiting process

## Setting Development
> python -m venv venv
> pip install -r requirements.txt

## Running
> flask run

## DEBUG
> flask --app app.py --debug run

## Testing
> python -m coverage run -m  unittest 
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

## Production 
- Build docker image 
    > docker build -t tn:{tag_number} .

- Tag the image to the repository
    > docker tag tn:{tag_number} 917957058161.dkr.ecr.sa-east-1.amazonaws.com/tn-repository:[{tag_number}]

- Logon AWS services
    > aws ecr get-login-password --region sa-east-1 
    > docker login -u AWS -p [BASE64_HASH_FROM_COMMAND_ABOVE] 917957058161.dkr.ecr.sa-east-1.amazonaws.com

- Push image
    > docker push 917957058161.dkr.ecr.sa-east-1.amazonaws.com/tn-repository

- Create new task on AWS ECR (Elastic Container Registry) Service "# tn_front" 

