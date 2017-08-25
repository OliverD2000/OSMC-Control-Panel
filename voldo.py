#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import time

# connect RPi numbered pins, connect button to RPi number 40 and GROUND
voldobutton = 40

# pins setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(voldobutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# wait for button press
GPIO.wait_for_edge(voldobutton, GPIO.FALLING)

# Command Volume Down, long button pressing means Volume gets lower and lower
while True:
        if(GPIO.input(voldobutton)== False):
                os.system('xbmc-send --action="VolumeDown"')

GPIO.cleanup()