# Rock Paper Scissors
from random import randint

options = ['rock', 'paper', 'scissors']

rock = {
    "beats": "scissors",
    "beaten_by": "paper"
}

scissors = {
    "beats": "paper",
    "beaten_by": "rock"
}

paper = {
    "beats": "rock",
    "beaten_by": "scissors"
}


print(options)
print(options[0])
print(rock["beats"])

computer_choice = options[randint(0, 2)]

# print("Computer chose %s" % computer_choice)

def define_user_choice(message):
    global user_choice
    user_choice = raw_input(message)

define_user_choice("Make your choice: ")

if not user_choice or user_choice not in options:
    define_user_choice("Invalid input. Please try again: ")

global result

print(user_choice[0])

# if user_choice["beats"] == computer_choice:
#     result = "User wins"
# elif user_choice["beaten_by"] == computer_choice:
#     result = "Computer wins"
# else:
#     result = "Draw"
#
# print("User selected %s and computer selected %s. %s" % user_choice, computer_choice, result)
