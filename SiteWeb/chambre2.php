<!DOCTYPE html>
<html>
    <head>
        <title>Chambre d'amis</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>

        <?php 	include("header.php");
				include("functions.php");
		if (isset ($_POST ["temp_chamb1"])){
			$temp_1 = $_POST ["temp_chamb1"];
			$temp_2 = $_POST ["temp_chamb2"];
			$temp_3 = $_POST ["temp_chamb3"];
			
			if (!sendCommandToRPi ("SET_TEMP A ". $temp_1)){
			echo "connect failed";
			}
			if (!sendCommandToRPi ("SET_TEMP B ". $temp_2)){
				echo "connect failed";
			}
			if (!sendCommandToRPi ("SET_TEMP C ". $temp_3)){
				echo "connect failed";
			}
			if (!sendCommandToRPi ("SET_MODE ". $_POST['Mode']." A")){
				echo "connect failed";
			}
		}
		// reception des température de la maison
		$temp_1_RPI= getinfoToRPi("GET_TEMP A");
		$temp_2_RPI= getinfoToRPi("GET_TEMP B");
		$temp_3_RPI= getinfoToRPi("GET_TEMP C");
		
		// reception des fenetre et porte de la maison 
		
		echo '<form action="chambre2.php" method="post">
		<label for="Temp_1">Température chambre 1: </label><input type="number" value="' . $temp_1_RPI . '" min="15" name="temp_chamb1"><br>
		<label for="Temp_2">Température chambre 2: </label><input type="number" value="' . $temp_2_RPI . '" min="15" name="temp_chamb2"><br>
		<label for="Temp_2">Température chambre 3: </label><input type="number" value="' . $temp_3_RPI . '" min="15" name="temp_chamb3"><br>
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
		<input type="submit" value= "ok">
		</form>
		';
		?>
	
		<!-- BENJA -->
        <?php include("header.php"); ?>

        <p class="Controler">
            <?php echo "Contrôle de la chambre d'amis"; ?>
        </p>

        <?php include("controler.php"); ?>