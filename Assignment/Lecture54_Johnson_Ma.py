def login():
    usernameInput = input('Username: ')
    passwordInput = input('Password: ')
    if usernameInput == 'admin' and passwordInput == '1234':
        return showMenu()
    else:
        return False
def showMenu():
    print('-----iShop-----')
    print('1. Vat Calculator')
    print('2. Price Calculator')
    return menuSelect()
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        return vatCalculate()
    elif userSelected == 2:
        return priceCalculate()
def vatCalculate():
    vat = 7
    inputNum = float(input("Price of the product: "))
    return inputNum+(inputNum*vat/100)
def priceCalculate():
    price1 = int(input("First product price: "))
    price2 = int(input("Second product price: "))
    return price1+price2
print(login())



