import json

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


def check_services():
    file = open(filename, "w+")

    status = {}

    if file.read() == "":
        status = {
            "mq-integration": False
        }
    else:
        status = json.load(file)

    check_integration(status)

    json.dump(status, file)

    file.close()


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
