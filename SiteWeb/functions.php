<?php
function sendCommandToRPi($command) {
	if(!($sock = socket_create(AF_INET, SOCK_STREAM, 0)))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    die("Couldn't create socket: [$errorcode] $errormsg \n");
	}

	//Connect socket to remote server
	if(!socket_connect($sock , '172.17.10.60' , 1111))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    die("Could not connect: [$errorcode] $errormsg \n");
	}

	//Send the message to the server
	if( ! socket_send ( $sock , $command , strlen($command) , 0))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    die("Could not send data: [$errorcode] $errormsg \n");
	}

	return true;	
}
