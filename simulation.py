import hackathon

def check_weather():
    inp = input("Is it wet out? ")
    if (inp.lower() == "yes"):
        hackathon.moisture_sensor.weather = hackathon.moisture_sensor.mock_weather_state.WET
        hackathon.mpr121.adafruit_mpr121.weather = hackathon.mpr121.adafruit_mpr121.mock_weather_state.WET
    else:
        hackathon.moisture_sensor.weather = hackathon.moisture_sensor.mock_weather_state.DRY
        hackathon.mpr121.adafruit_mpr121.weather = hackathon.mpr121.adafruit_mpr121.mock_weather_state.DRY

def check_touch():
    inp = input("Is a pad touched? ")
    if (inp.lower() == "yes"):
        hackathon.mpr121.adafruit_mpr121.touch = hackathon.mpr121.adafruit_mpr121.mock_touch_state.TOUCH
    else:
        hackathon.mpr121.adafruit_mpr121.touch = hackathon.mpr121.adafruit_mpr121.mock_touch_state.NO_TOUCH

def main():
    hackathon.setup()

    iteration = 0

    while True:
        if (iteration % 100 == 0):
            check_weather()
            check_touch()
        hackathon.loop()
        iteration += 1

if __name__ == '__main__':
    main()