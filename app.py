from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
from domain.models.user import *
from domain.models.record import *
from domain.models.operation import *

migrate = Migrate(app, db)

@app.route("/")
def test_connection():
    return "<p>It's UP</p>"

if __name__ == '__main__':
    app.run()
