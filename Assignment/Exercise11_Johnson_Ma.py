inputNumber = int(input("Number of layers of the Pyramid : "))
for x in range(inputNumber):
    text = ""
    for y in range(1):
        space = inputNumber - (x+1)
        star = "*"*(2*x+1)
        text = text + space*" " + star + space*" "
    print(text)