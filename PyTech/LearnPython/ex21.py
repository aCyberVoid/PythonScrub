# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │  Exercise 21: Functions Can Return Something                                              │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# "=" is used to assign values to variables
# now we wil use it with return to set variables to be a value from a function

# creating my functions
def add(a, b):
    print(f"ADDING {a} + {b}")
    # return the sum of a and b
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a}*{b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a}/{b}")
    return a / b


def power(a, b):
    print(f"POWER {a}^{b}")
    return a ** b


print("Let's do some math with just functions!")

# set the variables to the return value of the functions
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# print the values of the variables above
print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

# a puzzle for the extra credit, type it in any way
print("Here is a puzzle.")

# Calculating the "what" variable inside-out divide > multiply > subtract > add
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

result = power(2, 3)
print(f"Result: {result}")

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │  Study Drills                                                                             │
# │  4. Write a simple formula and use the functions in the same way to calculate it.         │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# Formula
# age * (10 + 3)
multiply(age, add(10, 3))
multiply(35, 13)
# 455
print(multiply(age, add(10, 3)))

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │  Write the following formula out using functions                                          │
# │  24 + 34 / 100 - 1023                                                                     │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# 24 + 34 / 100 - 1023
# add(24, divide(34, subtract(100, 1023)))
# Need to practice more on this
