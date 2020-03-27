usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("login Sucessful.")
    i = 0
    while i == 0:
        print("List Product")
        print("What do you want?")
        print("1 : Apple")
        print("2 : Papaya")
        print("3 : Banana")
        print("4 : Orange")
        print("5 : Finish")
        userInput = int(input(">> "))
        if userInput == 1:
            print("How many do you want?")
            priceInput = int(input(">> "))
            price = 10 * priceInput
        if userInput == 2:
            print("How many do you want?")
            priceInput = int(input(">> "))
            price = price + (20 * priceInput)
        if userInput == 3:
            print("How many do you want?")
            priceInput = int(input(">> "))
            price = price + (30 * priceInput)
        if userInput == 4:
            print("How many do you want?")
            priceInput = int(input(">> "))
            price = price + (40 * priceInput)
        if userInput == 5:
            print("Total Price :", price, "THB")
            print("Do you Sure?")
            print("1 : Sure")
            print("2 : Not Yet")
            userAgree = int(input(">> "))
            if userAgree == 1:
                print("Sucessful Thank you for visit")
                i = 1
            elif userAgree == 2:
                print("Sorry")
            else:
                print("Error")
        else:
            print("error")

else:
    print("Wrong Username or Password")