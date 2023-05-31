# Initialize an empty list called 'numbers'
numbers = []


def my_loop(limit):
    # Initialize variable 'i' to 0
    # i = 0
    for i in range(0, limit, 10):
        # Print the value of 'i' at the beginning of each iteration
        print(f"At the top i is {i}")

        # Append the value of 'i' to the 'numbers' list
        numbers.append(i)

        # Increment the value of 'i' by 1
        # i += 1

        # Print the current state of the 'numbers' list
        print("Numbers now: ", numbers)

        # Print the value of 'i' at the end of each iteration
        print(f"At the bottom i is {i}")


my_loop(101)
# Print the final state of the 'numbers' list
print("The numbers: ")

for num in numbers:
    # Print the value of 'num' (individual elements of the list)
    print(num)
