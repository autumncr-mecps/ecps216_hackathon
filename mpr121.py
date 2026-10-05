import time
import board
import busio
import adafruit_mpr121

num_pins = 12

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

def get_filtered(pin):
    return mpr121.filtered_data(pin)

def get_baseline(pin):
    return mpr121.baseline_data(pin)

def get_filtered_data():
    filtered = [0]*num_pins
    for i in range(num_pins):
        filtered[i] = get_filtered(i)
    return filtered

def get_baseline_data():
    baseline = [0]*num_pins
    for i in range(num_pins):
        baseline[i] = get_baseline(i)
    return baseline
