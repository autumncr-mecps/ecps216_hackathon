import time
import mpr121
import enum
import moisture_sensor
from gpiozero import Buzzer

import atexit
import signal
import sys

def cleanup():
    print("Cleaning up!")

def handle_sigint(signum, frame):
    sys.exit(0)  # This triggers atexit

atexit.register(cleanup)
signal.signal(signal.SIGINT, handle_sigint)

class WeatherStatus(enum.Enum):
    DRY = 0
    WET = 1

touched = [0] * mpr121.num_pins
calibration = [0] * mpr121.num_pins

# attach buzzer to pin 16
buzzer = Buzzer(16)
# to allow us to turn off the buzzer after a certain amount of time has passed
start = -1
max_on_time = 2

def setup():
    global calibration
    calibration = mpr121.calibrate()
    print(calibration)

def main():
    setup()

    while True:
        loop()

def read_moisture_sensor(): # read moisture sensor, currently mocked
    return moisture_sensor.read()

def get_valid_threshold(moisure_value) -> tuple[int,int]:
    # @TODO: figure out what value
    someval = 3
    status = WeatherStatus.DRY
    if moisure_value > someval:
        status = WeatherStatus.WET
    
    # @TODO: testing will show what touch and release thresholds to use
    wet_touch = 20
    wet_release = 10
    dry_touch = 12
    dry_release = 6
    if status == WeatherStatus.WET:
        return wet_touch, wet_release
    else:
        return dry_touch, dry_release

def loop():
    is_touched()

def is_touched():
    global calibration, start
    filtered = mpr121.get_filtered_data()
    baseline = mpr121.get_baseline_data()
    touch_threshold, release_threshold = get_valid_threshold(read_moisture_sensor())

    difference = [0] * mpr121.num_pins

    # hysteresis - this is can seemingly be done on board, but we can also control manually here
    touch_count = 0
    for i in range(mpr121.num_pins):
        difference[i] = filtered[i] - baseline[i]
        if (difference[i] >= touch_threshold):
            touched[i] = True
            touch_count += 1
        elif (difference[i] < release_threshold):
            touched[i] = False
        else:
            touched[i] = touched[i]

    print(difference)
    
    # if nothing is touched, turn off the buzzer
    if touch_count == 0:
        buzzer.off()
        start = -1
    # if at least one touch, register this as a touch
    else:
        send_touch()

def send_touch():
    global start
    # start being -1 means this is a new touch
    if start == -1:
        start = time.time() # track when we turned the buzzer on
        buzzer.on()
    
    # If the buzzer has been running for too long, turn it off
    # even if we're still registering a touch
    if time.time() - start >= max_on_time:
        print("Too much time on.")
        buzzer.off()

def check_weather():
    inp = input("Is it wet out? ")
    if (inp.lower() == "yes"):
        moisture_sensor.weather = moisture_sensor.mock_weather_state.WET
        mpr121.adafruit_mpr121.weather = mpr121.adafruit_mpr121.mock_weather_state.WET
    else:
        moisture_sensor.weather = moisture_sensor.mock_weather_state.DRY
        mpr121.adafruit_mpr121.weather = mpr121.adafruit_mpr121.mock_weather_state.DRY

def check_touch():
    inp = input("Is a pad touched? ")
    if (inp.lower() == "yes"):
        mpr121.adafruit_mpr121.touch = mpr121.adafruit_mpr121.mock_touch_state.TOUCH
    else:
        mpr121.adafruit_mpr121.touch = mpr121.adafruit_mpr121.mock_touch_state.NO_TOUCH

def simulate():
    setup()

    iteration = 0

    while True:
        if (iteration % 100 == 0):
            check_weather()
            check_touch()
        loop()
        iteration += 1


if __name__ == '__main__':
    simulate()