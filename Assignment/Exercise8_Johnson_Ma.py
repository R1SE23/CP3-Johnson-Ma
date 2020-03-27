print('♝♝♝♝♝♝♝♝♝♝♝')
print("Welcome to EShop!!!")
print('♝♝♝♝♝♝♝♝♝♝♝')
x = 'qwerqwer'
y = '123123'
while input("Username: ") != x or input("Password: ") != y:
    print("Incorrect Username/Password!!!")
print('You have one option to select products from any section')
print('1.Book Section')
print('2.Drink Section')

orderSelect = int(input('>> '))
if orderSelect == 1:
    print('1.High Speed Reading techniques by Pane Edin : 250 B')
    print('2.How to be productive by Josh White : 300 B')
    amount = int(input('>> '))
    if amount == 1:
        print('How many books do you want?')
        numofbook = int(input())
        price = 250 * numofbook
        print(price)

    elif amount == 2:
        print('How many books do you want?')
        numofbook = int(input())
        price = 300 * numofbook
        print(price)

elif orderSelect == 2:
    print('1.Pepsi : 20 B')
    print('2.Coke : 15 B')
    quan = int(input('>> '))
    if quan == 1:
        print('How many Pepsi do you want?')
        pep = int(input())
        price = 20 * pep
        print(price)

    elif quan == 2:

        print('How many Coke do you want?')
        coke = int(input())
        price = 15 * coke
        print(price)

