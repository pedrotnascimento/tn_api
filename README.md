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
> docker-compose up

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

## Load Balance URl

> http://tn-api-118067680.sa-east-1.elb.amazonaws.com/

#### Feedback:
Here are some comments on the points to improve:
- If the token is not valid the user should not be able to access the site. 
- Validations are missing in the operations and for this reason some of them fail. The error messages are not correct.
- More tests could have been added on the front-end. The logs are not enough to determine the failures in the application.
- The list of operations has some bugs, for example the sorting.
- Validations should also be included in the endpoint parameters on the API.
- The tests are not enough to cover the basic cases in the API. The password is not encrypted in the DB."


#### References:
- https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6
- https://realpython.com/flask-by-example-part-1-project-setup/
