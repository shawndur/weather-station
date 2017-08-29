<?php
  $address = 'localhost';
  $username = 'weather';
  $password = 'station';
  $dbname = 'weather-station';

  $conn = mysql_connect($address, $username, $password);
  if (!$conn) {
    die("Could not connect to MySql" . mysql_error())
  }

  if (!mysql_select_db($dbname)) {
    die("Database could not be selected: " . mysql_error());
  }

  $sql = 'SELECT * FROM READINGS WHERE reading_time > now() - INTERVAL 1 DAY';
  $res = mysql_query($sql, $conn);
  if (!res) {
    die("Could not load data" . mysql_error());
  }

  mysql_close($conn);
?>
