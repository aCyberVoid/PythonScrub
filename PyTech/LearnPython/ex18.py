# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Exercise 19 | Names, Variables, Code, Functions                                           │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯
#
# Functions do three things:
# 1. They name pieces of code the way variables name strings and numbers.
# 2. They take arguments the way your scripts take argv.
# 3. Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."
#
# You can create a function by using the word 'def' in Python.
# Functions are like mini-scripts because they can take arguments like your scripts.
# To 'run', 'call', or 'use' a function all mean the same thing.
#
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothing'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Study Drills                                                                              │
# │                                                                                           │
# │ 1. Did you start your function definition with def?                                       │
# │ 2. Does your function name have only characters and _ (underscore) characters?            │
# │ 3. Did you put an open parenthesis (right after the function name?)                       │
# │ 4. Did you put your arguments after the parenthesis ( separated by commas?                │
# │ 5. Did you make each argument unique (meaning no duplicated names)?                       │
# │ 6. Did you put a close parenthesis and a colon ): after the arguments?                    │
# │ 7. Did you indent all lines of code you want in the function four spaces?                 │
# │ 8. Did you "end" your function by going back to writing with no indent (dedenting we call │
# │    it)?                                                                                   │
# │                                                                                           │
# │ When you run ("use" or "call") a function, check these things:                            │
# │                                                                                           │
# │ 1. Did you call/use/run this function by typing its name?                                 │
# │ 2. Did you put the ( character after the name to run it?                                  │
# │ 3. Did you put the values you want into the parenthesis separated by commas?              │
# │ 4. Did you end the function call with a ) character?                                      │
# │                                                                                           │
# │ Use these two checklists on the remaining lessons until you do not need them anymore.     │
# │ Finally, repeat this a few times on your own, and make sure you do not need the           │
# │ checklists anymore.                                                                       │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯
