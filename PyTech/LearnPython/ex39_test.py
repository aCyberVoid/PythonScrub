# Dictionaries, Oh Lovely Dictionaries

# Mapping Authors to Books
book = {
    # Mapping author to book title
    'J.K. Rowling': "Harry Potter and the Sorcerer's Stone",
    'Harper Lee': 'To Kill a Mockingbird',
    'J.R.R. Tolkien': 'The Lord of the Rings',
    'George R.R. Martin': 'A Game of Thrones',
    'F. Scott Fitzgerald': 'The Great Gatsby',
    'Dan Brown': 'The Da Vinci Code',
    'Herman Melville': 'Moby-Dick'  
}

# Mapping Books to Authors
author = {
    # Mapping book title to author
    "Harry Potter and the Sorcerer's Stone": 'J.K. Rowling',
    'To Kill a Mockingbird': 'Harper Lee',
    'The Lord of the Rings': 'J.R.R. Tolkien',
    'A Game of Thrones': 'George R.R. Martin',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'The Da Vinci Code': 'Dan Brown',
    'Moby-Dick': 'Herman Melville'
}

# Mapping Books to Genres
genre = {
    # Mapping genre to book title
    'Fantasy': "Harry Potter and the Sorcerer's Stone",
    'Southern Gothic': 'To Kill a Mockingbird',
    'High Fantasy': 'The Lord of the Rings',
    'Epic Fantasy': 'A Game of Thrones',
    'Tragedy': 'The Great Gatsby',
    'Thriller': 'The Da Vinci Code',
    'Adventure': 'Moby-Dick'
}

# Add another book, author, and genre
# Adding a new book and its author
book['Agatha Christie'] = 'ABC Murders'
# Adding a new genre for a book
genre['Mystery'] = 'ABC Murders'

# print some books
print('\n--- Printing out some books ---')
# Accessing and printing a specific book title by author
print(f"J.K. Rowling wrote {book['J.K. Rowling']}")
print(f"Harper Lee wrote {book['Harper Lee']}\n")

# print some authors
print('--- Printing some authors ---')
# Accessing and printing a specific author by book title
print(f"To Kill a Mockingbird was written by {author['To Kill a Mockingbird']}")
print(f"The Da Vinci Code was written by {author['The Da Vinci Code']}\n")

# print every author and their book
print("--- Print out all books and authors ---")
# Printing each author and their corresponding book title
for author, book in list(book.items()):
    print(f"{author} wrote {book}.\n")

# print every book and its genre
print('--- Printing out books and their genres ---')
# Printing each book and its corresponding genre
for genre_name, book_title in list(genre.items()):
    print(f"{genre_name} is the category for {book_title}\n")

# Checking if the genre 'Action' exists in the genre dictionary
genre_exists = 'Action' in genre
# Printing the result
print(f"Checking if 'Action' exists...")
print(f"The genre 'Action' exists: {genre_exists}")

# Extra for myself - Check if a genre exists based on user input
genre_search = input("What genre are you looking for today?\n> ")
genre_exists = genre_search in genre
# Printing is genre exists
print(f"The genre {genre_search} exists: {genre_exists}.\n")