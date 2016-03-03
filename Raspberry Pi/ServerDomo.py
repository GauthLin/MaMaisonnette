#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import socket
import threading
import main
import RPi.GPIO as GPIO
import param


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

        r = self.clientsocket.recv(2048).upper().decode("utf-8")
        r = r.split(" ")
        print("Execution de : ", r, "...")
        # fp = open(r, 'rb')
        # self.clientsocket.send(fp.read())
        if r[0] == "INTERNET":
            print(self.myHouse.isInternetOn())

        # Command: SET_LAMP [status]
        elif r[0] == "LAMP":
            status = r[1]
            self.myHouse.setLamp(int(status))

        # Command: SET_TEMP [room] [value]
        elif r[0] == "SET_TEMP":
            room = r[1]
            value = r[2]
            self.myHouse.setTemp(room, int(value))

        # Command: SET_MODE [room] [value]
        elif r[0] == "SET_MODE":
            room = r[1]
            value = r[2]
            self.myHouse.setMode(room, value)

        # Command: GET_WINDOW [room]
        elif r[0] == "GET_WINDOW":
            room = r[1]
            msg = GPIO.input(param.GPIO['Windows'][room][1])
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

        # Command: GET_DOOR [room]
        elif r[0] == "GET_DOOR":
            room = r[1]
            msg = GPIO.input(param.GPIO['Doors'][room][1]
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

       # Command: GET_TEMP [room]
       elif r[0] == 'GET_TEMP':
            room = r[1]
            msg = GPIO.input(param.GPIO['Temp'][1])
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

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
