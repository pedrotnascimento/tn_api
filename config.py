from os import environ

class ProdConfig():
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

    # PURPOSE-ANTIPATTERN: its here just for simplicity when testing from local to production 
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin123@truenorth-db.cyj0wtj8tzvq.sa-east-1.rds.amazonaws.com:5432/truenorthDb"
    
    SECRET_KEY = environ.get('SECRET_KEY')


class DevConfig():
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    SECRET_KEY = "someRandomSecretKey"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/db_local"

class ContainerConfig():
    FLASK_ENV = "container"
    FLASK_DEBUG = True
    SECRET_KEY = "someRandomSecretKey"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@db:5432/db_local"