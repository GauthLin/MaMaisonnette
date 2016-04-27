# !/usr/bin/python
# -*- coding: utf-8 -*-

# @author: Gauthier Linard
# @date: 08.04.2016

from struct import unpack

import quick2wire.i2c as i2c
#import param
#from debug import *


class I2CManager:
    """
    Cette classe contient toutes les méthodes nécessaires à la communication I2C
    """
    def __init__(self):
        self.address = 0x08
        self.bus = i2c.I2CMaster()

    def read(self):
        """
        Permet d'aller lire sur l'Arduino

        Args:
            howMany: le nombre de bytes que l'on veut lire

        Returns:
            data: informations de la communication
        """
        print("Reading a l adresse %i" % self.address)
        data = self.bus.transaction(i2c.reading(self.address, 8))
        print(data)
        return unpack(data)

    def unPack(self, data):
        """
        Permet de convertir les bytes reçues lors de la communication I2C en entier non signé

        Args:
            data: les données de la communication
                data[0]: contient le nombre de bytes lues

        Returns:
            Array: tableau contenant la valeur des roues codeuses
        """
        d = unpack('BBBBBBBB', data[0])
        tempA = int.from_bytes([d[0], d[1]], byteorder='big', signed=False)
        tempB = int.from_bytes([d[2], d[3]], byteorder='big', signed=False)
        tempC = int.from_bytes([d[4], d[5]], byteorder='big', signed=False)
        tempD = int.from_bytes([d[6], d[6]], byteorder='big', signed=False)
        return [tempA, tempB, tempC, tempD, RCDroit, RCGauche]
