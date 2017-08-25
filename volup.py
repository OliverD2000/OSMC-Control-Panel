#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import time

# connect RPi numbered pins, connect button to RPi number 31 and GROUND
volupbutton = 31

# pins setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(volupbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# wait for button press
GPIO.wait_for_edge(volupbutton, GPIO.FALLING)

# Command Volume Up, long button pressing means Volume gets higher and higher
while True:
        if(GPIO.input(volupbutton)== False):
                os.system('xbmc-send --action="VolumeUP"')

GPIO.cleanup()