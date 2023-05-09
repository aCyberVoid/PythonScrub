# 🚨 Don't change the code below 👇
numbers = input("Provide a list of digits you need the average for: ").split()
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
# Add up all the numbers in the provided list
total = 0
for num in numbers:
    total += num
print(f"Total = {total}")
# Print the number of digits provided by user input
digits = 0
for nums in numbers:
    digits += 1
print(f"Digits you provided = {digits}")
# Calculate the average of the provided list of digits
average = round(total / digits)
print(f" The average of your list of digits are: {average}.")