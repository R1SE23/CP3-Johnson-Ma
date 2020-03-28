menuList= []
productPrice =[]
def totalPrice():
    for i in productPrice:
        return sum(productPrice)
def showbill():
    print('❀❀❀❀ My Food ❀❀❀❀')
    for number in range(len(menuList)):
        print(menuList[number], productPrice[number])
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = int(input("Price: "))
        productPrice.append(menuPrice)
        menuList.append(menuName)
showbill()
print('Total price is = '+ str(totalPrice()) + ' Baht')