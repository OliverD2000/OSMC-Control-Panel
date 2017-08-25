#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import time

# connect RPi numbered pins, connect button to RPi number 35 and GROUND
nextbutton = 35

# pins setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(nextbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# wait for button press
GPIO.wait_for_edge(nextbutton, GPIO.FALLING)

# Command Play previous song
# works only if you play music directly from the Raspi or for example from any connected external hard drive
# not working with UPNP streaming via Smartphone
while True:
        if(GPIO.input(nextbutton)== False):
                os.system('xbmc-send --action="PlayerControl(Next)"')
                time.sleep(0.5)
GPIO.cleanup()