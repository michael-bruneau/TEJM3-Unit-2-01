"""
Created by: Michael Bruneau
Created on: Feb 2025
This module is a Raspberrypy Pico program that causes a light to blink
"""

# This program uses python

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)

    led.value = False
    time.sleep(1)
    