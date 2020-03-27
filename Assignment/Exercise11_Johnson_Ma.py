number = int(input('Number of layer of the pyramid:'))

for x in range(number):
    text = " " * (number - x - 1)
    for y in range(x+1):
        text = text + ("*")
        star = "*" * (y)
    print(text+star)

# Another Solution
Number = int(input("Number of layers of the pyramid : "))
for x in range(Number):
    text = ""
    for y in range(1):
        space = Number - (x+1)
        star = "*"*(2*x+1)
        text = text + space*" " + star + space*" "
    print(text)

