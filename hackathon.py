import sys
import signal
import time
import mpr121
import enum
import gpiozero import Buzzer

class WeatherStatus(enum):
    DRY = 0
    WET = 1

touched = [0] * mpr121.num_pins
calibration = [0] * mpr121.num_pins
# attach buzzer to pin 16
buzzer = Buzzer(16)
# to allow us to turn off the buzzer after a certain amount of time has passed
start = -1
max_on_time = 2

def main():
    # setup and cleanup need to go here, as do loop and calls
    calibration = mpr121.calibrate()
    pass

def read_moisture_sensor():
    pass

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

def is_touched():
    filtered = mpr121.get_filtered_data()
    touch_threshold, release_threshold = get_valid_threshold(read_moisture_sensor())

    difference = [0] * mpr121.num_pins

    # hysteresis - this is can seemingly be done on board, but we can also control manually here
    touch_count = 0
    for i in range(mpr121.num_pins):
        difference[i] = filtered[i] - calibration[i]
        if (difference[i] > touch_threshold):
            touched[i] = True
            touch_count++
        elif (difference < release_threshold):
            touched[i] = False
        else:
            touched[i] = touched[i]
    
    # if nothing is touched, turn off the buzzer
    if touch_count == 0:
        buzzer.off()
        start = -1
    # if at least one touch, register this as a touch
    else:
        send_touch()

def send_touch():
    # start being -1 means this is a new touch
    if start == -1:
        start = time.time() # track when we turned the buzzer on
        buzzer.on()
    
    # If the buzzer has been running for too long, turn it off
    # even if we're still registering a touch
    if time.time() - start >= max_on_time:
        buzzer.off

if __name__ == '__main__':
    main()