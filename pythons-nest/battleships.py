# Two player battleships with a user and a computer

# Get user to place two ships on grid
# Then computer randomly places Two
# User makes a guess and check if correct
# Then computer randomly does
# Go back and forth until winner

from random import randint

def check_invalid_validity(row, column):
    if row not in range(7) or column not in range(7): print ("You've already failed")

def print_board(board):
    for row in board:
        print " ".join(row)

def check_winner():
    if user_correct_guesses == 2: print("You win!")
    elif computer_correct_guesses == 2: print("The computer won!")

user_board = []

for square in range(0, 6):
    user_board.append(["O"] * 6)

computer_board = []

for square in range(0, 6):
    computer_board.append(["O"] * 6)


computer_cruise_liner_row = randint(0, 5)
computer_cruise_liner_col = randint(0, 5)
computer_private_yacht_row = randint(0, 5)
computer_private_yacht_col = randint(0, 5)

# print("Computer's cruise liner is at %s/%s" % (computer_cruise_liner_row, computer_cruise_liner_col))
# print("Computer's yacht is at %s/%s" % (computer_private_yacht_row, computer_private_yacht_col))

user_correct_guesses = 0
computer_correct_guesses = 0



print("Welcome to Battleships!")

user_cruise_liner_row = int(raw_input("To begin, choose a row (0-6) for your P&O cruise liner: "))
user_cruise_liner_col = int(raw_input("Now choose its column (0-6): "))

check_invalid_validity(user_cruise_liner_row, user_cruise_liner_col)

user_private_yacht_row = int(raw_input("Now select a row (0-6) for your private yacht: "))
user_private_yacht_col = int(raw_input("And now select its column (0-6): "))

check_invalid_validity(user_private_yacht_row, user_private_yacht_col)



user_board[user_cruise_liner_row][user_cruise_liner_col] = "C"
user_board[user_private_yacht_row][user_private_yacht_col] = "Y"

print("Below if your board. C = cruise liner, and Y = private yacht")

print_board(user_board)

computer_board[computer_cruise_liner_row][computer_cruise_liner_col] = "C"
computer_board[computer_private_yacht_row][computer_private_yacht_col] = "Y"

# print("The computer's board is:")
# print_board(computer_board)


# Now that the game is set up, let's play some Battleships!
while user_correct_guesses != 2 and computer_correct_guesses != 2:
    users_turn = True

    while users_turn == True:
        user_guess_row = int(raw_input("Select a row (0-6) to guess: "))
        user_guess_col = int(raw_input("Now guess a column (0-6): "))

        if computer_board[user_guess_row][user_guess_col] == "C":
            print("You have sunk the computer's P&O cruise liner")
            computer_board[user_guess_row][user_guess_col] = "."
            user_correct_guesses = user_correct_guesses + 1
        elif computer_board[user_guess_row][user_guess_col] == "Y":
            print("You have sunk the computer's private yacht")
            computer_board[user_guess_row][user_guess_col] = "."
            user_correct_guesses = user_correct_guesses + 1
        elif computer_board[user_guess_row][user_guess_col] == "X" or computer_board[user_guess_row][user_guess_col] == ".":
            print("You already hit that spot")
        else:
            print("You missed!")
            computer_board[user_guess_row][user_guess_col] = "X"

        check_winner()
        users_turn = False

    while users_turn == False:
        computer_guess_row = randint(0, 5)
        computer_guess_col = randint(0, 5)

        if user_board[computer_guess_row][computer_guess_col] == "C":
            print("The computer sunk your P&O cruise liner")
            user_board[computer_guess_row][computer_guess_col] = "."
            print_board(user_board)
            computer_correct_guesses = computer_correct_guesses + 1
        elif user_board[computer_guess_row][computer_guess_col] == "Y":
            print("The computer sunk your private yacht")
            user_board[computer_guess_row][computer_guess_col] = "."
            print_board(user_board)
            computer_correct_guesses = computer_correct_guesses + 1
        elif user_board[computer_guess_row][computer_guess_col] == "X" or user_board[computer_guess_row][computer_guess_col] == ".":
            print("Computer is a massive dumb dumb because it already hit that spot")
            print_board(user_board)
        else:
            print("Compter missed!")
            user_board[computer_guess_row][computer_guess_col] = "X"
            print_board(user_board)

        check_winner()
        users_turn = True

check_winner()
