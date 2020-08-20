#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def gen_fib():

    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1, 1]
    elif count > 2:
        fib = [1, 1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    user_select = int(input("Position: "))

    return fib, fib[user_select-1]

print(gen_fib())
