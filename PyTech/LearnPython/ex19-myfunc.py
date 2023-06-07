# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Study Drill                                                                               │
# │ > Write a function and run it 10 different ways                                           │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# I wanted to make a greeting function that would take a name and a greeting as arguments
# and return a greeting with the name in it.

# My function - bin
def my_data(name, age):
    print(f"Hello {name}, you are {age} years old.")


# 1. Call the function with strings as arguments
my_data("Jane", "30")

# 2. Call the function with variables as arguments
my_name = "Jane"
my_age = "30"
my_data(my_name, my_age)

# 3. Call the function with math operations as arguments
my_data("Jane", "30" + "1")

# 4. Call the function with variables and math operations as arguments
my_data(my_name, my_age + "1")

# 5. Call the function with user input as arguments
my_data(input("What is your name? "), input("How old are you? "))

# 6. Call the function with user input and math operations as arguments
my_data(input("What is your name? "), input("How old are you? ") + "1")

# 7. Call the function with user input and variables as arguments
my_data(input("What is your name? "), my_age)

# 8. Call the function with user input, variables, and math operations as arguments
my_data(input("What is your name? "), my_age + "1")

# 9. Call a specific character from a string as an argument
my_data("Jane"[0], "30")

# 10. Call the function and ask if the user wants to change their name or age
#     If they do, ask for the new name or age and call the function again
#     If they don't, call the function with the original arguments
change_name = input("Do you want to change your name? ")
if change_name == "yes":
    my_name = input("What is your new name? ")
else:
    my_name = "Jane"
change_age = input("Do you want to change your age? ")
if change_age == "yes":
    my_age = input("What is your new age? ")
else:
    my_age = "30"
my_data(my_name, my_age)

# 11 - Conditional statement to check if user wants to change their name and age
#      If they do, ask for the new name or age and call the function again
#      If they don't, call the function with the original arguments
my_name = input("Do you want to change your name? ")
my_name = input("What is your new name? ") if my_name == "yes" else "Jane"

my_age = input("Do you want to change your age? ")
my_age = input("What is your new age? ") if my_age == "yes" else "30"

my_data(my_name, my_age)
