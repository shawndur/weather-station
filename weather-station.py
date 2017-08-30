#!/usr/bin/python3

from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timedelta
from sys import exit
import pymysql

#initialize program
sense = SenseHat()

#load config data
address = 'localhost'
username = 'weather'
password = 'station'
dbname = 'weather_station'
reading_delay = timedelta(seconds = 10)

#connect to mysql server
db = pymysql.connect(address, username, password)
if db is None:
    print("Error: Weather Station could not connect to MySql server")
    sys.exit(1)

try:
    with db.cursor() as cursor:
        #make db if it doesn't exist
        sql = 'CREATE DATABASE IF NOT EXISTS ' + dbname + ';'
        print (cursor.mogrify(sql))
        cursor.execute(sql)

        #select db
        sql = 'USE ' + dbname + ';'
        print (cursor.mogrify(sql))
        cursor.execute(sql)

        #make table if it doesn't exist
        sql = """
        CREATE TABLE IF NOT EXISTS readings (
          reading_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
          reading_time TIMESTAMP NOT NULL UNIQUE,
          reading_temp DECIMAL(5,2) NOT NULL,
          reading_pressure DECIMAL(6,2) NOT NULL,
          reading_humidity DECIMAL(5,2) NOT NULL,
          PRIMARY KEY(reading_id)
        );
        """
        print (cursor.mogrify(sql))
        cursor.execute(sql)

    #main loop
    while True:
        #get data
        temp = round(sense.get_temperature(), 2)
        pressure = round(sense.get_pressure(), 2)
        humidity = round(sense.get_humidity(), 2)

        #save in database
        with db.cursor() as cursor:
            sql = "INSERT INTO readings VALUES (DEFAULT, NOW(), %s, %s, %s)"
            try:
                print (cursor.mogrify(sql, (temp, pressure, humidity)))
                cursor.execute(sql, (temp, pressure, humidity))
                db.commit()
            except:
                db.rollback()

        #wait one reading_delay
        sleep(reading_delay.seconds)

finally:
    db.close();
