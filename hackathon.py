import sys
import signal
import time
import mpr121
import enum

class WeatherStatus(enum):
    DRY = 0
    WET = 1

touched = [0] * mpr121.num_pins

def main():
    # setup and cleanup need to go here, as do loop and calls
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
    baseline = mpr121.get_baseline_data()
    touch_threshold, release_threshold = get_valid_threshold(read_moisture_sensor())

    difference = [0] * mpr121.num_pins

    # hysteresis - this is can seemingly be done on board, but we can also control manually here
    for i in range(mpr121.num_pins):
        difference[i] = filtered[i] - baseline[i]
        if (difference[i] > touch_threshold):
            touched[i] = True
        elif (difference < release_threshold):
            touched[i] = False
        else:
            touched[i] = touched[i]

if __name__ == '__main__':
    main()