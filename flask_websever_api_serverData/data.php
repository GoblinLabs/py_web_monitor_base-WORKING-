<?php

$HOST = 'localhost';
$PORT = 3007;
$ENDPOINT = '/data';

$apiA = "http://" . $HOST . ":" . $PORT . $ENDPOINT;
$responseA = file_get_contents($apiA);
$jsonobjA  = json_decode($responseA, true);
    
    echo "<br>";
    echo $apiA;
    echo "<br>";

    echo "<pre>"; 
        print_r($jsonobjA);       
    echo "</pre>";

/*
    $data=$jsonobjA['data']['0'];
    
    $id=$data['id']; 
    $ip=$data['ip'];
    $hostname=$data['hostname'];
    $cpu=$data['cpu'];
    $ram_used=$data['ram_used'];
    $ram_tot=$data['ram_tot'];
    
    echo 
    "ID: " . $id . 
    " " . 
    "IP: " . $ip . 
    " " . 
    "HOST: " . $hostname . 
    " " .
    "RAM: " . number_format($ram_used,1) . "GB" . " / " . number_format($ram_tot,1) . "GB" .
    " " .
    "CPU: " . $cpu;
*/

?>
