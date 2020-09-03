"""
Controls the GIPO pins on the RaspberryPi
"""
import asyncio

from time import time


async def make_blink():
    for _ in range(5):
        print("---BLINK---", time())
        await asyncio.sleep(0.5)
