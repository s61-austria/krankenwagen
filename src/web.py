import json

from flask import Flask

from src.checker import read_status
from src.status import status

app = Flask(__name__)


@app.route("/")
def hello():
    return read_status()


@app.route("/status")
def get_status():
    return json.dumps(status())


if __name__ == '__main__':
    app.run()
