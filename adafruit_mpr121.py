# mock
import enum

class mock_weather_state(enum.Enum):
    DRY = 0
    WET = 1

class mock_touch_state(enum.Enum):
    NO_TOUCH = 0
    TOUCH = 1

weather = mock_weather_state.DRY
touch = mock_touch_state.NO_TOUCH

class MPR121():
    def __init__(self, i2c):
        self.i2c = i2c

    def baseline_data(self, pin):
        if (weather == mock_weather_state.WET):
            return 45. # just a random number
        else:
            return 20. # just a random number

    def filtered_data(self, pin): # i just picked random numbers to mock this
        if (weather == mock_weather_state.WET):
            if (touch == mock_touch_state.NO_TOUCH):
                return 48.
            else:
                return 78.
        else:
            if (touch == mock_touch_state.NO_TOUCH):
                return 20.
            else:
                return 40.