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
step_size = 0.05
duration = 10 

increment = 0.6
left_count = 0

for i in range(duration):
    left_count += increment

    print "Start Pulse square wave"
    if left_count > 1:
       GPIO.output(10, True)
       left_count -= 1
       print "Left side impulse " + str(left_count)
    GPIO.output(11, True)
    
    time.sleep(step_size)
    print "Set 10 to False"
    GPIO.output(10, False)
    GPIO.output(11, False)

    #time.sleep(step_size)

