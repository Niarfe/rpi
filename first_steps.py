#!/usr/bin/env python
##    LED BLINKER   ##
#  LED Blinker on Pin 11 (Stolen from "Raspberry Pi User Guide" pg 194)
#  Ver. 0.1
#  August 5, 2013
#  J. Hobson
#  Just prior to this, I imported "raspberry-gpio-python"library  (ibid pg 190)


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
step_size = 0.01
duration = 28 

for i in range(duration):
    
    print "Start Pulse square wave"
    GPIO.output(10, True)
    GPIO.output(11, True)
    
    time.sleep(step_size)
    print "Set 10 to False"
    GPIO.output(10, False)
    GPIO.output(11, False)

    #time.sleep(step_size)

