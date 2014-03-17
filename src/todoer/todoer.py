from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


def run():  # pragma: no cover
    app.run(debug=True)
