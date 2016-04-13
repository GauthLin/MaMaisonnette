<ul>
 <li>Données actuelles</li>

    <p class="Answer">
       	<?php echo "T° : "; ?> <input readonly type="text" id="getTemp">
       	<?php echo "Fenêtre : "; ?> <input readonly type="text" id="getWindowState">
    </p>


 <li>Données voulues</li>

    <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/themes/ui-lightness/jquery-ui.css" type="text/css" media="all" />
 <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript"></script>
 <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js" type="text/javascript"></script>

 
 
     <p class="Value">
        <?php echo "T° : "; ?>	  <input type="text" id="setTemp">
        <?php echo "Du : "; ?>    <input type="text" id="datepicker">
        <?php echo "Au : "; ?>    <input type="text" id="datepicker2">
        <input type="submit" name="Bouton" value="Appliquer" class="Btn"/>
    </p>


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

</ul>

