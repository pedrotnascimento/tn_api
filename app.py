from flask import Flask


app = Flask(__name__)


@app.route("/")
def test_connection():
    return "<p>It's UP</p>"

if __name__ == '__main__':
    app.run()
