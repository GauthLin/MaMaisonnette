<!DOCTYPE html>
<html>
    <head>
        <title>Chambre d'amis</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>

    
        <?php 
		include ("functions.php");		
		$ID_CHB = 3;
		
		if(IsSet($_POST['setTemp'])) {

			if ($ID_CHB == 3)
			{
				sendCommandToRPi('SET_TEMP C '.$_POST['setTemp']);
			}

		}
		
		if (IsSet($_POST['setTempVoulue']) && (IsSet($_POST['datepicker'])) && (IsSet($_POST['datepicker2']))){
			if ($ID_CHB == 3)
			{
				$timeStart = strtotime($_POST['datepicker']);
				$timeEnd = strtotime($_POST['datepicker2']);
				if($timeStart<$timeEnd){
					sendCommandToRPi('SET_CONSIGNE C '.$_POST['setTempVoulue'].' '.$timeStart.' '.$timeEnd);
				}
				else
				{
					echo '<p style="color:red"> La date de debut doit etre inferieure a la date de fin!</p>';
				}
				
			}
			
		}
        ?>
				




        <?php include("header.php");?> <!--En-tête-->
        

        <p class="Controler">
            <?php echo "Contrôle de la chambre d'amis"; ?>
        </p>

        <?php include("controler.php");?> <!--Zones de texte et boutons-->
        