# ╭── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╮
#        FUNCTIONS
# ╰── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╯

# In Python 3, a function is a piece of code that performs a specific task and can be called from other parts of your program. A function usually takes some input, performs some operation on that input, and then returns a result. Defining a function allows you to give it a name and use it repeatedly in your code, which can make your code more modular and easier to understand and maintain.

# function without parameters
def who_am_i():
    name = "Void"
    age = 30
    print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()

# function with a parameter
def add_one_hundred(num):
    print(num + 100)
add_one_hundred(100)

# function with multiple parameters
def add(x,y):
    print(x + y)
add(7,7)

def multiply(x,y):
    # In this function, the return statement is used to return the value of result to the caller. When this function is called, the value of result will be computed and returned to the caller, who can then use the returned value in their code.
    return x * y
multiply(7,7)
print(multiply(7,7))

# square root
def square_root(x):
    print(x ** .5)
square_root(64)

# creating a new line
def nl():
    print('\n')
nl()
print('Test the new line function from above')