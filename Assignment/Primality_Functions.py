import sympy
check_prime = []
list_of_prime = []
while True:
    user_function = int(input("Choose number: "))
    check_prime.append(user_function)
    if user_function == 0:
        break

for num in check_prime:
    if sympy.isprime(num):
        list_of_prime.append(num)
print(set(list_of_prime))