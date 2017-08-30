<?php
  $address = 'localhost';
  $username = 'weather';
  $password = 'station';
  $dbname = 'weather_station';

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
?>

<table>
  <tr>
    <th>Timestamp</th> <th>Temp</th> <th>Humidity</th> <th>Pressure</th>
  </tr>
  <?php while ($row = mysql_fetch_assoc($res)) { ?>
    <tr>
      <td><?php echo $row['reading_time']; ?></td>
      <td><?php echo $row['reading_temp']; ?></td>
      <td><?php echo $row['reading_humidity']; ?></td>
      <td><?php echo $row['reading_pressure']; ?></td>
    </tr>
  <?php } ?>
</table>

<?php mysql_close($conn); ?>
