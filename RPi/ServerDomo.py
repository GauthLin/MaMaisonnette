#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import multiprocessing
import time

import param
from myHouse import *


class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket, myHouse):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

        # self.adc = adc
        self.myHouse = myHouse

        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    # Fonction principale
    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(2048).upper().decode("utf-8")
        r = r.split(" ")
        print("Execution de : ", r, "...")

        if r[0] == "INTERNET":
            print(self.myHouse.isInternetOn())

        # Command: SET_LAMP [status]
        elif r[0] == "LAMP":
            status = r[1]
            self.myHouse.setLamp(int(status))

        # Command: SET_TEMP [room] [value]
        elif r[0] == "SET_TEMP":
            print('SET_TEMP')
            room = r[1]
            value = r[2]  
            self.myHouse.setDefaultTemp(room, round(value, 2))
        
        # Command: SET_CONSIGNE [room] [temp] [start_date] [end_date] 
        elif r[0] == "SET_CONSIGNE":
             print('SET_CONSIGNE')
             room = r[1]
             temp = r[2]
             start = r[3]
             end = r[4]
             self.myHouse.setConsigne(room, round(temp, 2), start, end)

        # Command: SET_MODE [room] [value]
        elif r[0] == "SET_MODE":
            print('SET_MODE')
            room = r[1]
            value = r[2]
            self.myHouse.setMode(room, value)

        # Command: GET_WINDOW [room]
        elif r[0] == "GET_WINDOW":
            print('GET_WINDOW')
            room = r[1]
            msg = self.myHouse.getWindow(param.GPIO['Windows'][room])
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

        # Command: GET_DOOR [room]
        elif r[0] == "GET_DOOR":
            print('GET_DOOR')
            room = r[1]
            msg = self.myHouse.getDoor(param.GPIO['Doors'][room])
            self.clientsocket.send(bytes(str(msg), 'UTF-8'))
            self.clientsocket.close()

        # Command: GET_TEMP [room]
        elif r[0] == "GET_TEMP":
            print('GET_TEMP')
            room = r[1]
            # temp = self.myHouse.getTemp(self.adc, param.GPIO['Temp'][room])
            self.clientsocket.send(bytes(str(18), 'UTF-8'))
            self.clientsocket.close()

        # print("Commander le chauffage: %s", nameHeating, " Status : %s", status)
        print("Client déconnecté...")

def regulate(myHouse):
    print("regulate")
    
    while True:
        myHouse.regulate()
        time.sleep(2)


if __name__ == '__main__':
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind(("", 1111))

    myHouse = MyHouse()
    p = multiprocessing.Process(name="running", target=regulate, args=(myHouse,))
    p.start()

    #i2c_helper = ABEHelpers()
    #bus = i2c_helper.get_smbus()
    #adc = ADCPi(bus, 0x6c, 0x6d, 12)
    #adc = None

    while True:
        tcpsock.listen(10)
        print("En écoute...")
        (clientsocket, (ip, port)) = tcpsock.accept()
        newthread = ClientThread(ip, port, clientsocket, myHouse) #adc)
        newthread.start()
