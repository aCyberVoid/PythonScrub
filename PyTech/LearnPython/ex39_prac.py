# Continued Practice of Python Dictionaries
# Resources
# Python Documentation - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Google > Python Dict and File - https://developers.google.com/edu/python/dict-files

# Dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates.
print("We started this lesson by creating a dictionary named 'capitals'. Below is what we have stored in it.")
capitals = {
    'USA': 'Washington D.C.',
    'India': 'New Delhi',
    'China': 'Beigjing',
    'Russia': 'Moscow'
}
print(capitals)
print()

# If you would like to see all of the different attributes and methods of a dict - use dir() function
# print(dir(capitals))

# If you want an indepth description of all the different attributes and methods - use help() function
# print(help(capitals))

# Return the value of a secpfied key using .get()
print(f"Print the capital for 'USA':", capitals.get('USA')) # Returns Washington D.C.
print(f"Print the capital of Japan:", capitals.get('Japan\n')) # Returns NONE instead of KeyError

# Return a value based on user input using an if-statement - commented while testing other dictionary scnearios
# capital_search = input("What country are you wanting to know the capital for? Please ensure its spelled correctly!\n>> ")
# if capitals.get(capital_search):
#     print(f"The capital of {capital_search} is: {capitals.get(capital_search)}")
# else:
#     print(f"The capital of {capital_search} does not exist in our dictionary")

# Update your dictionary - adding a new key:value pair or editting a current one
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Berlin'})
print(capitals)
print()

# Remove a key:value pair
del capitals['China']
capitals.pop('Russia')
print(capitals)
print()

# Get only Keys and not Values
keys = capitals.keys()
print(keys)
print()
# You can also loop through them
print('We can loop through just the keys.')
for key in capitals.keys():
    print(key)
print()

# Get only Values - You can loop through these too!
values = capitals.values()
print(values)
print()
# the loop!
print('We can loop through just the values.')
for values in capitals.values():
    print(values)
print()

# Items - returns the key-value pairs of the dictionary, as tuples in a list.
items = capitals.items()
print(items)
print()
# Yes, you can loop it also
print('Print every key:value pair.')
for key, value in capitals.items():
    print(f"{key}: {value}")