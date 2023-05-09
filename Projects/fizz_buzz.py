# FizzBuzz

# Instructions -
# For numbers 1-100, print "Fizz" if the number is divisible by 3
# Print "Buzz" if the number is divisible by 5
# Print "FizzBuzz" if the number is divisible by both 3 and 5.
# Otherwise, print the number.
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)