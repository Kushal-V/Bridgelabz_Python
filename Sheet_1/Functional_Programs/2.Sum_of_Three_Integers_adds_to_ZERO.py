def sumOfThree():
    n = int(input("Enter N value: "))
    A = []
    for i in range(n):
        A.append(int(input("Enter value: ")))
    count = 0
    triplets = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if A[i]+A[j]+A[k] == 0:
                    count += 1
                    triplets.add((A[i],A[j],A[k]))
    print(count)
    print(triplets) 

sumOfThree()
