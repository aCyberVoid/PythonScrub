# Exercise 31. Making Decisions

# Prompting the user with a question and offering two choices.
print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2?""")

# Getting user input to determine which door they choose.
door: str = input("> ")

# Checking if the user chose door #1.
if door == "1":
    # Actions when door #1 is chosen.
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # Getting user input to determine their action with the bear.
    bear = input("> ")

    # Checking the user's action with the bear.
    if bear == "1":
        # Outcome when the user takes the cake.
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        # Outcome when the user screams at the bear.
        print("The bear eats your legs off. Good job!")
    else:
        # Outcome when the user chooses an action other than 1 or 2.
        print(f"Well, doing '{bear}' is probably better.")
        print("Bear runs away.")

# Checking if the user chose door #2.
elif door == "2":
    # Actions when door #2 is chosen.
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # Getting user input to determine their choice in the abyss.
    insanity: str = input("> ")

    # Checking the user's choice in the abyss.
    if insanity == "1" or insanity == "2":
        # Outcome when the user chooses blueberries or clothespins.
        print("Your body survives, powered by a mind of jello.")
        print("Good job!")
    else:
        # Outcome when the user chooses an option other than 1 or 2.
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
