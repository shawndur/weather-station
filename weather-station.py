#!/usr/bin/python3

from sense_hat import SenseHat
import PyMySql
import sys

#initialize program
#load config data
address = 'localhost'
username = 'weather'
password = 'station'
dbname = 'weather-station'

#connect to mysql server
db = PyMySql.connect(address, username, password, dbname)
if db is None:
    print("Error: Weather Station could not connect to MySql server")
    sys.exit(1)

try:
    #make table if it doesn't exist
    with db.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS READINGS (
          reading_id UNSIGNED NOT NULL AUTO_INCREMENT,
          reading_time TIMESTAMP NOT NULL UNIQUE,
          reading_temp DECIMAL(5,2) NOT NULL,
          reading_pressure DECIMAL(6,2) NOT NULL,
          reading_humidity DECIMAL(5,2) NOT NULL,
          PRIMARY KEY(reading_id)
        );
        """
        cursor.execute(sql)

#main loop
 #every time unit
  #get data
   #get temp from pressure
   #get temp from humidity
   #find average temp
   #get pressure
   #get humidity
  #store data in server

finally:
    db.close();
