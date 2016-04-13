#!/usr/bin/python

############################################################
#  Fichier contenant les parametres des GPIO               #
#  03/02/16 - Linard Gauthier - DIDOUH Mohamed - KADRI Ali #
############################################################

GPIO = {
    'Temp': {
        'A': ('out', 2),
        'B': ('out', 3),
        'C': ('out', 4),
        'D': ('out', 5)
    },
    'Doors': {
        'AB': ('out', 6),
        'BC': ('out', 7),
        'BD': ('out', 8)
    },
    'Windows': {
        'BG': ('out', 9),
        'BD': ('out', 10),
        'C': ('out', 11),
        'D': ('out', 12)
    },
    'Lamp': ('in', 13),
    'Heating': {
        'B': ('in', 24),
        'C': ('in', 25),
        'D': ('in', 26)
    }
}

MySql = dict(

)
