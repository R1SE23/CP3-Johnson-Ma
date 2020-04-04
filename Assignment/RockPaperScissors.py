"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)
"""
# StraightForward
def choose_weapon():
    player1 = input("Player 1 - Rock, Paper, Scissors?: ".lower())
    player2 = input("Player 2 - Rock, Paper, Scissors?: ".lower())
    while player1 == player2:
        print("Draw")
        return choose_weapon()

    dict = {0:'rock',1:'paper',2:'scissors'}
    if player1 == dict[0] and player2 == dict[1]:
        print('Player 2 Wins')
    elif player1 == dict[0] and player2 == dict[2]:
        print('Player 1 Wins')
    elif player1 == dict[1] and player2 == dict[2]:
        print('Player 2 Wins')
    elif player1 == dict[2] and player2 == dict[1]:
        print('Player 1 Wins')
    elif player1 == dict[1] and player2 == dict[0]:
        print('Player 1 Wins')
    elif player1 == dict[2] and player2 == dict[0]:
        print('Player 2 Wins')
    return play_again()
def play_again():

    x = input("Play again?".lower())
    while x == 'yes':
        return choose_weapon()
    return False

# Complex Algorithm

choice = ['rock', 'scissors', 'paper']

# Game loop
while True:
    player1 = input("Player 1 - Rock, Paper, Scissors? ").lower()
    player2 = input("Player 2 - Rock, Paper, Scissors? ").lower()
    if choice.index(player1) == (choice.index(player2) + 1) % 3:
        print('Player 2 wins!')

    elif choice.index(player2) == (choice.index(player1) + 1) % 3:
        print('Player 1 wins!')

    else:
        print("Its a draw! Try again")

