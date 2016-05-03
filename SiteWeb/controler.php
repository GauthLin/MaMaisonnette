<ul>

<!--Relevé des données de la maison-->

 <li>Données actuelles</li>
	
    
	<?php
	echo $ID_CHB;
	
	echo '<p class="Answer">';
	if ($ID_CHB == 1)
	{
	$temp_1_RPI= getinfoToRPi("GET_TEMP A");	
	echo 'T° :  <input readonly type="text" id="getTemp"; value= "'.$temp_1_RPI.'">';
	echo' Fenêtre :   <input readonly type="text" id="getWindowState">';
	}
	if ($ID_CHB == 2)
	{
	$temp_2_RPI= getinfoToRPi("GET_TEMP B");	
	echo 'T° :  <input readonly type="text" id="getTemp" value= "'.$temp_2_RPI.'">';
	echo' Fenêtre :   <input readonly type="text" id="getWindowState">';
	}
	if ($ID_CHB == 3)
	{
	$temp_3_RPI= getinfoToRPi("GET_TEMP C");	
	echo 'T° :  <input readonly type="text" id="getTemp" value= "'.$temp_3_RPI.'">';
	echo' Fenêtre :   <input readonly type="text" id="getWindowState">';
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

        <?php echo "T° : "; ?>	  <input type="text" name="setTemp">
        <?php echo "Du : "; ?>    <input type="text" name="datepicker">
        <?php echo "Au : "; ?>    <input type="text" name="datepicker2">
        <input type="submit" name="Bouton" value="Appliquer" class="Btn" onclick ="Btn()"/>

    </p>
	 </form>

<!--Javascript pour la gestion du calendrier-->

   <script type="text/javascript">
   $(function() {
   	$("#datepicker" ).datepicker({
        beforeShowDay: function(date){
          var b = (date.getDay() < 5);
          var c = b ? "": "ui-state-disabled";
          return [b, c];
        }
      });

   	$("#datepicker2" ).datepicker({
        beforeShowDay: function(date){
          var b = (date.getDay() < 5);
          var c = b ? "": "ui-state-disabled";
          return [b, c];
        }
      });
   });
   </script>

   <!--Choix d'une température par défaut-->
   <li>Par défaut</li>
   <p class="Value">
        <?php echo "T° : "; ?>    <input type="number" min="0" max="30" value="18"  id="setTemp">
        <input type="submit" name="Bouton" value="Appliquer" class="Btn"/>
    </p>

</ul>

