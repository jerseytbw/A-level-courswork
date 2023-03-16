# initial set up of imports
from threading import Timer
import seeed_dht
import time
import datetime
# csv to be able to open file
import csv
import RPi.GPIO as GPIO
import DHT11_setup as dht11

# humididty and temp

def humi_temp():
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 14
    instance = dht11.DHT11(pin=14)
    result = instance.read()
    return (result)


def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%y")
    today = str(today)
    return (today)


def time_now():
    now = datetime.datetime.now().strftime("%H-%M-%S")
    now = str(now)
    return (now)


def Time_Float():
    # %day %month %year.%Hour%Minute%Ssecond%
    now = datetime.datetime.now().strftime("%d%m%y.%H%M%S")
    now = str(now)
    return (now)


def write_to_csv():
    #a is for append, if w for write is used then it overwrites the file
    with open("Sensor.csv", mode="a") as sensor_readings:
        sensor_write = csv.writer(sensor_readings, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_log = sensor_write.writerow([date_now(), time_now(), Time_Float(), humi_temp()])  # ,get_pressure()])
        return (write_to_log)


i = 1


def display():
    t = Timer(5, write_to_csv)
    t.start()


while i == 1:
    print(i)
    i = i + 1
    display()
    i = i - 1
    time.sleep(3)


