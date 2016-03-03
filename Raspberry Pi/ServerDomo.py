#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import socket
import threading
import main


class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

        self.myHouse = main.MyHouse()
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):

        print("Connection de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(2048).upper()
        print("Execution de : ", r, "...")
        # fp = open(r, 'rb')
        # self.clientsocket.send(fp.read())
        if r == "INTERNET":
            print(self.myHouse.isInternetOn())

        # Command: SET_LAMP [status]
        elif r.startswith("LAMP"):
            status = r.split(" ")[1]
            self.myHouse.setLamp(int(status))

        # Command: SET_TEMP [room] [value]
        elif r.startswith("SET_TEMP"):
            room = r.split(" ")[1]
            value = r.split(" ")[2]
            self.myHouse.setTemp(room, int(value))

        # Commend: SET_MODE [room] [value]
        elif r.startswith("SET_MODE"):
            room = r.split(" ")[1]
            value = r.split(" ")[2]
            self.myHouse.setMode(room, value)

        # print("Commander le chauffage: %s", nameHeating, " Status : %s", status)
        print("Client déconnecté...")


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
