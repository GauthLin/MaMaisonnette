<!-- Gestion de la chambre n°1 -->
<!DOCTYPE html>
<html>
    <head>
        <title>Chambre principale</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>

    
        <?php 	
        /*	
		include("functions.php");
		$ID_CHB = 1; 
		$temp_1_RPI= getinfoToRPi("GET_TEMP B");
		$temp_1_RPI= 30;
        */
		?>

 

        <?php
        include("header.php");      /*Affichage de l'en-tête*/
        ?>

        <p class="Controler">
            <?php echo "Contrôle de la chambre principale"; ?>
        </p>

        <?php
        include("controler.php");   /*Ajout zones de texte et boutons*/
        ?>
