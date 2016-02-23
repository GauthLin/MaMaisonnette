#!/usr/bin/env python
# coding: utf-8 

import socket
import threading
import main

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connection de %s %s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(2048)
        print("Execution de : ", r, "...")
        #fp = open(r, 'rb')
        #self.clientsocket.send(fp.read())
	if r == "Internet":
		main.MyHouse.isInternetOn()
	elif r.startswith("heat"):
		nameHeating = r.split(" ")[1]
		status = r.split(" ")[2]
		main.MyHouse.heat(nameHeating, int(status))
		#print("Commander le chauffage: %s", nameHeating, " Status : %s", status)
        print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
