# Book Class
class Book:
    def __init__(self, title, author): # Constructor for the Book class
        self.title = title  # Set the title of the book
        self.author = author  # Set the author of the book
        self.current_page = 1  # Set the current page of the book to 1
        self.due_date = None  # Set the due date of the book to None
        self.checked_out_by = ''  # Set the checked out by attribute to an empty string

    def load_books(self, filename): # Load books from a CSV file
        try: # Try to open the file - exception handling
            with open(filename, 'r') as file: # Open the file
                books_reader = csv.reader(file) # Create books_reader object
                next(books_reader) # Skip the header row
                for row in books_reader: # Iterate over the rows
                    title = row[0] # Get the title
                    author = row[1] # Get the author
                    restriction = row[2] # Get the restriction
                    restricted_class = row[3] if len(row) >= 4 else None # Get the restricted class
                    checked_out_by = row[4] if len(row) >= 5 and row[4] else None
            
                    if restriction.lower() == 'yes': # Check if the book is restricted
                        book = RestrictedBook(title, author, restricted_class) # Create a RestrictedBook object
                    else:
                        book = Book(title, author) # Create a Book object
            
                    book.checked_out_by = checked_out_by # Set the checked out by attribute
                    self.add_book(book) # Add the book to the library catalogue [books.csv]
        except FileNotFoundError: # Catch the FileNotFoundError exception
            print(f"Error: File '{filename}' not found.") # Print an error message

class RestrictedBook(Book):
    def __init__(self, title, author, restricted_class): # Constructor for the RestrictedBook class
        super().__init__(title, author) # Call the constructor of the parent class
        if isinstance(restricted_class, str):  # Check if a single class is provided
            restricted_class = [restricted_class]  # Convert the string to a list
        self.restricted_class = restricted_class # Set the restricted class of the book
