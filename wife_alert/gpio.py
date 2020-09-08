"""
Controls the GIPO pins on the RaspberryPi
by sending functions to a redis task queue
"""
import time

import RPi.GPIO as GPIO


def _setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT, inital=GPIO.LOW)


def make_blink():
    for _ in range(5):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
