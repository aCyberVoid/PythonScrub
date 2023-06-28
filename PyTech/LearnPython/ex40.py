# Title _________ Modules, Classes, and Objects
# Description ___ Print a nursery rhyme
# Usage _________ Run the script using `python3 ex40.py`
# Resources _____ https://youtu.be/RP_1Ng52BRY -- Learning Python The Hard Way by Zed A. Shaw

# Define a class named Rhyme.
class Rhyme(object):
    # Define the __init__ method, which is the constructor of the class.
    # It takes a parameter named "phrase."
    def __init__(self, phrase):
        # Set the "phrase" parameter as an instance variable.
        self.phrase = phrase

    # Define a method named "nursery_rhyme."
    def nursery_rhyme(self):
        # Iterate over each line in the "phrase" list.
        for line in self.phrase:
            # Print the current line.
            print(line)


# Create an instance of the Rhyme class with a list of phrases as an argument.
sl_sb = Rhyme(["Star light, star bright",
               "First star I see tonight",
               "I wish I may, I wish I might",
               "Have this wish I wish tonight"])

# Call the "nursery_rhyme" method on the "sl_sb" instance.
sl_sb.nursery_rhyme()
