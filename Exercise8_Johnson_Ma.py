price = {"Sprite": 1.50, "Tea": 2.00, "Coffee": 1.00, "Water": 0.50}
shopping_basket = {}
x = 'qwerqwer'
y = '123123'
while input("Username: ") != x or input("Password: ") != y:
    print("Incorrect Username/Password!!!")
print('♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝')
print("Welcome to the online drink store!\nThese are the drinks we offer\n1. Sprite: $1.50\n2. Tea: $2.00\n3. Coffee: $1.00\n4. Water: $0.50")
print('♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝')
buy_another = 1
total_cost = 0
total = 0

while buy_another != 0:
    option = int(input("Which drink would you like to purchase?: "))

    if option == 1:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 1.50
        print("The price is: " + str(total))
    elif option == 2:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 2.00
        print("The price is: " + str(total))
    elif option == 3:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 1.00
        print("The price is: " + str(total))
    elif option == 4:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 0.50
        print("The price is: " + str(total))
    else:
        print('Please select again!!!')

    total_cost += total

    buy_another = int(input("Would you like another item? enter Yes(1) or No(0):"))
print("The total price of your basket is: ", total_cost)