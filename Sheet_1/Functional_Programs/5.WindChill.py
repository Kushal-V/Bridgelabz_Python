import math

def windChill():
    t = int(input("Enter temperature: "))
    v = int(input("Enter wind speed: "))
    if t < 50 and v < 120 and v > 3:
        w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
        print(w)
    else:
        print("Temperature should be less than 50 and wind speed should be between 3 and 120")

windChill()