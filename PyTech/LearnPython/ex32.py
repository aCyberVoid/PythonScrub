# ╭───────────────────────────────────────────────────────────────────────────────────────────╮
# │ Exercise 32. Loops and Lists                                                              │
# ╰───────────────────────────────────────────────────────────────────────────────────────────╯

# For Loops will be used in this exercise
# For Loops are used to iterate over a sequence (list, tuple, string) or other iterable objects

# Lists are a datatype that stores a list of values
# Lists are created using square brackets

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for num in the_count:
    print(f"This is count {num}")

# Same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Also, we can go through mixed lists to
# Notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# We can also build lists, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # Append is a function that lists understand
    elements.append(i)

# Now we can print them out too
for i in elements:
    print(f"Element was: {i}")
