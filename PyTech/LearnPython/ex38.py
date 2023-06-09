# Assigning a string to the variable 'ten_things'
ten_things = "A B C D E F"

# Printing a message
print("Wait, there are not 10 things in the list. Let's fix this.")

# Splitting the string 'ten_things' into a list using space as the delimiter and assigning it to the variable 'stuff'
stuff = ten_things.split(' ')

# Creating a list 'more_stuff' with additional elements
more_stuff = ["G", "H", "I", "J"]

# Executing a loop until the length of 'stuff' becomes 10
while len(stuff) != 10:
    # Popping the last element from 'more_stuff' and assigning it to the variable 'next_one'
    next_one = more_stuff.pop()

    # Printing a message with the value of 'next_one'
    print("Adding: ", next_one)

    # Appending 'next_one' to the 'stuff' list
    stuff.append(next_one)

    # Printing the current length of 'stuff'
    print(f"There are {len(stuff)} items now.")

# Printing a message with the string 'stuff' as it is
print("There we go: ", stuff)

# Printing a message
print("Let's do some things with stuff.")

# Printing the element at index 1 of 'stuff'
print(stuff[1])

# Printing the last element of 'stuff'
print(stuff[-1])  # whoa! fancy

# Removing and returning the last element of 'stuff'
print(stuff.pop())

# Joining the elements of 'stuff' into a string using a space as the separator and printing it
print(' '.join(stuff))  # what? cool!

# Joining the elements from index 3 to index 5 of 'stuff' into a string using '#' as the separator and printing it
print('#'.join(stuff[3:5]))  # super stellar!

# Joining the elements from index 3 to index 8 of 'stuff' into a string using '--' as the separator and printing it
print('--'.join(stuff[3:8]))
