# ╭─── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ───╮
#   CONDITIONAL STATEMENTS
# ╰─── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ───╯

# In Python, a conditional statement is a control flow statement that allows you to execute code only if a certain condition is met. This is often used to perform different actions depending on the state of the program or the data it is processing.

# if/else
def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"
print(drink(3))
print(drink(1))

print('\n')

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money!"
    elif (age <= 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too young and too broke!"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))