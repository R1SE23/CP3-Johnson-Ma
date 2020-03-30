systemMenu = {'rice': 30, 'lemon': 20, 'chicken': 25, 'corn': 15}
menuList = []
def showbill():
    print('❀❀❀❀ My Food ❀❀❀❀')
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

while True:
    menuName = input('Please enter menu name>> ')
    if menuName.lower() == 'exit':
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])
def add():
    total = 0
    for num in range(len(menuList)):
        total += menuList[num][1]
    return total

showbill()
print(add('Price = '))
