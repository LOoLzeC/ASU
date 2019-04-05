
<html>
<head>
	<title>lo kontol</title>
</head>
<body>
<script>alert('hehe');</script>
<?php

	 /* (C) Copyright 407 Authentic Exploit
       Rebuild Copyright Can't make u real programmer:)
       Coded By Deray */
       
	$LOG=array(
		"ip" => $_SERVER["HTTP_X_FORWARDED_FOR"],
		"pr" => $_SERVER["REMOTE_PORT"],
		"ua" =>$_SERVER["HTTP_USER_AGENT"],
		"rq" =>$_SERVER["REQUEST_METHOD"]);
	$js=json_encode($LOG);
	$b=fopen("loggedIP.txt","a+");
	$c=fopen("haha.txt","w");
	fwrite($b,"$js
");
	fwrite($c,"$js
");
	fclose($b);
?>
memek
</body>
</html>
	