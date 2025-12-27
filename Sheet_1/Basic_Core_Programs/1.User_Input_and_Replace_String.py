def username():
    name = input("Enter username: ")
    if(len(name) < 3):
        print("Username is too short")
        username()
    else:
        print("Hello", name, "How are you?")

username()
