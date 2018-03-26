import json

from flask import Flask

import src.checker as checker
from src.status import status

app = Flask(__name__)
settings = json.load(open('config.json'))


@app.route("/")
def hello():
    return checker.read_status()


@app.route("/update")
def update():
    status_obj = {
        "services": {},
        "queues": {}
    }
    for service in settings['services']:
        status_obj['services'][service] = checker.fetch_service(service)

    for mq in settings['queues']:
        status_obj['queues'][mq['url']] = checker.check_mq(mq['url'], mq['user'], mq['pass'])

    checker.write_status(json.dumps(status_obj))
    return json.dumps(status_obj)


@app.route("/status")
def get_status():
    return json.dumps(status())


if __name__ == '__main__':
    app.run()
