x = 'Nattarach'
y = 'Larptawee'
if input("Username: ") == x and input("Password: ") == y:
    print("Welcome!!!")
else:
    print("Incorrect Username/Password!!!")


print('------------')
print('Grade Check')
print('------------')
score = int(input("Your score : "))
if score > 100:
    print('Out of range!!!')
elif score >= 80:
    print('A')
elif score >= 75:
    print('B+')
elif score >= 70:
    print('B')
elif score >= 65:
    print('C+')
elif score >= 60:
    print('C')
elif score >= 55:
    print('D+')
elif score >= 50:
    print('D')
else:
    print('F')

