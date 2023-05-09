# ╭── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╮
#      LISTS & TUPLES
# ╰── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ──╯

# In Python, a list is a data structure that stores a collection of items. Lists are ordered, meaning that the items in a list have a specific order, and they can be accessed by their index in the list. Lists are also mutable, meaning that you can change the items in a list once it has been created. Use brackets to create lists in a variable or when calling for a specific item in a list.

movies = ["The Adam's Family", "Harry Potter", "And Then There Were None", "The Fifth Element"]
# print the first movie
print(movies[0])
# prints the second movie
print(movies[1])
# splicing an index/indecies
# return first index number given tight until the last number, but not include the last number
print(movies[1:3])
# print everything from the index number
print(movies[1:])
# include everything before the index number
print(movies[:1])
# print the very last item
print(movies[-1])
# count the number of items in the list
print(len(movies))
# add to the end of the list
movies.append("Spiderman")
print(movies)
# insert movie into the list
movies.insert(2, "Cinderella")
print(movies)
# remove last item in list
movies.pop()
print(movies)
# remove specific item in a list
movies.pop(0)
print(movies)
# combine two lists
john_movies = ["Jaws", "The Notebook", "Jump Street"]
our_fav_movies = movies + john_movies
print(our_fav_movies)
# TD Lists
grades = [["Bob",82],["Jeff", 45],["Alice",98]]
# 0 = first index [x] , 1 = second index [y]
bob_grade = grades[0][1]
print(bob_grade)
# fixing bob's grade
grades[0][1] = 87
print(grades)

# In Python, a tuple is a data structure that stores a collection of items. Tuples are similar to lists, but they are immutable, which means that the items in a tuple cannot be changed once the tuple has been created. These use parenthesis, not brackets.
grades = ("A", "B", "C", "D", "F")
print(grades[2])