import random
import string
i = 1
password = []
# Build
def pwgen():
    while i != 0:
        generate_password = input("Generate password for you?".lower())
        if generate_password == 'yes':
            how_strong = int(input("How would you like your password to be?\n1.Strong\n2.Normal".lower()))
            if how_strong == 2:
                for num in range(3):
                    password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
                    password.append(str(random.choice(range(100000))))
                    password.append(random.choice('abcdefghijklmnopqrstuvwxyz'.upper()))
                break
            elif how_strong == 1:

                for num in range(10):
                    password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
                    password.append(str(random.choice(range(100000))))
                    password.append(random.choice('abcdefghijklmnopqrstuvwxyz'.upper()))

                break
    print(''.join(password))


# Don't know how to join num and str in this/ updated: Got it

"""
Combination of lower and uppercase letters
"""

import random
import string

def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
print("Random String with the combination of lowercase and uppercase letters")
print ("First Random String is ", randomString(8) )
print ("second Random String is ", randomString(8) )



# confuse between return and for