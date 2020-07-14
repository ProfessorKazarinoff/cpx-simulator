# main.py

from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.red_led = True
    elif cp.button_b:
        cp.red_led = True
