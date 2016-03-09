#!/usr/bin/python
# -*- coding: utf-8 -*-

import param
import socket
import RPi.GPIO as GPIO


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

        self.setup_gpio(param.GPIO)

    # GPIO configuration
    def setup_gpio(self, array):
        GPIO.setmode(GPIO.BCM)

        # v[0] contains the key
        # v[1] contains the value
        for v in array.items():
            if isinstance(v[1], dict):
                self.setup_gpio(v[1])
            else:
                if v[1][0].upper() == "IN":
                    GPIO.setup(v[1][1], GPIO.IN)
                else:
                    GPIO.setup(v[1][1], GPIO.OUT)

    # Test si la connexion est activee
    # Retourne True si internet est activee
    # Retourne False si non
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

    # Retourne la temperature d'une pièce
    def getTemp(self, name):
        room = r[1]
        list_room = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4
        }
        temp = round(self.adc.read_voltage(list_room[room]) / .01, 2)
        return temp

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

if __name__ == '__main__':
    MyHouse = MyHouse()
