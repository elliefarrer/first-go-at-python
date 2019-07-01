################### PLUGINS #######################
from random import randint

########################## DATA ####################
user_board = []
computer_board = []
# TODO: write a function to check no two points are the same.

user_ships = {
    "cruise_liner": [],
    "private_yacht": [],
    "dinghy": [],
    "submarine": []
}

gameplay_stats = {
    "user_correct_guesses": 0,
    "computer_correct_guesses": 0,
    "turns": 0
}


#################### FUNCTIONS ##################
def getUserPoint(ship, message):
    points = int(raw_input("%s: " % (message)))

    while points not in range(6):
        points = int(raw_input("That number is too big. Pick on between 0 and 5: "))

    user_ships[ship].append(points)

def place_point(board, obj, ship, char):
    board[obj[ship][0]][obj[ship][1]] = char

def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner():
    if gameplay_stats["user_correct_guesses"] == 4: print("Congrats, you won!")
    elif gameplay_stats["computer_correct_guesses"] == 4: print("Bad luck, the computer won...")


##################### GAMEPLAY SETUP #########################
for square in range(0, 6):
    user_board.append(["~"] * 6)
    computer_board.append(["~"] * 6)

computer_ships = {
    "cruise_liner": [randint(0, 5), randint(0, 5)],
    "private_yacht": [randint(0, 5), randint(0, 5)],
    "dinghy": [randint(0, 5), randint(0, 5)],
    "submarine": [randint(0, 5), randint(0, 5)]
}

getUserPoint("cruise_liner", "To begin, choose a number between 0 and 5 for the X position of your cruise liner")
getUserPoint("cruise_liner", "Now choose a number between 0 and 5 for the Y position")
getUserPoint("private_yacht", "Choose the X position of your private yacht")
getUserPoint("private_yacht", "Now choose the Y position")
getUserPoint("dinghy", "Now choose the X position of your dinghy")
getUserPoint("dinghy", "Now choose the Y point")
getUserPoint("submarine", "Choose an X position for your submarine")
getUserPoint("submarine", "Finally, choose the submarine's Y position")

place_point(user_board, user_ships, "cruise_liner", "C")
place_point(user_board, user_ships, "private_yacht", "Y")
place_point(user_board, user_ships, "dinghy", "D")
place_point(user_board, user_ships, "submarine", "S")
place_point(computer_board, computer_ships, "cruise_liner", "C")
place_point(computer_board, computer_ships, "private_yacht", "Y")
place_point(computer_board, computer_ships, "dinghy", "D")
place_point(computer_board, computer_ships, "submarine", "S")

print("Your board is below: ")

print_board(user_board)


########################## ACTUAL GAMEPLAY ##########################
while gameplay_stats["user_correct_guesses"] != 4 and gameplay_stats["computer_correct_guesses"] != 4:
    users_turn = True

    while users_turn == True:
        user_guess_row = int(raw_input("Rocket time! Choose an X point between 0 and 5: "))
        user_guess_col = int(raw_input("Now choose a Y point (0-5): "))

        if computer_board[user_guess_row][user_guess_col] == "C":
            print("You have sunk the computer's cruise liner")
            computer_board[user_guess_row][user_guess_col] = "X"
            gameplay_stats["user_correct_guesses"] = gameplay_stats["user_correct_guesses"] + 1
        elif computer_board[user_guess_row][user_guess_col] == "Y":
            print("You have sunk the computer's private yacht")
            computer_board[user_guess_row][user_guess_col] = "X"
            gameplay_stats["user_correct_guesses"] = gameplay_stats["user_correct_guesses"] + 1
        elif computer_board[user_guess_row][user_guess_col] == "D":
            print("You have sunk the computer's dinghy")
            computer_board[user_guess_row][user_guess_col] = "X"
            gameplay_stats["user_correct_guesses"] = gameplay_stats["user_correct_guesses"] + 1
        elif computer_board[user_guess_row][user_guess_col] == "S":
            print("You have sunk the computer's submarine")
            computer_board[user_guess_row][user_guess_col] = "X"
            gameplay_stats["user_correct_guesses"] = gameplay_stats["user_correct_guesses"] + 1
        elif computer_board[user_guess_row][user_guess_col] == "X" or computer_board[user_guess_row][
            user_guess_col] == ".":
            print("You already hit that spot")
        else:
            print("You missed!")
            computer_board[user_guess_row][user_guess_col] = "."

        check_winner()
        users_turn = False

    while users_turn == False:
        computer_guess_row = randint(0, 5)
        computer_guess_col = randint(0, 5)

        if user_board[computer_guess_row][computer_guess_col] == "C":
            print("The computer sunk your cruise liner")
            user_board[computer_guess_row][computer_guess_col] = "X"
            print_board(user_board)
            gameplay_stats["computer_correct_guesses"] = gameplay_stats["computer_correct_guesses"] + 1
        elif user_board[computer_guess_row][computer_guess_col] == "Y":
            print("The computer sunk your private yacht")
            user_board[computer_guess_row][computer_guess_col] = "X"
            print_board(user_board)
            gameplay_stats["computer_correct_guesses"] = gameplay_stats["computer_correct_guesses"] + 1
        elif user_board[computer_guess_row][computer_guess_col] == "D":
            print("The computer sunk your dinghy")
            user_board[computer_guess_row][computer_guess_col] = "X"
            print_board(user_board)
            gameplay_stats["computer_correct_guesses"] = gameplay_stats["computer_correct_guesses"] + 1
        elif user_board[computer_guess_row][computer_guess_col] == "S":
            print("The computer sunk your submarine")
            user_board[computer_guess_row][computer_guess_col] = "X"
            print_board(user_board)
            gameplay_stats["computer_correct_guesses"] = gameplay_stats["computer_correct_guesses"] + 1
        elif user_board[computer_guess_row][computer_guess_col] == "X" or user_board[computer_guess_row][
            computer_guess_col] == ".":
            print("Computer is a massive dumb dumb because it already hit that spot")
            print_board(user_board)
        else:
            print("Computer missed!")
            user_board[computer_guess_row][computer_guess_col] = "."
            print_board(user_board)


        gameplay_stats["turns"] = gameplay_stats["turns"] + 1
        check_winner()
        users_turn = True

    check_winner()
