"""
Controls the GIPO pins on the RaspberryPi
by sending functions to a redis task queue
"""
import time


def make_blink():
    for _ in range(5):
        print("---BLINK---", time.time())
        time.sleep(0.5)
