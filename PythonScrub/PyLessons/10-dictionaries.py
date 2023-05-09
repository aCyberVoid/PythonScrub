# In Python, a dictionary is a collection of key-value pairs using curly braces {}. Each key is associated with a value, and you can use the key to access the value associated with it. Dictionaries are often used to store data that is related, such as the results of a query to a database.

# drink = key, price = value
drinks = {"White Russian":7, "Old Fashion":10, "Lemon Drop":8}
print(drinks)
# Update a value
drinks["White Russian"] = 8
print(drinks)
# Grab the value of a key
print(drinks.get("White Russian"))

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louis", "Teddy"], "HR": ["Jimmy JR", "Mort"]}
print(employees)
# Add key value pair
employees["Legal"] = ["Mr. Frond"]
print(employees)
# Another way of adding a key valur pair
employees.update({"Sales": ["Andy", "Olly"]})
print(employees)

# Additional Information on Dictionaries
#
# Here's a simple exampleof how to create and use a dictionary in Python:
# Create an empty dictionary
# my_dict = {}
#
# Add some key-value pairs to the dictionary
# my_dict['name'] = 'John Doe'
# my_dict['age'] = 30
# my_dict['email'] = 'johndoe@example.com'
#
# Access the values in the dictionary using the keys
# print(my_dict['name'])  # prints 'John Doe'
# print(my_dict['age'])  # prints 30
# print(my_dict['email'])  # prints 'johndoe@example.com'
#
# In this example, we created an empty dictionary and then added three key-value pairs to it. We then accessed the values in the dictionary using the keys.
# Dictionaries are very useful in Python because they allow you to store data in a structured way and access it quickly using the keys. They are also very flexible, so you can add, remove, and modify the key-value pairs in a dictionary as needed.

