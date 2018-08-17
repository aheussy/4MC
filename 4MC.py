import sys

import time
from decimal import Decimal
import random
import datetime
import sqlite3
import Adafruit_DHT

conn = sqlite3.connect('IRC_IOT_B_Pi1.db')
c = conn.cursor()

local = "Oven 1"
ts = 0
pin = 4
status = "RED"

sensor = Adafruit_DHT.DHT22
##

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))



message_blue ="Work continues as normal"
message_green = "Make sure you drink plenty of water"
message_yellow = "75% Work 25% Rest Balance - No more than 45 minutes work without a 15 minute break"
message_orage = "50% Work 50% Rest Balance - No more than 30 minutes work without a 30 minute break"
message_red = "25% Work 75% Rest Balance - No more than 15 minutes work without a 45 minute break"
message_grey = "No work allowed without consulting industrial hygienist first"





def monitor_4MC_Condition(temp, humidity):
    ## variable correction, conversion
    temp = temp* 9/5.0 +32
    #temp = Decimal(temp) 
    #humidity = Decimal(humidity)
    temp= round(temp,2) 
    humidity= round(humidity, 2)
    
    BreakHourInterval = 1
    
    ## BLUE
    if temp in range(70, 75) and humidity > 70:
        status = "BLUE"
        BreakHourInterval = 6
    elif temp <= 80 and humidity <= 80:
        status = "BLUE"
        BreakHourInterval = 8
        
    ## GREEN
    elif temp <= 80 and humidity <= 80:
        status = "GREEN"
        BreakHourInterval = 5
        
    ## YELLOW
    elif temp <= 85 and humidity <= 70:
        status = "YELLOW"
        BreakHourInterval = 5
    elif temp <= 90 and humidity <= 50:
        status = "YELLOW"
        BreakHourInterval = 8
    ## RED
    elif temp >= 85 and humidity >= 70:
        status = "RED"
        BreakHourInterval = 3
    elif temp >= 90 and humidity >= 60:
        status = "RED"
        BreakHourInterval = 4
    ## GREY
    elif temp >= 90 and humidity >= 70:
        status = "GREY"
        BreakHourInterval = 0
        
 
    
    c.execute("INSERT INTO MCcondition (unix, datestamp, local, status, temp, humid) VALUES (?, ?, ?, ?, ?, ?)",
              (unix, date, local, status, temp, humidity))
    conn.commit()
    print(status)
    print("Temp: ", temp)
    print("Humidity: ", humidity)
    print("@: ", date, " Pacific Std")
    print("")
   
try: 
    while True:
        humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
        monitor_4MC_Condition(temp, humidity)
        time.sleep(300)
except KeyboardInterrupt:
    pass
##
##while True:
##    print(" The temp is: ",temp, " and humidity is: ", humidity)
##    print(ts, "  ", i)
##    time.sleep()
##    print("")