# mock
# python library: https://pypi.org/project/dht11/

import enum

class mock_weather_state(enum.Enum):
    DRY = 0
    WET = 1

weather = mock_weather_state.DRY

def read():
    if weather == mock_weather_state.WET:
        return 5
    else:
        return 1