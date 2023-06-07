# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │  Exercise 20: Functions and Files                                                         │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# Import argv from sys module
from sys import argv

# Get the script name and input file name from command-line arguments
script, input_file = argv


def print_all(f):
    # Read and print the entire contents of the file
    print(f.read())


def rewind(f):
    # Move the file position indicator to the beginning of the file
    f.seek(0)


def print_a_line(line_count, f):
    # Print the line number and its corresponding line from the file
    print(line_count, f.readline())


# Open a specified file and assign it to current_file variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# Print the entire contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Move the file position indicator to the beginning of the file
rewind(current_file)

print("Let's print three lines:")

# Print the current line number and the corresponding line from the file, increasing by one
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
