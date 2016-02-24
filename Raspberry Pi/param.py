#!/usr/bin/python

############################################################
## Fichier contenant les parametres des GPIO               #
## 03/02/16 - Linard Gauthier - DIDOUH Mohamed - KADRI Ali #
############################################################

Sensors = dict(
    Temp=dict(
        A=None,
        B=None,
        C=None,
        D=None
    ),
    Doors=dict(
        AB=None,
        BC=None,
        BD=None
    ),
    Windows=dict(
        B=dict(
            Gauche=None,
            Droite=None
        ),
        C=None,
        D=None
    )
)

Lamp = 18

Heating = dict(
    B=24,
    C=None,
    D=None
)

MySql = dict(

)
