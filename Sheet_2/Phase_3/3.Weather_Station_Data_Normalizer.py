# weather_data = {"station1": {"temp": 32, "unit": "F"}, "station2": {"temp": 0, "unit": "C"}}

import json

def main():
    
    print("Enter the weather data:")
    weather_data = json.loads(input())

    absolute_zero = -273.15
    
    def convert_to_celsius(item):
        station,data = item
        temp = data["temp"]
        unit = data["unit"]
        temp_c = (temp - 32) * 5 / 9 if unit == "F" else temp
        return station,temp_c

    converted_data = {
        station:{
            "temp": temp_c,
            "unit": "C"
        }
        for station,temp_c in map(convert_to_celsius, weather_data.items())
        if temp_c >= absolute_zero
    }
    print(converted_data)

main()
