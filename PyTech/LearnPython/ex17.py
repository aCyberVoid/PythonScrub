# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Exercise 17: Copy File to Another File                                                    │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# Python Script to Copy the Contents of One File to Another

# Importing argv from sys module
from sys import argv
# Importing exists from os.path module - returns True if file exists
from os.path import exists

# Unpacking argv into variables
script, from_file, to_file = argv

# Printing the file names
print(f"\nCopying from {from_file} to {to_file}")

# We could do these two on one line, how?
# Opening the file and reading it
in_file = open(from_file)
# Reading the file
indata = in_file.read()

# Printing the length of the file
print(f"\nThe input file is {len(indata)} bytes long")

# Printing if the output file exists
print(f"\nDoes the output file exist? {exists(to_file)}")
print("\nReady, hit RETURN to continue, CTRL-C to abort.")
input()

# Opening the file in write mode
out_file = open(to_file, 'w')
# Writing the data to the file
out_file.write(indata)

# Printing that the file has been copied
print("\nAlright, all done.")

# Closing the files
out_file.close()
in_file.close()

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Study Drills:                                                                             │
# │                                                                                           │
# │   1. See how short you can make the script                                                │
# │   2. Find out why you had to write 'out_file.close()                                      │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯
#
# 1
# from sys import argv
# from os.path import exists
# script, from_file, to_file = argv
# in_file = open(from_file)
# indata = in_file.read()
# out_file = open(to_file, 'w')
# out_file.close()
# in_file.close()
#
# You can make the code shorter by using a semicolon to have it all on one line. But it is
# better to have it on multiple lines, so it is easier to read.
#
# 2
# You had to write 'out_file.close()' because you opened the file in write mode. It is
# IMPORTANT to close the file after you are done with them. After opening a file and
# closing, we are essentially giving back memory.
#
