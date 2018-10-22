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

default_board = []

for square in range(0, 6):
    default_board.append(["O"] * 6)


computer_cruise_liner_row = randint(0, 6)
computer_cruise_liner_col = randint(0, 6)
computer_private_yacht_row = randint(0, 6)
computer_private_yacht_col = randint(0, 6)

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

user_board = default_board
user_board[user_cruise_liner_row][user_cruise_liner_col] = "C"
user_board[user_private_yacht_row][user_private_yacht_col] = "Y"

print("Below if your board. C = cruise liner, and Y = private yacht")

print_board(user_board)
