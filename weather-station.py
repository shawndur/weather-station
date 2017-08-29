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
    with db.cursor() as cursor:

#check if table exists
  #if not create table

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
