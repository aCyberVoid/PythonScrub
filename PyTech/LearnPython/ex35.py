# My own text based adventure game!! Enjoy!

# Exercise 35. Branches and Functons - if-statements galore
# Exercise 36: Designing and Debugging - https://scrnshot.app/tUkO2/LEHipazE19.txt

# Note: Each print statement includes the user input as a check

# Define a function for the first room of the game
def r1():
    # Ask the player to choose between door #1 or door #2
    door_choice = int(input("You find yourself in a dark room with two doors. Do you go through door #1 or door #2? "))
    # If the player chooses door #1, move to the second room
    if door_choice == 1:
        print(f"You chose door {door_choice}. Continue on. ➡️\n")
        r2()
    # If the player chooses door #2, move to the third room
    elif door_choice == 2:
        print(f"You chose door {door_choice}. Continue on.➡️\n")
        r3()
    # If the player enters an invalid choice, prompt them to choose again
    else:
        print(f"You chose door number {door_choice}. Please pick 1 or 2. Try again. 🙄\n")
        r1()

# Define a function for the second room of the game
def r2():
    # Ask the player to choose between fighting the bear or crossing the river
    action_choice = input("You are now in a forest. You can see a bear and a river. Would you like to ⚔️ 'fight the bear' or 🏊🏽 'cross the river'? \n")
    # If the player chooses to fight the bear, they lose the game
    if action_choice.lower() == "fight the bear":
        print(f"You chose to {action_choice}? The bear bit your leg off, my guy. Did you seriously think you could fight a bear? You lose! 🤣\n")
        exit()
    # If the player chooses to cross the river, move to the third room
    elif action_choice.lower() == "cross the river":
        print(f"You chose to {action_choice}. The bear was happy you did not fight him, so he gave you a jar of honey. Continue on.\n")
        r3()
    # If the player enters an invalid choice, prompt them to choose again
    else:
        print(f'You chose to {action_choice}. OMG, stop playing with me and pick one of the options I gave you. Try again! 😡😤\n')
        r2()

# Define a function for the third room of the game
def r3():
    # Ask the player a riddle presented by the friendly king in the castle
    riddle_choice = input("You are in a castle. There's a friendly king who asks you a riddle. If you answer correctly, you win. If not, you lose. Here's the riddle: 'What has keys but can’t open locks?' ")
    # If the player answers the riddle correctly, they win the game
    if riddle_choice.lower() == "piano":
        print(f"Your answer was {riddle_choice}. You win 1 Gold Coin! 🪙\n")
    # If the player answers the riddle incorrectly, they lose the game
    else:
        print(f"Your answer was {riddle_choice}. You lost. But it's better than what the winner got, so yeah. 💩\n")

# Start the game by calling the first room function
r1()
