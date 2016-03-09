#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import main
import RPi.GPIO as GPIO
import param
from ADCPi.ABE_ADCPi import ADCPi
from ADCPi.ABE_helpers import ABEHelpers


class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

        self.myHouse = main.MyHouse()
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()
        self.adc = ADCPi(bus, 0x68, 0x69, 12)

        self.start()

    # Fonction principale
    def start(self):
        pass

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
            self.myHouse.setTemp(room, round(value, 2))

        # Command: SET_MODE [room] [value]
        elif r[0] == "SET_MODE":
            room = r[1]
            value = r[2]
            self.myHouse.setMode(room, value)

        # Command: GET_WINDOW [room]
        elif r[0] == "GET_WINDOW":
            room = r[1]
            msg = self.myHouse.getWindow(param.GPIO['Windows'][room])
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

        # Command: GET_DOOR [room]
        elif r[0] == "GET_DOOR":
            room = r[1]
            msg = self.myHouse.getDoor(param.GPIO['Doors'][room])
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

        # Command: GET_TEMP [room]
        elif r[0] == "GET_TEMP":
            room = r[1]
            temp = self.myHouse.getTemp(param.GPIO['Temp'][room])
            self.clientsocket.send(bytes(str(temp), 'UTF-8'))
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
