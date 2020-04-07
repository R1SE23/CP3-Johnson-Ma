"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice,
 write this code inside a function.
"""
def take_num():
    list = []
    while True:

        try:
            user_input = int(input("Choose number: "))
            list.append(user_input)
            choose_another = input("Choose Another Number: Yes or NO?".lower())
        except:
            print("Enter a number!")
            continue
        if choose_another == 'no':
            break

    new_list = []
    new_list.append(list[0])
    new_list.append(list[-1])
    print(new_list)
take_num()