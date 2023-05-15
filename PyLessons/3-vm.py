# ╭── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╮
#   VARIABLES & METHODS
# ╰── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╯
#
# YouTube :: https://youtu.be/7utwZYKweho
# Ask Python :: https://www.askpython.com/python/string/strings-in-python
#
# In Python 3, a variable is a named location in memory that is used to store a value. A method is a function that is associated with an object and is used to perform an operation on that object. A function is a block of code that is used to perform a specific task. Unlike a method, a function is not associated with an object, and it can be called independently of any object.

# string stored inside a Variable
quote = "All is fair in love and war."
print(quote)

# Methods
# Upper Case
print(quote.upper())
# Lower Case
print(quote.lower())
# Title Case
print(quote.title())

# Len() is used to find the LENGTH of a string, list, array, or any other object that has a length. Returns an integer represneting the number ob itens in the object.
print(len(quote))

# string
name = "Void"
# integer
age = 28
# float
gpa = 3.7

# In Python 3, int() is a built-in function that converts a number or string to an integer. For example, int('42') would convert the string '42' to the integer 42.
print(int(age))
print(int(30.1))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)