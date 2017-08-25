#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import time

# connect RPi numbered pins, connect button to RPi number 33 and GROUND
button = 33

# pins setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# wait for button press
GPIO.wait_for_edge(button, GPIO.FALLING)

# Command Play/Pause
while True:
        if (GPIO.input(button)== False):
                os.system('xbmc-send --action="PlayerControl(Play)"')
                time.sleep(0.5)

GPIO.cleanup()