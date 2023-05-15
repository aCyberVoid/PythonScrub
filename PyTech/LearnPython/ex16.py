# ╭───────────────────────────╮
# │ Reading and Writing Files │
# ╰───────────────────────────╯

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Commands to Remember !!                                                                   │
# │     close -- Closes the file. Like File->Save.. in your editor.                           │
# │      read -- Reads the contents of the file. You can assign the result to a variable.     │
# │  readline -- Reads just one line of a text file.                                          │
# │  truncate -- Empties the file. Watch out if you care about the file.                      │
# │ write('') -- Writes "stuff" to the file.                                                  │
# │   seek(0) -- Move the read/write location to the beginning of the file.                   │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# Import argv from sys module
from sys import argv

# Assign command-line arguments to variables
script, filename = argv

# Prompt user before performing file operations
print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("? ")

# Open the file in write mode
print("\nOpening the file...")
target = open(filename, 'w')

# Truncate the file to remove its content
print("\nTruncating the file. Goodbye!")
target.truncate()

# Prompt the user for three lines of input
print("\nNow I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Write the lines to the file
print("\nNow I'm going to write these lines to the file.")
target.write(f"{line1}\n{line2}\n{line3}\n")

# Close the file
print("\nAnd finally, we close it.")
target.close()

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Study Drill                                                                               │
# │ > Write a similar script to ex15 that uses [read] and [argv] to read the file you just    │
# │ created.                                                                                  │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# Print a message indicating the file being displayed
print(f"\nHere's your file {filename}:")

# Oen the file specified by the filename
txt = open(filename)

# Read and print the contents of the file
print(txt.read())

# Close the files - BEST PRACTICE - close files when done with them
txt.close()

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Study Drill                                                                               │
# │ > There's too much repetition in this file. Use strings, formats, and escapes to print    │
# │ out line1, line2, and line3 with just one [target.write()] command instead of six.        │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# Old line -3 write commands
# target.write("\n")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Study Drill                                                                               │
# │ > If you open the file with 'w' mode, then do you really need the [target.truncate()]?    │
# │ Go read the docs for Python's [open] function and see if that's true.                     │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯
# https://docs.python.org/3/library/functions.html#open
# 'w' > open for writing, truncating the file first
# target.truncate() is not needed when opening the file in 'w' mode
