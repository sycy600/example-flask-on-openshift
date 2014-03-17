from __future__ import unicode_literals
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return b"Hello world"


def run():  # pragma: no cover
    app.run(debug=True)
