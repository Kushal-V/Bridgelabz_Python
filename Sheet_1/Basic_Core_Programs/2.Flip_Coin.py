
def flip_coin():
    flip = int(input("Enter number of times to flip coin: "))
    if flip < 0:
        print("Invalid input")
        flip_coin()
    else:
        import random
        heads = 0
        tails = 0
        for i in range(flip):
            coin = random.randint(0,1)
            if coin < 0.5:
                heads += 1
            else:
                tails += 1
        print("Heads percentage = ", heads/flip*100)
        print("Tails percentage = ", tails/flip*100)

flip_coin()