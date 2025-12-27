import math

def distance():
    x = int(input("Enter X value: "))
    y = int(input("Enter Y value: "))
    distance = math.sqrt(x*x + y*y)
    print(distance)

distance()