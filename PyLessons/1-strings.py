# ╭── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ──╮
#        STRINGS
# ╰── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ──╯
def nl():
    print("\n")

# YouTube :: https://youtu.be/7utwZYKweho
# Ask Python :: https://www.askpython.com/python/string/strings-in-python

# Strings in Python are amongst the widely used data types and are created by enclosing characters in quotes.
string1 = "Hello"
string2 = "welcome"

# Single quote
ex1 = 'Void'
# Double quote
ex2 = "Void"
# Triple quote
ex3 = """Void"""
ex4 = '''Welcome to the tutorial!'''
ex5 = """Welcome to the tutorial"""

# Accessing and Manipulating Strings in Python
var1 = 'Hello World!'
print(var1)
print("var1[0]: ", var1[0])
var1 = 'Hello World'
print("var1[-1]: ", var1[-1])
print("var1[-5]: ", var1[-5])
nl()

# Python String Slicing
# To access a range of characters from a string, Slicing in a String is done by employing a slicing operator (colon)
Str1 = "AskPython Strings Tutorial"
print(Str1[10:20])

print("\nSlicing characters from 3rd to 5th character: ")
print(Str1[3:5])
nl()

# String Concatenation
# Strings is concatenated using the “+” operator. The illustration of the same is shown below:
var1 = "Hi,"
var2 = "Good Morning!"
var3 = var1 + var2
print(var3)
nl()

# Updating Strings
# Strings are immutable, hence updation or deletion of characters isn’t possible. This can cause an error because the item assignment (case of updation) or item deletion from a String isn’t supported.

String1 = "Hello"
# Updating character
# print('The following error is meant to be here to show what happens when you attempt to update a string.')
# String1[2] = 'p'
print("Updating character at 2nd Index: ")
print('The error below is needed for notes to show you can not update immutable objects like strings.')
# print(String1)
error = """Traceback (most recent call last):
  File 'C:\/Users\/void\Documents\PythonScrub\PyLessons\/1-strings.py', line 56, in <module>
    String1[2] = 'p'
  TypeError: 'str' object does not support item assignment"""
print(error)
nl()
# the deletion of the entire String is feasible with the use of a built-in del keyword.
String1 = "hello"
del(String1)
# Updating entire string
String1 = "Hello"
print(String1)  # prints Hello
String1 = "Welcome"
print(String1)  # prints Welcome
# Concatenation and slicing to update string
var1 = 'Hello World!'
# prints Hello Python!
print("Updated String :- ", var1[:6] + 'Python')
nl()

# REPEATING STRINGS
# Strings may be repeated by using the asterisk (*) operator
var1 = "hello"
print(var1 * 2)

# FORMATTING STRINGS
# Latest - The string format operator % is unique to strings and behaves similar to C’s printf() family of formatting options.
print("%s has Rs %d with her" % ('Aisha', 100))
# The format() method for strings contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.
Str1 = "{} {}".format('Hi, It is', '2020')
print(Str1)
# The format() method in Python can be used to format integers by allowing conversions from decimal format to binary, octal, and hexadecimal.
num = int(input("What number would you like to get the binary representation of: "))
ar1 = "{0:b}".format(num)
print("\nBinary representation of ",num," is ", ar1)