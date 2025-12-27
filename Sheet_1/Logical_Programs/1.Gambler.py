import random

def gambler():
    stake = int(input("Enter stake: "))
    goal = int(input("Enter goal: "))
    times = int(input("Enter number of times: "))
    win = 0
    loss = 0
    for i in range(times):
        cash = stake
        while cash > 0 and cash < goal:
            if random.randint(0,1) == 0:
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            win += 1
        else:
            loss += 1
    print("Number of wins: ",win)
    print("Number of loss: ",loss)
    print("Percentage of wins: ",win/times)
    print("Percentage of losses: ",loss/times)

gambler()