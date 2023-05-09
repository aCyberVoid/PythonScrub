# ╭── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╮
#     ADVANCED STRINGS
# ╰── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╯
# Strings are immutable
my_name = "Void"
print(my_name[0])
print(my_name[1])
print(my_name[-1])

sentence = "This is a sentence."
# prints the first 4 items in the above string
print(sentence[:4])
# Use delimiter with space to see all items in a string
print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'Give me all your money!'"
print(quote)
# escape character cause it to ignore a character
quote = "He said, \"Give me all your money!\""
print(quote)

too_much_space = "                                   hello                        "
# strips out a character, such as spaces
print(too_much_space.strip())

# matching case sensitivity - test with True and False statments
# True Statement
print("A" in "Apple")
# False Statement
print("a" in "Apple")
letter = "A"
word = "Apple"
# Get lowercase to make it a True Statement
print(letter.lower() in word.lower())

# string formatting
movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.") # latest to do formatting in Python 3