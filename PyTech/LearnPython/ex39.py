# create a mapping of states to their abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("Let's print some cities.")
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Let's print some states.")
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# print every state then city dictionary
print('-' * 10)
print("Let's print every state then city.")
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
print("Let's print cities for each state")
for abbrev, city in list(cities.items()):
    print(f"{abbrev} state is abbreviated {abbrev} and has city {cities[abbrev]}")

# safely get an abbreviation by state that might not be there
print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

print("All the cities!")
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# print both at the same time
print('-' * 10)
print("Print both dictionaries now!")
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print('Sorry, no Texas.')

# get a city with a default value
city = cities.get('TX', 'Does not Exist!')
print(f"The city for the state 'TX' is: {city}")
