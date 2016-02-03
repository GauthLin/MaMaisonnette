#!/usr/bin/python

###########################################################
## Programme principale
## 03/02/16 - Linard Gauthier - DIDOUH Mohamed - KADRI Ali
###########################################################

import param
import socket
import RPi.GPIO as GPIO

class MyHouse:
	# Constructeur
	def __init__(self):
		pass

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
	# numChauf : nom du chauffage
	# status : True ou False
	def heat(self, nameHeating, status):
		GPIO.output(param.Heating[numHeating], status)

	# Allume ou eteint la lampe
	# status : True ou False
	def lamp(self, status):
		GPIO.output(param.Lamp, status)

	# Todo : convertir la tension en degre celsius
	# Retourne la temperature d une piece
	def getTemp(self, name):
		return GPIO.input(param.Sensors['Temp'][name])

	# Retourne True ou False si fenetre Ferme ou Ouvert
	def getWindow(self, name):
		return GPIO.input(param.Sensors['Windows'][name])
		
	# Retourne True ou False si porte Ferme ou Ouvert
	def getDoor(self, name)
		return GPIO.input(param.Sensors['Doors'][name])

MyHouse = MyHouse()
