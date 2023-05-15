# ╭───────────────────────────────────────────╮
# │ Goal: Open a file and print its contents  │
# │ We use [argv] to get a filename           │
# │ We use [open] to open the file            │
# │ We use [read] to read the file            │
# │ We use [close] to close the file          │
# ╰───────────────────────────────────────────╯

# Import argv from sys module
from sys import argv

# Assign the command-line arguments to variables
script, filename = argv

# Open the file specified by the filename
txt = open(filename)

# Print a message indicating the file being displayed
print(f"Here's your file {filename}:")

# Read and print the contents of the file
print(txt.read())

# Close the files - BEST PRACTICE - close files when done with them
txt.close()

# Prompt the user to enter the filename again
print("Type the filename again:")
file_again = input("> ")

# Open the file specified by the new filename entered by the user
txt_again = open(file_again)

# Read and print the contents of the new file
print(txt_again.read())

# Close the files - BEST PRACTICE - close files when done with them
txt.close()

# ╭───────────────────────────────────────────╮
# │ Try in Shell!!                            │
# │ 1. python3 ex15.py ex15_sample.txt        │
# │ 2. txt = open('ex15_sample.txt')          │
# │ 3. txt.read()                             │
# ╰───────────────────────────────────────────╯
