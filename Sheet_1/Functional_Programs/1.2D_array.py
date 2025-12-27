def array():
    row = int(input("Enter number of rows: "))
    col = int(input("Enter number of col: "))
    list = []

    for i in range (row):
        val = []
        for j in range (col):
            a = input(f"Enter value of [{i}][{j}]: ")
            if a == "true":
                a = True
            elif a == "false":
                a = False
            elif a.isdigit():
                a = int(a)
            elif "." in a:
                a = float(a)
            val.append(a)
        list.append(val)

    print(list)

array()