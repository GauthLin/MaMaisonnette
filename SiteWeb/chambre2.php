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
		$ID_CHB = 2;
		
		if(IsSet($_POST['setTemp'])) {
			
			echo $ID_CHB;


			if ($ID_CHB == 1)
			{
				sendCommandToRPi('SET_TEMP A '.$_POST['setTemp']);
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
				


	<!--		
		// fonction d'envoie des températures ...
		if (isset ($_POST ["temp_chamb1"])){

			$temp_2 = $_POST ["temp_chamb2"];
			
			if (!sendCommandToRPi ("SET_TEMP B ". $temp_2)){
				echo "connect failed";
			}
			if (!sendCommandToRPi ("SET_MODE ". $_POST['Mode']." B")){
				echo "connect failed";
			}
		}*/
		// reception des température de la maison

		//
			//$temp_2_RPI= 15;
		
		// reception des fenetre et porte de la maison 
		
/*		echo '<form action="chambre2.php" method="post">
		
		<label for="Temp_2">Température chambre 2: </label><input type="number" value="' . $temp_2_RPI . '" min="15" name="temp_chamb2"><br>
		<label for="mode"> Mode de fonctionnement
		<select name="Mode">
		';
		if (isset ($_POST ["Mode"]) && $_POST['Mode']=="AUTO")
		{
			echo'<option value="AUTO" selected>AUTO</option>';
		}
		else
		{
			echo'<option value="AUTO">AUTO</option>';
		}
		if (isset ($_POST ["Mode"]) && $_POST['Mode']=="ON")
		{
			echo'<option value="ON" selected>ON</option>';
		}
		else
		{
			echo'<option value="ON">ON</option>';
		}
		if (isset ($_POST ["Mode"]) && $_POST ['Mode']=="OFF")
		{
			echo'<option value="OFF" selected>OFF</option>';
		}
		else
		{
			echo'<option value="OFF">OFF</option>';
		}
		
		echo'
		</select>
		<br>
		<input type="submit" value= "ok" >
		
		</form>
		';
		}
		}
		*/?>
		-->

        <?php include("header.php");?> <!--En-tête-->
        

        <p class="Controler">
            <?php echo "Contrôle de la chambre d'amis"; ?>
        </p>

        <?php include("controler.php");?> <!--Zones de texte et boutons-->
        