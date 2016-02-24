#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.17.10.60", 1111))

print("Introduisez la commande a executer:")
command = input(">> ") # utilisez raw_input() pour les anciennes versions python
s.send(command.encode())
file_name = ':%s' % (command,)
r = s.recv(9999999)
print("Commande executee avec succes:")
