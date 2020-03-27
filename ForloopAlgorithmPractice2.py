for x in range(12):
    for y in range(12):
        print(x+1, "x", y+1, "=", (x+1)*(y+1))
InputNumber = 0
for InputNumber in range(11):
    InputNumber +=1
    for i in range(12):
        print(InputNumber+1,"X",(i+1),"=",((InputNumber+1)*(i+1)))
InputNumber = int(input("Input Number::"))
for i in range(12):
    print(InputNumber,"X",(i+1),"=",(InputNumber*(i+1)))