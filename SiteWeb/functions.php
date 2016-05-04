 <meta charset="utf-8" />
<?php
function sendCommandToRPi($command) {
	if(!($sock = socket_create(AF_INET, SOCK_STREAM, 0)))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    die("Couldn't create socket: [$errorcode] $errormsg \n");
	}

	//Connect socket to remote server
	try {
		if(!socket_connect($sock , '172.17.10.71' , 1111))
		{
			$errorcode = socket_last_error();
			$errormsg = socket_strerror($errorcode);
			echo $errormsg;
			return(False);
		}
	}	catch (Exception $e) {
	}

	//Send the message to the server
	if(!socket_send($sock , $command , strlen($command) , 0))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    return(False);
	}

	return true;
}

function getinfoToRPi($command) {
	
	if(!($sock = socket_create(AF_INET, SOCK_STREAM, 0)))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    die("Couldn't create socket: [$errorcode] $errormsg \n");
	}

	//Connect socket to remote server
	try {
		$varConnection = socket_connect($sock , '172.17.10.71' , 1111);
	}	catch (Exception $e) {
		var_dump($e);
	}
		if(!$varConnection)
		{
			$errorcode = socket_last_error();
			$errormsg = socket_strerror($errorcode);
	
			return(False);
		}

	//Send the message to the server
	if( ! socket_write ( $sock , $command , strlen($command)))
	{
	    $errorcode = socket_last_error();
	    $errormsg = socket_strerror($errorcode);

	    return(False);
	}
	$buff="";
	if (False !==($bytes=socket_recv($sock,$buff,10,MSG_WAITALL)))
	{
		return $buff;
	}

	return False;
}
