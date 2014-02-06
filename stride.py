#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
duration = 30 

gpio_pin =  [10,   11]

stride   =  [0.01, 0.01]
speed_damp = 0.00

def one_stride( _gpio_pin, _stride):

    GPIO.output(_gpio_pin, True)
    print str(_gpio_pin) +  " side impulse "
    time.sleep(_stride)
    GPIO.output(_gpio_pin, False)

side = 0
for i in range(duration):

    one_stride(gpio_pin[side], stride[side])

    time.sleep(speed_damp)

    if side == 0:
      side = 1
    else:
      side = 0

