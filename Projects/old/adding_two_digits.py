# Adding two digits together using Python
two_digit_number = input("Type a two digit number: ")

# Get the first and second digits using subscripting then convert string to integer.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)
