import random

game_options = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors'
}

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print("You chose:", game_options[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:", game_options[computer_choice])

if user_choice not in game_options:
    print("You typed an invalid number, you lose!")
elif user_choice == computer_choice:
    print("It's a draw")
elif (user_choice - computer_choice) % 3 == 1:
    print("You win!")
else:
    print("You lose!")