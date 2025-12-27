import math

def quadratic():
    print("Enter values of A, B, C in quadratic equation ax^2 + bx + c = 0")
    a = int(input("Enter A value: "))
    b = int(input("Enter B value: "))
    c = int(input("Enter C value: "))
    delta = b*b - 4*a*c
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        print(root1,root2)
    elif delta == 0:
        root = -b / (2*a)
        print(root)
    else:
        print("No real roots")

quadratic()