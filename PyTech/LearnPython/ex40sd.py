# Reference ____ /Exercises/ex40.py
# NOTE _________ ex40.py Study Drills. Extension of ex40.py.

# Write more phrases for the nursery rhyme and ensure you understand how they work.
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

# ADDED: CREATE ANOTHER PHRASE AND UNDERSTAND THAT YOU'RE PASSING A LIST OF STRINGS AS THE
# PHRASES ARGUMENT IN YOUR RHYME CLASS
jack_jill = Rhyme(["Jack and Jill went up the hill",
                   "To fetch a pail of water",
                   "Jack fell down and broke his crown",
                   "And Jill came tumbling after"])

# Print a divider
print("-" * 10)
# Print rhyme title
print("Rhyme: star light, star bright\n")
# Call the "nursery_rhyme" method on the "sl_sb" instance.
sl_sb.nursery_rhyme()

# Print a divider
print("-" * 10)
# Print rhyme title
print("Rhyme: Jack and Jill\n")
# ADDED: CALL THE "nursery_rhyme" METHOD ON THE "jack_jill" INSTANCE.
jack_jill.nursery_rhyme()

# Print a specific line from the "sl_sb" instance.
print("\nLet's print line 2 of the star light, star bright rhyme.")
print("Line 2: {}".format(sl_sb.phrase[1]))

# Print a line given by user input.
print("\nLet's print a line from the Jack and Jill rhyme.")
# Prompt the user to input a line number between 1 and 4.
line_number = input(
    "What line would you like to print? Please pick a number between 1 and 4.\n> ")

# Check if the entered line number is valid.
while line_number not in "1234":
    print("Please enter a valid number.")
    line_number = input(
        "What line would you like to print? Please pick a number between 1 and 4.\n> ")

# Print the line number and the corresponding line from the nursery rhyme.
print("Line {}: {}".format(line_number, jack_jill.phrase[int(line_number) - 1]))

# Breakdown of the Comments:
# File reference and note about being an extension of ex40.py.
# Comment explaining the purpose of the class and its constructor.
# Comment explaining the purpose of the nursery_rhyme method.
# Comment highlighting the creation of another instance of the Rhyme class.
# Comment indicating the creation of an additional rhyme and passing a list of strings as the
# argument.
# Divider comment before printing the first rhyme.
# Comment indicating the rhyme title.
# Comment mentioning the call to the nursery_rhyme method on the sl_sb instance.
# Divider comment before printing the second rhyme.
# Comment indicating the rhyme title.
# Comment mentioning the call to the nursery_rhyme method on the jack_jill instance.
# Comment introducing the printing of a specific line from the sl_sb instance.
# Comment prompting the user to input a line number for printing.
# Comment explaining the while loop and validity check for the entered line number.
# Comment indicating the printing of the line number and the corresponding line from the
# nursery rhyme.
