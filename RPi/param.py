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
        'AB': ('in', 23),
        'BC': ('in', 24),
        'BD': ('in', 25)
    },
    'Windows': {
        'BG': ('in', 17),
        'BD': ('in', 4),
        'C': ('in', 27),
        'D': ('in', 22)
    },
    'Lamp': ('in', 10),
    'Heating': {
        'B': ('out', 7),
        'C': ('out', 8),
        'D': ('out', 9)
    }
}

