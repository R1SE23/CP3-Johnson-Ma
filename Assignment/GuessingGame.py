"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
"""
import random

a = random.randint(1, 9)

while True:
    user_input = int(input("Guess number between 1 and 9: "))
    if user_input < a:
        print("Too low")
    elif user_input > a:
        print("Too high")
    elif user_input == a:
        print("Correct")
        break
