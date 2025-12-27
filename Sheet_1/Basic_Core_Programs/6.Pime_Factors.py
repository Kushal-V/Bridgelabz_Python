def primeFact():
    val = int(input("Enter value of N: "))
    i = 2
    while val!= 1:
        if(val % i == 0):
            print(i)
            val = val // i
        else:
            i+=1

primeFact()