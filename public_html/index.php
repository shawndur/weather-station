<?php
  $address = 'localhost';
  $username = 'weather';
  $password = 'station';
  $dbname = 'weather-station';
  $conn = mysql_connect($address, $username, $password);
  if (!$conn) {
    die("Could not connect to MySql")
  }
  if (!mysql_select_db($dbname)) {
    die("Database could not be selected");
  }

  mysql_close($conn);
?>
