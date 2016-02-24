#!/usr/bin/python
# -*- Coding: utf-8 -*-

import param
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class MyHouse:
    # Constructeur
    def __init__(self):
        # Température voulue dans les différentes pièces
        self.requestTemp = {
            'A': None,
            'B': None,
            'C': None
        }

        # Mode actuel dans les différentes pièces
        self.currentMode = {
            'A': 'AUTO',
            'B': 'AUTO',
            'C': 'AUTO'
        }

    # Initialisation de toutes les variables
    def setup(self):
        pass

    # Test si la connexion est activee
    ## Retourne True si internet est activee
    ## Retourne False si non
    def isInternetOn(self):
        try:
            host = socket.gethostbyname("www.google.com")
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

    # Allume ou eteint le chauffage
    # room : nom du chauffage
    # status : True ou False
    def heat(self, room, status):
        GPIO.setup(param.Heating['B'], GPIO.OUT)
        GPIO.output(param.Heating[room], status)

    # Allume ou eteint la lampe
    # status : True ou False
    def setLamp(self, status):
        GPIO.output(param.Lamp, status)

    # Todo : convertir la tension en degre celsius
    # Retourne la temperature d une piece
    def getTemp(self, name):
        return GPIO.input(param.Sensors['Temp'][name])

    def setTemp(self, room, temp):
        self.requestTemp[room] = temp

    def setMode(self, room, status):
        self.currentMode[room] = status

    # Retourne True ou False si fenetre Ferme ou Ouvert
    def getWindow(self, name):
        return GPIO.input(param.Sensors['Windows'][name])

    # Retourne True ou False si porte Ferme ou Ouvert
    def getDoor(self, name):
        return GPIO.input(param.Sensors['Doors'][name])


MyHouse = MyHouse()
