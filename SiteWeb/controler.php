<ul>

<!--Relevé des données de la maison-->

 <li>Données actuelles</li>
	
    
	<?php

	
	echo '<p class="Answer">';
	
	if ($ID_CHB == 1)
	{
	$temp_1_RPI= getinfoToRPi("GET_TEMP D");
	$temp_1_Default = getinfoToRPi("GET_DEFAULT_TEMP D");
	$fenetre_1 = getinfoToRPi ("GET_WINDOW D");
	echo 'T° :  <input readonly type="text" id="getTemp"; value= "'.$temp_1_RPI.'">';
	echo' Fenêtre :   <input readonly type="text" id="getWindowState" value ="'.$fenetre_1.'">';
	}
	if ($ID_CHB == 2)
	{
	$temp_2_RPI= getinfoToRPi("GET_TEMP B");
	$temp_2_Default = getinfoToRPi("GET_DEFAULT_TEMP B");
	$fenetre_2_1 = getinfoToRPi ("GET_WINDOW BG");
	$fenetre_2_2 = getinfoToRPi ("GET_WINDOW BD");	
	echo 'T° :  <input readonly type="text" id="getTemp" value= "'.$temp_2_RPI.'">';
	echo' Fenêtre 1 :   <input readonly type="text" id="getWindowState" value ="'.$fenetre_2_1.'">';
	echo' Fenêtre 2 :   <input readonly type="text" id="getWindowState" value ="'.$fenetre_2_2.'">';
	}
	if ($ID_CHB == 3)
	{
	$temp_3_RPI= getinfoToRPi("GET_TEMP C");
	$temp_3_Default = getinfoToRPi("GET_DEFAULT_TEMP C");
	$fenetre_3 = getinfoToRPi ("GET_WINDOW C");		
	echo 'T° :  <input readonly type="text" id="getTemp" value= "'.$temp_3_RPI.'">';
	echo' Fenêtre :   <input readonly type="text" id="getWindowState" value ="'.$fenetre_3.'">';
	}
	echo '</p>';
	?>
    

<!--Choix des données voulues-->

 <li>Données voulues</li>

 <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/themes/ui-lightness/jquery-ui.css" type="text/css" media="all" />
 <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript"></script>
 <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js" type="text/javascript"></script>

 
 	<form action="chambre<?php echo $ID_CHB; ?>.php" method="post">
		<p class="Value">

			<?php echo "T° : "; ?>	  <input type="text" id="setTempVoulue" name="setTempVoulue">
			<?php echo "Du : "; ?>    <input type="text" id="datepicker" name="datepicker">
			<?php echo "Au : "; ?>    <input type="text" id="datepicker2" name="datepicker2">
			<input type="submit" name="Bouton" value="Appliquer" class="Btn"/>
		</p>
	 </form>

<!--Javascript pour la gestion du calendrier-->

   <script type="text/javascript">
   $(function() {
   	$("#datepicker" ).datepicker({
        beforeShowDay: function(date){
          var b = (date.getDay() < 7);
          var c = b ? "": "ui-state-disabled";
          return [b, c];
        }
      });

   	$("#datepicker2" ).datepicker({
        beforeShowDay: function(date){
          var b = (date.getDay() < 7);
          var c = b ? "": "ui-state-disabled";
          return [b, c];
        }
      });
   });
   </script>

   <!--Choix d'une température par défaut-->
   <li>Par défaut</li>
   
   <form action="chambre<?php echo $ID_CHB; ?>.php" method="post">
		<p class="Value">
			<?php if ($ID_CHB == 1)	
				echo 'T° :  <input  type="number" id="getTemp"; value= "'.$temp_1_Default.'" name ="setTemp">';
			 if ($ID_CHB == 2)	
				echo 'T° :  <input  type="number" id="getTemp"; value= "'.$temp_2_Default.'" name ="setTemp">';
			 if ($ID_CHB == 3)	
				echo 'T° :  <input  type="number" id="getTemp"; value= "'.$temp_3_Default.'" name ="setTemp">';
			?>
			<input type="submit" name="Bouton" value="Appliquer" class="Btn" />
		</p>
	</form>

</ul>

