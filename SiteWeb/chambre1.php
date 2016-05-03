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

		include ("functions.php");		
		$ID_CHB = 1;
		
		if(IsSet($_POST['setTemp'])) {

			if ($ID_CHB == 1)
			{
				sendCommandToRPi('SET_TEMP D '.$_POST['setTemp']);
			}
			if ($ID_CHB == 2)
			{
				sendCommandToRPi('SET_TEMP B '.$_POST['setTemp']);

			}
			if ($ID_CHB == 3)
			{
				sendCommandToRPi('SET_TEMP C '.$_POST['setTemp']);
			}
		}

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
