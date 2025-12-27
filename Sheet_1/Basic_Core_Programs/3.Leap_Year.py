def leap_year():
    year = int(input("Enter year: "))
    if(len(str(year)) != 4):
        print("Enter year in 4 digit")
        leap_year()
    else:
        if(year % 4 == 0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")

leap_year()