from machine import Pin
from time import sleep
import dht

sensor=dht.DHT11(pin(2))

while (True):
    sensor.measure ()
    temp=sensor.temperature()
    him=sensor.humidity()
    print(temp)
    print(him)
    sleep(2)