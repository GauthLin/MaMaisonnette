<?php
	include ("functions.php");
		echo $ID_CHB;
	function Btn(){

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