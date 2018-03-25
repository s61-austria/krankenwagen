import json
import urllib.request

import pika
from pika.credentials import PlainCredentials

filename = 'status.json'


def read_status():
    """
    Reads the saved status file and returns it
    :return:
    """
    with open(filename, "r") as file:
        return file.read()


def write_status(string):
    """
    Write to status.json
    :param string:
    :return:
    """
    with open(filename, "w") as file:
        file.write(string)


def check_integration(status):
    """
    Check the Integration MQ status
    :param status:
    :return:
    """
    conn = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="ec2-18-197-180-1.eu-central-1.compute.amazonaws.com",
            virtual_host="vhost",
            credentials=PlainCredentials("rabbitmq", "rabbitmq")
        )
    )

    channel = conn.channel()

    status['mq-integration'] = channel.is_open


if __name__ == '__main__':
    check_services()


def fetch_service(url):
    try:
        return json.loads(urllib.request.urlopen("{0}/status".format(url), timeout=2))
    except Exception:
        return "down"
