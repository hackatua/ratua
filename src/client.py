#!/usr/bin/python3
#coding: utf-8

import socket
import logging
import json
from modules import runcommand

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG)

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 8081
ID = "acb123"


def send_message(socket: socket.socket, type: str, payload: dict):
    data = {
        "action": type,
        "payload": payload
    }

    message = json.dumps(data)
    logging.debug("Sending %s" % message)
    socket.send(message.encode())


def receive_message(socket: socket.socket) -> dict:
    message = socket.recv(4096)
    decoded_message = message.decode()
    logging.debug("Received %s" % decoded_message)
    return json.loads(decoded_message)


client = socket.socket()

logging.debug("Connection initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
logging.debug("Connection initiated!")

logging.debug('Sending CONNECT message...')
send_message(client, 'CONNECT', {"id": ID})
logging.debug('Sended')

logging.debug("Awaiting for configuration...")
message = receive_message(client)
config = message["payload"]
logging.debug(f'Configuration received: {config}')

while True:
    logging.debug("Awaiting commands...")
    message = receive_message(client)
    result = runcommand.run(**message["payload"])

    logging.debug("Sending response...")
    send_message(client, "RUNCOMMAND_RESPONSE", result)
