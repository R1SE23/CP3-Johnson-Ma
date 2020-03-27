x = int(input())
for y in range(x):
    print('*', end = ' ')
#Easier way below
x = int(input())
print('*'* x)


z = int(input())
stair = ''
for u in range(z):
    stair = stair + '*'
    print(stair)
# Another Solution

number = int(input())

for x in range(number):
    text = " "
    for y in range(x+1):
        text = text + "*"
    print(text)
# Another Solution
number = int(input())
for x in range(number):
    print('*'*(x+1))