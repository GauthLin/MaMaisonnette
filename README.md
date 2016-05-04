# MaMaisonnette
## Communication avec la Raspberry Pi
La fonction **sendCommandToRPi** (dans le dossier functions.php) permet d'envoyer une commande à la Raspberry. Cette fonction contient 1 paramètre qui est la commande à exécuter. Les différentes commandes sont listées ci-dessous:

* SET_LAMP [status] : permet d'allumer/éteindre la lampe extérieure. Les valeurs possibles sont **0** ou **1**
* SET_TEMP [room] [value] : permet de définir une nouvelle température (value) pour la pièce (room) définit. Valeurs possibles **0** ou **1**.
* SET_MODE [room] [value] : permet de changer le mode de la pièce (room). Le mode peut être **AUTO**, **OFF**, **ON**. Les valeurs possibles pour [room] sont **A**, **B** et **C**.
* GET_WINDOW [room] : permet de récupérer les états des fenêtres. romm peut valoir: **BG**, **BD**, **C**, **D**
* SET_CONSIGNE [room] [temp] [start_date] [end_date] : permet d'ajouter une nouvelle consigne à la base de données. "start_date" et "end_date" doivent être sous format Timestamp.
* GET_DOOR [room] : permet de récupérer l'état des porte. room peut avoir les valeurs:  **AB**, **BC**, **BD**
* GET_DEFAULT_TEMP [room] : permet de récupérer la valeur par défaut des différentes pièces

Bisous les loups !
