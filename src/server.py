#!/usr/bin/python3
#coding: utf-8

import socket

HOST = '127.0.0.1'
PORT = 8081

server = socket.socket()
server.bind((HOST, PORT))

print('[+] Server started')
print('[+] Listening for client connection ...')

server.listen(1)
client, client_addr = server.accept()

print(f'[+] {client_addr} Client connected to the server')

while True:
    command = input("Enter command: ")
    command = command.encode()

    client.send(command)

    print('[+] Command sent')

    output = client.recv(1024)
    output = output.decode()

    print(f'Output: {output}')
