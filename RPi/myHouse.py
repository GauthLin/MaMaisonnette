#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

import param
from DBManager import *

import socket
import RPi.GPIO as GPIO


class MyHouse:
    # Constructeur
    def __init__(self):
        # Température voulue dans les différentes pièces
        # [Temp, start_datetime, end_datetime]
        self.requestTemp = {
            'A': [None, None, None],
            'B': [None, None, None],
            'C': [None, None, None]
        }

        # Mode actuel dans les différentes pièces
        self.currentMode = {
            'A': 'AUTO',
            'B': 'AUTO',
            'C': 'AUTO'
        }

        # Température par défaut des différentes pièces
        self.defaultTemp = {
            'A': 18,
            'B': 18,
            'C': 18
        }

        self.setup_gpio(param.GPIO)

        self.db = DBManager()

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
        GPIO.setup(param.GPIO['Heating']['B'][1], GPIO.OUT)
        GPIO.output(param.GPIO['Heating'][room][1], status)

    # Allume ou eteint la lampe
    # status : True ou False
    def setLamp(self, status):
        GPIO.output(param.GPIO['Lamp'][1], status)

    # Retourne la temperature d'une pièce
    def getTemp(self, adc, name):
        list_room = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4
        }
        temp = round(adc.read_voltage(list_room[name]) / .01, 2)
        return temp

    # Sauvegarde la température par défault de la pièce
    def setDefaultTemp(self, room, temp):
        self.defaultTemp[room] = temp

        self.db.executeUpdate('UPDATE temp_default SET temp_default = ' + temp + ' WHERE room=' + room)

    # Récupère la température par défaut d'une pièce
    def getDefaultTemp(self, room):
        return self.defaultTemp[room]

    # Permet de récupérer la température pour la chambre et la date donnée
    def getRequestTemp(self, room, date):
        connection = self.db.getConnection()
        cursor = connection.cursor()

        cursor.execute('SELECT `temp` FROM `consigne` WHERE `room` = %s AND `end_order` < %s',
                       (str(room), str(date)))
        result = cursor.fetchone()
        requestTemp = result['temp']
        cursor.close()

        return requestTemp

    # Sauvegarde une consigne
    def setConsigne(self, room, temp, start_timestamp, end_timestamp):
        start_datetime = datetime.datetime.fromtimestamp(start_timestamp)
        end_datetime = datetime.datetime.fromtimestamp(end_timestamp)
        request_temp = self.requestTemp[room]
        request_temp[0] = temp
        request_temp[1] = start_datetime
        request_temp[2] = end_datetime
        self.db.executeUpdate(
            'INSERT INTO `consigne` (`temp`, `start_order`, `end_order`, `room`) VALUES (%s,%s,%s,%s)',
            (str(temp), str(start_datetime), str(end_datetime), room)
        )

    def setMode(self, room, status):
        self.currentMode[room] = status

    # Retourne True ou False si fenetre Ferme ou Ouvert
    def getWindow(self, name):
        return GPIO.input(param.GPIO['Sensors']['Windows'][name][1])

    # Retourne True ou False si porte Ferme ou Ouvert
    def getDoor(self, name):
        return GPIO.input(param.GPIO['Sensors']['Doors'][name][1])

    # Régule la maison
    def regulate(self):
        date = datetime.datetime.today()  # Contient la date du jour

