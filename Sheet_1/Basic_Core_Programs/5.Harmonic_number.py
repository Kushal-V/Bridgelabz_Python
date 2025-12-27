def harmonic():
    val = int(input("Enter N value: "))
    if(val == 0):
        print("N can't be 0")
        harmonic()
    else:
        sum = 0
        for i in range(1,val+1):
            sum = sum + (1/i)
        print(sum)

harmonic()