#!/usr/bin/python3

from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timedelta
from sys import exit
import PyMySql

#initialize program
sense = SenseHat()

#load config data
address = 'localhost'
username = 'weather'
password = 'station'
dbname = 'weather-station'
reading_delay = timedelta(hours=2)

#connect to mysql server
db = PyMySql.connect(address, username, password, dbname)
if db is None:
    print("Error: Weather Station could not connect to MySql server")
    sys.exit(1)

try:
    with db.cursor() as cursor:
        #make db if it doesn't exist
        sql = 'CREATE DATABASE IF NOT EXISTS %s;'
        cursor.execute(sql, (dbname))

        #make table if it doesn't exist
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
    while True:
        #get data
        temp = round(sense.get_temperature(), 2)
        pressure = round(sense.get_pressure(), 2)
        humidity = round(sense.get_humidity(), 2)

        #save in database
        with db.cursor() as cursor:
            sql = "INSERT INTO READINGS VALUES (DEFAULT, NOW(), %s, %s, %s)"
            try:
                cursor.execute(sql, (temp, pressure, humidity))
                db.commit()
            except:
                db.rollback()

        #wait one reading_delay
        cur_time = datetime.today()
        next_time = cur_time + reading_delay
        sleep((next_time-cur_time).seconds())

finally:
    db.close();
