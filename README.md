# MaMaisonnette
## Communication avec la Raspberry Pi
La fonction **sendCommenandToRPi** permet d'envoyer une commande à la Raspberry. Cette fonction contient 1 paramètre qui est la commande à exécuter. Les différentes commandes sont listées ci-dessous:

* SET_LAMP [status] : permet d'allumer/éteindre la lampe extérieure. Les valeurs possibles sont **0** ou **1**
* SET_TEMP [room] [value] : permet de définir une nouvelle température (value) pour la pièce (room) définit. Valeurs possibles **0** ou **1**.
* SET_MODE [room] [value] : permet de changer le mode de la pièce (room). Le mode peut être **AUTO**, **OFF**, **ON**.

Bisous les loups !