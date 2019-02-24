<?php
    $a=array(
    "lat" => $_GET["lat"],
    "lon" => $_GET["lon"]
    );
    $js=json_encode($a);
    $m=fopen("logMAP.txt","a+");
    $c=fopen("locate.txt","w");
    fwrite($c,"$js");
    fwrite($m,"$js");
    fclose($c);
    fclose($m);
?>