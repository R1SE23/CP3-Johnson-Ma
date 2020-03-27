number = int(input('Number of layer of the pyramid:'))

for x in range(number):
    text = " " * (number - x - 1)
    for y in range(x+1):
        text = text + ("*")
        star = "*" * (y)
    print(text+star)



