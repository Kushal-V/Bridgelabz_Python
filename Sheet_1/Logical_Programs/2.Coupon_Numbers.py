import random

def coupon():
    N = int(input("Enter N distinct coupon: "))
    count = 0
    number = set()
    while len(number) < N:
        a = random.randint(0,N-1)
        count += 1
        if a not in number:
            number.add(a)
    print(count)

coupon()