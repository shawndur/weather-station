<?php
  require_once("../../resources/config.php");

  $address = $config['db']['addr'];
  $username = $config['db']['user'];
  $password = $config['db']['pass'];
  $dbname = $config['db']['dbname'];

  $conn = mysql_connect($address, $username, $password);
  if (!$conn) {
    die("Could not connect to MySql" . mysql_error());
  }

  if (!mysql_select_db($dbname)) {
    die("Database could not be selected: " . mysql_error());
  }

  $sql = 'SELECT * FROM readings WHERE reading_time > now() - INTERVAL 1 DAY';
  $res = mysql_query($sql, $conn);
  if (!$res) {
    die("Could not load data" . mysql_error());
  }

  $return_string = '';

  while ($row = mysql_fetch_assoc($res)) {
    $return_string .= "
      <tr>
        <td>$row[reading_time]</td>
        <td>$row[reading_temp]</td>
        <td>$row[reading_humidity]</td>
        <td>$row[reading_pressure]</td>
      </tr>
    ";
  }

  mysql_close($conn);

  echo $return_string;
?>
