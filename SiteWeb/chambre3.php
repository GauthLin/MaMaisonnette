<!--Gestion du salon-->

<!DOCTYPE html>
<html>
    <head>
        <title>Salon</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
	    <?php 
		include ("functions.php");		
		$ID_CHB = 3;
		
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
			

        <?php include("header.php");?>

        <p class="Controler">
            <?php echo "Contrôle du salon"; ?>
        </p>

        <?php include("controler.php");?>

       