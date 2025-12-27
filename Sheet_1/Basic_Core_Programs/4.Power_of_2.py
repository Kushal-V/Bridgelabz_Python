def table():
    val = int(input("Enter value between 0 to 31: "))
    if(val < 0 or val > 31):
        table()
    else:
        for i in range (0,val):
            print(2**i)

table()
