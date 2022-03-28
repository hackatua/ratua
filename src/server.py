#!/usr/bin/python3
#coding: utf-8

import socket
import json

HOST = '127.0.0.1'
PORT = 8081


def get_client_configuration(id: str) -> dict:
    return {
        "id": id,
        "modules": []
    }


server = socket.socket()
server.bind((HOST, PORT))

print('[+] Server started')
print('[+] Listening for client connection ...')

server.listen(1)
client, client_addr = server.accept()

print(f'[+] {client_addr} Client connected to the server')

message = client.recv(1024)
message = message.decode()

print('[+] Message received: "%s"' % message)

client_id = message.split(" ")[1]

print('[+] Sending config to "%s"' % client_id)

message = ('SET_CONFIG %s' % json.dumps(
    get_client_configuration(client_id))).encode()
client.send(message)

while True:
    command = input("Enter command: ")
    command = command.encode()

    client.send(command)

    print('[+] Command sent')

    output = client.recv(1024)
    output = output.decode()

    print(f'Output: {output}')
