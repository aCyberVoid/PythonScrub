import random

# Define character sets as lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate easy password
easy_password_chars = [random.choice(letters) for _ in range(nr_letters)]
easy_password_chars += [random.choice(symbols) for _ in range(nr_symbols)]
easy_password_chars += [random.choice(numbers) for _ in range(nr_numbers)]
easy_password = ''.join(easy_password_chars)
print("Here is your unscrambled password:", easy_password)

# Generate hard password
hard_password_chars = [random.choice(letters) for _ in range(nr_letters)]
hard_password_chars += [random.choice(symbols) for _ in range(nr_symbols)]
hard_password_chars += [random.choice(numbers) for _ in range(nr_numbers)]
random.shuffle(hard_password_chars)
hard_password = ''.join(hard_password_chars)
print("Here is your scrambled password:", hard_password)
